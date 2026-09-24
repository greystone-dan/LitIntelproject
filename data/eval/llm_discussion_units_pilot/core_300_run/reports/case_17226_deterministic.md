# Discussion Units: case 17226

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **68**
- Continuity pairs: **67**
- Discussion Units: **4**
- Paragraph source hashes: **68**
- Sub-themes: **17**

## 17226:1 · paragraphs 0-2

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5570b086cb6d6fa711632c205fd192a4824e03d8c895b420b9ceda9a83deccb0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 17226:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicants, decision, immigration, reasons, refugees, adebayo, alternative, appeal`
- Display key terms: `refugees, adebayo, alternative`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: refugees, adebayo, alternative Rule/authority context: The RPD had found that the Applicants are not Convention refugees or persons in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] because of their lack of  Application context: The RPD had found that the Applicants are not Convention refugees or persons in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] because of their lack of  Operative outcome context: [2] For the reasons that follow, the Application is dismissed. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `4813030` offsets `191-201`; context: The RPD had found that the Applicants are not Convention refugees or persons in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] because of their lack of credibility and because that they had a reasonable Internal Flight Alternative [IFA].
- Evidence: `governing_rule` cue `under` at chunk `4813030` offsets `278-283`; context: The RPD had found that the Applicants are not Convention refugees or persons in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] because of their lack of credibility and because that they had a reasonable Internal Flight Alternative [IFA].
- Evidence: `reasoning_application` cue `because` at chunk `4813030` offsets `374-381`; context: The RPD had found that the Applicants are not Convention refugees or persons in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] because of their lack of credibility and because that they had a reasonable Internal Flight Alternative [IFA].
- Evidence: `disposition` cue `dismissed` at chunk `4813031` offsets `52-61`; context: [2] For the reasons that follow, the Application is dismissed.

#### Section text

Adebayo v. Canada (Immigration, Refugees and Citizenship)
Court (s) Database
Federal Court Decisions
Date
2019-03-19
Neutral citation
2019 FC 330
File numbers
IMM-3778-18
Decision Content
Date: 20190319
Docket: IMM-3778-18
Citation: 2019 FC 330
Ottawa, Ontario, March 19, 2019
PRESENT: The Honourable Madam Justice Kane
BETWEEN:
OLUBUNMI SUSAN ADEBAYO, GBADEBO DAVE ADEBAYO, TIMILEYIN REBECCA ADEBAYO, OLUWABUKUNFUNMI PAUL ADEBAYO, DAMILOLA COMFORT ADEBAYO
Applicants
and
THE MINISTER OF IMMIGRATION, REFUGEES AND CITIZENSHIP CANADA
Respondent
JUDGMENT AND REASONS

[1] The Applicants seek judicial review of the July 24, 2018 decision of the Refugee Appeal Division [RAD], which confirmed the decision of the Refugee Protection Division [RPD]. The RPD had found that the Applicants are not Convention refugees or persons in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] because of their lack of credibility and because that they had a reasonable Internal Flight Alternative [IFA].

[2] For the reasons that follow, the Application is dismissed.


## 17226:2 · paragraphs 3-31

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d1aa36edeca34cfe00cbedf08cded6a7702ab4043b78ddb135d6c1c94179892a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 17226:2:subtheme:1 · paragraphs 3-8

- Raw key terms: `applicants, applicant, claim, elegosi, male, family, made, nigeria`
- Display key terms: `elegosi, male, family, made, nigeria`
- Argument roles: `evidence_fact, party_position`
- Explanation: Observed roles: evidence_fact, party_position Display terms: elegosi, male, family, made, nigeria Position/evidence statements: The Applicants claim that to assume this role, the Male Applicant must participate in rituals which are against the Applicants’ religious beliefs. | The Applicants claim that if they are returned to Nigeria, the Male Applicant’s uncle and other elders will find him, force him to take on this role and force the family to undergo the rituals. Evidence spans paragraphs 3-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claim` at chunk `4813032` offsets `339-344`; context: The Applicants claim that to assume this role, the Male Applicant must participate in rituals which are against the Applicants’ religious beliefs.
- Evidence: `party_position` cue `claim` at chunk `4813033` offsets `216-221`; context: The Applicants claim that if they are returned to Nigeria, the Male Applicant’s uncle and other elders will find him, force him to take on this role and force the family to undergo the rituals.
- Evidence: `evidence_fact` cue `found that` at chunk `4813035` offsets `75-85`; context: The RPD found that material aspects of their claim were not credible and that they had a viable IFA in Port Harcourt.
- Evidence: `party_position` cue `submitted` at chunk `4813036` offsets `43-52`; context: [7] The RPD considered a newspaper article submitted and relied on by the Applicants to support their claim.
- Evidence: `evidence_fact` cue `found that` at chunk `4813036` offsets `605-615`; context: The RPD concluded that the article was not genuine, accorded it no weight and found that it undermined the Applicants’ credibility.

#### 17226:2:subtheme:2 · paragraphs 9-11

- Raw key terms: `applicants, concluded, credibility, female, genital, mutilation, subjected, uncle`
- Display key terms: `concluded, credibility, female, genital, mutilation, subjected, uncle`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: concluded, credibility, female, genital, mutilation, subjected, uncle Position/evidence statements: [10] In the Applicants’ appeal to the RAD, they argued that the RPD erred in assessing their credibility and failed to conduct a full IFA analysis. Rule/authority context: The Decision under Review – the RAD Decision Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4813037` offsets `307-314`; context: The RPD found it neither plausible nor credible that the Male Applicant did not know whether his female relatives had been subjected to female genital mutilation, given that a central aspect of the claim was the alleged threat to his wife and daughters of female genital mutilation.
- Evidence: `evidence_fact` cue `found that` at chunk `4813037` offsets `17-27`; context: [8] The RPD also found that the Male Applicant’s testimony in response to questions about the role of the Elegosi to be vague, despite the Male Applicant having known for 20 years that he was expected to assume this role.
- Evidence: `governing_rule` cue `under` at chunk `4813038` offsets `320-325`; context: The Decision under Review – the RAD Decision
- Evidence: `party_position` cue `argued` at chunk `4813039` offsets `48-54`; context: [10] In the Applicants’ appeal to the RAD, they argued that the RPD erred in assessing their credibility and failed to conduct a full IFA analysis.

#### 17226:2:subtheme:3 · paragraphs 12-14

- Raw key terms: `applicants, found, harcourt, port, ability, analysis, appeal, applicant`
- Display key terms: `harcourt, port, ability, analysis`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: harcourt, port, ability, analysis Application context: [13] The RAD applied the two prong test established in Rasaratnam v Canada (Minister of Employment & Immigration), [1992] 1 FC 706, [1991] FCJ No 1256 (CA) [Rasaratnam]. Operative outcome context: [11] The RAD found that the determinative issue was whether the Applicants have an IFA in Port Harcourt, concluded that they did and dismissed the appeal. Evidence spans paragraphs 12-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4813040` offsets `42-47`; context: [11] The RAD found that the determinative issue was whether the Applicants have an IFA in Port Harcourt, concluded that they did and dismissed the appeal.
- Evidence: `evidence_fact` cue `found that` at chunk `4813040` offsets `13-23`; context: [11] The RAD found that the determinative issue was whether the Applicants have an IFA in Port Harcourt, concluded that they did and dismissed the appeal.
- Evidence: `disposition` cue `dismissed` at chunk `4813040` offsets `133-142`; context: [11] The RAD found that the determinative issue was whether the Applicants have an IFA in Port Harcourt, concluded that they did and dismissed the appeal.
- Evidence: `evidence_fact` cue `found that` at chunk `4813041` offsets `13-23`; context: [12] The RAD found that the RPD’s credibility findings were reasonable regarding the Applicants’ claims that the Male Applicant is required to take on the role of Elegosi and about the uncle’s ability to track them down.
- Evidence: `counterargument_limitation` cue `However` at chunk `4813041` offsets `221-228`; context: However, the RAD found that the RPD had erred by not conducting a full IFA analysis.
- Evidence: `reasoning_application` cue `applied` at chunk `4813042` offsets `13-20`; context: [13] The RAD applied the two prong test established in Rasaratnam v Canada (Minister of Employment & Immigration), [1992] 1 FC 706, [1991] FCJ No 1256 (CA) [Rasaratnam].

