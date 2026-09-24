# Discussion Units: case 11888

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **67**
- Continuity pairs: **66**
- Discussion Units: **2**
- Paragraph source hashes: **67**
- Sub-themes: **22**

## 11888:1 · paragraphs 0-65

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `863a9f26a02549ea38e4aaadfcaab13dd905b5dec9ae4604a0cfbd3c4638f22a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11888:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `applicant, canada, ching, kheong, arrived, citation, citizen, citizenship`
- Display key terms: `ching, kheong, arrived, citation, citizen`
- Argument roles: `party_position`
- Explanation: Observed roles: party_position Display terms: ching, kheong, arrived, citation, citizen Position/evidence statements: [1] The applicant, Mr Wai Kheong Ching, a citizen of Malaysia, arrived in Canada in 2005 and claimed refugee protection in July 2013. Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claimed` at chunk `4596710` offsets `93-100`; context: [1] The applicant, Mr Wai Kheong Ching, a citizen of Malaysia, arrived in Canada in 2005 and claimed refugee protection in July 2013.

#### 11888:1:subtheme:2 · paragraphs 2-6

- Raw key terms: `protection, applicant, decision, judicial, national, opinion, political, review`
- Display key terms: `protection, judicial, national, opinion, political, review`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: protection, judicial, national, opinion, political, review Position/evidence statements: He then claimed refugee protection in 2013 based on the allegations described above. Rule/authority context: [3] The Refugee Protection Division of the Immigration and Refugee Board [RPD] denied his claim for protection as a Convention refugee and as a person in need of protection pursuant to sections 96 and 97 of the Immigrati | The RAD erred in applying judicial review principles and the reasonableness standard of review to the appeal of the RPD decision and failed to observe principles of procedural fairness by reviewing positive credibility f Application context: He also claims that he faces a risk to his life, cruel and unusual treatment or punishment and danger of torture in Malaysia because he will be required to participate in training for the National Service. | In addition, he claims that he will be persecuted for his political opinion because he protested for democracy and human rights in Malaysia. Operative outcome context: [3] The Refugee Protection Division of the Immigration and Refugee Board [RPD] denied his claim for protection as a Convention refugee and as a person in need of protection pursuant to sections 96 and 97 of the Immigrati | [4] This application for judicial review is allowed with respect to the section 97 claim only. Evidence spans paragraphs 2-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4596711` offsets `311-318`; context: He also claims that he faces a risk to his life, cruel and unusual treatment or punishment and danger of torture in Malaysia because he will be required to participate in training for the National Service.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4596712` offsets `173-184`; context: [3] The Refugee Protection Division of the Immigration and Refugee Board [RPD] denied his claim for protection as a Convention refugee and as a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act] on October 9, 2013.
- Evidence: `disposition` cue `denied` at chunk `4596712` offsets `79-85`; context: [3] The Refugee Protection Division of the Immigration and Refugee Board [RPD] denied his claim for protection as a Convention refugee and as a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act] on October 9, 2013.
- Evidence: `governing_rule` cue `principles` at chunk `4596713` offsets `137-147`; context: The RAD erred in applying judicial review principles and the reasonableness standard of review to the appeal of the RPD decision and failed to observe principles of procedural fairness by reviewing positive credibility findings of the RPD without providing the applicant with an opportunity to respond to the RAD’s concerns about the RPD’s credibility findings.
- Evidence: `reasoning_application` cue `because` at chunk `4596713` offsets `1151-1158`; context: In addition, he claims that he will be persecuted for his political opinion because he protested for democracy and human rights in Malaysia.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4596713` offsets `735-743`; context: Although he was subsequently granted a postponement of his training for military service, he claims that he must report for duty upon return to Malaysia.
- Evidence: `disposition` cue `allowed` at chunk `4596713` offsets `44-51`; context: [4] This application for judicial review is allowed with respect to the section 97 claim only.
- Evidence: `party_position` cue `claimed` at chunk `4596714` offsets `192-199`; context: He then claimed refugee protection in 2013 based on the allegations described above.
- Evidence: `evidence_fact` cue `evidence` at chunk `4596715` offsets `776-784`; context: The RPD decision [8] The RPD made several findings including that: the applicant was generally credible about his abuse by his uncle, gang recruitment and training for the National Service; he demonstrated a nexus to a Convention due to his political opinion concerning his opposition to the National Service; his egregious delay in claiming protection was not consistent with his alleged fear; he had not rebutted the presumption of state protection regarding gang recruitment; he had not established that he would be personally harassed by Malaysian authorities for his protesting activities; he failed to provide objective evidence of the risk to his life in the National Service; and, he would not face a risk of torture upon return, although he may be fined or jailed for up to six months for not completing his National Service.

#### 11888:1:subtheme:3 · paragraphs 7-8

- Raw key terms: `applicant, claim, determinative, found, protection, respect, section, appeal`
- Display key terms: `determinative, protection, respect, section`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: determinative, protection, respect, section Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4596716` offsets `41-46`; context: [9] The RPD found that the determinative issue with respect to the applicant’s section 96 claim was his “egregious” delay in claiming protection and this was fatal to his claim.
- Evidence: `evidence_fact` cue `found that` at chunk `4596716` offsets `12-22`; context: [9] The RPD found that the determinative issue with respect to the applicant’s section 96 claim was his “egregious” delay in claiming protection and this was fatal to his claim.
- Evidence: `issue` cue `issues` at chunk `4596717` offsets `80-86`; context: [10] With respect to the section 97 claim, the RPD found that the determinative issues were the applicant’s failure to rebut the presumption of state protection and his failure to establish that he would face a risk to his life or danger of torture upon return.
- Evidence: `evidence_fact` cue `found that` at chunk `4596717` offsets `51-61`; context: [10] With respect to the section 97 claim, the RPD found that the determinative issues were the applicant’s failure to rebut the presumption of state protection and his failure to establish that he would face a risk to his life or danger of torture upon return.

#### 11888:1:subtheme:4 · paragraphs 9-11

- Raw key terms: `appeal, applicant, because, claim, considered, decision, evidence, fact`
- Display key terms: `because, considered, fact`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: because, considered, fact Position/evidence statements: [11] On the appeal, the applicant argued: • The RPD erred in finding that he had not rebutted the presumption of state protection; • The RPD erred in not fully assessing his personalized risk pursuant to section 97; and, | [14] The RAD considered the applicant’s request to submit five articles as new evidence. Rule/authority context: [11] On the appeal, the applicant argued: • The RPD erred in finding that he had not rebutted the presumption of state protection; • The RPD erred in not fully assessing his personalized risk pursuant to section 97; and, | [13] The RAD then considered the standard of review it should apply to the appeal of the RPD decision. Application context: • Did the RPD err in its finding of fact that the applicant was a supporter of the opposition and that he demonstrated a nexus to the Convention because of his imputed political opinion? | [13] The RAD then considered the standard of review it should apply to the appeal of the RPD decision. Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4596718` offsets `426-432`; context: The RAD decision [12] After noting the issues raised by the applicant in the appeal, the RAD stated that it focused on four issues:
• Did the RPD err in its finding of fact that the applicant’s allegations of fear of gangs were credible?
- Evidence: `party_position` cue `argued` at chunk `4596718` offsets `34-40`; context: [11] On the appeal, the applicant argued:
• The RPD erred in finding that he had not rebutted the presumption of state protection;
• The RPD erred in not fully assessing his personalized risk pursuant to section 97; and,
• That new evidence should be accepted in accordance with subsection 110(4) of the Act to establish an objective basis for his fear of dying in the National Service.
- Evidence: `evidence_fact` cue `evidence` at chunk `4596718` offsets `232-240`; context: [11] On the appeal, the applicant argued:
• The RPD erred in finding that he had not rebutted the presumption of state protection;
• The RPD erred in not fully assessing his personalized risk pursuant to section 97; and,
• That new evidence should be accepted in accordance with subsection 110(4) of the Act to establish an objective basis for his fear of dying in the National Service.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4596718` offsets `192-203`; context: [11] On the appeal, the applicant argued:
• The RPD erred in finding that he had not rebutted the presumption of state protection;
• The RPD erred in not fully assessing his personalized risk pursuant to section 97; and,
• That new evidence should be accepted in accordance with subsection 110(4) of the Act to establish an objective basis for his fear of dying in the National Service.
- Evidence: `reasoning_application` cue `because` at chunk `4596718` offsets `873-880`; context: • Did the RPD err in its finding of fact that the applicant was a supporter of the opposition and that he demonstrated a nexus to the Convention because of his imputed political opinion?
- Evidence: `issue` cue `issues` at chunk `4596719` offsets `630-636`; context: The RAD noted that the RPD is, in most cases, in the best position to assess credibility and to make findings on issues of law, fact or mixed fact and law and concluded that it should apply the standard of reasonableness to these aspects of the RPD’s decision.
- Evidence: `governing_rule` cue `standard of review` at chunk `4596719` offsets `33-51`; context: [13] The RAD then considered the standard of review it should apply to the appeal of the RPD decision.
- Evidence: `reasoning_application` cue `apply` at chunk `4596719` offsets `62-67`; context: [13] The RAD then considered the standard of review it should apply to the appeal of the RPD decision.
- Evidence: `party_position` cue `submit` at chunk `4596720` offsets `51-57`; context: [14] The RAD considered the applicant’s request to submit five articles as new evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4596720` offsets `79-87`; context: [14] The RAD considered the applicant’s request to submit five articles as new evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4596720` offsets `556-563`; context: The RAD also found the evidence was not admissible because it did “not pass the requirements of Raza” (this refers to Raza v Canada (Minister of Citizenship and Immigration), 2007 FCA 385, [2007] FCJ No 1632 [Raza]).

