# Discussion Units: case 14106

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **54**
- Continuity pairs: **53**
- Discussion Units: **6**
- Paragraph source hashes: **54**
- Sub-themes: **19**

## 14106:1 · paragraphs 0-2

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `742f48c243077c90f60a54a88dbbc691bc101dc4951bec4183971ee692dbddfe`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 14106:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `agernew, applicant, application, canada, decision, dismissed, eshetie, immigration`
- Display key terms: `agernew, dismissed, eshetie`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: agernew, dismissed, eshetie Rule/authority context: The RAD dismissed the Applicant’s appeal of a decision of the Refugee Protection Division (RPD) and confirmed the RPD’s finding that he was neither a Convention refugee nor a person in need of protection pursuant to sect Operative outcome context: The RAD dismissed the Applicant’s appeal of a decision of the Refugee Protection Division (RPD) and confirmed the RPD’s finding that he was neither a Convention refugee nor a person in need of protection pursuant to sect | [2] For the reasons that follow, the application is dismissed. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4692130` offsets `384-395`; context: The RAD dismissed the Applicant’s appeal of a decision of the Refugee Protection Division (RPD) and confirmed the RPD’s finding that he was neither a Convention refugee nor a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA).
- Evidence: `disposition` cue `dismissed` at chunk `4692130` offsets `188-197`; context: The RAD dismissed the Applicant’s appeal of a decision of the Refugee Protection Division (RPD) and confirmed the RPD’s finding that he was neither a Convention refugee nor a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA).
- Evidence: `disposition` cue `dismissed` at chunk `4692131` offsets `52-61`; context: [2] For the reasons that follow, the application is dismissed.

#### Section text

Eshetie v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2019-08-01
Neutral citation
2019 FC 1036
File numbers
IMM-4396-18
Decision Content
Date: 20190801
Docket: IMM-4396-18
Citation: 2019 FC 1036
Ottawa, Ontario, August 1, 2019
PRESENT: Madam Justice Walker
BETWEEN:
AGERNEW TILAHUN ESHETIE
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] The Applicant, Mr. Agernew Tilahun Eshetie, seeks judicial review of a decision (Decision) of the Refugee Appeal Division (RAD) of the Immigration and Refugee Board of Canada. The RAD dismissed the Applicant’s appeal of a decision of the Refugee Protection Division (RPD) and confirmed the RPD’s finding that he was neither a Convention refugee nor a person in need of protection pursuant to sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA). The application for judicial review is brought pursuant to subsection 72(1) of the IRPA.

[2] For the reasons that follow, the application is dismissed.


## 14106:2 · paragraphs 3-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c9c55b45a51dca7470d50995c61114c39348fd33004656964e139a0cf9ea4fd5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 14106:2:subtheme:1 · paragraphs 3-8

- Raw key terms: `applicant, ethiopia, political, alleges, ethnicity, amharic, beaten, discrimination`
- Display key terms: `ethiopia, political, alleges, ethnicity, amharic, beaten, discrimination`
- Argument roles: `counterargument_limitation, disposition`
- Explanation: Observed roles: counterargument_limitation, disposition Display terms: ethiopia, political, alleges, ethnicity, amharic, beaten, discrimination Operative outcome context: He was denied access to opportunities for promotion and scholarships for advanced studies. Evidence spans paragraphs 3-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `denied` at chunk `4692133` offsets `255-261`; context: He was denied access to opportunities for promotion and scholarships for advanced studies.
- Evidence: `counterargument_limitation` cue `However` at chunk `4692134` offsets `69-76`; context: However, during the 2015 election, he volunteered to hand out flyers on behalf of the Semayawi Party.

#### 14106:2:subtheme:2 · paragraphs 9-13

- Raw key terms: `applicant, ethiopian, evidence, activities, august, canada, claim, credible`
- Display key terms: `ethiopian, activities, august, credible`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position Display terms: ethiopian, activities, august, credible Position/evidence statements: [9] Finally, the RPD considered the Applicant’s sur place claim and his political activities since arriving in Canada. Rule/authority context: Decision under review Operative outcome context: The RAD dismissed the appeal and confirmed the RPD’s decision. Evidence spans paragraphs 9-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4692137` offsets `86-91`; context: The determinative issue before the RPD panel was credibility.
- Evidence: `evidence_fact` cue `found that` at chunk `4692137` offsets `140-150`; context: The panel found that the Applicant was not credible with respect to core elements of his claim, noting inconsistencies and omissions among the information in his Basis of Claim (BOC) form and other forms, and his testimony and explanations at the hearing.
- Evidence: `party_position` cue `claim` at chunk `4692138` offsets `58-63`; context: [9] Finally, the RPD considered the Applicant’s sur place claim and his political activities since arriving in Canada.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692138` offsets `302-310`; context: The panel first reviewed the minimal scope of the Applicant’s political involvement in Ethiopia and stated:
The panel finds that the claimant did not provide credible and trustworthy evidence to establish, on a balance of probabilities, that he is perceived as an opponent of the Ethiopian government.
- Evidence: `governing_rule` cue `under` at chunk `4692140` offsets `212-217`; context: Decision under review
- Evidence: `disposition` cue `dismissed` at chunk `4692140` offsets `65-74`; context: The RAD dismissed the appeal and confirmed the RPD’s decision.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4692141` offsets `60-68`; context: Applicant’s New Evidence

#### 14106:2:subtheme:3 · paragraphs 14-14

- Raw key terms: `accordance, admissibility, admitted, analysis, appeal, applicant, application, certain`
- Display key terms: `accordance, admissibility, admitted, analysis, certain`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: accordance, admissibility, admitted, analysis, certain Position/evidence statements: [13] The Applicant submitted numerous items of new evidence to the RAD in support of his appeal. Evidence spans paragraphs 14-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4692142` offsets `189-197`; context: The RAD admitted certain documents and photos but rejected the majority of the documents in question as either pre-dating the RPD decision or as not relevant to the core issues in the Applicant’s claim.
- Evidence: `party_position` cue `submitted` at chunk `4692142` offsets `19-28`; context: [13] The Applicant submitted numerous items of new evidence to the RAD in support of his appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692142` offsets `51-59`; context: [13] The Applicant submitted numerous items of new evidence to the RAD in support of his appeal.
- Evidence: `counterargument_limitation` cue `but` at chunk `4692142` offsets `143-146`; context: The RAD admitted certain documents and photos but rejected the majority of the documents in question as either pre-dating the RPD decision or as not relevant to the core issues in the Applicant’s claim.

#### Section text

I. Background

[3] The Applicant is a citizen of Ethiopia of Amharic ethnicity. He alleges that his father was a member of the All-Amhara People’s Organization (AAPO) and was arrested in 1997 and imprisoned for four years in Ethiopia due his political activities and ethnicity. The Applicant states that he was detained and beaten for 12 hours in 1999 when he attended one of his father’s hearings. His father died in 2005.

[4] The Applicant worked as an academic at two universities in Ethiopia. He alleges he suffered discrimination at both universities due to his Amharic ethnicity and his refusal to join the Ethiopian People’s Revolutionary Democratic Front (EPRDF). He was denied access to opportunities for promotion and scholarships for advanced studies.

[5] The Applicant was not a member of a political party in Ethiopia. However, during the 2015 election, he volunteered to hand out flyers on behalf of the Semayawi Party. He ceased this activity when a manager at the bank where he was employed advised him that he was putting his job at risk.