#### 17226:2:subtheme:4 · paragraphs 15-17

- Raw key terms: `agreed, applicants, evidence, applicant, harcourt, knowledge, lack, male`
- Display key terms: `agreed, harcourt, knowledge, lack, male`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: agreed, harcourt, knowledge, lack, male Evidence spans paragraphs 15-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4813043` offsets `30-37`; context: [14] The RAD first considered whether there is a serious possibility of persecution, risk to life, or risk of cruel and unusual treatment or punishment for the Applicants in Port Harcourt.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813043` offsets `210-218`; context: The RAD reviewed the evidence and agreed with the RPD that on a balance of probabilities, the allegations of persecution were not credible.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813044` offsets `103-111`; context: [15] The RAD agreed with the RPD’s concerns about the newspaper article, which was the Applicants’ key evidence, and accorded it no weight.
- Evidence: `evidence_fact` cue `found that` at chunk `4813045` offsets `194-204`; context: The RAD found that other evidence, such as the psychological report for the Principal Applicant, a letter of support from family members and objective evidence in the national documentation package, did not support the fear of female genital mutilation.

#### 17226:2:subtheme:5 · paragraphs 18-20

- Raw key terms: `credibility, decision, findings, standard, whether, acknowledged, advantage, analysis`
- Display key terms: `credibility, findings, standard, whether, acknowledged, advantage, analysis`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: credibility, findings, standard, whether, acknowledged, advantage, analysis Rule/authority context: The Standard of Review Application context: The RAD noted the high threshold that applies, requiring evidence of conditions which would jeopardize the life and safety of a claimant. Evidence spans paragraphs 18-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4813046` offsets `29-36`; context: [17] The RAD then considered whether it would be unreasonable in the circumstances for the Applicants to seek refuge in Port Harcourt.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813046` offsets `192-200`; context: The RAD noted the high threshold that applies, requiring evidence of conditions which would jeopardize the life and safety of a claimant.
- Evidence: `reasoning_application` cue `applies` at chunk `4813046` offsets `173-180`; context: The RAD noted the high threshold that applies, requiring evidence of conditions which would jeopardize the life and safety of a claimant.
- Evidence: `issue` cue `issue` at chunk `4813047` offsets `9-14`; context: [18] The issue is whether the RAD’s decision is reasonable.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `4813047` offsets `241-259`; context: The Standard of Review
- Evidence: `evidence_fact` cue `testimony` at chunk `4813048` offsets `267-276`; context: However, the RAD may defer to the RPD on credibility findings “where the RPD enjoys a meaningful advantage”, for example, where the RPD has heard the testimony first hand (Canada (Citizenship and Immigration) v Huruglica, 2016 FCA 93 at para 70, [2016] 4 FCR 157 [Huruglica]).
- Evidence: `counterargument_limitation` cue `However` at chunk `4813048` offsets `117-124`; context: However, the RAD may defer to the RPD on credibility findings “where the RPD enjoys a meaningful advantage”, for example, where the RPD has heard the testimony first hand (Canada (Citizenship and Immigration) v Huruglica, 2016 FCA 93 at para 70, [2016] 4 FCR 157 [Huruglica]).

#### 17226:2:subtheme:6 · paragraphs 21-22

- Raw key terms: `paras, reasonableness, standard, acws, analysis, applies, canada, citizenship`
- Display key terms: `paras, reasonableness, standard, acws, analysis, applies`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: paras, reasonableness, standard, acws, analysis, applies Application context: [20] In the Court’s judicial review of a decision of the RAD, the Court applies the reasonableness standard with respect to the RAD’s determinations of factual issues, including credibility, and issues of mixed fact and  Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4813049` offsets `160-166`; context: [20] In the Court’s judicial review of a decision of the RAD, the Court applies the reasonableness standard with respect to the RAD’s determinations of factual issues, including credibility, and issues of mixed fact and law (Huruglica at paras 30-35).
- Evidence: `reasoning_application` cue `applies` at chunk `4813049` offsets `72-79`; context: [20] In the Court’s judicial review of a decision of the RAD, the Court applies the reasonableness standard with respect to the RAD’s determinations of factual issues, including credibility, and issues of mixed fact and law (Huruglica at paras 30-35).

#### 17226:2:subtheme:7 · paragraphs 23-31

- Raw key terms: `applicants, credibility, argue, canada, decision, evidence, finding, immigration`
- Display key terms: `credibility, argue, finding`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: credibility, argue, finding Position/evidence statements: [24] The Applicants argue that the RAD’s credibility findings are unreasonable because they were based on skepticism rather than an analysis of evidence. | [25] The Applicants submit that the RAD’s assessment of the newspaper article was unreasonable. Application context: [24] The Applicants argue that the RAD’s credibility findings are unreasonable because they were based on skepticism rather than an analysis of evidence. Evidence spans paragraphs 23-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4813051` offsets `161-168`; context: [22] The reasonableness standard focuses on “the existence of justification, transparency and intelligibility within the decision-making process” and considers “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir v New Brunswick, 2008 SCC 9 at para 47, [2008] 1 SCR 190).
- Evidence: `evidence_fact` cue `testimony` at chunk `4813052` offsets `132-141`; context: , the decision makers that hear the testimony and review the evidence—are ideally placed to assess credibility: Aguebor v Canada (Minister of Employment and Immigration), [1993] FCJ No 732 (QL) at para 4, 160 NR 315 (CA).
- Evidence: `party_position` cue `argue` at chunk `4813053` offsets `20-25`; context: [24] The Applicants argue that the RAD’s credibility findings are unreasonable because they were based on skepticism rather than an analysis of evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813053` offsets `144-152`; context: [24] The Applicants argue that the RAD’s credibility findings are unreasonable because they were based on skepticism rather than an analysis of evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4813053` offsets `79-86`; context: [24] The Applicants argue that the RAD’s credibility findings are unreasonable because they were based on skepticism rather than an analysis of evidence.
- Evidence: `party_position` cue `submit` at chunk `4813054` offsets `20-26`; context: [25] The Applicants submit that the RAD’s assessment of the newspaper article was unreasonable.
- Evidence: `party_position` cue `argue` at chunk `4813055` offsets `175-180`; context: The Applicants argue that his testimony was sufficiently detailed given the Male Applicant’s explanation that he had left his community as a child.
- Evidence: `evidence_fact` cue `testimony` at chunk `4813055` offsets `97-106`; context: [26] The Applicants dispute the RAD’s finding that the Male Applicant was not forthcoming in his testimony regarding the traditional rituals the family feared.
- Evidence: `party_position` cue `submit` at chunk `4813056` offsets `28-34`; context: [27] The Applicants further submit that the RAD failed to consider the Principal Applicant’s psychological report in assessing her credibility or the viability of the IFA.
- Evidence: `party_position` cue `submit` at chunk `4813057` offsets `25-31`; context: [28] The Applicants also submit that the RAD erred by ignoring relevant objective evidence about the pervasiveness of female genital mutilation in Nigeria.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813057` offsets `82-90`; context: [28] The Applicants also submit that the RAD erred by ignoring relevant objective evidence about the pervasiveness of female genital mutilation in Nigeria.
- Evidence: `party_position` cue `submits` at chunk `4813058` offsets `20-27`; context: [29] The Respondent submits that the RAD reasonably found that the newspaper article relied on by the Applicants as a central piece of evidence lacked credibility.
- Evidence: `evidence_fact` cue `found that` at chunk `4813058` offsets `52-62`; context: [29] The Respondent submits that the RAD reasonably found that the newspaper article relied on by the Applicants as a central piece of evidence lacked credibility.
- Evidence: `party_position` cue `submits` at chunk `4813059` offsets `28-35`; context: [30] The Respondent further submits that the RAD did not err in its credibility findings.