#### 11888:1:subtheme:5 · paragraphs 12-18

- Raw key terms: `applicant, found, evidence, finding, political, reasonable, claim, erred`
- Display key terms: `finding, political, reasonable, erred`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: finding, political, reasonable, erred Position/evidence statements: The RAD concluded that there was no sufficient evidence to ground a claim that the applicant would be perceived as having a political opinion opposing the government. Application context: Findings found by the RAD to be unreasonable [16] The RAD found that the RPD erred in finding that the applicant’s allegation of fear of gangs was credible because the RPD omitted to consider evidence central to that cla | [21] The RPDs finding that the applicant had not been personally harassed by authorities in Malaysia due to his alleged opposition or political profile was also found to be reasonable because there was no credible eviden Evidence spans paragraphs 12-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4596721` offsets `61-67`; context: [15] Although the RAD indicated that it focussed on the four issues set out above, the RAD considered all of the findings of the RPD and found some to be unreasonable and others to be reasonable, but concluded that the overall decision of the RPD was reasonable.
- Evidence: `evidence_fact` cue `found that` at chunk `4596721` offsets `321-331`; context: Findings found by the RAD to be unreasonable [16] The RAD found that the RPD erred in finding that the applicant’s allegation of fear of gangs was credible because the RPD omitted to consider evidence central to that claim.
- Evidence: `reasoning_application` cue `because` at chunk `4596721` offsets `419-426`; context: Findings found by the RAD to be unreasonable [16] The RAD found that the RPD erred in finding that the applicant’s allegation of fear of gangs was credible because the RPD omitted to consider evidence central to that claim.
- Evidence: `evidence_fact` cue `found that` at chunk `4596722` offsets `18-28`; context: [17] The RAD also found that the RPD’s finding that the applicant had established a nexus to a Convention ground of political opinion was not reasonable.
- Evidence: `counterargument_limitation` cue `but` at chunk `4596722` offsets `229-232`; context: The RAD noted that the applicant’s evidence to the Board was inconsistent, but generally he was only a silent supporter.
- Evidence: `party_position` cue `claim` at chunk `4596723` offsets `327-332`; context: The RAD concluded that there was no sufficient evidence to ground a claim that the applicant would be perceived as having a political opinion opposing the government.
- Evidence: `evidence_fact` cue `found that` at chunk `4596723` offsets `18-28`; context: [18] The RAD also found that RPD erred in finding that the applicant’s opposition to National Service was linked to imputed political opinion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4596725` offsets `214-222`; context: [21] The RPDs finding that the applicant had not been personally harassed by authorities in Malaysia due to his alleged opposition or political profile was also found to be reasonable because there was no credible evidence to support this claim.
- Evidence: `reasoning_application` cue `because` at chunk `4596725` offsets `184-191`; context: [21] The RPDs finding that the applicant had not been personally harassed by authorities in Malaysia due to his alleged opposition or political profile was also found to be reasonable because there was no credible evidence to support this claim.
- Evidence: `evidence_fact` cue `found that` at chunk `4596726` offsets `28-38`; context: [22] In conclusion, the RAD found that, based on its review of the totality of the evidence, the RPD erred in its treatment of the evidence regarding the applicant’s political opinion and his fear of gangs.
- Evidence: `evidence_fact` cue `found that` at chunk `4596727` offsets `13-23`; context: [23] The RAD found that the RPD did not err in finding that the applicant’s delay in claiming protection was egregious and not satisfactorily explained, noting this was not challenged in the appeal.

#### 11888:1:subtheme:6 · paragraphs 19-21

- Raw key terms: `applicant, erred, standard, adopting, appeal, argues, credibility, decision`
- Display key terms: `erred, standard, adopting, argues, credibility`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: erred, standard, adopting, argues, credibility Position/evidence statements: The Applicant’s Submissions [26] The applicant submits that the RAD explored issues, particularly the credibility findings of the RPD, that he did not raise in his appeal without notice to him and without any opportunity | [27] The applicant argues that the RAD erred in adopting reasonableness as the standard of review and applying judicial review principles to the appeal of the RPD decision. Rule/authority context: [24] The RAD found that the RPD’s finding that the applicant would not be personally subject to a risk to his life, to a risk of cruel or unusual treatment or punishment or to a danger of torture pursuant to section 97 w | [27] The applicant argues that the RAD erred in adopting reasonableness as the standard of review and applying judicial review principles to the appeal of the RPD decision. Application context: The Issues [25] This application raises several issues, including: the role of the RAD on appeal and the standard of review it should apply to a decision of the RPD; whether the RAD breached a duty of procedural fairness Evidence spans paragraphs 19-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4596728` offsets `239-245`; context: The Issues [25] This application raises several issues, including: the role of the RAD on appeal and the standard of review it should apply to a decision of the RPD; whether the RAD breached a duty of procedural fairness to the applicant by reviewing findings of credibility without providing the applicant an opportunity to address those findings and without holding an oral hearing; whether the RAD erred in rejecting new evidence; and, whether the RAD’s approach to this appeal could be perceived as demonstrating a reasonable apprehension of bias.
- Evidence: `party_position` cue `submits` at chunk `4596728` offsets `834-841`; context: The Applicant’s Submissions [26] The applicant submits that the RAD explored issues, particularly the credibility findings of the RPD, that he did not raise in his appeal without notice to him and without any opportunity for him to respond.
- Evidence: `evidence_fact` cue `found that` at chunk `4596728` offsets `13-23`; context: [24] The RAD found that the RPD’s finding that the applicant would not be personally subject to a risk to his life, to a risk of cruel or unusual treatment or punishment or to a danger of torture pursuant to section 97 was reasonable.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4596728` offsets `196-207`; context: [24] The RAD found that the RPD’s finding that the applicant would not be personally subject to a risk to his life, to a risk of cruel or unusual treatment or punishment or to a danger of torture pursuant to section 97 was reasonable.
- Evidence: `reasoning_application` cue `apply` at chunk `4596728` offsets `369-374`; context: The Issues [25] This application raises several issues, including: the role of the RAD on appeal and the standard of review it should apply to a decision of the RPD; whether the RAD breached a duty of procedural fairness to the applicant by reviewing findings of credibility without providing the applicant an opportunity to address those findings and without holding an oral hearing; whether the RAD erred in rejecting new evidence; and, whether the RAD’s approach to this appeal could be perceived as demonstrating a reasonable apprehension of bias.
- Evidence: `party_position` cue `argues` at chunk `4596729` offsets `19-25`; context: [27] The applicant argues that the RAD erred in adopting reasonableness as the standard of review and applying judicial review principles to the appeal of the RPD decision.
- Evidence: `governing_rule` cue `standard of review` at chunk `4596729` offsets `79-97`; context: [27] The applicant argues that the RAD erred in adopting reasonableness as the standard of review and applying judicial review principles to the appeal of the RPD decision.
- Evidence: `party_position` cue `argues` at chunk `4596730` offsets `246-252`; context: The applicant argues that the RAD erred in not holding an oral hearing in accordance with subsection 110(6) of the Act and/or in accordance with the principles of procedural fairness.
- Evidence: `governing_rule` cue `principles` at chunk `4596730` offsets `381-391`; context: The applicant argues that the RAD erred in not holding an oral hearing in accordance with subsection 110(6) of the Act and/or in accordance with the principles of procedural fairness.

#### 11888:1:subtheme:7 · paragraphs 22-23

