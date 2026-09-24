# Discussion Units: case 10091

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **40**
- Continuity pairs: **39**
- Discussion Units: **2**
- Paragraph source hashes: **40**
- Sub-themes: **13**

## 10091:1 · paragraphs 0-37

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2b22e9693718daa3325b0c8fbc04e49203c40aa08d51d498e946c9b4b365dbcd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10091:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `canada, okoh, applicants, chidubem, children, chinyere, decision, henry`
- Display key terms: `okoh, chidubem, children, chinyere, henry`
- Argument roles: `disposition, governing_rule, party_position`
- Explanation: Observed roles: disposition, governing_rule, party_position Display terms: okoh, chidubem, children, chinyere, henry Position/evidence statements: [3] At the RPD hearing, Ms Okoh alleged that she was a victim of domestic violence and claimed that she and her children have a well-founded fear of persecution from her late husband’s brother. Rule/authority context: INTRODUCTION [1] The applicants seek judicial review of a decision dated January 29, 2016 by the Refugee Appeal Division of the Immigration and Refugee Board (RAD), wherein the RAD dismissed their appeal and confirmed th Operative outcome context: INTRODUCTION [1] The applicants seek judicial review of a decision dated January 29, 2016 by the Refugee Appeal Division of the Immigration and Refugee Board (RAD), wherein the RAD dismissed their appeal and confirmed th Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4508728` offsets `910-921`; context: INTRODUCTION [1] The applicants seek judicial review of a decision dated January 29, 2016 by the Refugee Appeal Division of the Immigration and Refugee Board (RAD), wherein the RAD dismissed their appeal and confirmed the decision of the Refugee Protection Division (RPD) that the applicants are not Convention refugees or persons in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA).
- Evidence: `disposition` cue `dismissed` at chunk `4508728` offsets `738-747`; context: INTRODUCTION [1] The applicants seek judicial review of a decision dated January 29, 2016 by the Refugee Appeal Division of the Immigration and Refugee Board (RAD), wherein the RAD dismissed their appeal and confirmed the decision of the Refugee Protection Division (RPD) that the applicants are not Convention refugees or persons in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA).
- Evidence: `party_position` cue `claimed` at chunk `4508730` offsets `87-94`; context: [3] At the RPD hearing, Ms Okoh alleged that she was a victim of domestic violence and claimed that she and her children have a well-founded fear of persecution from her late husband’s brother.

#### 10091:1:subtheme:2 · paragraphs 3-4

- Raw key terms: `alternative, applicants, decided, found, issue, among, appealed, appeared`
- Display key terms: `alternative, decided, among, appealed, appeared`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: alternative, decided, among, appealed, appeared Rule/authority context: DECISION UNDER REVIEW [5] The RAD panel conducted its own assessment of the RPD’s decision. Evidence spans paragraphs 3-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4508731` offsets `100-105`; context: The RPD decided that the determinative issue was credibility as there were several inconsistencies in the evidence and the principal applicant’s testimony.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508731` offsets `167-175`; context: The RPD decided that the determinative issue was credibility as there were several inconsistencies in the evidence and the principal applicant’s testimony.
- Evidence: `governing_rule` cue `UNDER` at chunk `4508731` offsets `522-527`; context: DECISION UNDER REVIEW [5] The RAD panel conducted its own assessment of the RPD’s decision.
- Evidence: `issue` cue `issue` at chunk `4508732` offsets `13-18`; context: [6] The only issue to be decided in this matter, the RAD found, was whether a viable Internal Flight Alternative (IFA) existed for the applicants within Nigeria.

#### 10091:1:subtheme:3 · paragraphs 5-10

- Raw key terms: `considered, employment, noted, agents, appellants, applicant, assessment, canada`
- Display key terms: `considered, employment, noted, agents, appellants, assessment`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: considered, employment, noted, agents, appellants, assessment Position/evidence statements: The RAD found that there was no persuasive evidence submitted to show that the principal applicant would not be able to obtain employment in Lagos, or live in another part of Lagos away from her brother’s house. Application context: [9] In its IFA assessment, the RAD set out and applied the two-pronged test found in Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706 (CA) suitably modified to take account of section 97 of t | Therefore, an appellant cannot be required to encounter great physical danger or to undergo undue hardship in traveling there or staying there: Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] F Evidence spans paragraphs 5-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4508733` offsets `76-81`; context: [7] There was evidence before the RPD of the existence of the determinative issue of an accessible and reasonable IFA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508733` offsets `14-22`; context: [7] There was evidence before the RPD of the existence of the determinative issue of an accessible and reasonable IFA.
- Evidence: `counterargument_limitation` cue `although` at chunk `4508733` offsets `138-146`; context: The RAD noted that although the RPD questioned the applicants about the existence of an IFA, the RPD made no findings with respect to the IFA.
- Evidence: `reasoning_application` cue `applied` at chunk `4508735` offsets `47-54`; context: [9] In its IFA assessment, the RAD set out and applied the two-pronged test found in Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706 (CA) suitably modified to take account of section 97 of the IRPA.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4508736` offsets `202-211`; context: Therefore, an appellant cannot be required to encounter great physical danger or to undergo undue hardship in traveling there or staying there: Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] FC 589 (CA).
- Evidence: `party_position` cue `submitted` at chunk `4508738` offsets `157-166`; context: The RAD found that there was no persuasive evidence submitted to show that the principal applicant would not be able to obtain employment in Lagos, or live in another part of Lagos away from her brother’s house.
- Evidence: `evidence_fact` cue `found that` at chunk `4508738` offsets `113-123`; context: The RAD found that there was no persuasive evidence submitted to show that the principal applicant would not be able to obtain employment in Lagos, or live in another part of Lagos away from her brother’s house.