#### Section text

I. Background

[3] The Applicants are a family of five—the Principal Applicant, the Male Applicant and their three children—and are citizens of Nigeria. The Applicants recount that the Male Applicant is obliged to become a traditional chief in their town in Nigeria, called the Elegosi, as the first male grandchild of the previous chief. The Applicants claim that to assume this role, the Male Applicant must participate in rituals which are against the Applicants’ religious beliefs. They also allege that the Principal Applicant and her daughters would be subjected to female genital mutilation and that their son would be forced to have traditional incisions made on his body.

[4] The Applicants recount that they faced harassment and threats from the Male Applicant’s uncle and other elders in their community due to the Male Applicant’s reluctance to become the next Elegosi. The Applicants claim that if they are returned to Nigeria, the Male Applicant’s uncle and other elders will find him, force him to take on this role and force the family to undergo the rituals. The Applicants claim that the uncle is wealthy and powerful and would be supported by corrupt police to track down the Applicants.

[5] The Applicants recount that while they were on vacation in the United States in 2016, the Male Applicant’s grandfather, who was the presiding Elegosi, died. The Male Applicant’s family demanded that they return home to Nigeria. The Male Applicant testified at the RPD hearing that threats were made by his uncle to his in-laws in an effort to have the Applicants return. The Applicants state that they did not seek asylum in the United States due to the high cost of living and other factors. The Applicants travelled to Canada and sought refugee protection in May 2017.
A. The RPD decision

[6] On September 14, 2017, the RPD rejected the Applicants’ claim. The RPD found that material aspects of their claim were not credible and that they had a viable IFA in Port Harcourt.

[7] The RPD considered a newspaper article submitted and relied on by the Applicants to support their claim. The article names the Male Applicant as the next Elegosi and mentions the required rituals. The RPD noted that there were several grammatical and other errors in the article, including a sentence that was a fragment, which was not consistent with the quality of the other articles in the same newspaper. The RPD also noted a border around the article which made it appear that the page was photocopied onto the paper. The RPD concluded that the article was not genuine, accorded it no weight and found that it undermined the Applicants’ credibility.

[8] The RPD also found that the Male Applicant’s testimony in response to questions about the role of the Elegosi to be vague, despite the Male Applicant having known for 20 years that he was expected to assume this role. The RPD found it neither plausible nor credible that the Male Applicant did not know whether his female relatives had been subjected to female genital mutilation, given that a central aspect of the claim was the alleged threat to his wife and daughters of female genital mutilation. Similarly, the RPD found that the Male Applicant’s testimony regarding the ability of the Male Applicant’s uncle to find them was vague and inconsistent with their documentary evidence, given their allegation that the uncle had harassed the family for years, causing them to move multiple times. The RPD concluded, on a balance of probabilities, that the Male Applicant was not expected to become the next Elegosi.

[9] The RPD gave little weight to other supporting documents and concluded that they could not overcome the credibility concerns. The RPD concluded that the Applicants are not being pursued by the uncle and that they would not be forcibly subjected to female genital mutilation or traditional incisions.
B. The Decision under Review – the RAD Decision

[10] In the Applicants’ appeal to the RAD, they argued that the RPD erred in assessing their credibility and failed to conduct a full IFA analysis.

[11] The RAD found that the determinative issue was whether the Applicants have an IFA in Port Harcourt, concluded that they did and dismissed the appeal.

[12] The RAD found that the RPD’s credibility findings were reasonable regarding the Applicants’ claims that the Male Applicant is required to take on the role of Elegosi and about the uncle’s ability to track them down. However, the RAD found that the RPD had erred by not conducting a full IFA analysis. The RAD conducted this analysis and reached the same conclusion: that the Applicants have an IFA in Port Harcourt.

[13] The RAD applied the two prong test established in Rasaratnam v Canada (Minister of Employment & Immigration), [1992] 1 FC 706, [1991] FCJ No 1256 (CA) [Rasaratnam].

[14] The RAD first considered whether there is a serious possibility of persecution, risk to life, or risk of cruel and unusual treatment or punishment for the Applicants in Port Harcourt. The RAD reviewed the evidence and agreed with the RPD that on a balance of probabilities, the allegations of persecution were not credible.

[15] The RAD agreed with the RPD’s concerns about the newspaper article, which was the Applicants’ key evidence, and accorded it no weight. The RAD also agreed that the Male Applicant’s testimony was undermined by his lack of knowledge about the Elegosi’s duties and by his vague testimony about his uncle’s ability and motive to find the Applicants and force the Male Applicant to be the next Elegosi.

[16] The RAD also agreed that the fear of forced female genital mutilation lacked credibility due to the Male Applicant’s lack of knowledge about the traditional practice in his family. The RAD found that other evidence, such as the psychological report for the Principal Applicant, a letter of support from family members and objective evidence in the national documentation package, did not support the fear of female genital mutilation. The RAD concluded that the Applicants are not at risk of forced female genital mutilation in Nigeria or Port Harcourt in particular.

[17] The RAD then considered whether it would be unreasonable in the circumstances for the Applicants to seek refuge in Port Harcourt. The RAD noted the high threshold that applies, requiring evidence of conditions which would jeopardize the life and safety of a claimant. The RAD noted that Port Harcourt is a major urban area and suggested that there would not be significant cultural challenges in a big city. The RAD acknowledged that the Applicants may face some economic hardship but noted that the Applicants had been and could be self‑employed. The RAD found that the social conditions do not rise to a level which would jeopardize their lives.
II. The Issues

[18] The issue is whether the RAD’s decision is reasonable. This in turn requires consideration of:
Whether the RAD erred in finding that the RPD’s credibility findings are reasonable; and
Whether the RAD erred in its IFA analysis.
III. The Standard of Review

[19] The RAD conducts an appeal of the RPD’s decision and reviews the RPD’s findings on the standard of correctness. However, the RAD may defer to the RPD on credibility findings “where the RPD enjoys a meaningful advantage”, for example, where the RPD has heard the testimony first hand (Canada (Citizenship and Immigration) v Huruglica, 2016 FCA 93 at para 70, [2016] 4 FCR 157 [Huruglica]).

[20] In the Court’s judicial review of a decision of the RAD, the Court applies the reasonableness standard with respect to the RAD’s determinations of factual issues, including credibility, and issues of mixed fact and law (Huruglica at paras 30-35).

[21] The determination of the RAD regarding an IFA analysis is also reviewed on the standard of reasonableness: Ugbekile v Canada (Citizenship and Immigration), 2016 FC 1397 at paras 12-14, 275 ACWS (3d) 360.

[22] The reasonableness standard focuses on “the existence of justification, transparency and intelligibility within the decision-making process” and considers “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir v New Brunswick, 2008 SCC 9 at para 47, [2008] 1 SCR 190).