- Raw key terms: `appeal, applicant, submits, addresses, admissibility, admitted, adverse, appellants`
- Display key terms: `submits, addresses, admissibility, admitted, adverse, appellants`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: submits, addresses, admissibility, admitted, adverse, appellants Position/evidence statements: [29] The applicant further argues that the RAD erred in rejecting his new evidence, including by relying on the test in Raza. | The applicant submits that the RAD’s adverse credibility findings could disadvantage him in other future applications. Rule/authority context: The applicant argues that Raza addresses the admissibility of new evidence of risk on a Pre-Removal Risk Assessment [PRRA], which is a completely different context, and should not apply to whether new evidence should be  Application context: The applicant argues that Raza addresses the admissibility of new evidence of risk on a Pre-Removal Risk Assessment [PRRA], which is a completely different context, and should not apply to whether new evidence should be  | [30] The applicant also suggests that the conduct of the RAD could be perceived as showing a reasonable apprehension of bias because the RAD went well beyond the issues he raised on appeal to ensure that his appeal would Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4596731` offsets `315-322`; context: The applicant argues that Raza addresses the admissibility of new evidence of risk on a Pre-Removal Risk Assessment [PRRA], which is a completely different context, and should not apply to whether new evidence should be admitted on an appeal pursuant to subsection 110(4).
- Evidence: `party_position` cue `argues` at chunk `4596731` offsets `27-33`; context: [29] The applicant further argues that the RAD erred in rejecting his new evidence, including by relying on the test in Raza.
- Evidence: `evidence_fact` cue `evidence` at chunk `4596731` offsets `74-82`; context: [29] The applicant further argues that the RAD erred in rejecting his new evidence, including by relying on the test in Raza.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4596731` offsets `368-379`; context: The applicant argues that Raza addresses the admissibility of new evidence of risk on a Pre-Removal Risk Assessment [PRRA], which is a completely different context, and should not apply to whether new evidence should be admitted on an appeal pursuant to subsection 110(4).
- Evidence: `reasoning_application` cue `apply` at chunk `4596731` offsets `306-311`; context: The applicant argues that Raza addresses the admissibility of new evidence of risk on a Pre-Removal Risk Assessment [PRRA], which is a completely different context, and should not apply to whether new evidence should be admitted on an appeal pursuant to subsection 110(4).
- Evidence: `issue` cue `issues` at chunk `4596732` offsets `162-168`; context: [30] The applicant also suggests that the conduct of the RAD could be perceived as showing a reasonable apprehension of bias because the RAD went well beyond the issues he raised on appeal to ensure that his appeal would not succeed.
- Evidence: `party_position` cue `submits` at chunk `4596732` offsets `248-255`; context: The applicant submits that the RAD’s adverse credibility findings could disadvantage him in other future applications.
- Evidence: `reasoning_application` cue `because` at chunk `4596732` offsets `125-132`; context: [30] The applicant also suggests that the conduct of the RAD could be perceived as showing a reasonable apprehension of bias because the RAD went well beyond the issues he raised on appeal to ensure that his appeal would not succeed.

#### 11888:1:subtheme:8 · paragraphs 24-28

- Raw key terms: `respondent, reasonableness, respect, review, standard, submits, appeal, apply`
- Display key terms: `reasonableness, respect, review, standard, submits, apply`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: reasonableness, respect, review, standard, submits, apply Position/evidence statements: [32] With respect to the applicable standard of review, the respondent submits that this Court should apply the reasonableness standard to the issue of the RAD’s choice of the reasonableness standard of review to its app | [33] The respondent also submits that the RAD did not err in with respect to the standard of review; the RAD should apply the reasonableness standard to appeals from the RPD on questions of fact and mixed fact and law. Rule/authority context: [32] With respect to the applicable standard of review, the respondent submits that this Court should apply the reasonableness standard to the issue of the RAD’s choice of the reasonableness standard of review to its app | [33] The respondent also submits that the RAD did not err in with respect to the standard of review; the RAD should apply the reasonableness standard to appeals from the RPD on questions of fact and mixed fact and law. Application context: [32] With respect to the applicable standard of review, the respondent submits that this Court should apply the reasonableness standard to the issue of the RAD’s choice of the reasonableness standard of review to its app | [33] The respondent also submits that the RAD did not err in with respect to the standard of review; the RAD should apply the reasonableness standard to appeals from the RPD on questions of fact and mixed fact and law. Evidence spans paragraphs 24-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4596733` offsets `143-148`; context: [32] With respect to the applicable standard of review, the respondent submits that this Court should apply the reasonableness standard to the issue of the RAD’s choice of the reasonableness standard of review to its appeal of decisions of the RPD.
- Evidence: `party_position` cue `submits` at chunk `4596733` offsets `71-78`; context: [32] With respect to the applicable standard of review, the respondent submits that this Court should apply the reasonableness standard to the issue of the RAD’s choice of the reasonableness standard of review to its appeal of decisions of the RPD.
- Evidence: `governing_rule` cue `standard of review` at chunk `4596733` offsets `36-54`; context: [32] With respect to the applicable standard of review, the respondent submits that this Court should apply the reasonableness standard to the issue of the RAD’s choice of the reasonableness standard of review to its appeal of decisions of the RPD.
- Evidence: `reasoning_application` cue `apply` at chunk `4596733` offsets `102-107`; context: [32] With respect to the applicable standard of review, the respondent submits that this Court should apply the reasonableness standard to the issue of the RAD’s choice of the reasonableness standard of review to its appeal of decisions of the RPD.
- Evidence: `party_position` cue `submits` at chunk `4596734` offsets `25-32`; context: [33] The respondent also submits that the RAD did not err in with respect to the standard of review; the RAD should apply the reasonableness standard to appeals from the RPD on questions of fact and mixed fact and law.
- Evidence: `governing_rule` cue `standard of review` at chunk `4596734` offsets `81-99`; context: [33] The respondent also submits that the RAD did not err in with respect to the standard of review; the RAD should apply the reasonableness standard to appeals from the RPD on questions of fact and mixed fact and law.
- Evidence: `reasoning_application` cue `apply` at chunk `4596734` offsets `116-121`; context: [33] The respondent also submits that the RAD did not err in with respect to the standard of review; the RAD should apply the reasonableness standard to appeals from the RPD on questions of fact and mixed fact and law.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4596735` offsets `35-48`; context: [34] The respondent notes that the jurisprudence of this Court supports the view that the RAD may defer to findings of the RPD regarding credibility.
- Evidence: `party_position` cue `submits` at chunk `4596736` offsets `62-69`; context: [35] With respect to the merits of the appeal, the respondent submits that the RAD reasonably rejected the new evidence in accordance with the RAD Rules which require the appellant to indicate how the new evidence relates to his appeal and in accordance with subsection 110(4).
- Evidence: `evidence_fact` cue `evidence` at chunk `4596736` offsets `111-119`; context: [35] With respect to the merits of the appeal, the respondent submits that the RAD reasonably rejected the new evidence in accordance with the RAD Rules which require the appellant to indicate how the new evidence relates to his appeal and in accordance with subsection 110(4).
- Evidence: `counterargument_limitation` cue `although` at chunk `4596736` offsets `343-351`; context: It was also reasonable for the RAD to consider the test in Raza, although it dealt with the application of section 113 of the Act, given the analogous wording of subsection 110(4).
- Evidence: `evidence_fact` cue `evidence` at chunk `4596737` offsets `42-50`; context: [36] Moreover, the RAD considered the new evidence and provided reasons for not accepting it; the articles did not address the basis for the applicant’s fear but referred to a variety of illnesses, injuries and individual disputes between members of the National Service.
- Evidence: `counterargument_limitation` cue `but` at chunk `4596737` offsets `158-161`; context: [36] Moreover, the RAD considered the new evidence and provided reasons for not accepting it; the articles did not address the basis for the applicant’s fear but referred to a variety of illnesses, injuries and individual disputes between members of the National Service.

#### 11888:1:subtheme:9 · paragraphs 29-31