#### 10091:1:subtheme:4 · paragraphs 11-13

- Raw key terms: `fact, abuja, appeal, applicants, application, available, benin, city`
- Display key terms: `fact, abuja, available, benin, city`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: fact, abuja, available, benin, city Rule/authority context: [En blanc/Blank] Referrals Renvoi (2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that (2) Elle ne peut procéder au renvoi que si elle estime, à la fois :  | [18] The standard of review by the RAD of the RPD’s decision is correctness. Application context: Standard of Review [17] The appropriate standard of review to be applied by this Court to the RAD’s decision is reasonableness: Canada (Minister of Citizenship and Immigration) v Huruglica, 2016 FCA 93 at paras 30, 34 an Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4508739` offsets `157-164`; context: It noted that the test for reasonableness is whether it would be unduly harsh to expect the claimants to move to a less hostile part of the country before seeking status abroad.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508739` offsets `476-484`; context: Rather, the RAD considered the totality of the evidence including, the fact that the applicants testified that they are practicing Christians and the documentary evidence showed that at least Ibadan and Lagos host predominantly Christian residents.
- Evidence: `issue` cue `issue` at chunk `4508740` offsets `105-110`; context: The IFA issue is determinative and the RAD did not find it necessary to consider the other grounds that were raised on appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508740` offsets `1586-1594`; context: [En blanc/Blank]
Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `governing_rule` cue `under` at chunk `4508740` offsets `1537-1542`; context: [En blanc/Blank]
Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `reasoning_application` cue `applied` at chunk `4508740` offsets `2335-2342`; context: Standard of Review [17] The appropriate standard of review to be applied by this Court to the RAD’s decision is reasonableness: Canada (Minister of Citizenship and Immigration) v Huruglica, 2016 FCA 93 at paras 30, 34 and 35.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4508740` offsets `1514-1520`; context: [En blanc/Blank]
Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `governing_rule` cue `standard of review` at chunk `4508741` offsets `9-27`; context: [18] The standard of review by the RAD of the RPD’s decision is correctness.

#### 10091:1:subtheme:5 · paragraphs 14-15

- Raw key terms: `appeal, applicants, court, decision, issue, agudelo, alternate, although`
- Display key terms: `agudelo, alternate, although`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: agudelo, alternate, although Application context: [21] This issue was not raised by the applicants but was brought to the Court’s attention by counsel for the respondent because of a recent decision by Justice Richard Bell: Angwah v Canada (Minister of Citizenship and I Evidence spans paragraphs 14-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4508742` offsets `208-215`; context: [19] Although the RAD did not have the benefit of the Court of Appeal’s decision in Huruglica, it nonetheless concluded that it would conduct its own assessment of the RPD’s decision and independently assess whether the applicants are Convention refugees or persons in need of protection.
- Evidence: `issue` cue `issue` at chunk `4508743` offsets `404-409`; context: [21] This issue was not raised by the applicants but was brought to the Court’s attention by counsel for the respondent because of a recent decision by Justice Richard Bell: Angwah v Canada (Minister of Citizenship and Immigration), 2016 FC 654.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508743` offsets `72-80`; context: [20] The availability of a viable IFA is a factual inquiry based on the evidence and is reviewed on the reasonableness standard: Agudelo v Canada (Minister of Citizenship and Immigration), 2009 FC 465 at para 17; Khokhar v Canada (Minister of Citizenship and Immigration), 2008 FC 449 at para 21.
- Evidence: `reasoning_application` cue `because` at chunk `4508743` offsets `514-521`; context: [21] This issue was not raised by the applicants but was brought to the Court’s attention by counsel for the respondent because of a recent decision by Justice Richard Bell: Angwah v Canada (Minister of Citizenship and Immigration), 2016 FC 654.
- Evidence: `counterargument_limitation` cue `but` at chunk `4508743` offsets `443-446`; context: [21] This issue was not raised by the applicants but was brought to the Court’s attention by counsel for the respondent because of a recent decision by Justice Richard Bell: Angwah v Canada (Minister of Citizenship and Immigration), 2016 FC 654.

#### 10091:1:subtheme:6 · paragraphs 16-18

- Raw key terms: `credibility, matter, angwah, findings, respect, stated, accessible, adopting`
- Display key terms: `credibility, matter, angwah, findings, respect, stated, accessible, adopting`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: credibility, matter, angwah, findings, respect, stated, accessible, adopting Operative outcome context: On appeal, the RAD upheld the rejection of the refugee claim on the alternative ground that she had an accessible and viable IFA. Evidence spans paragraphs 16-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4508744` offsets `116-121`; context: In that case, the RPD found that the determinative issue was credibility based on a number of contradictions in the applicant’s testimony.
- Evidence: `evidence_fact` cue `found that` at chunk `4508744` offsets `87-97`; context: In that case, the RPD found that the determinative issue was credibility based on a number of contradictions in the applicant’s testimony.
- Evidence: `disposition` cue `upheld` at chunk `4508744` offsets `223-229`; context: On appeal, the RAD upheld the rejection of the refugee claim on the alternative ground that she had an accessible and viable IFA.
- Evidence: `issue` cue `whether` at chunk `4508745` offsets `109-116`; context: [23] However, unlike in this matter, the RAD in Angwah expressly stated that it was unnecessary to determine whether the RPD had made a reviewable error with respect to its credibility findings.

#### 10091:1:subtheme:7 · paragraphs 19-20

- Raw key terms: `concluded, findings, found, ground, issue, made, submissions, without`
- Display key terms: `concluded, findings, ground, made, submissions, without`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: concluded, findings, ground, made, submissions, without Rule/authority context: [26] In Angwah, the RAD concluded that pursuant to its statutory authority to confirm or substitute a decision of the RPD pursuant to paragraphs 111(1) (a) and (b) of the Act, it could confirm the determination of the RP Application context: They sought to have the RPD’s findings set aside on the ground that the principal applicant had made mistakes in her evidence because of the effects of her PTSD. Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4508747` offsets `156-162`; context: [25] In conducting its analysis of the merits of the appeal, the RAD noted at the outset that the appellants had conceded that there were a few credibility issues with respect to the principal appellant’s written and oral testimony.
- Evidence: `evidence_fact` cue `testimony` at chunk `4508747` offsets `222-231`; context: [25] In conducting its analysis of the merits of the appeal, the RAD noted at the outset that the appellants had conceded that there were a few credibility issues with respect to the principal appellant’s written and oral testimony.
- Evidence: `reasoning_application` cue `because` at chunk `4508747` offsets `359-366`; context: They sought to have the RPD’s findings set aside on the ground that the principal applicant had made mistakes in her evidence because of the effects of her PTSD.
- Evidence: `issue` cue `issue` at chunk `4508748` offsets `286-291`; context: [26] In Angwah, the RAD concluded that pursuant to its statutory authority to confirm or substitute a decision of the RPD pursuant to paragraphs 111(1) (a) and (b) of the Act, it could confirm the determination of the RPD on alternative grounds and decide the claim uniquely on the IFA issue without making a finding that the RPD had erred.
- Evidence: `evidence_fact` cue `found that` at chunk `4508748` offsets `349-359`; context: The RAD found that the RPD had fully canvassed the possibility of an IFA but made no findings in that regard.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4508748` offsets `39-50`; context: [26] In Angwah, the RAD concluded that pursuant to its statutory authority to confirm or substitute a decision of the RPD pursuant to paragraphs 111(1) (a) and (b) of the Act, it could confirm the determination of the RPD on alternative grounds and decide the claim uniquely on the IFA issue without making a finding that the RPD had erred.
- Evidence: `counterargument_limitation` cue `but` at chunk `4508748` offsets `414-417`; context: The RAD found that the RPD had fully canvassed the possibility of an IFA but made no findings in that regard.

#### 10091:1:subtheme:8 · paragraphs 21-24

- Raw key terms: `decision, bell, erred, evidence, huruglica, justice, angwah, appeal`
- Display key terms: `bell, erred, huruglica, justice, angwah`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: bell, erred, huruglica, justice, angwah Rule/authority context: Justice Bell found that the appropriate standard of review for determination of that issue was reasonableness as it was a question falling wholly within the jurisdiction of the RAD and is not one of general application:  | This translates into an application of the correctness standard of review. Application context: Those paragraphs read as follows: 78 At this stage of my analysis, I find that the role of the RAD is to intervene when the RPD is wrong in law, in fact or in fact and law. | Therefore, Justice Bell found that the RAD’s decision was neither transparent nor intelligible and, did not meet the test of reasonableness. Evidence spans paragraphs 21-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4508749` offsets `276-281`; context: Justice Bell found that the appropriate standard of review for determination of that issue was reasonableness as it was a question falling wholly within the jurisdiction of the RAD and is not one of general application: Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190; Huruglica, above.
- Evidence: `evidence_fact` cue `found that` at chunk `4508749` offsets `204-214`; context: Justice Bell found that the appropriate standard of review for determination of that issue was reasonableness as it was a question falling wholly within the jurisdiction of the RAD and is not one of general application: Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190; Huruglica, above.
- Evidence: `governing_rule` cue `standard of review` at chunk `4508749` offsets `231-249`; context: Justice Bell found that the appropriate standard of review for determination of that issue was reasonableness as it was a question falling wholly within the jurisdiction of the RAD and is not one of general application: Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190; Huruglica, above.
- Evidence: `issue` cue `issue` at chunk `4508750` offsets `952-957`; context: …
103 I conclude from my statutory analysis that with respect to findings of fact (and mixed fact and law) such as the one involved here, which raised no issue of credibility of oral evidence, the RAD is to review RPD decisions applying the correctness standard.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508750` offsets `734-742`; context: It can also set it aside, substituting its own determination of the claim, unless it is satisfied that it cannot do either without hearing the evidence presented to the RPD: paragraph 111(2)(b) of the IRPA.
- Evidence: `governing_rule` cue `standard of review` at chunk `4508750` offsets `481-499`; context: This translates into an application of the correctness standard of review.
- Evidence: `reasoning_application` cue `I find` at chunk `4508750` offsets `320-326`; context: Those paragraphs read as follows:
78 At this stage of my analysis, I find that the role of the RAD is to intervene when the RPD is wrong in law, in fact or in fact and law.
- Evidence: `evidence_fact` cue `found that` at chunk `4508751` offsets `33-43`; context: [29] In the result, Justice Bell found that the RAD had not concluded that the RPD had made such an error.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4508751` offsets `262-271`; context: Therefore, Justice Bell found that the RAD’s decision was neither transparent nor intelligible and, did not meet the test of reasonableness.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508752` offsets `727-735`; context: That would, in my view, be contrary to the evident intent of Parliament that matters heard by the RAD not be referred back to the RPD for redetermination unless it is clear that: (a) the RPD had erred in law or in fact or mixed fact and law; or (b) the RAD cannot make a decision without hearing evidence as set out in subsection 111 (2) of the IRPA.
- Evidence: `counterargument_limitation` cue `however` at chunk `4508752` offsets `294-301`; context: I am not convinced, however, that it was the intent of the legislators or of the Court of Appeal to impose such a limitation on the jurisdiction of the RAD.

#### 10091:1:subtheme:9 · paragraphs 25-28

- Raw key terms: `applicant, applicants, canada, consider, immigration, principal, proposed, submit`
- Display key terms: `consider, principal, proposed, submit`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: consider, principal, proposed, submit Position/evidence statements: [32] The applicants submit that, in making an IFA determination, the underlying factor to consider is whether it is objectively reasonable for the applicants to live in a proposed IFA destination without fear of persecut | [33] With respect to the second prong of the IFA test, the applicants contend that the RAD failed to consider the evidence in light of the Chairperson’s Gender Guidelines. Application context: They argue that having already relocated to at least one of the suggested IFA’s, Lagos, where they were found and the principal applicant was threatened and attacked by the agent of persecution, it was unreasonable for t | Therefore, the applicants submit that the RAD failed to consider the hardship they would experience in moving and establishing residence in any of the proposed cities: Kayumba v Canada (Citizenship and Immigration), 2010 Evidence spans paragraphs 25-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4508753` offsets `113-119`; context: [31] Based on the record, my conclusion is that the RAD was satisfied that the RPD’s decision on the credibility issues was sound but chose to decide the appeal on the IFA ground as that would be, in any event, determinative.
- Evidence: `party_position` cue `submit` at chunk `4508753` offsets `405-411`; context: [32] The applicants submit that, in making an IFA determination, the underlying factor to consider is whether it is objectively reasonable for the applicants to live in a proposed IFA destination without fear of persecution: Kulanthavelu v Canada (Minister of Employment and Immigration), [1993] FCJ No 1273 at para 8.
- Evidence: `evidence_fact` cue `record` at chunk `4508753` offsets `18-24`; context: [31] Based on the record, my conclusion is that the RAD was satisfied that the RPD’s decision on the credibility issues was sound but chose to decide the appeal on the IFA ground as that would be, in any event, determinative.
- Evidence: `reasoning_application` cue `conclude` at chunk `4508753` offsets `934-942`; context: They argue that having already relocated to at least one of the suggested IFA’s, Lagos, where they were found and the principal applicant was threatened and attacked by the agent of persecution, it was unreasonable for the RAD to conclude that they would be safe in that city.
- Evidence: `counterargument_limitation` cue `but` at chunk `4508753` offsets `130-133`; context: [31] Based on the record, my conclusion is that the RAD was satisfied that the RPD’s decision on the credibility issues was sound but chose to decide the appeal on the IFA ground as that would be, in any event, determinative.
- Evidence: `party_position` cue `contend` at chunk `4508754` offsets `70-77`; context: [33] With respect to the second prong of the IFA test, the applicants contend that the RAD failed to consider the evidence in light of the Chairperson’s Gender Guidelines.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508754` offsets `114-122`; context: [33] With respect to the second prong of the IFA test, the applicants contend that the RAD failed to consider the evidence in light of the Chairperson’s Gender Guidelines.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4508754` offsets `425-434`; context: Therefore, the applicants submit that the RAD failed to consider the hardship they would experience in moving and establishing residence in any of the proposed cities: Kayumba v Canada (Citizenship and Immigration), 2010 FC 138.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4508754` offsets `279-285`; context: The principal applicant is a widow and has four minor children (ages ranging from 13 to 17 years old); she cannot hide and has to be able to move freely for the best interests of her children.
- Evidence: `party_position` cue `submit` at chunk `4508755` offsets `25-31`; context: [34] The applicants also submit that the RAD failed to consider the psychological report in the record which found that the principal applicant suffers from anxiety and PTSD.
- Evidence: `evidence_fact` cue `record` at chunk `4508755` offsets `96-102`; context: [34] The applicants also submit that the RAD failed to consider the psychological report in the record which found that the principal applicant suffers from anxiety and PTSD.

#### 10091:1:subtheme:10 · paragraphs 29-30

- Raw key terms: `court, place, requires, safe, threshold, absence, actual, addition`
- Display key terms: `place, requires, safe, threshold, absence, actual, addition`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: place, requires, safe, threshold, absence, actual, addition Position/evidence statements: First, as this Court said in Thirunavukkarasu, [at page 599], the definition of refugee under the Convention “requires claimants to be unable or unwilling by reason of fear of persecution to claim the protection of their Rule/authority context: First, as this Court said in Thirunavukkarasu, [at page 599], the definition of refugee under the Convention “requires claimants to be unable or unwilling by reason of fear of persecution to claim the protection of their Evidence spans paragraphs 29-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4508757` offsets `392-399`; context: The absence of relatives in a safe place, whether taken alone or in conjunction with other factors, can only amount to such condition if it meets that threshold, that is to say if it establishes that, as a result, a claimant’s life or safety would be jeopardized.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508757` offsets `321-329`; context: In addition, it requires actual and concrete evidence of such conditions.
- Evidence: `party_position` cue `claim` at chunk `4508758` offsets `276-281`; context: First, as this Court said in Thirunavukkarasu, [at page 599], the definition of refugee under the Convention “requires claimants to be unable or unwilling by reason of fear of persecution to claim the protection of their home country in any part of that country”.
- Evidence: `governing_rule` cue `under` at chunk `4508758` offsets `173-178`; context: First, as this Court said in Thirunavukkarasu, [at page 599], the definition of refugee under the Convention “requires claimants to be unable or unwilling by reason of fear of persecution to claim the protection of their home country in any part of that country”.

#### 10091:1:subtheme:11 · paragraphs 31-33

- Raw key terms: `applicants, applicant, away, brother, conclude, difficult, evidence, found`
- Display key terms: `away, brother, conclude, difficult`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: away, brother, conclude, difficult Application context: The lack of relatives in other parts of Lagos or the other cities could make it more difficult for them to live there but it was reasonable for the RAD to conclude that the hardship associated with relocation is not the  | It was not unreasonable for the RAD to conclude that an IFA could be found away from the brother’s home. Evidence spans paragraphs 31-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4508759` offsets `83-88`; context: [36] In the Court’s view, the RAD did not misconstrue the evidence relating to the issue of whether the applicants had a viable IFA nor did the RAD ignore any evidence particular to the applicant’s circumstances.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508759` offsets `58-66`; context: [36] In the Court’s view, the RAD did not misconstrue the evidence relating to the issue of whether the applicants had a viable IFA nor did the RAD ignore any evidence particular to the applicant’s circumstances.
- Evidence: `evidence_fact` cue `found that` at chunk `4508760` offsets `13-23`; context: [37] The RAD found that the applicants could reside in Lagos, a city of some 28 million people, if they lived somewhere away from her brother’s house.
- Evidence: `reasoning_application` cue `conclude` at chunk `4508760` offsets `306-314`; context: The lack of relatives in other parts of Lagos or the other cities could make it more difficult for them to live there but it was reasonable for the RAD to conclude that the hardship associated with relocation is not the kind that renders an IFA unreasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508761` offsets `38-46`; context: [38] The applicants failed to provide evidence that the brother in law had the ability to influence police actions in Nigeria or access resources to locate the applicants if they were to relocate within the country.
- Evidence: `reasoning_application` cue `conclude` at chunk `4508761` offsets `470-478`; context: It was not unreasonable for the RAD to conclude that an IFA could be found away from the brother’s home.

#### 10091:1:subtheme:12 · paragraphs 34-37

- Raw key terms: `applicants, decision, proposed, able, acceptable, adapt, address, areas`
- Display key terms: `proposed, able, acceptable, adapt, address, areas`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: proposed, able, acceptable, adapt, address, areas Application context: Pilowsky, quite commonly seen in refugee claims, was of little assistance to the IFA issue because it did not address the conditions in Nigeria or consider the psychological impact of her relocation within that country. | [40] On the evidence, it was reasonable for the RAD to conclude that the applicants would likely be able to adapt to their new surroundings, pursue their studies or obtain employment, and that they would not have to live Evidence spans paragraphs 34-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4508762` offsets `275-280`; context: Pilowsky, quite commonly seen in refugee claims, was of little assistance to the IFA issue because it did not address the conditions in Nigeria or consider the psychological impact of her relocation within that country.
- Evidence: `reasoning_application` cue `because` at chunk `4508762` offsets `281-288`; context: Pilowsky, quite commonly seen in refugee claims, was of little assistance to the IFA issue because it did not address the conditions in Nigeria or consider the psychological impact of her relocation within that country.
- Evidence: `evidence_fact` cue `evidence` at chunk `4508763` offsets `12-20`; context: [40] On the evidence, it was reasonable for the RAD to conclude that the applicants would likely be able to adapt to their new surroundings, pursue their studies or obtain employment, and that they would not have to live in hiding in any of the proposed IFA areas.
- Evidence: `reasoning_application` cue `conclude` at chunk `4508763` offsets `55-63`; context: [40] On the evidence, it was reasonable for the RAD to conclude that the applicants would likely be able to adapt to their new surroundings, pursue their studies or obtain employment, and that they would not have to live in hiding in any of the proposed IFA areas.

#### Section text

Okechukwu v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2016-10-14
Neutral citation
2016 FC 1142
File numbers
IMM-838-16
Decision Content
Date: 20161014
Docket: IMM-838-16
Citation: 2016 FC 1142
Ottawa, Ontario, October 14, 2016
PRESENT: The Honourable Mr. Justice Mosley
BETWEEN:
JENIFFER CHINYERE OKECHUKWU OKOH KASIE SOPHIA OKECHUKWU
PRECIOUS CHIAMAKA OKECHUKWU
KOSISOCHUKWU FRANCIA OKECHUKWU
CHIDUBEM HENRY OKECHUKWU
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. INTRODUCTION [1] The applicants seek judicial review of a decision dated January 29, 2016 by the Refugee Appeal Division of the Immigration and Refugee Board (RAD), wherein the RAD dismissed their appeal and confirmed the decision of the Refugee Protection Division (RPD) that the applicants are not Convention refugees or persons in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA).

[2] The applicants are citizens of Nigeria. The principal applicant, Jeniffer Chinyere Okechukwu Okoh, a widow, was born on September 17, 1972. She is the designated representative of her four minor children (Kasie Sophia Okechukwu, Precious Okechukwu, Chidubem Henry Okechukwu, and Kosisochukwu Francis Okechukwu). The family arrived in Canada on March 17, 2015.

[3] At the RPD hearing, Ms Okoh alleged that she was a victim of domestic violence and claimed that she and her children have a well-founded fear of persecution from her late husband’s brother. On February 13, 2015, as a result of an assault and threats of death over the disposition of her husband’s estate, she was forced to relocate with her children from the city where she lived in Onitsha to her brother’s home in Lagos. She testified that the brother in law and hired agents managed to find her there a few days later and attempted to kill her. Her screams for help averted the attack. That prompted her decision to flee Nigeria and seek protection in Canada.

[4] The applicants appeared before the RPD on June 24, 2015. The RPD decided that the determinative issue was credibility as there were several inconsistencies in the evidence and the principal applicant’s testimony. Among the evidence submitted to the RPD was a psychological assessment prepared by Dr. J. Pilowsky which found that the principal applicant suffered from Post-traumatic Stress Disorder (PTSD). A negative decision was issued on July 31, 2015. The applicants appealed that decision to the RAD.
II. DECISION UNDER REVIEW [5] The RAD panel conducted its own assessment of the RPD’s decision. The panel observed that under the IRPA it has the power to confirm or substitute the determination of the RPD. In confirming a RPD determination, the RAD stated, it was not bound by the reasoning in the RPD’s decision. This was evident, it stated, from the use of the word “determination” in paragraphs 111 (1) (a) and (b). Further, the RAD concluded, the restrictions on remittal in subsection 111(2) suggest that Parliament’s intent was to have the RAD finalize refugee protection claims where it can do so fairly, including by confirming a determination on alternative grounds.

[6] The only issue to be decided in this matter, the RAD found, was whether a viable Internal Flight Alternative (IFA) existed for the applicants within Nigeria.

[7] There was evidence before the RPD of the existence of the determinative issue of an accessible and reasonable IFA. The RAD noted that although the RPD questioned the applicants about the existence of an IFA, the RPD made no findings with respect to the IFA. The RAD conducted its own assessment of the viability of an IFA based upon the record before it. Notably, the RAD invited the applicants’ counsel to make submissions regarding the IFA which the RAD received and considered. It concluded that there are viable IFAs for the applicants in the cities of Ibadan, Abuja, Benin City or Lagos.

[8] In reaching its conclusion, the RAD considered the Chairperson’s Gender Guidelines (Guideline 4: Women Refugee Claimants Fearing Gender-Related Persecution) as well as the social and cultural context in which the female principal applicant’s allegations arose. The RAD also took into consideration the Chairperson’s Guidelines on Children Refugees.

[9] In its IFA assessment, the RAD set out and applied the two-pronged test found in Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706 (CA) suitably modified to take account of section 97 of the IRPA.

[10] The RAD noted that the burden of proof rests with the appellants to show that an IFA does not exist in the circumstances. The RAD also noted that the IFA must be a realistic and attainable option. Therefore, an appellant cannot be required to encounter great physical danger or to undergo undue hardship in traveling there or staying there: Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] FC 589 (CA).

[11] The RAD relied on the United Kingdom Home Office Operational Guidance Note for Nigeria which states that internal relocation to escape ill-treatment from non-state agents is almost always an option and, in the absence of exceptional circumstances, it would not be unduly harsh for any individual to internally relocate.

[12] The RAD noted that Lagos has a population of over 28 million and is one of Nigeria’s largest ports. The RAD found that there was no persuasive evidence submitted to show that the principal applicant would not be able to obtain employment in Lagos, or live in another part of Lagos away from her brother’s house. The RAD also found that the problems faced by the principal applicant with her deceased husband’s family were local in nature. The RAD considered the profile and influence of the agents of persecution in relation to the IFA. It did not find any persuasive evidence on the record that they would be able to find the appellants elsewhere in Lagos or other cities in Nigeria.

[13] The RAD also considered the reasonableness of the IFA in the cities of Ibadan, Abuja, Benin City or Lagos. It noted that the test for reasonableness is whether it would be unduly harsh to expect the claimants to move to a less hostile part of the country before seeking status abroad. The RAD noted that its finding of an IFA in the cities of Ibadan, Abuja, Benin City or Lagos is not dependent on the size of these cities. Rather, the RAD considered the totality of the evidence including, the fact that the applicants testified that they are practicing Christians and the documentary evidence showed that at least Ibadan and Lagos host predominantly Christian residents. The RAD was satisfied that the applicants would have sources of moral and spiritual assistance and support available to them in either of those cities. Finally, the RAD found that the applicants did not adduce persuasive evidence to indicate that they would have to live in hiding in the cities of Ibadan, Abuja, Benin City or Lagos.

[14] Based on the forgoing, the RAD concluded that a viable IFA was available to the applicants. The IFA issue is determinative and the RAD did not find it necessary to consider the other grounds that were raised on appeal.
III. RELEVANT LEGISLATION [15] The relevant provisions of the IRPA reads as follows:
Decision
Décision
111 (1) After considering the appeal, the Refugee Appeal Division shall make one of the following decisions:
111 (1) La Section d’appel des réfugiés confirme la décision attaquée, casse la décision et y substitue la décision qui aurait dû être rendue ou renvoie, conformément à ses instructions, l’affaire à la Section de la protection des réfugiés.
(a) confirm the determination of the Refugee Protection Division;
[En blanc/Blank]
(b) set aside the determination and substitute a determination that, in its opinion, should have been made; or
[En blanc/Blank]
(c) refer the matter to the Refugee Protection Division for re determination, giving the directions to the Refugee Protection Division that it considers appropriate.
[En blanc/Blank]
Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
b) qu’elle ne peut confirmer la décision attaquée ou casser la décision et y substituer la décision qui aurait dû être rendue sans tenir une nouvelle audience en vue du réexamen des éléments de preuve qui ont été présentés à la Section de la protection des réfugiés.
IV. ISSUES [16] This application for judicial review raises the following issues:
A. What is the appropriate standard of review?
B. Was it open to the RAD to dismiss the appeal on an alternate ground to that found by the RPD?
C. Did the RAD err in determining that the applicants have a viable IFA in Lagos, Ibadan, Abuja and Benin City?
V. ANALYSIS A. Standard of Review [17] The appropriate standard of review to be applied by this Court to the RAD’s decision is reasonableness: Canada (Minister of Citizenship and Immigration) v Huruglica, 2016 FCA 93 at paras 30, 34 and 35.

[18] The standard of review by the RAD of the RPD’s decision is correctness. In Huruglica, at para 78, the Court of Appeal stated that:
…the role of the RAD is to intervene when the RPD is wrong in law, in fact or in fact and law. This translates into an application of the correctness standard of review. If there is an error, the RAD can still confirm the decision of the RPD on another basis…
[Emphasis added]

[19] Although the RAD did not have the benefit of the Court of Appeal’s decision in Huruglica, it nonetheless concluded that it would conduct its own assessment of the RPD’s decision and independently assess whether the applicants are Convention refugees or persons in need of protection. The applicants did not take issue with the RAD’s scope of review of the RPD’s decision.

[20] The availability of a viable IFA is a factual inquiry based on the evidence and is reviewed on the reasonableness standard: Agudelo v Canada (Minister of Citizenship and Immigration), 2009 FC 465 at para 17; Khokhar v Canada (Minister of Citizenship and Immigration), 2008 FC 449 at para 21.
B. Was it open to the RAD to dismiss the appeal on an alternate ground to that found by the RPD? [21] This issue was not raised by the applicants but was brought to the Court’s attention by counsel for the respondent because of a recent decision by Justice Richard Bell: Angwah v Canada (Minister of Citizenship and Immigration), 2016 FC 654.

[22] The facts of Angwah are very similar to the present matter. In that case, the RPD found that the determinative issue was credibility based on a number of contradictions in the applicant’s testimony. On appeal, the RAD upheld the rejection of the refugee claim on the alternative ground that she had an accessible and viable IFA.

[23] However, unlike in this matter, the RAD in Angwah expressly stated that it was unnecessary to determine whether the RPD had made a reviewable error with respect to its credibility findings.

[24] In this matter, the RAD quoted passages from Justice Michael Phelan’s decision in Huruglica v Canada (Minister of Citizenship and Immigration) 2014 FC 799 at paras 54 and 55. Adopting Justice Phelan’s language, the RAD stated that it “will recognize and respect the credibility findings of the RPD or other findings where the RPD has a particular advantage in arriving at its conclusions.”

[25] In conducting its analysis of the merits of the appeal, the RAD noted at the outset that the appellants had conceded that there were a few credibility issues with respect to the principal appellant’s written and oral testimony. They sought to have the RPD’s findings set aside on the ground that the principal applicant had made mistakes in her evidence because of the effects of her PTSD. The RAD referred to the arguments that the appellants had raised about the reasonableness of the RPD’s credibility findings. The panel concluded its remarks on the findings by stating “[c]ounsel addressed these issues in his post hearing submissions but the panel failed to give weight.” In my view, those remarks indicate that the RAD found no error in the RPD’s credibility findings although that was not expressly stated. The RAD went on, however, to focus on the IFA issue. The question is whether it was entitled to do so without having found an error on the part of the RPD.

[26] In Angwah, the RAD concluded that pursuant to its statutory authority to confirm or substitute a decision of the RPD pursuant to paragraphs 111(1) (a) and (b) of the Act, it could confirm the determination of the RPD on alternative grounds and decide the claim uniquely on the IFA issue without making a finding that the RPD had erred. The RAD found that the RPD had fully canvassed the possibility of an IFA but made no findings in that regard. Before reaching a conclusion on the alternate ground, the RAD afforded counsel the opportunity to provide additional submissions on the issue of the IFA, as was done in this matter.

[27] On the application for judicial review before Justice Bell, the applicant contended that the RAD erred in deciding the appeal on grounds other than those considered in the RPD decision. Justice Bell found that the appropriate standard of review for determination of that issue was reasonableness as it was a question falling wholly within the jurisdiction of the RAD and is not one of general application: Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190; Huruglica, above. He concluded, after reviewing the legislation and authorities cited by the applicant, that the RAD was “clothed with jurisdiction to decide such an issue”: Angwah, at para 15. I agree with that conclusion.

[28] Justice Bell went on, however, to find that “when the RAD confirms the decision of the RPD on another basis, it must do so after it determines the existence of an error in the RPD decision”: Angwah, at para 16 citing Huruglica at paras 78 and 103. Those paragraphs read as follows:
78 At this stage of my analysis, I find that the role of the RAD is to intervene when the RPD is wrong in law, in fact or in fact and law. This translates into an application of the correctness standard of review. If there is an error, the RAD can still confirm the decision of the RPD on another basis. It can also set it aside, substituting its own determination of the claim, unless it is satisfied that it cannot do either without hearing the evidence presented to the RPD: paragraph 111(2)(b) of the IRPA.
…
103 I conclude from my statutory analysis that with respect to findings of fact (and mixed fact and law) such as the one involved here, which raised no issue of credibility of oral evidence, the RAD is to review RPD decisions applying the correctness standard. Thus, after carefully considering the RPD decision, the RAD carries out its own analysis of the record to determine whether, as submitted by the appellant, the RPD erred. Having done this, the RAD is to provide a final determination of the merits of the refugee claim. It is only when the RAD is of the opinion that it cannot provide such a final determination without hearing the oral evidence presented to the RPD that the matter can be referred back to the RPD for redetermination. No other interpretation of the relevant statutory provisions is reasonable.

[29] In the result, Justice Bell found that the RAD had not concluded that the RPD had made such an error. Moreover, it was not clear that the RAD had disabused itself of the RPD’s credibility finding and had considered new evidence that was not before the RPD. Therefore, Justice Bell found that the RAD’s decision was neither transparent nor intelligible and, did not meet the test of reasonableness.

[30] I appreciate that the paragraphs cited from the Court of Appeal’s decision in Huruglica can be read as requiring a predicate finding by the RAD that the RPD has erred before the RAD may consider an alternate ground on which to uphold the decision dismissing the claim. I am not convinced, however, that it was the intent of the legislators or of the Court of Appeal to impose such a limitation on the jurisdiction of the RAD. That would, in my view, be contrary to the evident intent of Parliament that matters heard by the RAD not be referred back to the RPD for redetermination unless it is clear that: (a) the RPD had erred in law or in fact or mixed fact and law; or (b) the RAD cannot make a decision without hearing evidence as set out in subsection 111 (2) of the IRPA.

[31] Based on the record, my conclusion is that the RAD was satisfied that the RPD’s decision on the credibility issues was sound but chose to decide the appeal on the IFA ground as that would be, in any event, determinative. I see no reason to interfere with that result.
C. Did the RAD err in determining that the applicants have a viable IFA in Lagos, Ibadan, Abuja and Benin City? [32] The applicants submit that, in making an IFA determination, the underlying factor to consider is whether it is objectively reasonable for the applicants to live in a proposed IFA destination without fear of persecution: Kulanthavelu v Canada (Minister of Employment and Immigration), [1993] FCJ No 1273 at para 8. They argue that having already relocated to at least one of the suggested IFA’s, Lagos, where they were found and the principal applicant was threatened and attacked by the agent of persecution, it was unreasonable for the RAD to conclude that they would be safe in that city. As Lagos is further away from the other proposed IFA’s, there is a serious possibility that the brother in law could find them in any of the other proposed cities.

[33] With respect to the second prong of the IFA test, the applicants contend that the RAD failed to consider the evidence in light of the Chairperson’s Gender Guidelines. The principal applicant is a widow and has four minor children (ages ranging from 13 to 17 years old); she cannot hide and has to be able to move freely for the best interests of her children. The proposed IFA cities would not allow her to move freely. Therefore, the applicants submit that the RAD failed to consider the hardship they would experience in moving and establishing residence in any of the proposed cities: Kayumba v Canada (Citizenship and Immigration), 2010 FC 138.

[34] The applicants also submit that the RAD failed to consider the psychological report in the record which found that the principal applicant suffers from anxiety and PTSD. Had this key piece of evidence been considered by the RAD, they submit, the panel would have come to a different conclusion.

[35] There is a high onus on claimants to demonstrate that a proposed IFA is unreasonable: Ranganathan v Canada (Minister of Citizenship and Immigration), [2001] 2 FCR 164 at paras 15-17, referring to Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] FC 589 (CA):

[15] We read the decision of Linden J.A. for this Court as setting up a very high threshold for the unreasonableness test. It requires nothing less than conditions which would jeopardize the life and safety of a claimant in traveling or temporarily relocating to a safe area. In addition, it requires actual and concrete evidence of such conditions. The absence of relatives in a safe place, whether taken alone or in conjunction with other factors, can only amount to such condition if it meets that threshold, that is to say if it establishes that, as a result, a claimant’s life or safety would

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 10091:2 · paragraphs 38-39

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `16cf36958cc8d7983a75e821a4199910bbe75dc0baddcada5749b22c2a4e2640`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10091:2:subtheme:1 · paragraphs 38-39

- Raw key terms: `judgment, mosley, appearances, applicants, application, attorney, barrister, bridget`
- Display key terms: `mosley, barrister, bridget`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: mosley, barrister, bridget Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that the application is dismissed. Evidence spans paragraphs 38-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4508765` offsets `109-118`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application is dismissed.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that the application is dismissed. No questions are certified.
“Richard G. Mosley”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-838-16
STYLE OF CAUSE:
JENIFFER CHINYERE OKECHUKWU OKOH
KASIE SOPHIA OKECHUKWU
PRECIOUS CHIAMAKA OKECHUKWU
KOSISOCHUKWU FRANCIA OKECHUKWU
CHIDUBEM HENRY OKECHUKWU v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
October 5, 2016
JUDGMENT AND Reasons:
MOSLEY, J.
DATED:
october 14, 2016
APPEARANCES:
Peter Obuba Kalu
For The ApplicantS
Bridget A. O’Leary
For The Respondent
SOLICITORS OF RECORD:
Peter Obuba Kalu
Barrister & Solicitor
Toronto, Ontario
For The ApplicantS
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