[23] With respect to credibility findings, it is well-established that boards and tribunals—i.e., the decision makers that hear the testimony and review the evidence—are ideally placed to assess credibility: Aguebor v Canada (Minister of Employment and Immigration), [1993] FCJ No 732 (QL) at para 4, 160 NR 315 (CA). Their credibility findings should be given significant deference: Lin v Canada (Citizenship and Immigration), 2008 FC 1052 at para 13, [2008] FCJ No 1329 (QL); Fatih v Canada (Citizenship and Immigration), 2012 FC 857 at para 65, 415 FTR 82; Lubana v Canada (Minister of Citizenship and Immigration), 2003 FCT 116 at para 7, 228 FTR 43.
IV. Did the RAD err in finding that the RPD’s credibility findings were reasonable?
A. The Applicants’ Submissions

[24] The Applicants argue that the RAD’s credibility findings are unreasonable because they were based on skepticism rather than an analysis of evidence. They allege that the RAD simply adopted the RPD’s findings. The Applicants also argue that they are entitled to the presumption of truth in their sworn statement (Maldonado v Canada (Minister of Employment and Immigration), [1980] 2 FC 302 at para 5, [1979] FCJ No 248 (QL) (CA).

[25] The Applicants submit that the RAD’s assessment of the newspaper article was unreasonable. They argue that the RAD did not identify specific errors in the article other than one incomplete sentence. They submit that the incomplete sentence is not incomplete and “conveys meaning”. The Applicants also submit that it is an error to assess the article by western standards and that other articles in the newspaper also contained some errors. Moreover, spelling and grammar errors do not prove that a document is fraudulent (Mohamud v Canada (Citizenship and Immigration), 2018 FC 170 at paras 6-8, 289 ACWS (3d) 600 [Mohamud]). The Applicants point to a formatting error in the RAD decision as an example, noting that this does not indicate that the decision is inauthentic.

[26] The Applicants dispute the RAD’s finding that the Male Applicant was not forthcoming in his testimony regarding the traditional rituals the family feared. The Applicants argue that his testimony was sufficiently detailed given the Male Applicant’s explanation that he had left his community as a child.

[27] The Applicants further submit that the RAD failed to consider the Principal Applicant’s psychological report in assessing her credibility or the viability of the IFA. The Applicants argue that the failure to address the psychological report renders the decision unreasonable, particularly regarding the reasonableness of the IFA (Atay v Canada (Citizenship and Immigration), 2008 FC 201 at para 32, [2008] FCJ No 251 (QL) [Atay]).

[28] The Applicants also submit that the RAD erred by ignoring relevant objective evidence about the pervasiveness of female genital mutilation in Nigeria. The Applicants dispute the RAD’s finding that the objective evidence demonstrates that in Nigeria, parents can refuse female genital mutilation and the practice is banned. The Applicants point to other parts of the National Documentation Package which state that the practice remains prevalent and there is little enforcement of the law.
B. The Respondent’s Submissions

[29] The Respondent submits that the RAD reasonably found that the newspaper article relied on by the Applicants as a central piece of evidence lacked credibility. It contained errors and irregularities that were not consistent with the quality of other articles in the same publication. The RAD reasonably assigned it little weight.

[30] The Respondent further submits that the RAD did not err in its credibility findings. The Respondent submits that it was not credible that the Male Applicant would have such limited knowledge of the traditional practice of female genital mutilation in his own family given that this is a central element of the alleged persecution.
C. The RAD did not err in finding that the credibility findings were reasonable

## 17226:3 · paragraphs 32-39

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7183ec2396938db71b3ed3b92bf6f80e167b95f409726c6ad73ac15499dd4742`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 17226:3:subtheme:1 · paragraphs 32-37

- Raw key terms: `article, applicants, applicant, court, male, newspaper, assessment, ekiti`
- Display key terms: `article, male, newspaper, assessment, ekiti`
- Argument roles: `counterargument_limitation, evidence_fact`
- Explanation: Observed roles: counterargument_limitation, evidence_fact Display terms: article, male, newspaper, assessment, ekiti Evidence spans paragraphs 32-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `testimony` at chunk `4813060` offsets `182-191`; context: [31] Contrary to the Applicants’ submission, the RAD is entitled to rely on the credibility findings of the RPD, as the RPD had an advantage in conducting the hearing, receiving the testimony of the Applicants and questioning them.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813061` offsets `84-92`; context: [32] The Applicants acknowledge that the newspaper article was the central piece of evidence they relied on to support their allegation that they would face persecution by the uncle upon their return.
- Evidence: `evidence_fact` cue `found that` at chunk `4813062` offsets `24-34`; context: [33] The RAD reasonably found that the newspaper article, which identifies the Male Applicant as the next Elegosi in Ilogbo Ekiti, was not credible.
- Evidence: `counterargument_limitation` cue `However` at chunk `4813063` offsets `356-363`; context: However, the errors in the newspaper articles go well beyond typographical and clerical errors.
- Evidence: `evidence_fact` cue `found that` at chunk `4813064` offsets `24-34`; context: [35] The RAD reasonably found that the RPD’s assessment of the article was reasonable and was entitled to defer to the RPD’s findings (Huruglica, at para 70).
- Evidence: `counterargument_limitation` cue `However` at chunk `4813064` offsets `159-166`; context: However, the RAD also assessed the article and the Male Applicant’s testimony and found that the problems identified could not be explained by the Male Applicant.

#### 17226:3:subtheme:2 · paragraphs 38-39

- Raw key terms: `applicant, applicants, evidence, added, allegations, argument, asked, assessing`
- Display key terms: `added, allegations, argument, asked, assessing`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: added, allegations, argument, asked, assessing Position/evidence statements: Applicants cannot simply point to Maldonado as a “cure all” for a claim that is not supported with credible evidence. Application context: [38] The Applicants’ submission that the RAD failed to consider the Principal Applicant’s psychological report in assessing her credibility is without merit because the Principal Applicant did not provide any oral eviden Evidence spans paragraphs 38-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4813066` offsets `961-967`; context: These issues were put to the Male Applicant and his testimony was found not to be credible.
- Evidence: `party_position` cue `claim` at chunk `4813066` offsets `365-370`; context: Applicants cannot simply point to Maldonado as a “cure all” for a claim that is not supported with credible evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813066` offsets `407-415`; context: Applicants cannot simply point to Maldonado as a “cure all” for a claim that is not supported with credible evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813067` offsets `214-222`; context: [38] The Applicants’ submission that the RAD failed to consider the Principal Applicant’s psychological report in assessing her credibility is without merit because the Principal Applicant did not provide any oral evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4813067` offsets `157-164`; context: [38] The Applicants’ submission that the RAD failed to consider the Principal Applicant’s psychological report in assessing her credibility is without merit because the Principal Applicant did not provide any oral evidence.

#### Section text

[31] Contrary to the Applicants’ submission, the RAD is entitled to rely on the credibility findings of the RPD, as the RPD had an advantage in conducting the hearing, receiving the testimony of the Applicants and questioning them. In the present case, the RAD also conducted its own assessment of the evidence by reviewing the transcript of the hearing and the documentary evidence.

[32] The Applicants acknowledge that the newspaper article was the central piece of evidence they relied on to support their allegation that they would face persecution by the uncle upon their return. There was little other evidence provided.

[33] The RAD reasonably found that the newspaper article, which identifies the Male Applicant as the next Elegosi in Ilogbo Ekiti, was not credible. The errors noted are not simply typos or missed punctuation. Rather, there are sentences that have no beginning or end which make no sense (for example, “the leadership is on their side which has always being” and “learnt the Oba of the town”).

[34] As noted in Mohamud at paras 6-7 by Justice Grammond, typographical errors are not enough to find a document to be fraudulent and “clerical errors are not necessarily determinative of authenticity (see Arubi v Canada (Citizenship and Immigration), 2012 FC 36 at para 35). They occur even in decisions of this Court (Ali at para 31)” [emphasis added]. However, the errors in the newspaper articles go well beyond typographical and clerical errors. The RPD had the benefit of reviewing the quality of the original article and comparing it to other articles in the same newspaper. The RPD acknowledged that other articles contained some awkward language, but not to the extent of the article relied on by the Applicants. The RPD also noted the odd border which suggested that the article was pasted into the newspaper.

[35] The RAD reasonably found that the RPD’s assessment of the article was reasonable and was entitled to defer to the RPD’s findings (Huruglica, at para 70). However, the RAD also assessed the article and the Male Applicant’s testimony and found that the problems identified could not be explained by the Male Applicant. The Court agrees that the Male Applicant’s testimony was scarce and vague regarding the article. He indicated that he had only read it once and that he was aware that his name was mentioned in the article.

[36] The Court also notes that the content of the article would not support the Applicants’ claims of persecution by his uncle in any event. The article appears to be a criticism of the antiquated practices in Ilogbo Ekiti, noting that the barbaric practices, including eating human flesh, are “unacceptable in today’s society”. The article questions why these practices would continue given the many prominent and educated members of this town. The article notes that the Male Applicant, who would succeed his grandfather as Elegosi, had left the country, first for South Africa and then for the United States. It does not mention that his uncle is threatening him to return.

[37] With respect to the Applicants’ argument that they are entitled to the presumption of truth in their sworn statement (Maldonado v Canada (Minister of Employment and Immigration), [1980] 2 FC 302, [1979] FCJ No 248 at para 5 (CA) [Maldonado]), I note that this presumption was clearly rebutted. Applicants cannot simply point to Maldonado as a “cure all” for a claim that is not supported with credible evidence. The oft-cited principle must be read in its entirety and understood: “[w]hen an applicant swears to the truth of certain allegations, this creates a presumption that those allegations are true unless there be reason to doubt their truthfulness” [emphasis added]. In the present case, the RPD had reason to doubt the truthfulness of the allegations regarding the role of the Elegosi, the Male Applicant’s uncle’s threats and the risk that the Applicants would be subjected to the rituals which they claimed stemmed from being the Elegosi. These issues were put to the Male Applicant and his testimony was found not to be credible.

[38] The Applicants’ submission that the RAD failed to consider the Principal Applicant’s psychological report in assessing her credibility is without merit because the Principal Applicant did not provide any oral evidence. She was asked if she wished to do so and declined.

## 17226:4 · paragraphs 40-67

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `281a41eeb7535cdd22b11c7d200ed3b676fbb6291c6799d58a810377d4144627`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 17226:4:subtheme:1 · paragraphs 40-43

- Raw key terms: `applicant, applicants, male, credible, elegosi, explain, power, role`
- Display key terms: `male, credible, elegosi, explain, power, role`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: male, credible, elegosi, explain, power, role Position/evidence statements: His explanation that he had left his town as a child is not sufficient to excuse him from knowledge of the very rituals he claims he and his family will be subjected to and which form the basis of their claim for protect | [42] The Applicants submit that the RAD erred in finding that they had an IFA in Port Harcourt. Application context: As the RAD noted, he claims that he has known for over 20 years that he would become the Elegosi because he is the first male grandchild. Evidence spans paragraphs 40-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `4813068` offsets `222-228`; context: His explanation that he had left his town as a child is not sufficient to excuse him from knowledge of the very rituals he claims he and his family will be subjected to and which form the basis of their claim for protection.
- Evidence: `evidence_fact` cue `testimony` at chunk `4813068` offsets `49-58`; context: [39] Contrary to the Applicants’ submission, the testimony of the Male Applicant was not detailed.
- Evidence: `reasoning_application` cue `because` at chunk `4813068` offsets `421-428`; context: As the RAD noted, he claims that he has known for over 20 years that he would become the Elegosi because he is the first male grandchild.
- Evidence: `issue` cue `whether` at chunk `4813069` offsets `73-80`; context: [40] The Male Applicant could not explain the power held by the Elegosi, whether the role was only spiritual or whether there was any influence over the local or other government, or the size of the town over which the Elegosi would reign.
- Evidence: `evidence_fact` cue `testimony` at chunk `4813070` offsets `20-29`; context: [41] Similarly, his testimony regarding his uncle’s ability to find the Applicants was very vague.
- Evidence: `party_position` cue `submit` at chunk `4813071` offsets `20-26`; context: [42] The Applicants submit that the RAD erred in finding that they had an IFA in Port Harcourt.

#### 17226:4:subtheme:2 · paragraphs 44-48

- Raw key terms: `harcourt, port, applicants, applicant, evidence, find, analysis, argue`
- Display key terms: `harcourt, port, find, analysis, argue`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: harcourt, port, find, analysis, argue Position/evidence statements: [43] First, the Applicants argue that the RAD erred in its analysis of the whether there was a serious risk of persecution in the proposed IFA by ignoring their evidence that the uncle could use his power and influence w | [44] Second, the Applicants argue that the RAD failed to consider the Applicant’s circumstances. Application context: The Applicants argue that Port Harcourt is an unreasonable IFA because the cost of living is too high, they will be regarded as outsiders, their children will not be able to attend the best schools and, contrary to the R | The Respondent submits that the RAD applied the correct test to determine the IFA and that its findings are reasonable. Evidence spans paragraphs 44-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4813072` offsets `75-82`; context: [43] First, the Applicants argue that the RAD erred in its analysis of the whether there was a serious risk of persecution in the proposed IFA by ignoring their evidence that the uncle could use his power and influence with the police to find them.
- Evidence: `party_position` cue `argue` at chunk `4813072` offsets `27-32`; context: [43] First, the Applicants argue that the RAD erred in its analysis of the whether there was a serious risk of persecution in the proposed IFA by ignoring their evidence that the uncle could use his power and influence with the police to find them.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813072` offsets `161-169`; context: [43] First, the Applicants argue that the RAD erred in its analysis of the whether there was a serious risk of persecution in the proposed IFA by ignoring their evidence that the uncle could use his power and influence with the police to find them.
- Evidence: `party_position` cue `argue` at chunk `4813073` offsets `28-33`; context: [44] Second, the Applicants argue that the RAD failed to consider the Applicant’s circumstances.
- Evidence: `reasoning_application` cue `because` at chunk `4813073` offsets `160-167`; context: The Applicants argue that Port Harcourt is an unreasonable IFA because the cost of living is too high, they will be regarded as outsiders, their children will not be able to attend the best schools and, contrary to the RAD’s speculation, they will not be able to start their businesses.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813074` offsets `33-41`; context: [45] The Applicants point to the evidence about Port Harcourt in the national documentation package, which notes that the costs of living, housing and healthcare are high and that it is difficult to find employment.
- Evidence: `party_position` cue `argued` at chunk `4813075` offsets `61-67`; context: [46] At the hearing of this Application, the Applicants also argued that the RAD ignored the Principal Applicant’s psychological report and the submission that an IFA in Port Harcourt would be detrimental to her mental health.
- Evidence: `party_position` cue `submits` at chunk `4813076` offsets `84-91`; context: The Respondent submits that the RAD applied the correct test to determine the IFA and that its findings are reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813076` offsets `270-278`; context: The RAD conducted a full IFA analysis and in doing so, reviewed all the relevant evidence and concluded that there was no credible evidence of the key allegations that the Male Applicant’s uncle would persecute them and subject them to rituals, let alone evidence that he would find them in Port Harcourt.
- Evidence: `reasoning_application` cue `applied` at chunk `4813076` offsets `105-112`; context: The Respondent submits that the RAD applied the correct test to determine the IFA and that its findings are reasonable.

#### 17226:4:subtheme:3 · paragraphs 49-52

- Raw key terms: `proposed, unreasonable, canada, circumstances, claimant, employment, enough, immigration`
- Display key terms: `proposed, unreasonable, circumstances, employment, enough`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: proposed, unreasonable, circumstances, employment, enough Position/evidence statements: [48] The Respondent submits that the Applicants failed to provide sufficient evidence to establish that it would be unreasonable for them to relocate to Port Harcourt. Rule/authority context: The IFA Finding is reasonable (1) The jurisprudence Application context: [49] The two part test for an IFA established in Rasaratnam has been consistently applied and elaborated upon, including in Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] 1 FC 589 at paras 2,  Evidence spans paragraphs 49-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4813077` offsets `234-240`; context: The Respondent notes that housing and living costs and employment issues are not enough to reject an IFA; the circumstances must be unduly harsh in the proposed IFA and there is no evidence that this is the case.
- Evidence: `party_position` cue `submits` at chunk `4813077` offsets `20-27`; context: [48] The Respondent submits that the Applicants failed to provide sufficient evidence to establish that it would be unreasonable for them to relocate to Port Harcourt.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813077` offsets `77-85`; context: [48] The Respondent submits that the Applicants failed to provide sufficient evidence to establish that it would be unreasonable for them to relocate to Port Harcourt.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4813077` offsets `422-435`; context: The IFA Finding is reasonable
(1) The jurisprudence
- Evidence: `reasoning_application` cue `applied` at chunk `4813078` offsets `82-89`; context: [49] The two part test for an IFA established in Rasaratnam has been consistently applied and elaborated upon, including in Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] 1 FC 589 at paras 2, 12, [1993] FCJ No 1172 (QL) (CA) [Thirunavukkarasu].

#### 17226:4:subtheme:4 · paragraphs 53-57

- Raw key terms: `test, claimant, country, onus, place, refugee, safe, threshold`
- Display key terms: `country, onus, place, refugee, safe, threshold`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: country, onus, place, refugee, safe, threshold Position/evidence statements: First, as this Court said in Thirunavukkarasu, the definition of refugee under the Convention “requires claimants to be unable or unwilling by reason of fear of persecution to claim the protection of their home country i | Therefore, a refugee claimant cannot seek the refugee protection of another country while there is a place within their own country—even if it may not be where they wish to live—which offers safety from the risk they cla Rule/authority context: First, as this Court said in Thirunavukkarasu, the definition of refugee under the Convention “requires claimants to be unable or unwilling by reason of fear of persecution to claim the protection of their home country i | [52] In Valasquez v Canada (Citizenship and Immigration), 2010 FC 1201, [2010] FCJ No 1496 (QL), relied on by the Applicants, Justice O’Reilly summarized the approach and principles from the jurisprudence at paragraph 15 Application context: [52] In Valasquez v Canada (Citizenship and Immigration), 2010 FC 1201, [2010] FCJ No 1496 (QL), relied on by the Applicants, Justice O’Reilly summarized the approach and principles from the jurisprudence at paragraph 15 | Therefore, a refugee claimant cannot seek the refugee protection of another country while there is a place within their own country—even if it may not be where they wish to live—which offers safety from the risk they cla Evidence spans paragraphs 53-57. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4813081` offsets `410-417`; context: The absence of relatives in a safe place, whether taken alone or in conjunction with other factors, can only amount to such condition if it meets that threshold, that is to say if it establishes that, as a result, a claimant's life or safety would be jeopardized.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813081` offsets `339-347`; context: In addition, it requires actual and concrete evidence of such conditions.
- Evidence: `party_position` cue `claim` at chunk `4813082` offsets `261-266`; context: First, as this Court said in Thirunavukkarasu, the definition of refugee under the Convention “requires claimants to be unable or unwilling by reason of fear of persecution to claim the protection of their home country in any part of that country”.
- Evidence: `governing_rule` cue `under` at chunk `4813082` offsets `158-163`; context: First, as this Court said in Thirunavukkarasu, the definition of refugee under the Convention “requires claimants to be unable or unwilling by reason of fear of persecution to claim the protection of their home country in any part of that country”.
- Evidence: `governing_rule` cue `principles` at chunk `4813083` offsets `171-181`; context: [52] In Valasquez v Canada (Citizenship and Immigration), 2010 FC 1201, [2010] FCJ No 1496 (QL), relied on by the Applicants, Justice O’Reilly summarized the approach and principles from the jurisprudence at paragraph 15:
The concept of an IFA is an inherent part of the Convention refugee definition because a claimant must be a refugee from a country, not from a particular region of a country (Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706 at para 6).
- Evidence: `reasoning_application` cue `because` at chunk `4813083` offsets `301-308`; context: [52] In Valasquez v Canada (Citizenship and Immigration), 2010 FC 1201, [2010] FCJ No 1496 (QL), relied on by the Applicants, Justice O’Reilly summarized the approach and principles from the jurisprudence at paragraph 15:
The concept of an IFA is an inherent part of the Convention refugee definition because a claimant must be a refugee from a country, not from a particular region of a country (Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706 at para 6).
- Evidence: `party_position` cue `claim` at chunk `4813084` offsets `369-374`; context: Therefore, a refugee claimant cannot seek the refugee protection of another country while there is a place within their own country—even if it may not be where they wish to live—which offers safety from the risk they claim and is not unreasonable in all the circumstances.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813084` offsets `504-512`; context: In all cases, a refugee claimant bears the onus of establishing with objective evidence that the proposed IFA is unreasonable.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4813084` offsets `27-40`; context: [53] As highlighted in the jurisprudence, a refugee claimant is a refugee from their country as a whole, not from a village or region of their country.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4813084` offsets `152-161`; context: Therefore, a refugee claimant cannot seek the refugee protection of another country while there is a place within their own country—even if it may not be where they wish to live—which offers safety from the risk they claim and is not unreasonable in all the circumstances.
- Evidence: `reasoning_application` cue `applied` at chunk `4813085` offsets `13-20`; context: [54] The RAD applied the correct test and did not err in finding that the Applicants had not met the onus on them to establish on a balance of probabilities that the IFA in Port Harcourt is not reasonable.

#### 17226:4:subtheme:5 · paragraphs 58-60

- Raw key terms: `agent, allegation, alleged, applicant, applicants, daughters, evidence, female`
- Display key terms: `agent, allegation, alleged, daughters, female`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: agent, allegation, alleged, daughters, female Position/evidence statements: [56] The RAD acknowledged the general articles submitted by the Applicants regarding female genital mutilation as a harmful practice. Evidence spans paragraphs 58-60. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4813086` offsets `71-78`; context: [55] With respect to the first part of the test, the RAD’s analysis of whether the Applicants were at a serious risk of persecution focused on whether it was likely that the Male Applicant’s uncle—who was the alleged agent of persecution—would find them.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813086` offsets `301-309`; context: The RAD noted that the Applicants provided no evidence of how the uncle knew they had gone to the United States or had moved within Nigeria.
- Evidence: `party_position` cue `submitted` at chunk `4813087` offsets `47-56`; context: [56] The RAD acknowledged the general articles submitted by the Applicants regarding female genital mutilation as a harmful practice.
- Evidence: `evidence_fact` cue `found that` at chunk `4813088` offsets `302-312`; context: The RPD and the RAD both reasonably found that this allegation was not credible as there was no evidence that the uncle had such power or influence.

#### 17226:4:subtheme:6 · paragraphs 61-65

- Raw key terms: `applicant, applicants, principal, considering, credibility, evidence, findings, found`
- Display key terms: `principal, considering, credibility, findings`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: principal, considering, credibility, findings Rule/authority context: As noted in the jurisprudence, the threshold is very high and an applicant’s preferences or the impact of adjusting to a new place are not enough to reject an IFA. Application context: [58] With respect to the second prong of the test, which focuses on whether relocation to the proposed IFA would be reasonable in all the circumstances, including the personal circumstances of the Applicants, a high thre Evidence spans paragraphs 61-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4813089` offsets `68-75`; context: [58] With respect to the second prong of the test, which focuses on whether relocation to the proposed IFA would be reasonable in all the circumstances, including the personal circumstances of the Applicants, a high threshold applies.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813089` offsets `286-294`; context: The onus is on the Applicants to provide objective evidence to establish that the IFA is not reasonable for them.
- Evidence: `reasoning_application` cue `applies` at chunk `4813089` offsets `226-233`; context: [58] With respect to the second prong of the test, which focuses on whether relocation to the proposed IFA would be reasonable in all the circumstances, including the personal circumstances of the Applicants, a high threshold applies.
- Evidence: `evidence_fact` cue `evidence` at chunk `4813090` offsets `173-181`; context: However, the RAD noted that the objective evidence established that Port Harcourt was a large city, where the Applicants’ language was spoken and with large communities that practice the Applicants’ Christian faith.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4813090` offsets `539-552`; context: As noted in the jurisprudence, the threshold is very high and an applicant’s preferences or the impact of adjusting to a new place are not enough to reject an IFA.
- Evidence: `counterargument_limitation` cue `However` at chunk `4813090` offsets `131-138`; context: However, the RAD noted that the objective evidence established that Port Harcourt was a large city, where the Applicants’ language was spoken and with large communities that practice the Applicants’ Christian faith.
- Evidence: `evidence_fact` cue `testimony` at chunk `4813093` offsets `144-153`; context: [62] As noted, in the present case, there were no credibility findings made with respect to the Principal Applicant and she did not provide any testimony.