- Raw key terms: `appeal, applicant, challenged, finding, hearing, respondent, section, submits`
- Display key terms: `challenged, finding, hearing, section, submits`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: challenged, finding, hearing, section, submits Position/evidence statements: [37] The respondent further submits that the RAD did not err by not holding an oral hearing. | [38] With respect to the applicant’s reference to bias by the RAD, the respondent notes the high threshold to be met and submits that the record does not disclose any evidence to support such an allegation. Rule/authority context: The Applicant Is Not a Convention Refugee Pursuant to Section 96 [39] The RPD found that the applicant’s delay in claiming protection was egregious and fatal to his claim pursuant to section 96. | [40] Despite the RAD’s confirmation of this finding on the basis of the reasonableness standard of review, the RAD noted that this finding was not challenged on appeal. Evidence spans paragraphs 29-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4596738` offsets `97-102`; context: The issue of credibility was not central to the RAD’s findings as there were many findings to support the RPD’s decision and the RAD’s decision.
- Evidence: `party_position` cue `submits` at chunk `4596738` offsets `28-35`; context: [37] The respondent further submits that the RAD did not err by not holding an oral hearing.
- Evidence: `party_position` cue `submits` at chunk `4596739` offsets `121-128`; context: [38] With respect to the applicant’s reference to bias by the RAD, the respondent notes the high threshold to be met and submits that the record does not disclose any evidence to support such an allegation.
- Evidence: `evidence_fact` cue `record` at chunk `4596739` offsets `138-144`; context: [38] With respect to the applicant’s reference to bias by the RAD, the respondent notes the high threshold to be met and submits that the record does not disclose any evidence to support such an allegation.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `4596739` offsets `249-260`; context: The Applicant Is Not a Convention Refugee Pursuant to Section 96 [39] The RPD found that the applicant’s delay in claiming protection was egregious and fatal to his claim pursuant to section 96.
- Evidence: `governing_rule` cue `standard of review` at chunk `4596740` offsets `87-105`; context: [40] Despite the RAD’s confirmation of this finding on the basis of the reasonableness standard of review, the RAD noted that this finding was not challenged on appeal.

#### 11888:1:subtheme:10 · paragraphs 32-41

- Raw key terms: `review, standard, appeal, court, applied, apply, canada, citizenship`
- Display key terms: `review, standard, applied, apply`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: review, standard, applied, apply Position/evidence statements: [41] Therefore, the only issues on the appeal before the RAD related to the section 97 claim. Rule/authority context: The Standard of Review To be applied by the Court [42] The jurisprudence continues to develop with respect to the standard of review that the Court should apply to the RAD’s determination of the appropriate standard of r | [43] Several recent cases have addressed the standard of review to be applied by this Court to decisions of the RAD on the issue of the standard of review the RAD should apply in appeals from the RPD. Application context: [41] Therefore, the only issues on the appeal before the RAD related to the section 97 claim. | [43] Several recent cases have addressed the standard of review to be applied by this Court to decisions of the RAD on the issue of the standard of review the RAD should apply in appeals from the RPD. Evidence spans paragraphs 32-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4596741` offsets `25-31`; context: [41] Therefore, the only issues on the appeal before the RAD related to the section 97 claim.
- Evidence: `party_position` cue `claim` at chunk `4596741` offsets `87-92`; context: [41] Therefore, the only issues on the appeal before the RAD related to the section 97 claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4596741` offsets `579-587`; context: The Standard of Review To be applied by the Court [42] The jurisprudence continues to develop with respect to the standard of review that the Court should apply to the RAD’s determination of the appropriate standard of review and to other specific determinations, including the RAD’s credibility findings and findings whether to admit new evidence.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4596741` offsets `244-262`; context: The Standard of Review To be applied by the Court [42] The jurisprudence continues to develop with respect to the standard of review that the Court should apply to the RAD’s determination of the appropriate standard of review and to other specific determinations, including the RAD’s credibility findings and findings whether to admit new evidence.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4596741` offsets `5-14`; context: [41] Therefore, the only issues on the appeal before the RAD related to the section 97 claim.
- Evidence: `issue` cue `issue` at chunk `4596742` offsets `123-128`; context: [43] Several recent cases have addressed the standard of review to be applied by this Court to decisions of the RAD on the issue of the standard of review the RAD should apply in appeals from the RPD.
- Evidence: `governing_rule` cue `standard of review` at chunk `4596742` offsets `45-63`; context: [43] Several recent cases have addressed the standard of review to be applied by this Court to decisions of the RAD on the issue of the standard of review the RAD should apply in appeals from the RPD.
- Evidence: `reasoning_application` cue `applied` at chunk `4596742` offsets `70-77`; context: [43] Several recent cases have addressed the standard of review to be applied by this Court to decisions of the RAD on the issue of the standard of review the RAD should apply in appeals from the RPD.
- Evidence: `evidence_fact` cue `found that` at chunk `4596743` offsets `234-244`; context: Justice Gagné found that this Court should apply the reasonableness standard to the review of decisions of the RAD on its choice of the standard of review, noting that reasonableness is the presumptive standard and that there are no other circumstances to justify departing from the presumptive standard.
- Evidence: `governing_rule` cue `standard of review` at chunk `4596743` offsets `356-374`; context: Justice Gagné found that this Court should apply the reasonableness standard to the review of decisions of the RAD on its choice of the standard of review, noting that reasonableness is the presumptive standard and that there are no other circumstances to justify departing from the presumptive standard.
- Evidence: `reasoning_application` cue `apply` at chunk `4596743` offsets `263-268`; context: Justice Gagné found that this Court should apply the reasonableness standard to the review of decisions of the RAD on its choice of the standard of review, noting that reasonableness is the presumptive standard and that there are no other circumstances to justify departing from the presumptive standard.
- Evidence: `evidence_fact` cue `evidence` at chunk `4596745` offsets `46-54`; context: [46] With respect to the admissibility of new evidence, in Singh v Canada (Minister of Citizenship and Immigration), 2014 FC 1022 at paras 36-42, 246 ACWS (3d) 433 [Singh], Justice Gagné held that the standard of reasonableness applies to questions regarding the admissibility of new evidence before the RAD (see also Khachatourian v Canada (Citizenship and Immigration), 2015 FC 182 at para 37, [2015] FCJ No 156 [Khachatourian]).
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4596745` offsets `637-650`; context: To be applied by the RAD to decisions of the RPD [47] I acknowledge the respondent’s position that the RAD should apply the reasonableness standard to the appeal of RPD decisions, but remain guided by the jurisprudence of this Court.
- Evidence: `reasoning_application` cue `applies` at chunk `4596745` offsets `228-235`; context: [46] With respect to the admissibility of new evidence, in Singh v Canada (Minister of Citizenship and Immigration), 2014 FC 1022 at paras 36-42, 246 ACWS (3d) 433 [Singh], Justice Gagné held that the standard of reasonableness applies to questions regarding the admissibility of new evidence before the RAD (see also Khachatourian v Canada (Citizenship and Immigration), 2015 FC 182 at para 37, [2015] FCJ No 156 [Khachatourian]).
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4596746` offsets `9-22`; context: [48] The jurisprudence has consistently held that it is a reviewable error for the RAD to perform a judicial review function and apply the reasonableness standard to the RPD’s decision.
- Evidence: `reasoning_application` cue `apply` at chunk `4596746` offsets `129-134`; context: [48] The jurisprudence has consistently held that it is a reviewable error for the RAD to perform a judicial review function and apply the reasonableness standard to the RPD’s decision.
- Evidence: `evidence_fact` cue `found that` at chunk `4596747` offsets `69-79`; context: [49] With respect to questions of credibility, the jurisprudence has found that the RAD may or should defer to the RPD because the RPD has heard the witnesses directly, has had an opportunity to probe their testimony or has had some advantage not enjoyed by the RAD; see, for example, Huruglica, at para 55; Iyamuremye, at para 40; Akuffo, at para 27; Nahal v Canada (Minister of Citizenship and Immigration), 2014 FC 1208 at para 25, [2014] FCJ No 1254.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4596747` offsets `51-64`; context: [49] With respect to questions of credibility, the jurisprudence has found that the RAD may or should defer to the RPD because the RPD has heard the witnesses directly, has had an opportunity to probe their testimony or has had some advantage not enjoyed by the RAD; see, for example, Huruglica, at para 55; Iyamuremye, at para 40; Akuffo, at para 27; Nahal v Canada (Minister of Citizenship and Immigration), 2014 FC 1208 at para 25, [2014] FCJ No 1254.
- Evidence: `reasoning_application` cue `because` at chunk `4596747` offsets `119-126`; context: [49] With respect to questions of credibility, the jurisprudence has found that the RAD may or should defer to the RPD because the RPD has heard the witnesses directly, has had an opportunity to probe their testimony or has had some advantage not enjoyed by the RAD; see, for example, Huruglica, at para 55; Iyamuremye, at para 40; Akuffo, at para 27; Nahal v Canada (Minister of Citizenship and Immigration), 2014 FC 1208 at para 25, [2014] FCJ No 1254.
- Evidence: `reasoning_application` cue `applied` at chunk `4596748` offsets `88-95`; context: [50] In the present case, the RAD erred in determining that the reasonableness standard applied and in taking a judicial review approach to the appeal.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4596749` offsets `80-93`; context: [51] I note, however, that the RAD did not have the guidance of the more recent jurisprudence at the time of the appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4596750` offsets `222-230`; context: In the present case, the RAD analyzed the evidence on the record to conclude that the specific credibility findings were not supported and, in fact, were contradicted.
- Evidence: `governing_rule` cue `standard of review` at chunk `4596750` offsets `562-580`; context: The RAD would have logically reached the same finding – that the credibility findings were flawed – if it had applied a less deferential standard of review.
- Evidence: `reasoning_application` cue `conclude` at chunk `4596750` offsets `248-256`; context: In the present case, the RAD analyzed the evidence on the record to conclude that the specific credibility findings were not supported and, in fact, were contradicted.

#### 11888:1:subtheme:11 · paragraphs 42-43