[6] The Applicant studied in Belgium on a scholarship but alleges that, shortly after his return to Ethiopia in September 2016, he was beaten and interrogated about political matters. He also alleges that his wife and mother have been approached by individuals and government agents threatening to kill both the Applicant and his wife.

[7] The Applicant left Ethiopia on October 31, 2016 by bribing an airport security officer and came to Canada. He filed a refugee claim in November 2016 alleging that he and his family had suffered systemic discrimination, harassment and threats in Ethiopia due to their ethnicity and imputed political opinion.

[8] The Applicant’s claim was refused by the RPD on August 1, 2017. The determinative issue before the RPD panel was credibility. The panel found that the Applicant was not credible with respect to core elements of his claim, noting inconsistencies and omissions among the information in his Basis of Claim (BOC) form and other forms, and his testimony and explanations at the hearing. The RPD identified in detail material credibility issues with respect to: Amhara nationalism and oppression by the Ethiopian government; the reasons for the Applicant’s refusal to join the EPRDF; his evidence regarding his father’s political activities, charges, court decisions, and medical issues; the alleged discrimination in promotion and advanced studies; the Applicant’s failure to claim protection in Belgium and the reasons given for his inaction, together with the alleged threats made to his wife during this period; and, notably, the Applicant’s alleged detention in September 2016, his subsequent delay in departing Ethiopia, and inconsistent evidence regarding the manner of his departure.

[9] Finally, the RPD considered the Applicant’s sur place claim and his political activities since arriving in Canada. The panel first reviewed the minimal scope of the Applicant’s political involvement in Ethiopia and stated:
The panel finds that the claimant did not provide credible and trustworthy evidence to establish, on a balance of probabilities, that he is perceived as an opponent of the Ethiopian government. While the panel did not find the claimant to be a credible witness, the panel also notes again that he stated in his testimony that his participation on behalf of the Semayawi Party in Ethiopia was limited to one occasion when he distributed flyers in 2015, and that he did not participate in other activities or protests there.

[10] The RPD then concluded that the Applicant’s participation in protests in Canada had not created a profile that would attract the negative attention of the Ethiopian authorities such that he would face a serious possibility of persecution or one of the harms enumerated in section 97 of the IRPA.

[11] The Applicant appealed the RPD decision to the RAD. The RAD dismissed the appeal and confirmed the RPD’s decision. The Applicant seeks judicial review of the RAD’s Decision in this application.
II. Decision under review

[12] The Decision is dated August 22, 2018.
Applicant’s New Evidence

[13] The Applicant submitted numerous items of new evidence to the RAD in support of his appeal. The RAD admitted certain documents and photos but rejected the majority of the documents in question as either pre-dating the RPD decision or as not relevant to the core issues in the Applicant’s claim. The panel gave reasons for each determination in accordance with subsection 110(4) of the IRPA and/or Rule 29 of the Refugee Appeal Division Rules, SOR/2012-257 (Rules). The Applicant contests certain of the RAD’s admissibility determinations in this application.
RAD’s analysis

## 14106:3 · paragraphs 15-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c2f2f0494935e69f322eb25b5e23d2111d67ba44dfc294f5f9920ad7b910bbc8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 14106:3:subtheme:1 · paragraphs 15-17

- Raw key terms: `applicant, analysis, apprehension, authorities, bias, ethiopia, give, lack`
- Display key terms: `analysis, apprehension, authorities, bias, ethiopia, give, lack`
- Argument roles: `disposition, evidence_fact, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position Display terms: analysis, apprehension, authorities, bias, ethiopia, give, lack Position/evidence statements: The RPD erred in its analysis of the Applicant's sur place claim. Operative outcome context: [16] Reasonable apprehension of bias: The Applicant alleged that the RPD member used a surprised and ridiculing tone when he was explaining how he bribed security at the Addis Ababa airport and that the member interrupte Evidence spans paragraphs 15-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4692143` offsets `40-46`; context: [14] The Applicant raised the following issues in his RAD appeal:
1.
- Evidence: `party_position` cue `claim` at chunk `4692143` offsets `1026-1031`; context: The RPD erred in its analysis of the Applicant's sur place claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692143` offsets `196-204`; context: The RPD erred in its analysis of the Applicant’s evidence regarding his father’s involvement in politics in Ethiopia (particularly with the AAPO), the problems he had with the Ethiopian government, and its corresponding negative credibility findings;
3.
- Evidence: `issue` cue `issue` at chunk `4692144` offsets `66-71`; context: [15] The RAD began its analysis by stating that the determinative issue before it was whether the Applicant had established a sufficiently significant political profile to give rise to a serious possibility of persecution by the authorities if he were to be returned to Ethiopia.
- Evidence: `evidence_fact` cue `record` at chunk `4692145` offsets `771-777`; context: The RAD considered the Applicant’s allegations of intimidation but found nothing in the record to substantiate the Applicant’s statements, concluding that the hearings were conducted in a professional manner that did not give rise to a reasonable apprehension of bias.
- Evidence: `disposition` cue `denied` at chunk `4692145` offsets `226-232`; context: [16] Reasonable apprehension of bias: The Applicant alleged that the RPD member used a surprised and ridiculing tone when he was explaining how he bribed security at the Addis Ababa airport and that the member interrupted and denied him the opportunity to explain his answers when questioned.

#### 14106:3:subtheme:2 · paragraphs 18-19

- Raw key terms: `applicant, eprdf, ethiopia, join, persecution, refusal, above, activities`
- Display key terms: `eprdf, ethiopia, join, persecution, refusal, above, activities`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: eprdf, ethiopia, join, persecution, refusal, above, activities Operative outcome context: [18] Workplace discrimination in Ethiopia: The RAD upheld the RPD’s conclusion that the Applicant had not suffered persecution while working at two universities in Ethiopia. Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4692146` offsets `436-442`; context: The RAD stated that his father’s alleged political activities, detention and medical issues were not determinative of the Applicant’s claim which was based on his own political profile (his ongoing refusal to join the EPRDF and his political activities in Canada).
- Evidence: `evidence_fact` cue `found that` at chunk `4692147` offsets `184-194`; context: The panel found that it was not credible that the Applicant would be hired as a senior professor at Mizan Tepi University if the Ethiopian authorities were concerned with his refusal to join the EPRDF, nor would he be permitted to remain at the university for seven years.
- Evidence: `disposition` cue `upheld` at chunk `4692147` offsets `51-57`; context: [18] Workplace discrimination in Ethiopia: The RAD upheld the RPD’s conclusion that the Applicant had not suffered persecution while working at two universities in Ethiopia.

#### 14106:3:subtheme:3 · paragraphs 20-21

- Raw key terms: `agreed, alleged, applicant, detention, explanation, abuse, activities, against`
- Display key terms: `agreed, alleged, detention, explanation, abuse, activities, against`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: agreed, alleged, detention, explanation, abuse, activities, against Rule/authority context: [20] The Applicant’s delay in leaving Ethiopia: The Applicant stated that he delayed his departure from Ethiopia for one month after he was released from detention, despite holding a valid Canadian visa, because Ethiopia Application context: [20] The Applicant’s delay in leaving Ethiopia: The Applicant stated that he delayed his departure from Ethiopia for one month after he was released from detention, despite holding a valid Canadian visa, because Ethiopia Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4692148` offsets `221-226`; context: The RAD took issue with a letter from the Applicant’s wife that outlined threats against the Applicant but made no mention of any threats against her personally, contrary to the Applicant’s testimony.
- Evidence: `evidence_fact` cue `testimony` at chunk `4692148` offsets `398-407`; context: The RAD took issue with a letter from the Applicant’s wife that outlined threats against the Applicant but made no mention of any threats against her personally, contrary to the Applicant’s testimony.
- Evidence: `governing_rule` cue `under` at chunk `4692149` offsets `225-230`; context: [20] The Applicant’s delay in leaving Ethiopia: The Applicant stated that he delayed his departure from Ethiopia for one month after he was released from detention, despite holding a valid Canadian visa, because Ethiopia was under a state of emergency and he wanted to prepare safe arrangements for his departure.
- Evidence: `reasoning_application` cue `because` at chunk `4692149` offsets `204-211`; context: [20] The Applicant’s delay in leaving Ethiopia: The Applicant stated that he delayed his departure from Ethiopia for one month after he was released from detention, despite holding a valid Canadian visa, because Ethiopia was under a state of emergency and he wanted to prepare safe arrangements for his departure.