#### 17226:4:subtheme:7 · paragraphs 66-67

- Raw key terms: `general, imm-3778-18, judgment, kane, account, address, adebayo, appearances`
- Display key terms: `imm-3778-18, kane, account, address, adebayo`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: imm-3778-18, kane, account, address, adebayo Operative outcome context: JUDGMENT in IMM-3778-18 THIS COURT’S JUDGMENT is that The Application is dismissed. Evidence spans paragraphs 66-67. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4813094` offsets `448-456`; context: There is no question for certification.
- Evidence: `disposition` cue `dismissed` at chunk `4813094` offsets `425-434`; context: JUDGMENT in IMM-3778-18
THIS COURT’S JUDGMENT is that
The Application is dismissed.

#### Section text

[39] Contrary to the Applicants’ submission, the testimony of the Male Applicant was not detailed. His explanation that he had left his town as a child is not sufficient to excuse him from knowledge of the very rituals he claims he and his family will be subjected to and which form the basis of their claim for protection. As the RAD noted, he claims that he has known for over 20 years that he would become the Elegosi because he is the first male grandchild. He also claimed that his uncle had been threatening him causing the family to move. It is not credible that the family would move to avoid the uncle if they did not have a better idea of the role of the Elegosi or the rituals.

[40] The Male Applicant could not explain the power held by the Elegosi, whether the role was only spiritual or whether there was any influence over the local or other government, or the size of the town over which the Elegosi would reign.

[41] Similarly, his testimony regarding his uncle’s ability to find the Applicants was very vague. He indicated only that his uncle was wealthy, travelled for his cocoa business and could use “thugs” to threaten the Applicants. He also stated that his uncle was “fetish” (explained to mean devilish), which does not address the uncle’s capacity to find them. The RPD and RAD reasonably found that there was no credible evidence that the uncle had the ability or power to track them down. The Male Applicant could not explain how his uncle knew that the Applicants were in the United States or had previously moved within Nigeria. All he could offer is that his uncle travels due to his cocoa business.
V. Did the RAD err in its IFA analysis?
A. The Applicants’ Submissions

[42] The Applicants submit that the RAD erred in finding that they had an IFA in Port Harcourt. The Applicants submit that they would face a serious risk of persecution in Port Harcourt and that they will not be able to live in that city for a range of personal reasons.

[43] First, the Applicants argue that the RAD erred in its analysis of the whether there was a serious risk of persecution in the proposed IFA by ignoring their evidence that the uncle could use his power and influence with the police to find them. The Applicants argue that the RAD ignored the evidence in the National Documentation Package regarding the prevalence of female genital mutilation, including in Port Harcourt. The Applicants also argue that the RAD erred in imposing a higher standard than a “serious possibility of persecution”.

[44] Second, the Applicants argue that the RAD failed to consider the Applicant’s circumstances. The Applicants argue that Port Harcourt is an unreasonable IFA because the cost of living is too high, they will be regarded as outsiders, their children will not be able to attend the best schools and, contrary to the RAD’s speculation, they will not be able to start their businesses.

[45] The Applicants point to the evidence about Port Harcourt in the national documentation package, which notes that the costs of living, housing and healthcare are high and that it is difficult to find employment.

[46] At the hearing of this Application, the Applicants also argued that the RAD ignored the Principal Applicant’s psychological report and the submission that an IFA in Port Harcourt would be detrimental to her mental health.
B. The Respondent’s Submissions

[47] The Respondent notes that the IFA is the determinative finding. The Respondent submits that the RAD applied the correct test to determine the IFA and that its findings are reasonable. The RAD conducted a full IFA analysis and in doing so, reviewed all the relevant evidence and concluded that there was no credible evidence of the key allegations that the Male Applicant’s uncle would persecute them and subject them to rituals, let alone evidence that he would find them in Port Harcourt.

[48] The Respondent submits that the Applicants failed to provide sufficient evidence to establish that it would be unreasonable for them to relocate to Port Harcourt. The Respondent notes that housing and living costs and employment issues are not enough to reject an IFA; the circumstances must be unduly harsh in the proposed IFA and there is no evidence that this is the case.
C. The IFA Finding is reasonable
(1) The jurisprudence

[49] The two part test for an IFA established in Rasaratnam has been consistently applied and elaborated upon, including in Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] 1 FC 589 at paras 2, 12, [1993] FCJ No 1172 (QL) (CA) [Thirunavukkarasu]. First, the decision-maker must be satisfied, on a balance of probabilities, that there is no serious possibility of the applicant being persecuted in the proposed IFA. Second, the conditions in the proposed IFA must be such that it would not be unreasonable for the applicant to seek refuge there, upon consideration of all the circumstances, including the personal circumstances of the applicant.

[50] As noted in Thirunavukkarasu at paragraph 14:
An IFA cannot be speculative or theoretical only; it must be a realistic, attainable option. Essentially, this means that the alternative place of safety must be realistically accessible to the claimant. Any barriers to getting there should be reasonably surmountable. The claimant cannot be required to encounter great physical danger or to undergo undue hardship in travelling there or in staying there. For example, claimants should not be required to cross battle lines where fighting is going on at great risk to their lives in order to reach a place of safety. Similarly, claimants should not be compelled to hide out in an isolated region of their country, like a cave in the mountains, or in a desert or a jungle, if those are the only areas of internal safety available. But neither is it enough for refugee claimants to say that they do not like the weather in a safe area, or that they have no friends or relatives there, or that they may not be able to find suitable work there. If it is objectively reasonable in these latter cases to live in these places, without fear of persecution, then IFA exists and the claimant is not a refugee.
[Emphasis added]

[51] The high onus on a refugee claimant to demonstrate that a proposed IFA is unreasonable was explained in Ranganathan v Canada (Minister of Citizenship and Immigration), [2001] 2 FC 164 at paras 15-17, 193 FTR 320 (CA) [Ranganathan]:

[15] We read the decision of Linden J.A. for this Court as setting up a very high threshold for the unreasonableness test. It requires nothing less than the existence of conditions which would jeopardize the life and safety of a claimant in travelling or temporarily relocating to a safe area. In addition, it requires actual and concrete evidence of such conditions. The absence of relatives in a safe place, whether taken alone or in conjunction with other factors, can only amount to such condition if it meets that threshold, that is to say if it establishes that, as a result, a claimant's life or safety would be jeopardized. This is in sharp contrast with undue hardship resulting from loss of employment, loss of status, reduction in quality of life, loss of aspirations, loss of beloved ones and frustration of one's wishes and expectations.

[16] There are at least two reasons why it is important not to lower that threshold. First, as this Court said in Thirunavukkarasu, the definition of refugee under the Convention “requires claimants to be unable or unwilling by reason of fear of persecution to claim the protection of their home country in any part of that country”. Put another way, what makes a person a refugee under the Convention is his fear of persecution by his home country in any part of that country. To expand and lower the standard for assessing reasonableness of the IFA is to fundamentally denature the definition of refugee: one becomes a refugee who has no fear of persecution and who would be better off in Canada physically, economically and emotionally than in a safe place in his own country.
[Emphasis added]

[52] In Valasquez v Canada (Citizenship and Immigration), 2010 FC 1201, [2010] FCJ No 1496 (QL), relied on by the Applicants, Justice O’Reilly summarized the approach and principles from the jurisprudence at paragraph 15:
The concept of an IFA is an inherent part of the Convention refugee definition because a claimant must be a refugee from a country, not from a particular region of a country (Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706 at para 6). Once an IFA has been proposed by the Board, it must consider the viability of the IFA according to the disjunctive two part test set out in Rasaratnam. The claimant bears the onus and must demonstrate that the IFA does not exist or is unreasonable in the circumstances. That is, the claimant must persuade the Board on a balance of probabilities either that there is a serious possibility that he or she will be persecuted in the location proposed by the Board as an IFA, or that it would be unreasonable to seek [refuge] in the proposed IFA given his or her particular circumstances.
[Emphasis added]

[53] As highlighted in the jurisprudence, a refugee claimant is a refugee from their country as a whole, not from a village or region of their country. Therefore, a refugee claimant cannot seek the refugee protection of another country while there is a place within their own country—even if it may not be where they wish to live—which offers safety from the risk they claim and is not unreasonable in all the circumstances. In all cases, a refugee claimant bears the onus of establishing with objective evidence that the proposed IFA is unreasonable. This means establishing that there is a serious possibility of being persecuted in the proposed IFA or that the conditions in the proposed IFA make it unreasonable to relocate there, taking into consideration all the circumstances, including their personal circumstances. The high threshold set in Ranganathan at para 15 (“nothing less than the existence of conditions which would jeopardize the life and safety of a claimant in travelling or temporarily relocating to a safe area”) applies to both parts of the test.
(2) The IFA finding is reasonable

[54] The RAD applied the correct test and did not err in finding that the Applicants had not met the onus on them to establish on a balance of probabilities that the IFA in Port Harcourt is not reasonable.

[55] With respect to the first part of the test, the RAD’s analysis of whether the Applicants were at a serious risk of persecution focused on whether it was likely that the Male Applicant’s uncle—who was the alleged agent of persecution—would find them. The RAD noted that the Applicants provided no evidence of how the uncle knew they had gone to the United States or had moved within Nigeria. The RAD reasonably found that the Male Applicant’s evidence about the uncle’s ability and power was vague and did not support the allegation.

[56] The RAD acknowledged the general articles submitted by the Applicants regarding female genital mutilation as a harmful practice. The RAD relied on the National Documentation Package which indicates that parents can refuse to have their daughters undergo the practice. The RAD also noted that the Violence Against Persons (Prohibition) Act, passed in 2015, bans the practice. The RAD acknowledged that while the practice continues in some parts of Nigeria, state protection is available, as is protection by some religious organizations.

[57] With respect to the alleged risk that the Principal Applicant and her daughters would be subjected to female genital mutilation and their son subjected to other rituals, it must be remembered that the alleged agent of persecution is the uncle—not state actors. The RPD and the RAD both reasonably found that this allegation was not credible as there was no evidence that the uncle had such power or influence.

[58] With respect to the second prong of the test, which focuses on whether relocation to the proposed IFA would be reasonable in all the circumstances, including the personal circumstances of the Applicants, a high threshold applies. The onus is on the Applicants to provide objective evidence to establish that the IFA is not reasonable for them. The RAD reasonably found that the Applicants had not met the threshold.

[59] The Applicants’ submissions focused on the high cost of living and housing, job and business prospects and language barriers. However, the RAD noted that the objective evidence established that Port Harcourt was a large city, where the Applicants’ language was spoken and with large communities that practice the Applicants’ Christian faith. The RAD acknowledged that there would be some economic hardship but reasonably concluded that these hardships did not rise to the level of jeopardizing their health or safety. As noted in the jurisprudence, the threshold is very high and an applicant’s preferences or the impact of adjusting to a new place are not enough to reject an IFA.

[60] The RAD did not err in not considering the psychological report of the Principal Applicant to assess the reasonableness of the IFA.

[61] The Applicants’ reliance on Atay at para 32 to support their argument that the RAD erred in not considering the psychological report for the Principal Applicant is misplaced. In Atay, Justice O’Keefe found at para 32:
As the contents of the psychological report were relevant to the Board’s credibility findings, the Board should have taken the time to consider how the applicant’s medical condition affected his behaviour before making its credibility finding. As the Board did not do this, I have no way of knowing what the Board’s credibility finding would have been had the report been considered first. I am of the view that the Board made a reviewable error.

[62] As noted, in the present case, there were no credibility findings made with respect to the Principal Applicant and she did not provide any testimony. As a result, the recommendation that the Principal Applicant be given breaks in the provision of her testimony due to her PTSD was not ignored; it was simply not applicable.

[63] Moreover, the psychological report of Dr. Devins, prepared based on one interview and only on the Principal Applicant’s account, referred to “traumatic events” without any particularity. It did not address the impact of a proposed IFA, but made the general statement that her “condition will deteriorate with exposure to further threats of harm”.
JUDGMENT in IMM-3778-18
THIS COURT’S JUDGMENT is that
The Application is dismissed.
There is no question for certification.
"Catherine M. Kane"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-3778-18
STYLE OF CAUSE:
OLUBUNMI SUSAN ADEBAYO, GBADEBO DAVE ADEBAYO, TIMILEYIN REBECCA ADEBAYO, OLUWABUKUNFUNMI PAUL ADEBAYO, DAMILOLA COMFORT ADEBAYO v THE MINISTER OF IMMIGRATION, REFUGEES AND CITIZENSHIP CANADA
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
March 6, 2019
JUDGMENT and reasons:
KANE J.
DATED:
march 19, 2019
APPEARANCES:
Dotun Davies
For The Applicants
Neeta Logsetty
For The Respondent
SOLICITORS OF RECORD:
Topmarké Attorneys LLP
Barristers and Solicitors
Toronto, Ontario
For The Applicants
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