- Raw key terms: `appeal, credibility, findings, accept, applicable, applicant, based, below`
- Display key terms: `credibility, findings, accept, applicable, based, below`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: credibility, findings, accept, applicable, based, below Evidence spans paragraphs 42-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4596751` offsets `99-105`; context: [53] However, the credibility findings were not determinative of the section 96 claim and the only issues on the appeal related to the section 97 claim.
- Evidence: `issue` cue `whether` at chunk `4596752` offsets `267-274`; context: The New Evidence [55] The RAD’s determination whether to accept new evidence on the appeal is its own finding, based on the Act and the applicable Rules.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4596752` offsets `229-237`; context: The New Evidence [55] The RAD’s determination whether to accept new evidence on the appeal is its own finding, based on the Act and the applicable Rules.

#### 11888:1:subtheme:12 · paragraphs 44-45

- Raw key terms: `appeal, applicant, evidence, factor, factors, materiality, raza, relevance`
- Display key terms: `factor, factors, materiality, raza, relevance`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: factor, factors, materiality, raza, relevance Rule/authority context: [56] I agree with the applicant that the Raza test should not automatically apply to a determination under subsection 110(4). Application context: [56] I agree with the applicant that the Raza test should not automatically apply to a determination under subsection 110(4). Evidence spans paragraphs 44-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4596753` offsets `298-305`; context: The Raza test or factors, which include consideration of credibility, relevance, newness and materiality, are not necessarily applicable to subsection 110(4) which governs whether new evidence is admissible in the context of an appeal as opposed to a PRRA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4596753` offsets `310-318`; context: The Raza test or factors, which include consideration of credibility, relevance, newness and materiality, are not necessarily applicable to subsection 110(4) which governs whether new evidence is admissible in the context of an appeal as opposed to a PRRA.
- Evidence: `governing_rule` cue `under` at chunk `4596753` offsets `101-106`; context: [56] I agree with the applicant that the Raza test should not automatically apply to a determination under subsection 110(4).
- Evidence: `reasoning_application` cue `apply` at chunk `4596753` offsets `76-81`; context: [56] I agree with the applicant that the Raza test should not automatically apply to a determination under subsection 110(4).
- Evidence: `evidence_fact` cue `evidence` at chunk `4596754` offsets `182-190`; context: The RAD stated more generally that the new evidence did not meet the requirements of Raza.

#### 11888:1:subtheme:13 · paragraphs 46-47