#### 14106:3:subtheme:4 · paragraphs 22-22

- Raw key terms: `activities, against, applicant, article, assessed, assessment, attendance, attended`
- Display key terms: `activities, against, article, assessed, assessment, attendance, attended`
- Argument roles: `disposition, evidence_fact, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position Display terms: activities, against, article, assessed, assessment, attendance, attended Position/evidence statements: [21] The Applicant’s sur place claim: The RAD considered whether the Applicant’s political activities in Canada created a sufficient political profile to bring him to the attention of the Ethiopian authorities. Operative outcome context: The RAD upheld the RPD’s conclusion that the Applicant’s political profile was not sufficient to give rise to a risk of persecution as the only evidence before the RPD panel was an article regarding a meeting organized b Evidence spans paragraphs 22-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4692150` offsets `57-64`; context: [21] The Applicant’s sur place claim: The RAD considered whether the Applicant’s political activities in Canada created a sufficient political profile to bring him to the attention of the Ethiopian authorities.
- Evidence: `party_position` cue `claim` at chunk `4692150` offsets `31-36`; context: [21] The Applicant’s sur place claim: The RAD considered whether the Applicant’s political activities in Canada created a sufficient political profile to bring him to the attention of the Ethiopian authorities.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692150` offsets `283-291`; context: The panel first reviewed whether the RPD erred in its assessment of the evidence before it.
- Evidence: `disposition` cue `upheld` at chunk `4692150` offsets `311-317`; context: The RAD upheld the RPD’s conclusion that the Applicant’s political profile was not sufficient to give rise to a risk of persecution as the only evidence before the RPD panel was an article regarding a meeting organized by Unity for Democracy and Human Rights Toronto (UDHR) that the Applicant attended.

#### Section text

[14] The Applicant raised the following issues in his RAD appeal:
1. The RPD exhibited a reasonable apprehension of bias against the Applicant;
2. The RPD erred in its analysis of the Applicant’s evidence regarding his father’s involvement in politics in Ethiopia (particularly with the AAPO), the problems he had with the Ethiopian government, and its corresponding negative credibility findings;
3. The RPD erred in its assessment of the lack of medical evidence regarding the health of the Applicant’s father;
4. The RPD erred in its analysis of the Applicant’s evidence regarding the problems he faced in Ethiopia, including workplace discrimination;
5. The RPD erred in its analysis of the Applicant's evidence and negative credibility finding regarding his detention and mistreatment at the hands of the Ethiopian authorities in September 2016;
6. The RPD erred in its negative credibility finding arising from the Applicant's delay in leaving Ethiopia; and
7. The RPD erred in its analysis of the Applicant's sur place claim.

[15] The RAD began its analysis by stating that the determinative issue before it was whether the Applicant had established a sufficiently significant political profile to give rise to a serious possibility of persecution by the authorities if he were to be returned to Ethiopia.

[16] Reasonable apprehension of bias: The Applicant alleged that the RPD member used a surprised and ridiculing tone when he was explaining how he bribed security at the Addis Ababa airport and that the member interrupted and denied him the opportunity to explain his answers when questioned. He also alleged that the RPD member was intimidating and threw a pen down during the hearing. The RAD reviewed the audio recording of the three RPD hearings and concluded that the RPD member was surprised at one juncture but there was no ridicule. The RAD stated that the RPD’s questions were clear and that the member attempted to clarify any lack of clarity in the Applicant’s responses. The RAD considered the Applicant’s allegations of intimidation but found nothing in the record to substantiate the Applicant’s statements, concluding that the hearings were conducted in a professional manner that did not give rise to a reasonable apprehension of bias.

[17] Applicant’s political profile (items 2 & 3 above): The RAD reviewed the National Documentation Package for Ethiopia in the context of the Applicant’s allegations of Amharic persecution but concluded that an individual’s Amharic ethnicity alone would not place them at risk of persecution. Rather, the focus must be on their political activities. The RAD stated that his father’s alleged political activities, detention and medical issues were not determinative of the Applicant’s claim which was based on his own political profile (his ongoing refusal to join the EPRDF and his political activities in Canada).

[18] Workplace discrimination in Ethiopia: The RAD upheld the RPD’s conclusion that the Applicant had not suffered persecution while working at two universities in Ethiopia. The panel found that it was not credible that the Applicant would be hired as a senior professor at Mizan Tepi University if the Ethiopian authorities were concerned with his refusal to join the EPRDF, nor would he be permitted to remain at the university for seven years.

[19] Detention and mistreatment by Ethiopian authorities: The Applicant alleged that he was detained and beaten by Ethiopian authorities after his return from Belgium in 2016 due to his political activities. The RAD took issue with a letter from the Applicant’s wife that outlined threats against the Applicant but made no mention of any threats against her personally, contrary to the Applicant’s testimony. The RAD rejected the Applicant’s explanation that he had asked her to provide something “short and precise” as this contradiction was a crucial detail in the narrative. While the RAD agreed that the RPD’s assessment of the language used to describe the beating the Applicant alleges to have suffered in detention was microscopic, the panel concluded that this error was not fatal to the RPD’s overall finding that the detention and abuse of the Applicant by the authorities did not take place.

[20] The Applicant’s delay in leaving Ethiopia: The Applicant stated that he delayed his departure from Ethiopia for one month after he was released from detention, despite holding a valid Canadian visa, because Ethiopia was under a state of emergency and he wanted to prepare safe arrangements for his departure. The RAD confirmed two aspects of the RPD’s reasoning in this regard. First, the Applicant’s explanation of his departure and bribing of an airport security officer was not credible as it “evolved and changed as it was challenged”. Second, the RAD agreed with the RPD that, if the Applicant was in the danger he alleged, he would not have delayed his departure.

[21] The Applicant’s sur place claim: The RAD considered whether the Applicant’s political activities in Canada created a sufficient political profile to bring him to the attention of the Ethiopian authorities. The panel first reviewed whether the RPD erred in its assessment of the evidence before it. The RAD upheld the RPD’s conclusion that the Applicant’s political profile was not sufficient to give rise to a risk of persecution as the only evidence before the RPD panel was an article regarding a meeting organized by Unity for Democracy and Human Rights Toronto (UDHR) that the Applicant attended. The panel then assessed the Applicant’s new evidence which established the Applicant’s attendance at a protest against the Ethiopian government in September 2017 in Toronto and a UDHR meeting in October 2017. The RAD reviewed the evidence and concluded that the Applicant had not established that he was a leading figure or organizer in any political organization which would draw the attention of the Ethiopian authorities. At best, the Applicant’s evidence suggested a mere possibility of persecution should he return to Ethiopia.
III. Issues

## 14106:4 · paragraphs 23-50

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `bcfa7e66dfc4d73501a734b3e5250f8409cc5257a9c4e9fea93a4148d6bb72ec`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 14106:4:subtheme:1 · paragraphs 23-24

- Raw key terms: `applicant, apprehension, bias, claim, credibility, evidence, place, raises`
- Display key terms: `apprehension, bias, credibility, place, raises`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: apprehension, bias, credibility, place, raises Position/evidence statements: Did the RAD err in its refusal of the Applicant’s sur place claim? | The RAD’s interpretation of subsection 110(4) of the IRPA and its decisions concerning the admission of new evidence are subject to review by this Court for reasonableness, as is its consideration of the Applicant’s sur  Rule/authority context: Standard of review Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4692151` offsets `31-37`; context: [22] The Applicant raises four issues in this application:
Did the RAD err in determining that the conduct of the RPD gave rise to no reasonable apprehension of bias?
- Evidence: `party_position` cue `claim` at chunk `4692151` offsets `361-366`; context: Did the RAD err in its refusal of the Applicant’s sur place claim?
- Evidence: `evidence_fact` cue `evidence` at chunk `4692151` offsets `225-233`; context: Did the RAD err in refusing to admit certain items of new evidence?
- Evidence: `governing_rule` cue `Standard of review` at chunk `4692151` offsets `372-390`; context: Standard of review
- Evidence: `issue` cue `issue` at chunk `4692152` offsets `9-14`; context: [23] The issue of reasonable apprehension of bias raises a question of procedural fairness and is reviewable for correctness.
- Evidence: `party_position` cue `claim` at chunk `4692152` offsets `537-542`; context: The RAD’s interpretation of subsection 110(4) of the IRPA and its decisions concerning the admission of new evidence are subject to review by this Court for reasonableness, as is its consideration of the Applicant’s sur place claim, in accordance with the presumption that an administrative body’s interpretation of its home statute is owed deference by a reviewing court (Canada (Citizenship and Immigration) v Singh, 2016 FCA 96 at para 29 (Singh); Deng v Canada (Citizenship and Immigration), 2016 FC 887 at paras 6-7).
- Evidence: `evidence_fact` cue `evidence` at chunk `4692152` offsets `419-427`; context: The RAD’s interpretation of subsection 110(4) of the IRPA and its decisions concerning the admission of new evidence are subject to review by this Court for reasonableness, as is its consideration of the Applicant’s sur place claim, in accordance with the presumption that an administrative body’s interpretation of its home statute is owed deference by a reviewing court (Canada (Citizenship and Immigration) v Singh, 2016 FCA 96 at para 29 (Singh); Deng v Canada (Citizenship and Immigration), 2016 FC 887 at paras 6-7).

#### 14106:4:subtheme:2 · paragraphs 25-26

- Raw key terms: `apprehension, bias, decision, made, reasonable, rise, acceptable, adjectives`
- Display key terms: `apprehension, bias, made, reasonable, rise, acceptable, adjectives`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: apprehension, bias, made, reasonable, rise, acceptable, adjectives Position/evidence statements: [25] The Applicant submits that the RAD failed to meaningfully consider the various examples of bias and lack of impartiality on the part of the RPD that, taken together, give rise to a reasonable apprehension of bias. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4692153` offsets `537-544`; context: The Dunsmuir criteria are met if the reasons provided by the tribunal “allow the reviewing court to understand why the tribunal made its decision and permit it to determine whether the conclusion is within the range of acceptable outcomes” (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at para 16).
- Evidence: `party_position` cue `submits` at chunk `4692154` offsets `19-26`; context: [25] The Applicant submits that the RAD failed to meaningfully consider the various examples of bias and lack of impartiality on the part of the RPD that, taken together, give rise to a reasonable apprehension of bias.
- Evidence: `evidence_fact` cue `testimony` at chunk `4692154` offsets `271-280`; context: He alleges that the RPD member interrupted both his testimony and his counsel’s questions and clarifications, and made improper comments suggesting the member pre-judged his credibility.

#### 14106:4:subtheme:3 · paragraphs 27-29

- Raw key terms: `allegations, applicant, bias, conclude, decide, fairly, member, person`
- Display key terms: `allegations, bias, conclude, decide, fairly, person`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: allegations, bias, conclude, decide, fairly, person Application context: [26] It is well-established that the test for reasonable apprehension of bias is whether an informed person, reviewing the matter realistically and practically, and having thought the matter through, would conclude that  | [27] I find that the RAD correctly reviewed the Applicant’s allegations of bias. Evidence spans paragraphs 27-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4692155` offsets `81-88`; context: [26] It is well-established that the test for reasonable apprehension of bias is whether an informed person, reviewing the matter realistically and practically, and having thought the matter through, would conclude that the decision-maker would not decide fairly (Committee for Justice and Liberty et al.
- Evidence: `reasoning_application` cue `conclude` at chunk `4692155` offsets `206-214`; context: [26] It is well-established that the test for reasonable apprehension of bias is whether an informed person, reviewing the matter realistically and practically, and having thought the matter through, would conclude that the decision-maker would not decide fairly (Committee for Justice and Liberty et al.
- Evidence: `evidence_fact` cue `record` at chunk `4692156` offsets `101-107`; context: I have reviewed the record and the RAD’s analysis of the Applicant’s allegations and find that the reasonable person would not conclude that the RPD member lacked impartiality and would not decide the case fairly.
- Evidence: `reasoning_application` cue `I find` at chunk `4692156` offsets `5-11`; context: [27] I find that the RAD correctly reviewed the Applicant’s allegations of bias.
- Evidence: `evidence_fact` cue `found that` at chunk `4692157` offsets `284-294`; context: The RAD panel addressed the Applicant’s argument that the RPD member used a surprised and ridiculing tone but found that, although the member was surprised at one point in the hearing, there was no ridicule on the part of the RPD.

#### 14106:4:subtheme:4 · paragraphs 30-36

- Raw key terms: `applicant, evidence, decision, case, para, regarding, answer, appeal`
- Display key terms: `case, para, regarding, answer`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: case, para, regarding, answer Position/evidence statements: For example, the Applicant submits that, had the RPD approached the issue of exit delay with an open mind, “it would have understood that the Applicant has reasonably explained his delay in exiting his country”. | [30] The Applicant argues that the RPD member’s statement during the hearing that the member had a problem with the Applicant’s credibility establishes a reasonable apprehension of bias as she prejudged his case. Rule/authority context: I find that the RAD’s assessment of the evidence against the requirements of subsection 110(4) of the IRPA and Rule 29 of the Rules, together with the relevant jurisprudence regarding admission of evidence by the RAD (Si Application context: I find that the RAD’s assessment of the evidence against the requirements of subsection 110(4) of the IRPA and Rule 29 of the Rules, together with the relevant jurisprudence regarding admission of evidence by the RAD (Si Evidence spans paragraphs 30-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4692158` offsets `206-214`; context: These arguments question the substance of the RPD’s decision; they do not establish bias.
- Evidence: `party_position` cue `submits` at chunk `4692158` offsets `307-314`; context: For example, the Applicant submits that, had the RPD approached the issue of exit delay with an open mind, “it would have understood that the Applicant has reasonably explained his delay in exiting his country”.
- Evidence: `issue` cue `issue` at chunk `4692159` offsets `311-316`; context: However, a decision-maker may form tentative views on matters as a hearing unfolds so long as the issue has not been pre-judged (Yukon Francophone School Board, Education Area #23 v Yukon (Attorney General), 2015 SCC 25 at para 33).
- Evidence: `party_position` cue `argues` at chunk `4692159` offsets `19-25`; context: [30] The Applicant argues that the RPD member’s statement during the hearing that the member had a problem with the Applicant’s credibility establishes a reasonable apprehension of bias as she prejudged his case.
- Evidence: `counterargument_limitation` cue `However` at chunk `4692159` offsets `213-220`; context: However, a decision-maker may form tentative views on matters as a hearing unfolds so long as the issue has not been pre-judged (Yukon Francophone School Board, Education Area #23 v Yukon (Attorney General), 2015 SCC 25 at para 33).
- Evidence: `party_position` cue `argues` at chunk `4692160` offsets `28-34`; context: [31] Finally, the Applicant argues that the RAD failed to address his allegation that the RPD member threw a pen down in apparent frustration during the hearing.
- Evidence: `evidence_fact` cue `record` at chunk `4692160` offsets `260-266`; context: The RAD specifically addressed this allegation in the Decision but found no substantiation in the record.
- Evidence: `counterargument_limitation` cue `but` at chunk `4692160` offsets `225-228`; context: The RAD specifically addressed this allegation in the Decision but found no substantiation in the record.
- Evidence: `party_position` cue `submitted` at chunk `4692161` offsets `19-28`; context: [32] The Applicant submitted substantial new evidence to the RAD.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692161` offsets `45-53`; context: [32] The Applicant submitted substantial new evidence to the RAD.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4692161` offsets `370-383`; context: I find that the RAD’s assessment of the evidence against the requirements of subsection 110(4) of the IRPA and Rule 29 of the Rules, together with the relevant jurisprudence regarding admission of evidence by the RAD (Singh at paras 39-49; Raza v Canada (Citizenship and Immigration), 2007 FCA 385 at para 13), was reasonable.
- Evidence: `reasoning_application` cue `I find` at chunk `4692161` offsets `210-216`; context: I find that the RAD’s assessment of the evidence against the requirements of subsection 110(4) of the IRPA and Rule 29 of the Rules, together with the relevant jurisprudence regarding admission of evidence by the RAD (Singh at paras 39-49; Raza v Canada (Citizenship and Immigration), 2007 FCA 385 at para 13), was reasonable.
- Evidence: `party_position` cue `submit` at chunk `4692162` offsets `268-274`; context: A RAD appeal is not a second chance to submit evidence to answer weaknesses identified by the RPD (Abdullahi v Canada (Citizenship and Immigration), 2016 FC 260 at para 15):
- Evidence: `evidence_fact` cue `evidence` at chunk `4692162` offsets `82-90`; context: [33] It is important to bear in mind that an analysis of the admissibility of new evidence before the RAD begins with the premise that the appeal of an RPD decision is intended to be a paper-based appeal (Singh at paras 35, 51).
- Evidence: `party_position` cue `claim` at chunk `4692163` offsets `140-145`; context: [15] In other words, responding to an inadequacy identified by the RPD in a party’s case cannot be a legitimate foundation for the party to claim that had she known about the deficiency she could have presented better evidence that was always in existence from persons that could have been called, in this case from her cousin.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692163` offsets `218-226`; context: [15] In other words, responding to an inadequacy identified by the RPD in a party’s case cannot be a legitimate foundation for the party to claim that had she known about the deficiency she could have presented better evidence that was always in existence from persons that could have been called, in this case from her cousin.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692164` offsets `116-124`; context: In this case, a great deal of the new evidence submitted by the Applicant could and should have been provided to the RPD.

#### 14106:4:subtheme:5 · paragraphs 37-38

- Raw key terms: `admit, applicant, assessment, decision, ethiopia, opinion, regarding, relevance`
- Display key terms: `admit, assessment, ethiopia, opinion, regarding, relevance`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: admit, assessment, ethiopia, opinion, regarding, relevance Position/evidence statements: I note that the Applicant argues that the RAD erred in disregarding a report regarding the violence perpetrated against the Amhara people in Ethiopia because it was based on historic events and information even though th Application context: I note that the Applicant argues that the RAD erred in disregarding a report regarding the violence perpetrated against the Amhara people in Ethiopia because it was based on historic events and information even though th | I find that the panel made no error in rejecting the two documents. Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4692165` offsets `120-125`; context: [35] The RAD’s assessment of the admissibility of the new evidence must be reviewed in the context of the determinative issue in the case: whether the Applicant had established a political profile that placed him at a serious possibility of persecution by the authorities in Ethiopia.
- Evidence: `party_position` cue `argues` at chunk `4692165` offsets `731-737`; context: I note that the Applicant argues that the RAD erred in disregarding a report regarding the violence perpetrated against the Amhara people in Ethiopia because it was based on historic events and information even though the report itself post-dated the RPD decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692165` offsets `58-66`; context: [35] The RAD’s assessment of the admissibility of the new evidence must be reviewed in the context of the determinative issue in the case: whether the Applicant had established a political profile that placed him at a serious possibility of persecution by the authorities in Ethiopia.
- Evidence: `reasoning_application` cue `because` at chunk `4692165` offsets `855-862`; context: I note that the Applicant argues that the RAD erred in disregarding a report regarding the violence perpetrated against the Amhara people in Ethiopia because it was based on historic events and information even though the report itself post-dated the RPD decision.
- Evidence: `issue` cue `issues` at chunk `4692166` offsets `479-485`; context: The opinion was intended to address the RPD’s decision to award little weight to the Applicant’s support letters from Ethiopia but it did not deal with the unavailability of the writers of the letters and the vagueness in the letters themselves, both issues identified by the RPD.
- Evidence: `reasoning_application` cue `I find` at chunk `4692166` offsets `160-166`; context: I find that the panel made no error in rejecting the two documents.
- Evidence: `counterargument_limitation` cue `but` at chunk `4692166` offsets `355-358`; context: The opinion was intended to address the RPD’s decision to award little weight to the Applicant’s support letters from Ethiopia but it did not deal with the unavailability of the writers of the letters and the vagueness in the letters themselves, both issues identified by the RPD.

#### 14106:4:subtheme:6 · paragraphs 39-42

- Raw key terms: `applicant, credibility, evidence, find, findings, omissions, testimony, alleged`
- Display key terms: `credibility, find, findings, omissions, testimony, alleged`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: credibility, find, findings, omissions, testimony, alleged Position/evidence statements: [37] The Applicant submits that the RAD’s credibility findings regarding his central claim of persecution due to actual and imputed political opinions are unreasonable. | [39] The Applicant submits that the RPD made no general negative credibility finding in its decision and that the RAD provides little analysis of this omission, stating only that the RPD did not err in its overall credib Application context: I find the RAD’s conclusions reasonable and its explanations thorough. Evidence spans paragraphs 39-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4692167` offsets `189-194`; context: He takes particular issue with the reasons which led the RAD to find that he was not detained and abused by the Ethiopian authorities in 2016: the omissions in his wife’s letter about the threats against her personally; the Applicant’s delay in exiting Ethiopia after the alleged detention; and his evolving testimony regarding the manner in which he exited Ethiopia by paying a bribe to an airport security officer.
- Evidence: `party_position` cue `submits` at chunk `4692167` offsets `19-26`; context: [37] The Applicant submits that the RAD’s credibility findings regarding his central claim of persecution due to actual and imputed political opinions are unreasonable.
- Evidence: `evidence_fact` cue `testimony` at chunk `4692167` offsets `477-486`; context: He takes particular issue with the reasons which led the RAD to find that he was not detained and abused by the Ethiopian authorities in 2016: the omissions in his wife’s letter about the threats against her personally; the Applicant’s delay in exiting Ethiopia after the alleged detention; and his evolving testimony regarding the manner in which he exited Ethiopia by paying a bribe to an airport security officer.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692168` offsets `249-257`; context: In essence, the Applicant is asking the Court to re-weigh the evidence before both the RPD and the RAD.
- Evidence: `reasoning_application` cue `I find` at chunk `4692168` offsets `116-122`; context: I find the RAD’s conclusions reasonable and its explanations thorough.
- Evidence: `party_position` cue `submits` at chunk `4692169` offsets `19-26`; context: [39] The Applicant submits that the RPD made no general negative credibility finding in its decision and that the RAD provides little analysis of this omission, stating only that the RPD did not err in its overall credibility findings.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692169` offsets `490-498`; context: At the beginning of its analysis, the RPD panel noted “inconsistencies, omissions and implausibilities in the claimant’s evidence, some of which emerged from a comparison of the information the claimant provided in his BOC and other forms, and the testimony and explanations provided at the hearing”.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692170` offsets `276-284`; context: Both the RPD and the RAD identified a series of material omissions and inconsistencies in the Applicant’s documentary evidence and testimony regarding his detention which, when coupled with his subsequent delay in exiting the country despite holding a Canadian visa, led to serious concerns regarding his credibility.

#### 14106:4:subtheme:7 · paragraphs 43-46

- Raw key terms: `canada, activities, applicant, claim, place, authorities, chance, citizenship`
- Display key terms: `activities, place, authorities, chance`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position Display terms: activities, place, authorities, chance Position/evidence statements: [41] The RAD concluded that the Applicant’s activities in Canada were not sufficiently significant to warrant the attention of the Ethiopian authorities and dismissed his sur place claim. Rule/authority context: In order to show a well-founded fear of persecution under section 96 of the Act, an applicant must establish that there is a “reasonable chance” or “serious possibility” of persecution (Adjei v Canada (Minister of Employ Operative outcome context: [41] The RAD concluded that the Applicant’s activities in Canada were not sufficiently significant to warrant the attention of the Ethiopian authorities and dismissed his sur place claim. Evidence spans paragraphs 43-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4692171` offsets `253-258`; context: The Applicant challenges the RAD’s findings stating that the key issue in his case was whether his actions may have come to the notice of the Ethiopian authorities.
- Evidence: `party_position` cue `claim` at chunk `4692171` offsets `181-186`; context: [41] The RAD concluded that the Applicant’s activities in Canada were not sufficiently significant to warrant the attention of the Ethiopian authorities and dismissed his sur place claim.
- Evidence: `disposition` cue `dismissed` at chunk `4692171` offsets `157-166`; context: [41] The RAD concluded that the Applicant’s activities in Canada were not sufficiently significant to warrant the attention of the Ethiopian authorities and dismissed his sur place claim.
- Evidence: `issue` cue `whether` at chunk `4692172` offsets `53-60`; context: [42] The analysis of a sur place claim is focused on whether the activities of an individual abroad might give rise to a negative reaction on the part of the authorities in their home country and lead to a reasonable chance of persecution in the event of return (Ngongo v Canada (Minister of Citizenship and Immigration), [1999] FCJ No 1627 (QL) at para 23).
- Evidence: `governing_rule` cue `under` at chunk `4692173` offsets `150-155`; context: In order to show a well-founded fear of persecution under section 96 of the Act, an applicant must establish that there is a “reasonable chance” or “serious possibility” of persecution (Adjei v Canada (Minister of Employment and Immigration), [1989] 2 FC 680 (FCA) at paras 5-8; Sebastio v Canada (Minister of Citizenship and Immigration), 2016 FC 803 at paras 13-14 [Sebastio]).
- Evidence: `counterargument_limitation` cue `However` at chunk `4692173` offsets `568-575`; context: However, once proven, the legal threshold to demonstrate persecution is only a “serious possibility”.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692174` offsets `26-34`; context: [43] The RAD reviewed the evidence of the Applicant’s political activities in Canada before the RPD and the new evidence regarding his participation in a protest and meeting in Toronto.
- Evidence: `counterargument_limitation` cue `but` at chunk `4692174` offsets `316-319`; context: The panel accepted his participation in the various events, noting that he can be seen in some of the videos posted of the events but that he is not identified individually.

#### 14106:4:subtheme:8 · paragraphs 47-49

- Raw key terms: `activities, applicant, attention, authorities, documentary, establish, ethiopia, ethiopian`
- Display key terms: `activities, attention, authorities, documentary, establish, ethiopia, ethiopian`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: activities, attention, authorities, documentary, establish, ethiopia, ethiopian Application context: I find that the RAD’s conclusion that the Applicant’s profile was not sufficient to establish that he would draw the attention of the Ethiopian authorities is consistent with the documentary evidence for Ethiopia and rea Operative outcome context: [46] The application will be dismissed. Evidence spans paragraphs 47-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4692175` offsets `22-29`; context: [44] The RAD assessed whether the Applicant’s activities would come to the attention of the Ethiopian authorities.
- Evidence: `evidence_fact` cue `evidence` at chunk `4692175` offsets `154-162`; context: Based on its review of the documentary evidence for Ethiopia, the panel stated that the Ethiopian authorities’ monitoring of the diaspora centred on high-profile targets but acknowledged that there are varying opinions on how “high-profile” an individual must be in order to be monitored.
- Evidence: `counterargument_limitation` cue `but` at chunk `4692175` offsets `285-288`; context: Based on its review of the documentary evidence for Ethiopia, the panel stated that the Ethiopian authorities’ monitoring of the diaspora centred on high-profile targets but acknowledged that there are varying opinions on how “high-profile” an individual must be in order to be monitored.
- Evidence: `issue` cue `question` at chunk `4692176` offsets `111-119`; context: [45] There is no suggestion in the record that the Applicant was a leader or organizer of any of the events in question.
- Evidence: `evidence_fact` cue `record` at chunk `4692176` offsets `35-41`; context: [45] There is no suggestion in the record that the Applicant was a leader or organizer of any of the events in question.
- Evidence: `reasoning_application` cue `I find` at chunk `4692176` offsets `204-210`; context: I find that the RAD’s conclusion that the Applicant’s profile was not sufficient to establish that he would draw the attention of the Ethiopian authorities is consistent with the documentary evidence for Ethiopia and reasonable in light of the Applicant’s political activities in Canada.
- Evidence: `disposition` cue `dismissed` at chunk `4692177` offsets `29-38`; context: [46] The application will be dismissed.

#### 14106:4:subtheme:9 · paragraphs 50-50

- Raw key terms: `arises, case, certification, none, parties, proposed, question`
- Display key terms: `arises, case, certification, none, proposed, question`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: arises, case, certification, none, proposed, question Evidence spans paragraphs 50-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4692178` offsets `8-16`; context: [47] No question for certification was proposed by the parties and none arises in this case.

#### Section text

[22] The Applicant raises four issues in this application:
Did the RAD err in determining that the conduct of the RPD gave rise to no reasonable apprehension of bias?
Did the RAD err in refusing to admit certain items of new evidence?
Did the RAD err in its assessment of the Applicant’s credibility?
Did the RAD err in its refusal of the Applicant’s sur place claim?
IV. Standard of review

[23] The issue of reasonable apprehension of bias raises a question of procedural fairness and is reviewable for correctness. No deference is owed to the RAD’s findings (Lakatos v Canada (Citizenship and Immigration), 2018 FC 1061 at para 12; But v Canada (Citizenship and Immigration), 2016 FC 626 at para 4). The RAD’s interpretation of subsection 110(4) of the IRPA and its decisions concerning the admission of new evidence are subject to review by this Court for reasonableness, as is its consideration of the Applicant’s sur place claim, in accordance with the presumption that an administrative body’s interpretation of its home statute is owed deference by a reviewing court (Canada (Citizenship and Immigration) v Singh, 2016 FCA 96 at para 29 (Singh); Deng v Canada (Citizenship and Immigration), 2016 FC 887 at paras 6-7). I will also review the RAD’s consideration of the evidence and the Applicant’s credibility on the standard of reasonableness (Canada (Citizenship and Immigration) v Huruglica), 2016 FCA 93 at para 35; Gebremichael v Canada (Citizenship and Immigration), 2016 FC 646 at para 8).

[24] The reasonableness standard is concerned with ensuring that the decision of a tribunal is justified, transparent and intelligible, and that the decision falls within a range of possible and acceptable outcomes which are defensible in respect of the facts and law applicable in the particular case (Dunsmuir v New Brunswick, 2008 SCC 9 at para 47 (Dunsmuir)). The Dunsmuir criteria are met if the reasons provided by the tribunal “allow the reviewing court to understand why the tribunal made its decision and permit it to determine whether the conclusion is within the range of acceptable outcomes” (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at para 16).
V. Analysis
1. Did the RAD err in determining that the conduct of the RPD gave rise to no reasonable apprehension of bias?

[25] The Applicant submits that the RAD failed to meaningfully consider the various examples of bias and lack of impartiality on the part of the RPD that, taken together, give rise to a reasonable apprehension of bias. He alleges that the RPD member interrupted both his testimony and his counsel’s questions and clarifications, and made improper comments suggesting the member pre-judged his credibility. The Applicant argues that the RPD decision includes unwarranted adjectives which demonstrate the RPD’s lack of objectivity and mischaracterize as vague his well-articulated responses to the panel’s questions. He also argues that the RPD ignored his explanation as to why he delayed his departure from Ethiopia for a month after his release from detention. Finally, the Applicant argues that the RAD did not consider the RPD’s judgmental, improper and intimidating behaviour, particularly the allegation that the member threw a pen down during one of the hearings.

[26] It is well-established that the test for reasonable apprehension of bias is whether an informed person, reviewing the matter realistically and practically, and having thought the matter through, would conclude that the decision-maker would not decide fairly (Committee for Justice and Liberty et al. v National Energy Board et al., [1978] 1 SCR 369; Ma v Canada (Citizenship and Immigration), 2019 FC 392 at para 26). The threshold for finding bias or a reasonable apprehension of bias is high as decision-makers are presumed to be impartial (Sagkeeng First Nation v Canada (Attorney General), 2015 FC 1113 at para 105).

[27] I find that the RAD correctly reviewed the Applicant’s allegations of bias. I have reviewed the record and the RAD’s analysis of the Applicant’s allegations and find that the reasonable person would not conclude that the RPD member lacked impartiality and would not decide the case fairly.

[28] The RAD reviewed the audio recording of the three RPD hearings and considered the Applicant’s allegations regarding the manner and extent of the questioning by the RPD. The RAD panel addressed the Applicant’s argument that the RPD member used a surprised and ridiculing tone but found that, although the member was surprised at one point in the hearing, there was no ridicule on the part of the RPD. The RAD also found that the RPD had not unduly interrupted the hearing; that its questioning was not vague; and that the RPD member was focused on obtaining clarification from the Applicant. The RAD panel was alive to the Applicant’s concerns and addressed them intelligibly.

[29] A number of the Applicant’s arguments centre on the nature of the RPD’s questioning and the reasonableness of the RPD’s conclusions regarding the Applicant’s responses and credibility. These arguments question the substance of the RPD’s decision; they do not establish bias. For example, the Applicant submits that, had the RPD approached the issue of exit delay with an open mind, “it would have understood that the Applicant has reasonably explained his delay in exiting his country”.

[30] The Applicant argues that the RPD member’s statement during the hearing that the member had a problem with the Applicant’s credibility establishes a reasonable apprehension of bias as she prejudged his case. However, a decision-maker may form tentative views on matters as a hearing unfolds so long as the issue has not been pre-judged (Yukon Francophone School Board, Education Area #23 v Yukon (Attorney General), 2015 SCC 25 at para 33). The member’s comment was made during the course of an attempt by the Applicant to clarify a prior answer regarding his reasons for not returning to Ethiopia. The member’s statement indicated an obvious concern with credibility in the context of a discussion with counsel as to whether or not the Applicant was maintaining a prior answer.

[31] Finally, the Applicant argues that the RAD failed to address his allegation that the RPD member threw a pen down in apparent frustration during the hearing. The RAD specifically addressed this allegation in the Decision but found no substantiation in the record.
2. Did the RAD err in refusing to admit certain items of new evidence?

[32] The Applicant submitted substantial new evidence to the RAD. The panel reviewed each category of evidence submitted and made specific determinations which it set out clearly and concisely in the Decision. I find that the RAD’s assessment of the evidence against the requirements of subsection 110(4) of the IRPA and Rule 29 of the Rules, together with the relevant jurisprudence regarding admission of evidence by the RAD (Singh at paras 39-49; Raza v Canada (Citizenship and Immigration), 2007 FCA 385 at para 13), was reasonable.

[33] It is important to bear in mind that an analysis of the admissibility of new evidence before the RAD begins with the premise that the appeal of an RPD decision is intended to be a paper-based appeal (Singh at paras 35, 51). A RAD appeal is not a second chance to submit evidence to answer weaknesses identified by the RPD (Abdullahi v Canada (Citizenship and Immigration), 2016 FC 260 at para 15):

[15] In other words, responding to an inadequacy identified by the RPD in a party’s case cannot be a legitimate foundation for the party to claim that had she known about the deficiency she could have presented better evidence that was always in existence from persons that could have been called, in this case from her cousin. This would make the RPD process a monumental waste of time, which is surely not Parliament’s intention in providing appeal rights.

[34] An applicant is required to put his or her best foot forward to the RPD. In this case, a great deal of the new evidence submitted by the Applicant could and should have been provided to the RPD.

[35] The RAD’s assessment of the admissibility of the new evidence must be reviewed in the context of the determinative issue in the case: whether the Applicant had established a political profile that placed him at a serious possibility of persecution by the authorities in Ethiopia. The RAD’s focus was on the Applicant’s personal political activities and profile, not those of his father who passed away in 2005. In addition, the Applicant’s Amharic ethnicity and his general knowledge of Amhara nationalism were not at issue. As a result, the RAD reasonably refused to admit general evidence regarding persecution of the Amhara in Ethiopia and opinion evidence regarding his father’s medical records. I note that the Applicant argues that the RAD erred in disregarding a report regarding the violence perpetrated against the Amhara people in Ethiopia because it was based on historic events and information even though the report itself post-dated the RPD decision. While I agree that the date of publication is relevant to a subsection 110(4) determination, in this case, the report in question would not be admissible on the basis of lack of relevance to the core issue in the Applicant’s claim.

[36] The RAD did not admit an opinion on the subject of Ethiopian affidavits and an email from the University of Antwerp regarding the Applicant’s scholarship. I find that the panel made no error in rejecting the two documents. The opinion was intended to address the RPD’s decision to award little weight to the Applicant’s support letters from Ethiopia but it did not deal with the unavailability of the writers of the letters and the vagueness in the letters themselves, both issues identified by the RPD. With respect to the email from the University, the Applicant made no submissions to the RAD as to the relevance of the document nor did the Applicant address the fact that the document pre-dated the RPD decision.
3. Did the RAD err in its assessment of the Applicant’s credibility?

[37] The Applicant submits that the RAD’s credibility findings regarding his central claim of persecution due to actual and imputed political opinions are unreasonable. He takes particular issue with the reasons which led the RAD to find that he was not detained and abused by the Ethiopian authorities in 2016: the omissions in his wife’s letter about the threats against her personally; the Applicant’s delay in exiting Ethiopia after the alleged detention; and his evolving testimony regarding the manner in which he exited Ethiopia by paying a bribe to an airport security officer.

[38] I have reviewed the Applicant’s arguments contesting the RAD’s confirmation of the RPD’s credibility findings. I find the RAD’s conclusions reasonable and its explanations thorough. In essence, the Applicant is asking the Court to re-weigh the evidence before both the RPD and the RAD.

[39] The Applicant submits that the RPD made no general negative credibility finding in its decision and that the RAD provides little analysis of this omission, stating only that the RPD did not err in its overall credibility findings. I do not find the Applicant’s argument persuasive. The RPD made a number of general or overall credibility findings in its decision. At the beginning of its analysis, the RPD panel noted “inconsistencies, omissions and implausibilities in the claimant’s evidence, some of which emerged from a comparison of the information the claimant provided in his BOC and other forms, and the testimony and explanations provided at the hearing”. The panel also made the general statement that the Applicant was not a credible witness as he often failed to answer questions directly despite being advised to do so. In addition to its general findings, the RPD assessed each aspect of the Applicant’s testimony and made discrete credibility findings throughout its decision. Despite the Applicant’s submissions, there is no lack of clarity in the RPD’s findings. The RPD’s credibility analysis is detailed and the RAD reasonably reviewed each element of that analysis.

[40] The Applicant’s refugee claim of political persecution is based primarily on his alleged detention and abuse by Ethiopian authorities in September 2016. Both the RPD and the RAD identified a series of material omissions and inconsistencies in the Applicant’s documentary evidence and testimony regarding his detention which, when coupled with his subsequent delay in exiting the country despite holding a Canadian visa, led to serious concerns regarding his credibility. The Applicant has pointed to no omissions or errors in the RAD’s review of the RPD’s decision that warrant intervention by this Court.
4. Did the RAD err in its refusal of the Applicant’s sur place claim?

[41] The RAD concluded that the Applicant’s activities in Canada were not sufficiently significant to warrant the attention of the Ethiopian authorities and dismissed his sur place claim. The Applicant challenges the RAD’s findings stating that the key issue in his case was whether his actions may have come to the notice of the Ethiopian authorities. He states that one need not be a leading figure or organizer in order to be targeted by the government.

[42] The analysis of a sur place claim is focused on whether the activities of an individual abroad might give rise to a negative reaction on the part of the authorities in their home country and lead to a reasonable chance of persecution in the event of return (Ngongo v Canada (Minister of Citizenship and Immigration), [1999] FCJ No 1627 (QL) at para 23). The application of the test was recently considered by Justice McVeigh in Gebremedhin v Canada (Immigration, Refugees and Citizenship), 2017 FC 497 at para 28:

[28] The legal threshold for a sur place claim should not be confused with the standard of proof. In order to show a well-founded fear of persecution under section 96 of the Act, an applicant must establish that there is a “reasonable chance” or “serious possibility” of persecution (Adjei v Canada (Minister of Employment and Immigration), [1989] 2 FC 680 (FCA) at paras 5-8; Sebastio v Canada (Minister of Citizenship and Immigration), 2016 FC 803 at paras 13-14 [Sebastio]). The standard of proof for facts on which a claimant relies is a balance of probabilities. However, once proven, the legal threshold to demonstrate persecution is only a “serious possibility”.

[43] The RAD reviewed the evidence of the Applicant’s political activities in Canada before the RPD and the new evidence regarding his participation in a protest and meeting in Toronto. The panel accepted his participation in the various events, noting that he can be seen in some of the videos posted of the events but that he is not identified individually.

[44] The RAD assessed whether the Applicant’s activities would come to the attention of the Ethiopian authorities. Based on its review of the documentary evidence for Ethiopia, the panel stated that the Ethiopian authorities’ monitoring of the diaspora centred on high-profile targets but acknowledged that there are varying opinions on how “high-profile” an individual must be in order to be monitored. The Applicant disagrees with the RAD’s review of the documentary evidence and takes the position that any individual who is actively involved in Ethiopian politics abroad may be monitored. In my view, this position does not accurately reflect either the various country reports in the record or the requirement that a claimant must provide credible evidence to establish, on a balance of probabilities, that they face a serious possibility of persecution.

[45] There is no suggestion in the record that the Applicant was a leader or organizer of any of the events in question. He relies solely on his participation in the Toronto events to establish his risk. I find that the RAD’s conclusion that the Applicant’s profile was not sufficient to establish that he would draw the attention of the Ethiopian authorities is consistent with the documentary evidence for Ethiopia and reasonable in light of the Applicant’s political activities in Canada.
VI. Conclusion

[46] The application will be dismissed.

[47] No question for certification was proposed by the parties and none arises in this case.


## 14106:5 · paragraphs 51-52

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `35786c79211e21dedf928af89ca13907899e40d7c662d7456e0c4c5f9dfdd2b2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 14106:5:subtheme:1 · paragraphs 51-52

- Raw key terms: `imm-4396-18, agernew, application, april, cause, certified, citizenship, court`
- Display key terms: `imm-4396-18, agernew, april, certified`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: imm-4396-18, agernew, april, certified Operative outcome context: JUDGMENT in IMM-4396-18 THIS COURT’S JUDGMENT is that: The application for judicial review is dismissed. Evidence spans paragraphs 51-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4692178` offsets `201-209`; context: No question of general importance is certified.
- Evidence: `disposition` cue `dismissed` at chunk `4692178` offsets `187-196`; context: JUDGMENT in IMM-4396-18
THIS COURT’S JUDGMENT is that:
The application for judicial review is dismissed.

#### Section text

JUDGMENT in IMM-4396-18
THIS COURT’S JUDGMENT is that:
The application for judicial review is dismissed.
No question of general importance is certified.
“Elizabeth Walker”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-4396-18
STYLE OF CAUSE:
AGERNEW TILAHUN ESHETIE v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
APRIL 4, 2018


## 14106:6 · paragraphs 53-53

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c2becd4243f07432b819891aea712faf37821390ccad9556b127b4932fd8bc04`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 14106:6:subtheme:1 · paragraphs 53-53

- Raw key terms: `appearances, applicant, attorney, august, canada, christodoulides, dated, general`
- Display key terms: `august, christodoulides, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: august, christodoulides, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 53-53. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
WALKER J.
DATED:
August 1, 2019
APPEARANCES:
Liyusew Kidane
For The Applicant
Laoura Christodoulides
For The Respondent
SOLICITORS OF RECORD:
The Law Office of Teklemichael AB Sahlemariam
Toronto, Ontario
For The Applicant
Attorney General of Canada
Toronto, Ontario
For The Respondent