- Raw key terms: `appeal, case, evidence, hearing, rules, section, subject, accept`
- Display key terms: `case, hearing, rules, section, subject, accept`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position Display terms: case, hearing, rules, section, subject, accept Position/evidence statements: If the RAD refers to Raza for guidance, given the analogous wording of the provisions, the RAD must consider how those factors should be adapted to the context of new evidence submitted on an appeal of specific issues. Rule/authority context: In the present case, the applicant sought to admit new evidence related to his allegations of personalised risk under section 97. Operative outcome context: [58] Given that the application for the judicial review must be allowed based on the RAD’s error in applying the reasonableness standard, on the reconsideration of the appeal, the RAD should consider whether the new evid Evidence spans paragraphs 46-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4596755` offsets `200-207`; context: [58] Given that the application for the judicial review must be allowed based on the RAD’s error in applying the reasonableness standard, on the reconsideration of the appeal, the RAD should consider whether the new evidence meets the requirements of the Act and the Rules.
- Evidence: `party_position` cue `submitted` at chunk `4596755` offsets `450-459`; context: If the RAD refers to Raza for guidance, given the analogous wording of the provisions, the RAD must consider how those factors should be adapted to the context of new evidence submitted on an appeal of specific issues.
- Evidence: `evidence_fact` cue `evidence` at chunk `4596755` offsets `216-224`; context: [58] Given that the application for the judicial review must be allowed based on the RAD’s error in applying the reasonableness standard, on the reconsideration of the appeal, the RAD should consider whether the new evidence meets the requirements of the Act and the Rules.
- Evidence: `governing_rule` cue `under` at chunk `4596755` offsets `605-610`; context: In the present case, the applicant sought to admit new evidence related to his allegations of personalised risk under section 97.
- Evidence: `disposition` cue `allowed` at chunk `4596755` offsets `64-71`; context: [58] Given that the application for the judicial review must be allowed based on the RAD’s error in applying the reasonableness standard, on the reconsideration of the appeal, the RAD should consider whether the new evidence meets the requirements of the Act and the Rules.
- Evidence: `evidence_fact` cue `record` at chunk `4596756` offsets `160-166`; context: 1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division, and may accept documentary evidence and written submissions from the Minister and the person who is the subject of the appeal and, in the case of a matter that is conducted before a panel of three members, written submissions from a representative or agent of the United Nations High Commissioner for Refugees and any other person described in the rules of the Board.

#### 11888:1:subtheme:14 · paragraphs 48-50

- Raw key terms: `credibility, hearing, appeal, applicant, because, central, claim, decision`
- Display key terms: `credibility, hearing, because, central`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: credibility, hearing, because, central Position/evidence statements: [62] The applicant argues that the RAD should have held an oral hearing because it reviewed the RPD’s credibility findings, which the applicant had not raised on appeal, but did not provide any opportunity for the applic Application context: [62] The applicant argues that the RAD should have held an oral hearing because it reviewed the RPD’s credibility findings, which the applicant had not raised on appeal, but did not provide any opportunity for the applic | [63] The Board’s discretion to hold a hearing would not come into play in these circumstances because the RAD relied on the record of the RPD and not on other documentary evidence. Evidence spans paragraphs 48-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4596757` offsets `399-404`; context: [61] Subsection 110(6) gives the RAD discretion to hold a hearing where three conditions are met:
(6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4596757` offsets `190-198`; context: [61] Subsection 110(6) gives the RAD discretion to hold a hearing where three conditions are met:
(6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
- Evidence: `party_position` cue `argues` at chunk `4596758` offsets `19-25`; context: [62] The applicant argues that the RAD should have held an oral hearing because it reviewed the RPD’s credibility findings, which the applicant had not raised on appeal, but did not provide any opportunity for the applicant to make submissions to respond to the RAD’s concerns.
- Evidence: `reasoning_application` cue `because` at chunk `4596758` offsets `72-79`; context: [62] The applicant argues that the RAD should have held an oral hearing because it reviewed the RPD’s credibility findings, which the applicant had not raised on appeal, but did not provide any opportunity for the applicant to make submissions to respond to the RAD’s concerns.
- Evidence: `counterargument_limitation` cue `but` at chunk `4596758` offsets `170-173`; context: [62] The applicant argues that the RAD should have held an oral hearing because it reviewed the RPD’s credibility findings, which the applicant had not raised on appeal, but did not provide any opportunity for the applicant to make submissions to respond to the RAD’s concerns.
- Evidence: `evidence_fact` cue `record` at chunk `4596759` offsets `124-130`; context: [63] The Board’s discretion to hold a hearing would not come into play in these circumstances because the RAD relied on the record of the RPD and not on other documentary evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4596759` offsets `94-101`; context: [63] The Board’s discretion to hold a hearing would not come into play in these circumstances because the RAD relied on the record of the RPD and not on other documentary evidence.

#### 11888:1:subtheme:15 · paragraphs 51-52

- Raw key terms: `appellate, case, issue, issues, principles, raise, above, addressed`
- Display key terms: `appellate, case, issues, principles, raise, above, addressed`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: appellate, case, issues, principles, raise, above, addressed Rule/authority context: Procedural Fairness [65] As noted above, the RAD should assume its appellate role rather than adopt judicial review principles. | Although Mian was a criminal case, the principles have been applied in other proceedings, including the administrative context. Application context: Although Mian was a criminal case, the principles have been applied in other proceedings, including the administrative context. Evidence spans paragraphs 51-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4596760` offsets `18-23`; context: [64] However, the issue of whether the RAD should have provided the applicant with an opportunity to respond to the RAD’s concerns about the RPD’s credibility findings requires further consideration, apart from the requirements of subsection 110(6).
- Evidence: `governing_rule` cue `principles` at chunk `4596760` offsets `366-376`; context: Procedural Fairness [65] As noted above, the RAD should assume its appellate role rather than adopt judicial review principles.
- Evidence: `issue` cue `issues` at chunk `4596761` offsets `154-160`; context: [66] In R v Mian, 2014 SCC 54, [2014] 2 SCR 689 [Mian], the Supreme Court of Canada addressed the scope of an appellate court’s jurisdiction to raise new issues, what constitutes a new issue, when such jurisdiction should be exercised and the procedures to be followed.
- Evidence: `governing_rule` cue `principles` at chunk `4596761` offsets `309-319`; context: Although Mian was a criminal case, the principles have been applied in other proceedings, including the administrative context.
- Evidence: `reasoning_application` cue `applied` at chunk `4596761` offsets `330-337`; context: Although Mian was a criminal case, the principles have been applied in other proceedings, including the administrative context.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4596761` offsets `270-278`; context: Although Mian was a criminal case, the principles have been applied in other proceedings, including the administrative context.

#### 11888:1:subtheme:16 · paragraphs 53-54

- Raw key terms: `court, issue, para, able, added, address, adequately, advance`
- Display key terms: `para, able, added, address, adequately, advance`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: para, able, added, address, adequately, advance Rule/authority context: [67] The Court defined a “new issue” at para 30: An issue is new when it raises a new basis for potentially finding error in the decision under appeal beyond the grounds of appeal as framed by the parties. Evidence spans paragraphs 53-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4596762` offsets `30-35`; context: [67] The Court defined a “new issue” at para 30:
An issue is new when it raises a new basis for potentially finding error in the decision under appeal beyond the grounds of appeal as framed by the parties.
- Evidence: `governing_rule` cue `under` at chunk `4596762` offsets `138-143`; context: [67] The Court defined a “new issue” at para 30:
An issue is new when it raises a new basis for potentially finding error in the decision under appeal beyond the grounds of appeal as framed by the parties.
- Evidence: `issue` cue `issue` at chunk `4596763` offsets `102-107`; context: [68] The Court concluded at para 41, that although an appellate court has jurisdiction to raise a new issue, this would be rare and only “when failing to do so would risk an injustice.
- Evidence: `evidence_fact` cue `record` at chunk `4596763` offsets `246-252`; context: The court should also consider whether there is a sufficient record on which to raise the issue and whether raising the issue would result in procedural prejudice to any party.

#### 11888:1:subtheme:17 · paragraphs 55-56

- Raw key terms: `appellate, court, issue, opportunity, parties, respond, basis, consider`
- Display key terms: `appellate, opportunity, respond, basis, consider`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: appellate, opportunity, respond, basis, consider Evidence spans paragraphs 55-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4596764` offsets `106-112`; context: [69] The Court elaborated on the considerations regarding the discretion of appellate courts to raise new issues, including: the jurisdiction of the court to consider the issue; whether there is a sufficient basis in the record on which to resolve the issue; and, whether there would be any procedural prejudice to either party (i.
- Evidence: `evidence_fact` cue `record` at chunk `4596764` offsets `221-227`; context: [69] The Court elaborated on the considerations regarding the discretion of appellate courts to raise new issues, including: the jurisdiction of the court to consider the issue; whether there is a sufficient basis in the record on which to resolve the issue; and, whether there would be any procedural prejudice to either party (i.
- Evidence: `issue` cue `issue` at chunk `4596765` offsets `64-69`; context: [70] The Court noted that when the appellate court raises a new issue, generally, the parties must be notified and given the opportunity to respond to the new issue.

#### 11888:1:subtheme:18 · paragraphs 57-58

- Raw key terms: `appeals, injustice, issue, make, opportunity, principles, submissions, adapted`
- Display key terms: `appeals, injustice, make, opportunity, principles, submissions, adapted`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: appeals, injustice, make, opportunity, principles, submissions, adapted Rule/authority context: [71] In my view, these principles should apply beyond the context of criminal appeals and, with the necessary modifications, to the context of appeals before the RAD. | If the principles in Mian are adapted and applied to appeals conducted by the RAD, at minimum, the RAD should have considered whether the credibility findings were new issues and whether it was essential to address these Application context: [71] In my view, these principles should apply beyond the context of criminal appeals and, with the necessary modifications, to the context of appeals before the RAD. | If the principles in Mian are adapted and applied to appeals conducted by the RAD, at minimum, the RAD should have considered whether the credibility findings were new issues and whether it was essential to address these Evidence spans paragraphs 57-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4596766` offsets `204-209`; context: The RAD should first consider if the issue is “new” and if failing to raise the new issue would risk injustice.
- Evidence: `governing_rule` cue `principles` at chunk `4596766` offsets `23-33`; context: [71] In my view, these principles should apply beyond the context of criminal appeals and, with the necessary modifications, to the context of appeals before the RAD.
- Evidence: `reasoning_application` cue `apply` at chunk `4596766` offsets `41-46`; context: [71] In my view, these principles should apply beyond the context of criminal appeals and, with the necessary modifications, to the context of appeals before the RAD.
- Evidence: `issue` cue `issues` at chunk `4596767` offsets `97-103`; context: [72] In conducting a full fact based appeal, the RAD would not be precluded from considering new issues not raised on the appeal.
- Evidence: `governing_rule` cue `principles` at chunk `4596767` offsets `352-362`; context: If the principles in Mian are adapted and applied to appeals conducted by the RAD, at minimum, the RAD should have considered whether the credibility findings were new issues and whether it was essential to address these findings to avoid an injustice.
- Evidence: `reasoning_application` cue `applied` at chunk `4596767` offsets `387-394`; context: If the principles in Mian are adapted and applied to appeals conducted by the RAD, at minimum, the RAD should have considered whether the credibility findings were new issues and whether it was essential to address these findings to avoid an injustice.

#### 11888:1:subtheme:19 · paragraphs 59-61

- Raw key terms: `affecting, based, canada, decision, decisions, fairness, issues, noted`
- Display key terms: `affecting, based, decisions, fairness, issues, noted`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, reasoning_application Display terms: affecting, based, decisions, fairness, issues, noted Rule/authority context: [74] Whether or not the principles in Mian should be applied by the RAD, it is a basic principle of natural justice and procedural fairness that a party should have an opportunity to respond to new issues and concerns th Application context: [74] Whether or not the principles in Mian should be applied by the RAD, it is a basic principle of natural justice and procedural fairness that a party should have an opportunity to respond to new issues and concerns th Operative outcome context: The RAD need not have revisited these issues given that the section 96 claim was denied based on the applicant’s delay in seeking protection and this finding was not appealed. Evidence spans paragraphs 59-61. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4596768` offsets `341-347`; context: The RAD need not have revisited these issues given that the section 96 claim was denied based on the applicant’s delay in seeking protection and this finding was not appealed.
- Evidence: `counterargument_limitation` cue `but` at chunk `4596768` offsets `92-95`; context: [73] As noted above, the determinative finding for the section 96 claim was not credibility but the applicant’s delay in seeking protection.
- Evidence: `disposition` cue `denied` at chunk `4596768` offsets `384-390`; context: The RAD need not have revisited these issues given that the section 96 claim was denied based on the applicant’s delay in seeking protection and this finding was not appealed.
- Evidence: `issue` cue `Whether` at chunk `4596769` offsets `5-12`; context: [74] Whether or not the principles in Mian should be applied by the RAD, it is a basic principle of natural justice and procedural fairness that a party should have an opportunity to respond to new issues and concerns that will have a bearing on a decision affecting them.
- Evidence: `governing_rule` cue `principles` at chunk `4596769` offsets `24-34`; context: [74] Whether or not the principles in Mian should be applied by the RAD, it is a basic principle of natural justice and procedural fairness that a party should have an opportunity to respond to new issues and concerns that will have a bearing on a decision affecting them.
- Evidence: `reasoning_application` cue `applied` at chunk `4596769` offsets `53-60`; context: [74] Whether or not the principles in Mian should be applied by the RAD, it is a basic principle of natural justice and procedural fairness that a party should have an opportunity to respond to new issues and concerns that will have a bearing on a decision affecting them.

#### 11888:1:subtheme:20 · paragraphs 62-63

- Raw key terms: `bias, actual, allegations, although, applicant, apprehension, board, canada`
- Display key terms: `bias, actual, allegations, although, apprehension`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: bias, actual, allegations, although, apprehension Application context: The RAD did not demonstrate bias [77] The test for determining whether actual bias or a reasonable apprehension of bias exists is what an informed person, viewing the matter realistically and practically – and having tho Evidence spans paragraphs 62-63. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4596771` offsets `335-342`; context: The RAD did not demonstrate bias [77] The test for determining whether actual bias or a reasonable apprehension of bias exists is what an informed person, viewing the matter realistically and practically – and having thought the matter through – would conclude and whether that informed person would think that the decision maker, in this case the RAD, either consciously or unconsciously, would not decide fairly (Committee for Justice and Liberty v Canada (National Energy Board), [1978] 1 SCR 369 at 394, 68 DLR (3d) 716).
- Evidence: `reasoning_application` cue `conclude` at chunk `4596771` offsets `524-532`; context: The RAD did not demonstrate bias [77] The test for determining whether actual bias or a reasonable apprehension of bias exists is what an informed person, viewing the matter realistically and practically – and having thought the matter through – would conclude and whether that informed person would think that the decision maker, in this case the RAD, either consciously or unconsciously, would not decide fairly (Committee for Justice and Liberty v Canada (National Energy Board), [1978] 1 SCR 369 at 394, 68 DLR (3d) 716).

#### 11888:1:subtheme:21 · paragraphs 64-65

- Raw key terms: `record, allowed, although, appears, appellate, applicant, application, beyond`
- Display key terms: `allowed, although, appears, appellate, beyond`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: allowed, although, appears, appellate, beyond Operative outcome context: The application for judicial review is allowed with respect to the section 97 claim; and 2. Evidence spans paragraphs 64-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4596773` offsets `106-112`; context: Although the RAD explored issues beyond those raised by the applicant, this appears to be related to how the RAD viewed its appellate role and nothing more.
- Evidence: `evidence_fact` cue `record` at chunk `4596773` offsets `29-35`; context: [79] There is nothing on the record to suggest any bias on the part of the RAD.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4596773` offsets `80-88`; context: Although the RAD explored issues beyond those raised by the applicant, this appears to be related to how the RAD viewed its appellate role and nothing more.
- Evidence: `disposition` cue `allowed` at chunk `4596773` offsets `319-326`; context: The application for judicial review is allowed with respect to the section 97 claim; and
2.

#### Section text

Ching v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2015-06-09
Neutral citation
2015 FC 725
File numbers
IMM-1272-14
Decision Content
Date: 20150609
Docket: IMM-1272-14
Citation: 2015 FC 725
Ottawa, Ontario, June 9, 2015
PRESENT: The Honourable Madam Justice Kane
BETWEEN:
WAI KHEONG CHING
Applicant
and
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] The applicant, Mr Wai Kheong Ching, a citizen of Malaysia, arrived in Canada in 2005 and claimed refugee protection in July 2013.

[2] Mr Ching claims that if he is returned to Malaysia, he will face a risk of persecution by reason of race, nationality, membership in a particular social group and political opinion. He also claims that he faces a risk to his life, cruel and unusual treatment or punishment and danger of torture in Malaysia because he will be required to participate in training for the National Service.

[3] The Refugee Protection Division of the Immigration and Refugee Board [RPD] denied his claim for protection as a Convention refugee and as a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act] on October 9, 2013. He then appealed the RPD’s decision to the Refugee Appeal Division [RAD]. The RAD dismissed the appeal and confirmed the decision of the RPD on January 5, 2014. The applicant now seeks judicial review of the decision of the RAD pursuant to section 72 of the Act.

[4] This application for judicial review is allowed with respect to the section 97 claim only. The RAD erred in applying judicial review principles and the reasonableness standard of review to the appeal of the RPD decision and failed to observe principles of procedural fairness by reviewing positive credibility findings of the RPD without providing the applicant with an opportunity to respond to the RAD’s concerns about the RPD’s credibility findings. Other aspects of the RAD decision are also problematic and arise from the RAD’s approach to its appellate role.
Background [5] The applicant came to Canada on a visitor’s visa in July 2005. He was required to report for training for the Malaysian National Service in June 2006. Although he was subsequently granted a postponement of his training for military service, he claims that he must report for duty upon return to Malaysia. He claims that he fears he will die in his training. He also claims abuse by his uncle, attacks by gangs due to his refusal to be recruited and lack of police protection from the gangs. In addition, he claims that he will be persecuted for his political opinion because he protested for democracy and human rights in Malaysia.

[6] Mr Ching made an application for permanent residence in 2011 and then made another application based on Humanitarian and Compassionate grounds in 2012, both of which were refused. He then claimed refugee protection in 2013 based on the allegations described above.

[7] Although the decision of the RAD is the subject of this judicial review, the findings of the RPD are summarized to provide the necessary context.
The RPD decision [8] The RPD made several findings including that: the applicant was generally credible about his abuse by his uncle, gang recruitment and training for the National Service; he demonstrated a nexus to a Convention due to his political opinion concerning his opposition to the National Service; his egregious delay in claiming protection was not consistent with his alleged fear; he had not rebutted the presumption of state protection regarding gang recruitment; he had not established that he would be personally harassed by Malaysian authorities for his protesting activities; he failed to provide objective evidence of the risk to his life in the National Service; and, he would not face a risk of torture upon return, although he may be fined or jailed for up to six months for not completing his National Service.

[9] The RPD found that the determinative issue with respect to the applicant’s section 96 claim was his “egregious” delay in claiming protection and this was fatal to his claim. This finding was not challenged by the applicant on appeal to the RAD.

[10] With respect to the section 97 claim, the RPD found that the determinative issues were the applicant’s failure to rebut the presumption of state protection and his failure to establish that he would face a risk to his life or danger of torture upon return.

[11] On the appeal, the applicant argued:
• The RPD erred in finding that he had not rebutted the presumption of state protection;
• The RPD erred in not fully assessing his personalized risk pursuant to section 97; and,
• That new evidence should be accepted in accordance with subsection 110(4) of the Act to establish an objective basis for his fear of dying in the National Service.
The RAD decision [12] After noting the issues raised by the applicant in the appeal, the RAD stated that it focused on four issues:
• Did the RPD err in its finding of fact that the applicant’s allegations of fear of gangs were credible?
• Did the RPD err in its finding of fact that the applicant did not want to complete military service?
• Did the RPD err in its finding of fact that the applicant was a supporter of the opposition and that he demonstrated a nexus to the Convention because of his imputed political opinion?
• Did the RPD err in its finding of fact that the applicant’s delay in claiming undermined his subjective fear, which was fatal to his claim?

[13] The RAD then considered the standard of review it should apply to the appeal of the RPD decision. The RAD noted the provisions of the Act, the factors set out Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 at para 44, [2011] 4 WWR 232, and the differences between the RPD, a tribunal of first instance, and the RAD, which was created to review the decisions made by the RPD on questions of law, fact or mixed fact and law, with the ability to substitute a different determination where appropriate. The RAD noted that the RPD is, in most cases, in the best position to assess credibility and to make findings on issues of law, fact or mixed fact and law and concluded that it should apply the standard of reasonableness to these aspects of the RPD’s decision.

[14] The RAD considered the applicant’s request to submit five articles as new evidence. The RAD referred to each article and found that the articles were not relevant or material to the facts that underpin the claim. The RAD noted with respect to subsection 110(4) and Rule 3(3)(g)(iii) of the Refugee Appeal Division Rules, SOR/2012-257 [RAD Rules] that the applicant had provided a blanket statement that the documents met the requirements of the Act but did not indicate how, as directed by the Rule. The RAD also found the evidence was not admissible because it did “not pass the requirements of Raza” (this refers to Raza v Canada (Minister of Citizenship and Immigration), 2007 FCA 385, [2007] FCJ No 1632 [Raza]).

[15] Although the RAD indicated that it focussed on the four issues set out above, the RAD considered all of the findings of the RPD and found some to be unreasonable and others to be reasonable, but concluded that the overall decision of the RPD was reasonable.
Findings found by the RAD to be unreasonable [16] The RAD found that the RPD erred in finding that the applicant’s allegation of fear of gangs was credible because the RPD omitted to consider evidence central to that claim. The RAD also found that the RPD erred in not exploring omissions in the applicant’s testimony about his efforts to seek police protection which were contradicted by the affidavit of the applicant’s sister. Given that the RPD did not refer to the totality of the evidence, the RPD’s finding about the applicant’s allegations of gang recruitment, his fear of gangs and the refusal of the police to protect him were not reasonable.

[17] The RAD also found that the RPD’s finding that the applicant had established a nexus to a Convention ground of political opinion was not reasonable. The RAD noted that the applicant’s evidence to the Board was inconsistent, but generally he was only a silent supporter.

[18] The RAD also found that RPD erred in finding that the applicant’s opposition to National Service was linked to imputed political opinion. There was no factual basis to link participation in the National Service with government suppression of opposition. The RAD concluded that there was no sufficient evidence to ground a claim that the applicant would be perceived as having a political opinion opposing the government.
Findings found by the RAD to be reasonable [19] The RAD found that the RPD’s finding that there is no risk to the applicant’s life nor danger of torture arising from his required National Service was reasonable; his fear was not objectively well founded.

[20] The RAD also noted that he could pay the fine that may be imposed for failure to report for training, which would not be onerous for him.

[21] The RPDs finding that the applicant had not been personally harassed by authorities in Malaysia due to his alleged opposition or political profile was also found to be reasonable because there was no credible evidence to support this claim.

[22] In conclusion, the RAD found that, based on its review of the totality of the evidence, the RPD erred in its treatment of the evidence regarding the applicant’s political opinion and his fear of gangs.

[23] The RAD found that the RPD did not err in finding that the applicant’s delay in claiming protection was egregious and not satisfactorily explained, noting this was not challenged in the appeal.

[24] The RAD found that the RPD’s finding that the applicant would not be personally subject to a risk to his life, to a risk of cruel or unusual treatment or punishment or to a danger of torture pursuant to section 97 was reasonable.
The Issues [25] This application raises several issues, including: the role of the RAD on appeal and the standard of review it should apply to a decision of the RPD; whether the RAD breached a duty of procedural fairness to the applicant by reviewing findings of credibility without providing the applicant an opportunity to address those findings and without holding an oral hearing; whether the RAD erred in rejecting new evidence; and, whether the RAD’s approach to this appeal could be perceived as demonstrating a reasonable apprehension of bias.
The Applicant’s Submissions [26] The applicant submits that the RAD explored issues, particularly the credibility findings of the RPD, that he did not raise in his appeal without notice to him and without any opportunity for him to respond. The applicant submits that this is breach of procedural fairness.

[27] The applicant argues that the RAD erred in adopting reasonableness as the standard of review and applying judicial review principles to the appeal of the RPD decision.

[28] The applicant notes that despite adopting the reasonableness standard, which is an error, the RAD did not defer to the RPD’s credibility findings. The RAD made its own credibility findings, but did not conduct an oral hearing. The applicant argues that the RAD erred in not holding an oral hearing in accordance with subsection 110(6) of the Act and/or in accordance with the principles of procedural fairness.

[29] The applicant further argues that the RAD erred in rejecting his new evidence, including by relying on the test in Raza. The applicant argues that Raza addresses the admissibility of new evidence of risk on a Pre-Removal Risk Assessment [PRRA], which is a completely different context, and should not apply to whether new evidence should be admitted on an appeal pursuant to subsection 110(4). The applicant submits that the new evidence is objective and supports his subjective fear of dying in the National Service.

[30] The applicant also suggests that the conduct of the RAD could be perceived as showing a reasonable apprehension of bias because the RAD went well beyond the issues he raised on appeal to ensure that his appeal would not succeed. The applicant submits that the RAD’s adverse credibility findings could disadvantage him in other future applications.
The Respondent’s Submissions [31] The respondent notes that, unlike the Rules for the RPD, there is no requirement in the Rules for the RAD to provide notice to appellants of the issues to be considered.

[32] With respect to the applicable standard of review, the respondent submits that this Court should apply the reasonableness standard to the issue of the RAD’s choice of the reasonableness standard of review to its appeal of decisions of the RPD.

[33] The respondent also submits that the RAD did not err in with respect to the standard of review; the RAD should apply the reasonableness standard to appeals from the RPD on questions of fact and mixed fact and law.

[34] The respondent notes that the jurisprudence of this Court supports the view that the RAD may defer to findings of the RPD regarding credibility. The respondent adds that both the appellate standard of palpable and overriding error and the judicial review standard of reasonableness provide deference and would lead to the same result in this case.

[35] With respect to the merits of the appeal, the respondent submits that the RAD reasonably rejected the new evidence in accordance with the RAD Rules which require the appellant to indicate how the new evidence relates to his appeal and in accordance with subsection 110(4). It was also reasonable for the RAD to consider the test in Raza, although it dealt with the application of section 113 of the Act, given the analogous wording of subsection 110(4).

[36] Moreover, the RAD considered the new evidence and provided reasons for not accepting it; the articles did not address the basis for the applicant’s fear but referred to a variety of illnesses, injuries and individual disputes between members of the National Service.

[37] The respondent further submits that the RAD did not err by not holding an oral hearing. The issue of credibility was not central to the RAD’s findings as there were many findings to support the RPD’s decision and the RAD’s decision.

[38] With respect to the applicant’s reference to bias by the RAD, the respondent notes the high threshold to be met and submits that the record does not disclose any evidence to support such an allegation.
The Applicant Is Not a Convention Refugee Pursuant to Section 96 [39] The RPD found that the applicant’s delay in claiming protection was egregious and fatal to his claim pursuant to section 96. This finding was not challenged on appeal.

[40] Despite the RAD’s confirmation of this finding on the basis of the reasonableness standard of review, the RAD noted that this finding was not challenged on appeal. In addition, the applicant agreed at the hearing of this judicial review that the section 96 finding stands.

[41] Therefore, the only issues on the appeal before the RAD related to the section 97 claim. Similarly, the only issues that should be considered on this judicial review of the RAD’s decision are those that relate to the section 97 claim.
The Standard of Review To be applied by the Court [42] The jurisprudence continues to develop with respect to the standard of review that the Court should apply to the RAD’s determination of the appropriate standard of review and to other specific determinations, including the RAD’s credibility findings and findings whether to admit new evidence.

[43] Several recent cases have addressed the standard of review to be applied by this Court to decisions of the RAD on the issue of the standard of review the RAD should apply in appeals from the RPD. In Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 at paras 25-34, [2014] FCJ No 845, Justice Phelan provided a comprehensive analysis leading to the conclusion that this Court should review the RAD’s choice of standard of review on the correctness standard. Other decisions followed the same approach including Iyamuremye v Canada (Minister of Citizenship and Immigration), 2014 FC 494 at para 20, [2014] FCJ No 523 [Iyamuremye]; Eng v Canada (Minister of Citizenship and Immigration), 2014 FC 711 at paras 17-18, 245 ACWS (3d) 644; Alvarez v Canada (Minister of Citizenship and Immigration), 2014 FC 702 at para 17, [2014] FCJ No 740 [Alvarez]; Yetna v Canada (Minister of Citizenship and Immigration), 2014 FC 858 at paras 14-15, [2014] FCJ No 906; Triastcin v Canada (Minister of Citizenship and Immigration), 2014 FC 975 at paras 18-19, [2014] FCJ No 1011; Tamayo v Canada (Minister of Citizenship and Immigration), 2014 FC 1127 at para 18, [2014] FCJ No 1172; and Bahta v Canada (Minister of Citizenship and Immigration), 2014 FC 1245 at para 10, 248 ACWS (3d) 419 [Bahta].

[44] Justice Gagné reached the contrary conclusion, also after conducting a comprehensive analysis, in Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 at paras 17-26, [2014] FCJ No 1116 [Akuffo]. Justice Gagné found that this Court should apply the reasonableness standard to the review of decisions of the RAD on its choice of the standard of review, noting that reasonableness is the presumptive standard and that there are no other circumstances to justify departing from the presumptive standard. Justice Martineau reached the same conclusion following his analysis in Djossou v Canada (Minister of Citizenship and Immigration), 2014 FC 1080 at paras 13-37, [2014] FCJ No 1130 [Djossou].

[45] There is no dispute that the Court should review the RAD’s application of the law to the facts of the case and the RAD’s decision regarding the RPD’s credibility findings on the standard of reasonableness (Dunsmuir v New Brunswick, 2008 SCC 9 at paras 53-54, [2008] 1 SCR 190).

[46] With respect to the admissibility of new evidence, in Singh v Canada (Minister of Citizenship and Immigration), 2014 FC 1022 at paras 36-42, 246 ACWS (3d) 433 [Singh], Justice Gagné held that the standard of reasonableness applies to questions regarding the admissibility of new evidence before the RAD (see also Khachatourian v Canada (Citizenship and Immigration), 2015 FC 182 at para 37, [2015] FCJ No 156 [Khachatourian]).
To be applied by the RAD to decisions of the RPD [47] I acknowledge the respondent’s position that the RAD should apply the reasonableness standard to the appeal of RPD decisions, but remain guided by the jurisprudence of this Court.

[48] The jurisprudence has consistently held that it is a reviewable error for the RAD to perform a judicial review function and apply the reasonableness standard to the RPD’s decision. The RAD should perform its appeal function: Huruglica, at para 54; Iyamuremye, at para 38; Alyafi v Canada (Minister of Citizenship and Immigration), 2014 FC 952 at para 10, [2014] FCJ No 989; Guardado v Canada (Minister of Citizenship and Immigration), 2014 FC 953 at para 4, [2014] FCJ No 1038; Diarra v Canada (Minister of Citizenship and Immigration), 2014 FC 1009 at para 29, [2014] FCJ No 1111; Djossou, at para 37; Bahta, at paras 11-16; Aloulou v Canada (Minister of Citizenship and Immigration), 2014 FC 1236 at paras 52-59, [2014] FCJ No 1307 [Aloulou]; Bui v Canada (Minister of Citizenship and Immigration), 2014 FC 1145 at para 22, [2014] FCJ No 1271; Genu c Canada (Ministre de la Citoyenneté et Immigration), 2015 CF 129 at para 30, [2015] ACF no 159; Alvarez, at para 30 and other more recent cases.

[49] With respect to questions of credibility, the jurisprudence has found that the RAD may or should defer to the RPD because the RPD has heard the witnesses directly, has had an opportunity to probe their testimony or has had some advantage not enjoyed by the RAD; see, for example, Huruglica, at para 55; Iyamuremye, at para 40; Akuffo, at para 27; Nahal v Canada (Minister of Citizenship and Immigration), 2014 FC 12

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 11888:2 · paragraphs 66-66

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4a0a85c53fadee2a36563b6c8ba1d526a8c3aa6d20e5486e74a99fa57de6ca9d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11888:2:subtheme:1 · paragraphs 66-66

- Raw key terms: `appearances, applicant, attorney, barrister, briscoe, canada, dated, deputy`
- Display key terms: `barrister, briscoe, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, briscoe, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 66-66. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
KANE J.
DATED:
JUNE 9, 2015
APPEARANCES:
Dov Maierovitz
For The Applicant
Leanne Briscoe
For The Respondent
SOLICITORS OF RECORD:
Dov Maierovitz
Barrister and Solicitor
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
