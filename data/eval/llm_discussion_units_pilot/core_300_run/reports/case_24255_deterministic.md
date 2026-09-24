# Discussion Units: case 24255

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **88**
- Continuity pairs: **87**
- Discussion Units: **7**
- Paragraph source hashes: **88**
- Sub-themes: **20**

## 24255:1 · paragraphs 0-19

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ef7833ddf3fb60f6418fd293d14020d9a90f0dcbd1296b0898daaadbff0dbfd1`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24255:1:subtheme:1 · paragraphs 0-9

- Raw key terms: `applicant, homosexual, oman, police, august, board, brother, decision`
- Display key terms: `homosexual, oman, police, august, brother`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: homosexual, oman, police, august, brother Position/evidence statements: He claims that in 1981 he married his cousin and that he has eight children of that marriage. | The Applicant submits that homosexual conduct is not accepted and is illegal in Oman. Rule/authority context: [1] This is the judicial review of the decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated August 24th, 2012, in which it concluded that the Applicant was not a Convention r | Decision under Review Application context: He claims that he fears that, if he is returned Oman, he will be found and killed by his family members or that he will be found by the police who are seeking his capture as a result of charges against him because he is  Operative outcome context: [8] In a decision dated August 24, 2012, the Board denied the Applicant’s claim for refugee protection (Decision). Evidence spans paragraphs 0-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5139982` offsets `262-273`; context: [1] This is the judicial review of the decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated August 24th, 2012, in which it concluded that the Applicant was not a Convention refugee nor a person in need of protection pursuant to sections 96 or 97, respectively, of the Immigration and Refugee Protection Act, SC 2001, c 27 (the IRPA).
- Evidence: `party_position` cue `claims` at chunk `5139983` offsets `43-49`; context: He claims that in 1981 he married his cousin and that he has eight children of that marriage.
- Evidence: `party_position` cue `submits` at chunk `5139984` offsets `223-230`; context: The Applicant submits that homosexual conduct is not accepted and is illegal in Oman.
- Evidence: `party_position` cue `claims` at chunk `5139988` offsets `86-92`; context: He claims that he fears that, if he is returned Oman, he will be found and killed by his family members or that he will be found by the police who are seeking his capture as a result of charges against him because he is a homosexual.
- Evidence: `reasoning_application` cue `because` at chunk `5139988` offsets `289-296`; context: He claims that he fears that, if he is returned Oman, he will be found and killed by his family members or that he will be found by the police who are seeking his capture as a result of charges against him because he is a homosexual.
- Evidence: `governing_rule` cue `under` at chunk `5139989` offsets `170-175`; context: Decision under Review
- Evidence: `disposition` cue `denied` at chunk `5139989` offsets `51-57`; context: [8] In a decision dated August 24, 2012, the Board denied the Applicant’s claim for refugee protection (Decision).
- Evidence: `evidence_fact` cue `found that` at chunk `5139990` offsets `14-24`; context: [9] The Board found that the Applicant was not a Convention refugee nor was he a person in need of protection pursuant to sections 96 or 97(1)(a) and (b) of the IRPA.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5139990` offsets `110-121`; context: [9] The Board found that the Applicant was not a Convention refugee nor was he a person in need of protection pursuant to sections 96 or 97(1)(a) and (b) of the IRPA.

#### 24255:1:subtheme:2 · paragraphs 10-14

- Raw key terms: `applicant, board, claim, basis, evidence, found, objective, oman`
- Display key terms: `basis, objective, oman`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: basis, objective, oman Position/evidence statements: [14] The Board applied its credibility findings to the Applicant’s subsection 97(1) claim that he faces a risk to his life or of being subjected to cruel and unusual treatment or punishment in Oman. Application context: [12] The Board stated that when the Applicant was asked to explain his failure to provide documentary evidence such as the warrant, hotel bills, divorce documents or at the least an affidavit from his brother, his respon | [14] The Board applied its credibility findings to the Applicant’s subsection 97(1) claim that he faces a risk to his life or of being subjected to cruel and unusual treatment or punishment in Oman. Evidence spans paragraphs 10-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5139991` offsets `23-28`; context: [10] The determinative issue was credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `5139991` offsets `90-98`; context: In particular, based on the totality of the evidence, the Board found that the Applicant was not a credible witness and that there was no objective basis to his fears if returned to “Albania”.
- Evidence: `evidence_fact` cue `evidence` at chunk `5139992` offsets `43-51`; context: [11] The Board interpreted the documentary evidence from independent and reliable sources as indicating that there were no reports of prosecution for homosexual conduct in Oman during the year 2010.
- Evidence: `evidence_fact` cue `evidence` at chunk `5139993` offsets `102-110`; context: [12] The Board stated that when the Applicant was asked to explain his failure to provide documentary evidence such as the warrant, hotel bills, divorce documents or at the least an affidavit from his brother, his response was that he had made no effort to seek out those documents because he did not wish anyone to know where he was.
- Evidence: `reasoning_application` cue `because` at chunk `5139993` offsets `282-289`; context: [12] The Board stated that when the Applicant was asked to explain his failure to provide documentary evidence such as the warrant, hotel bills, divorce documents or at the least an affidavit from his brother, his response was that he had made no effort to seek out those documents because he did not wish anyone to know where he was.
- Evidence: `evidence_fact` cue `found that` at chunk `5139994` offsets `98-108`; context: [13] The Board was not persuaded that the Applicant was involved in a homosexual relationship and found that there was no objective basis for his claim.
- Evidence: `party_position` cue `claim` at chunk `5139995` offsets `84-89`; context: [14] The Board applied its credibility findings to the Applicant’s subsection 97(1) claim that he faces a risk to his life or of being subjected to cruel and unusual treatment or punishment in Oman.
- Evidence: `evidence_fact` cue `found that` at chunk `5139995` offsets `202-212`; context: It found that because he was not a credible witness and as his fear had no objective basis, he would not face a risk to his life, be subjected to cruel and unusual punishment or to a danger of being tortured if returned to Oman.
- Evidence: `reasoning_application` cue `applied` at chunk `5139995` offsets `15-22`; context: [14] The Board applied its credibility findings to the Applicant’s subsection 97(1) claim that he faces a risk to his life or of being subjected to cruel and unusual treatment or punishment in Oman.

#### 24255:1:subtheme:3 · paragraphs 15-16

- Raw key terms: `applicant, board, issues, analysis, citizens, claim, consider, credibility`
- Display key terms: `issues, analysis, citizens, consider, credibility`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: issues, analysis, citizens, consider, credibility Position/evidence statements: Did the Board consider the Applicant’s subsection 97(1) claim? Rule/authority context: Standard of Review Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5139996` offsets `211-217`; context: Issues
- Evidence: `evidence_fact` cue `found that` at chunk `5139996` offsets `15-25`; context: [15] The Board found that there was no persuasive documentary evidence to indicate that the Applicant would be subjected to any other risk, other than the risk of general violence faced by all citizens of Oman.
- Evidence: `issue` cue `issues` at chunk `5139997` offsets `21-27`; context: [16] In my view, the issues can be framed as follows:
1.
- Evidence: `party_position` cue `claim` at chunk `5139997` offsets `163-168`; context: Did the Board consider the Applicant’s subsection 97(1) claim?
- Evidence: `governing_rule` cue `Standard of Review` at chunk `5139997` offsets `170-188`; context: Standard of Review

#### 24255:1:subtheme:4 · paragraphs 17-18

- Raw key terms: `canada, citizenship, immigration, jurisprudence, minister, para, standard, adopt`
- Display key terms: `jurisprudence, para, standard, adopt`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: jurisprudence, para, standard, adopt Rule/authority context: [17] A standard of review analysis need not be conducted in every instance. | [18] It is established jurisprudence that credibility findings are essentially pure findings of fact that are reviewable on a reasonableness standard (Zhou v Canada (Citizenship and Immigration), 2013 FC 619 at para 26;  Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5139998` offsets `141-149`; context: Instead, where the standard of review applicable to a particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 at para 57 [Dunsmuir]; Kisana v Canada (Minister of Citizenship and Immigration), 2009 FCA 189 at para 18 [Kisana]).
- Evidence: `governing_rule` cue `standard of review` at chunk `5139998` offsets `7-25`; context: [17] A standard of review analysis need not be conducted in every instance.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5139999` offsets `23-36`; context: [18] It is established jurisprudence that credibility findings are essentially pure findings of fact that are reviewable on a reasonableness standard (Zhou v Canada (Citizenship and Immigration), 2013 FC 619 at para 26; Rodriguez Ramirez v Canada (Citizenship and Immigration), 2013 FC 261 at para 32; Wu v Canada (Minister of Citizenship and Immigration), 2009 FC 929 at para 18; Aguebor v Canada (Minister of Employment and Immigration), [1993] FCJ No 732 (QL) (CA)).

#### 24255:1:subtheme:5 · paragraphs 19-19

- Raw key terms: `aguilar, aleman, canada, citizenship, claimant, faces, generalized, immigration`
- Display key terms: `aguilar, aleman, faces, generalized`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: aguilar, aleman, faces, generalized Rule/authority context: [19] As for the question of whether a claimant faces a generalized risk to violence pursuant to section 97, the standard of review is reasonableness (De Jesus Aleman Aguilar v Canada (Citizenship and Immigration), 2013 F Evidence spans paragraphs 19-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5140000` offsets `16-24`; context: [19] As for the question of whether a claimant faces a generalized risk to violence pursuant to section 97, the standard of review is reasonableness (De Jesus Aleman Aguilar v Canada (Citizenship and Immigration), 2013 FC 809 at para 20; Portillo v Canada (Minister of Citizenship and Immigration), 2012 FC 678 at para 18 [Portillo]).
- Evidence: `governing_rule` cue `pursuant to` at chunk `5140000` offsets `84-95`; context: [19] As for the question of whether a claimant faces a generalized risk to violence pursuant to section 97, the standard of review is reasonableness (De Jesus Aleman Aguilar v Canada (Citizenship and Immigration), 2013 FC 809 at para 20; Portillo v Canada (Minister of Citizenship and Immigration), 2012 FC 678 at para 18 [Portillo]).

#### Section text

Ismaili v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-01-24
Neutral citation
2014 FC 84
File numbers
IMM-10401-12
Decision Content
Date: 20140124
Docket:
IMM-10401-12
Citation: 2014 FC 84
Ottawa, Ontario, January 24, 2014
PRESENT: The Honourable Madam Justice Strickland
BETWEEN:
ALI SALEH ZAHRAN AL ISMAILI
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is the judicial review of the decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated August 24th, 2012, in which it concluded that the Applicant was not a Convention refugee nor a person in need of protection pursuant to sections 96 or 97, respectively, of the Immigration and Refugee Protection Act, SC 2001, c 27 (the IRPA). This application is brought pursuant to section 72 of the IRPA.
Background

[2] The Applicant is a citizen of Oman. He claims that in 1981 he married his cousin and that he has eight children of that marriage. In 2005 he began a secret homosexual relationship.

[3] He and his homosexual partner often visited the Dream Resort Hotel in Oman. In July 2010, while they were in their room at the hotel, two police officers entered their room, arrested and then jailed them. The Applicant submits that homosexual conduct is not accepted and is illegal in Oman.

[4] The Applicant states that he contacted his brother who was able to have him released from jail by bribing police officers. With his brother’s assistance, he went into hiding in the village of Fanja.

[5] While he was in Fanja, his brother informed him that his wife was angry and ashamed of him. He agreed to her request for a divorce. His brother and his uncle also told him that the Al Ismaili family, to which he and his wife belonged, were angry and determined to kill him for dishonouring them. The Applicant describes the Al Ismaili family as a very old and wealthy family in Oman.

[6] After his release from jail, the charges against him for homosexual behaviour remained outstanding. While he was in Fanja, his brother also informed him that officers at the Seeb police station had told him that a warrant for his arrest had been issued.

[7] The Applicant left Oman on August 29, 2010, arriving in Canada two days later. He claims that he fears that, if he is returned Oman, he will be found and killed by his family members or that he will be found by the police who are seeking his capture as a result of charges against him because he is a homosexual.

[8] In a decision dated August 24, 2012, the Board denied the Applicant’s claim for refugee protection (Decision). This is the judicial review of that Decision.
Decision under Review

[9] The Board found that the Applicant was not a Convention refugee nor was he a person in need of protection pursuant to sections 96 or 97(1)(a) and (b) of the IRPA.

[10] The determinative issue was credibility. In particular, based on the totality of the evidence, the Board found that the Applicant was not a credible witness and that there was no objective basis to his fears if returned to “Albania”. It later refers to “Oman”.

[11] The Board interpreted the documentary evidence from independent and reliable sources as indicating that there were no reports of prosecution for homosexual conduct in Oman during the year 2010. When this was put to him, the Applicant had no comment except to say that there was a warrant issued for his arrest, that his brother had seen the warrant and that the police sought to capture him for being involved in a homosexual relationship. The Board gave more weight to the documentary evidence, particularly as the Applicant did not provide any documentary evidence to corroborate his claim that he was caught engaging in a homosexual relationship resulting in a divorce from his wife.

[12] The Board stated that when the Applicant was asked to explain his failure to provide documentary evidence such as the warrant, hotel bills, divorce documents or at the least an affidavit from his brother, his response was that he had made no effort to seek out those documents because he did not wish anyone to know where he was. The Board did not find this explanation to be reasonable given that the Personal Information Form (PIF) and RPD Screening Form instructed him to provide such evidence to establish his claim.

[13] The Board was not persuaded that the Applicant was involved in a homosexual relationship and found that there was no objective basis for his claim. It found that the Applicant fabricated his story to bolster his refugee claim.

[14] The Board applied its credibility findings to the Applicant’s subsection 97(1) claim that he faces a risk to his life or of being subjected to cruel and unusual treatment or punishment in Oman. It found that because he was not a credible witness and as his fear had no objective basis, he would not face a risk to his life, be subjected to cruel and unusual punishment or to a danger of being tortured if returned to Oman.

[15] The Board found that there was no persuasive documentary evidence to indicate that the Applicant would be subjected to any other risk, other than the risk of general violence faced by all citizens of Oman.
Issues

[16] In my view, the issues can be framed as follows:
1. Did the Board err in its credibility analysis?
2. Did the Board consider the Applicant’s subsection 97(1) claim?
Standard of Review

[17] A standard of review analysis need not be conducted in every instance. Instead, where the standard of review applicable to a particular question before the court is well-settled by past jurisprudence, the reviewing court may adopt that standard (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 at para 57 [Dunsmuir]; Kisana v Canada (Minister of Citizenship and Immigration), 2009 FCA 189 at para 18 [Kisana]).

[18] It is established jurisprudence that credibility findings are essentially pure findings of fact that are reviewable on a reasonableness standard (Zhou v Canada (Citizenship and Immigration), 2013 FC 619 at para 26; Rodriguez Ramirez v Canada (Citizenship and Immigration), 2013 FC 261 at para 32; Wu v Canada (Minister of Citizenship and Immigration), 2009 FC 929 at para 18; Aguebor v Canada (Minister of Employment and Immigration), [1993] FCJ No 732 (QL) (CA)).

[19] As for the question of whether a claimant faces a generalized risk to violence pursuant to section 97, the standard of review is reasonableness (De Jesus Aleman Aguilar v Canada (Citizenship and Immigration), 2013 FC 809 at para 20; Portillo v Canada (Minister of Citizenship and Immigration), 2012 FC 678 at para 18 [Portillo]).

## 24255:2 · paragraphs 20-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4fd399245efaeef4930e82613d7bc6bbf86074399650f3c210a8b8f608a312c4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24255:2:subtheme:1 · paragraphs 20-22

- Raw key terms: `applicant, board, credibility, submits, above, acceptable, accordingly, adequate`
- Display key terms: `credibility, submits, above, acceptable, accordingly, adequate`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: credibility, submits, above, acceptable, accordingly, adequate Position/evidence statements: [21] The Applicant submits that the Board is required to make clear findings of credibility and to provide adequate reasons (Armson v Canada (Minister of Employment and Immigration) (1989), 9 Imm LR (2d) 150, [1989] FCJ  | [22] The Applicant submits that the Board’s reference to Albania undercuts its statement that it has considered all the evidence. Rule/authority context: [20] Accordingly, the reasonableness standard of review applies in this matter. Application context: [20] Accordingly, the reasonableness standard of review applies in this matter. Evidence spans paragraphs 20-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5140001` offsets `211-218`; context: Reasonableness is concerned with the justification, transparency and intelligibility of the decision-making process, but also with whether the decision falls within a range of possible, acceptable outcomes defensible in respect of the facts and law (Dunsmuir, above, at para 47).
- Evidence: `governing_rule` cue `standard of review` at chunk `5140001` offsets `37-55`; context: [20] Accordingly, the reasonableness standard of review applies in this matter.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5140001` offsets `5-16`; context: [20] Accordingly, the reasonableness standard of review applies in this matter.
- Evidence: `counterargument_limitation` cue `but` at chunk `5140001` offsets `197-200`; context: Reasonableness is concerned with the justification, transparency and intelligibility of the decision-making process, but also with whether the decision falls within a range of possible, acceptable outcomes defensible in respect of the facts and law (Dunsmuir, above, at para 47).
- Evidence: `party_position` cue `submits` at chunk `5140002` offsets `19-26`; context: [21] The Applicant submits that the Board is required to make clear findings of credibility and to provide adequate reasons (Armson v Canada (Minister of Employment and Immigration) (1989), 9 Imm LR (2d) 150, [1989] FCJ No 800 (QL) (CA)).
- Evidence: `party_position` cue `submits` at chunk `5140003` offsets `19-26`; context: [22] The Applicant submits that the Board’s reference to Albania undercuts its statement that it has considered all the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140003` offsets `120-128`; context: [22] The Applicant submits that the Board’s reference to Albania undercuts its statement that it has considered all the evidence.

#### 24255:2:subtheme:2 · paragraphs 23-27

- Raw key terms: `board, applicant, canada, documentary, documents, evidence, immigration, minister`
- Display key terms: `documentary, documents`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: documentary, documents Position/evidence statements: [24] The Applicant submits that the Board misapprehended the documentary evidence and then relied on this to contradict his claim that he is subject to prosecution in Oman. | [25] The Respondent submits that the Board’s reference to “Albania” in its opening paragraph was a clerical error. Rule/authority context: Jurisprudence indicates that clerical errors do not merit judicial review (Gabriel v Canada (Minister of Citizenship and Immigration), 2008 FC 232 at para 3; Chavez v Canada (Minister of Citizenship and Immigration), 200 Application context: The Applicant’s inability to obtain corroborative documents is understandable in all the circumstances and the Board erred in failing to apply the presumption of truthfulness given the absence of any other reason to doub Evidence spans paragraphs 23-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5140004` offsets `225-233`; context: [23] Further, that the Board’s negative credibility finding was based solely on its findings concerning a lack of documentary evidence and the document cited by the Board which supposedly called the Applicant’s evidence into question.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140004` offsets `126-134`; context: [23] Further, that the Board’s negative credibility finding was based solely on its findings concerning a lack of documentary evidence and the document cited by the Board which supposedly called the Applicant’s evidence into question.
- Evidence: `reasoning_application` cue `apply` at chunk `5140004` offsets `372-377`; context: The Applicant’s inability to obtain corroborative documents is understandable in all the circumstances and the Board erred in failing to apply the presumption of truthfulness given the absence of any other reason to doubt the veracity of his testimony (Maldonado v Canada (Minister of Employment and Immigration), [1980] 2 FC 302 (CA) [Maldonado]).
- Evidence: `issue` cue `issue` at chunk `5140005` offsets `627-632`; context: The Board also failed to consider counsel’s submissions on the issue of the cogency of the report as positive evidence of the veracity of the Applicant’s allegations.
- Evidence: `party_position` cue `submits` at chunk `5140005` offsets `19-26`; context: [24] The Applicant submits that the Board misapprehended the documentary evidence and then relied on this to contradict his claim that he is subject to prosecution in Oman.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140005` offsets `73-81`; context: [24] The Applicant submits that the Board misapprehended the documentary evidence and then relied on this to contradict his claim that he is subject to prosecution in Oman.
- Evidence: `party_position` cue `submits` at chunk `5140006` offsets `20-27`; context: [25] The Respondent submits that the Board’s reference to “Albania” in its opening paragraph was a clerical error.
- Evidence: `governing_rule` cue `Jurisprudence` at chunk `5140006` offsets `115-128`; context: Jurisprudence indicates that clerical errors do not merit judicial review (Gabriel v Canada (Minister of Citizenship and Immigration), 2008 FC 232 at para 3; Chavez v Canada (Minister of Citizenship and Immigration), 2007 FC 10 at para 5; Adams v Canada (Minister of Citizenship and Immigration), 2008 FC 256 at paras 17-18; Messaoud v Canada (Minister of Citizenship and Immigration), 2007 FC 18 at para 1).
- Evidence: `party_position` cue `submits` at chunk `5140007` offsets `20-27`; context: [26] The Respondent submits that while the Applicant states that his failure to produce corroborative evidence is understandable, he has not explained why he was unable to obtain such evidence such as hotel bills or his divorce documents.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140007` offsets `102-110`; context: [26] The Respondent submits that while the Applicant states that his failure to produce corroborative evidence is understandable, he has not explained why he was unable to obtain such evidence such as hotel bills or his divorce documents.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5140007` offsets `337-343`; context: While it may be understandable that he could not obtain a copy of the warrant of arrest, the same cannot be said of an affidavit from his brother.

#### Section text

[20] Accordingly, the reasonableness standard of review applies in this matter. Reasonableness is concerned with the justification, transparency and intelligibility of the decision-making process, but also with whether the decision falls within a range of possible, acceptable outcomes defensible in respect of the facts and law (Dunsmuir, above, at para 47).
Analysis
Did the Board err in its credibility analysis?
Applicant’s Submissions

[21] The Applicant submits that the Board is required to make clear findings of credibility and to provide adequate reasons (Armson v Canada (Minister of Employment and Immigration) (1989), 9 Imm LR (2d) 150, [1989] FCJ No 800 (QL) (CA)). Plausibility findings should be made only in the clearest of cases (Valtchev v Canada (Minister of Citizenship and Immigration), 2001 FCT 776; Kalonda v Canada (Minister of Citizenship and Immigration), 2001 FCT 39).

[22] The Applicant submits that the Board’s reference to Albania undercuts its statement that it has considered all the evidence. This is more than a mere typographical or clerical error.

[23] Further, that the Board’s negative credibility finding was based solely on its findings concerning a lack of documentary evidence and the document cited by the Board which supposedly called the Applicant’s evidence into question. The Applicant’s inability to obtain corroborative documents is understandable in all the circumstances and the Board erred in failing to apply the presumption of truthfulness given the absence of any other reason to doubt the veracity of his testimony (Maldonado v Canada (Minister of Employment and Immigration), [1980] 2 FC 302 (CA) [Maldonado]).

[24] The Applicant submits that the Board misapprehended the documentary evidence and then relied on this to contradict his claim that he is subject to prosecution in Oman. The US Department of State Report on Human Rights Practices for 2011 (US DOS Report) was interpreted by the Board as indicating that there were no reports of prosecution for homosexual conduct in Oman in 2010 when in fact the report deals with 2011, and also states that the most recent year for which statistics are available is 2009, in which year there were nine prosecutions for sodomy. The Board also failed to consider counsel’s submissions on the issue of the cogency of the report as positive evidence of the veracity of the Applicant’s allegations.
Respondent’s Submissions

[25] The Respondent submits that the Board’s reference to “Albania” in its opening paragraph was a clerical error. Jurisprudence indicates that clerical errors do not merit judicial review (Gabriel v Canada (Minister of Citizenship and Immigration), 2008 FC 232 at para 3; Chavez v Canada (Minister of Citizenship and Immigration), 2007 FC 10 at para 5; Adams v Canada (Minister of Citizenship and Immigration), 2008 FC 256 at paras 17-18; Messaoud v Canada (Minister of Citizenship and Immigration), 2007 FC 18 at para 1).

[26] The Respondent submits that while the Applicant states that his failure to produce corroborative evidence is understandable, he has not explained why he was unable to obtain such evidence such as hotel bills or his divorce documents. While it may be understandable that he could not obtain a copy of the warrant of arrest, the same cannot be said of an affidavit from his brother.

[27] Subsection 100(4) of the IRPA provides in part that “the claimant must produce all documents and information as required by the rules of the Board”. Rule 7 (currently Rule 11) of the Refugee Protection Division Rules, SOR/2012-256 (Rules) requires a claimant to provide acceptable documents establishing the elements of his claim. If such documents are not provided, then the claimant must explain why they were unable to obtain such documents and the efforts made to obtain them. Where a claimant’s story is found to be implausible or otherwise lacking in credibility, a lack of documentary corroboration can be a valid consideration for the purposes of assessing credibility. A lack of acceptable documents without a reasonable explanation, or failure to take reasonable steps to obtain them, is a significant factor in assessing credibility (Byaje v Canada (Minister of Citizenship and Immigration), 2010 FC 90 at paras 26‑27 [Byaje]; Ortiz Juarez v Canada (Minister of Citizenship and Immigration), 2006 FC 288 at paras 7-9 [Ortiz Juarez]).

## 24255:3 · paragraphs 28-55

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a8dd584a98588dfefc7e792ceb3792a1575450f9458053b8862cc3ed2b1affb4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24255:3:subtheme:1 · paragraphs 28-44

- Raw key terms: `evidence, applicant, board, canada, citizenship, credibility, immigration, para`
- Display key terms: `credibility, para`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: credibility, para Position/evidence statements: [30] The Respondent submits that it was not unreasonable for the Board to doubt the credibility of the Applicant’s claim that he was being persecuted for homosexual conduct. | [32] However, the onus is always upon the claimant to prove its claim. Rule/authority context: [35] Jurisprudence concerning Rule 7 makes it clear that the Board can take into account an applicant’s lack of efforts to obtain corroborative evidence where it should be available and that the presumption of truth is a Application context: Similarly, in Ortiz Juarez, the Board drew adverse conclusions as to credibility because the applicants’ oral evidence raised significant new information not included in their PIF’s, they had failed to provide satisfacto Evidence spans paragraphs 28-44. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140009` offsets `53-61`; context: [28] The Applicant did not provide any corroborative evidence and the Board did not err in drawing a negative inference from his unwillingness to do so.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140010` offsets `668-676`; context: This information was put to the Applicant who did not produce his own evidence of recent prosecutions.
- Evidence: `party_position` cue `submits` at chunk `5140011` offsets `20-27`; context: [30] The Respondent submits that it was not unreasonable for the Board to doubt the credibility of the Applicant’s claim that he was being persecuted for homosexual conduct.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140011` offsets `435-443`; context: The Board is entitled to weigh the evidence and the Court can only interfere where there was clearly no credible evidence upon which the Board could have come to its conclusion (Khosa v Canada (Minister of Citizenship and Immigration), 2009 SCC 12, [2009] 1 SCR 339 at paras 59-62 [Khosa]; Yang v Canada (Minister of Citizenship and Immigration), 2006 FC 1013 at para 5; Hernandez Perez v Canada (Minister of Citizenship and Immigration), 2009 FC 1065 at paras 12-14).
- Evidence: `party_position` cue `claim` at chunk `5140013` offsets `64-69`; context: [32] However, the onus is always upon the claimant to prove its claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140014` offsets `159-167`; context: [33] And, in evaluating the merit of a refugee claim, “[…] the Board [is] entitled to take into account the applicant's lack of effort to obtain corroborative evidence to establish [elements of his claim] and to draw a negative inference of his credibility based on this” (Samseen, above, at para 30).
- Evidence: `evidence_fact` cue `evidence` at chunk `5140017` offsets `144-152`; context: [35] Jurisprudence concerning Rule 7 makes it clear that the Board can take into account an applicant’s lack of efforts to obtain corroborative evidence where it should be available and that the presumption of truth is always reviewable (Nagy v Canada (Citizenship and Immigration), 2013 FC 640 at para 66 [Nagy]; Samseen, above, at para 30).
- Evidence: `governing_rule` cue `Jurisprudence` at chunk `5140017` offsets `5-18`; context: [35] Jurisprudence concerning Rule 7 makes it clear that the Board can take into account an applicant’s lack of efforts to obtain corroborative evidence where it should be available and that the presumption of truth is always reviewable (Nagy v Canada (Citizenship and Immigration), 2013 FC 640 at para 66 [Nagy]; Samseen, above, at para 30).
- Evidence: `party_position` cue `submits` at chunk `5140018` offsets `20-27`; context: [36] The Respondent submits that where a claimant’s story is found to be implausible or lacking in credibility, a lack of documentary evidence can be a valid consideration for the purposes of assessing credibility (Byaje and Ortiz Juarez, both above).
- Evidence: `evidence_fact` cue `evidence` at chunk `5140018` offsets `134-142`; context: [36] The Respondent submits that where a claimant’s story is found to be implausible or lacking in credibility, a lack of documentary evidence can be a valid consideration for the purposes of assessing credibility (Byaje and Ortiz Juarez, both above).
- Evidence: `counterargument_limitation` cue `However` at chunk `5140018` offsets `283-290`; context: However, to be applicable, there must be a valid reason to doubt the Applicant’s credibility or the Board must have found the Applicant’s story to be implausible.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140019` offsets `459-467`; context: Similarly, in Ortiz Juarez, the Board drew adverse conclusions as to credibility because the applicants’ oral evidence raised significant new information not included in their PIF’s, they had failed to provide satisfactory explanations for those omissions, and, there was an absence of corroborating documentary evidence.
- Evidence: `reasoning_application` cue `because` at chunk `5140019` offsets `430-437`; context: Similarly, in Ortiz Juarez, the Board drew adverse conclusions as to credibility because the applicants’ oral evidence raised significant new information not included in their PIF’s, they had failed to provide satisfactory explanations for those omissions, and, there was an absence of corroborating documentary evidence.
- Evidence: `party_position` cue `claim` at chunk `5140021` offsets `177-182`; context: [10] It is well established that a panel cannot make negative inferences solely from the fact that a refugee claimant failed to produce any extrinsic documents to corroborate a claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140021` offsets `425-433`; context: But where there are valid reasons to doubt a claimant's credibility, a failure to provide corroborating documentation is a proper consideration for a panel if the Board does not accept the applicant's explanation for failing to produce that evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140023` offsets `155-163`; context: [22] …Where valid reasons to doubt a claimant’s credibility exist, the Board may draw negative credibility inferences from a failure to provide supporting evidence.
- Evidence: `counterargument_limitation` cue `However` at chunk `5140023` offsets `165-172`; context: However, in my opinion, these inferences may only be drawn where the applicant has also been unable to provide a reasonable explanation for his or her lack of corroborating material.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140025` offsets `147-155`; context: [6] There is no general requirement for corroboration and it would be an error to make a credibility finding based on the absence of corroborative evidence alone: Dundar v Canada (Citizenship and Immigration), 2007 FC 1026 at paras 19-22.

#### 24255:3:subtheme:2 · paragraphs 45-47

- Raw key terms: `credibility, board, central, findings, above, acceptable, adverse, always`
- Display key terms: `credibility, central, findings, above, acceptable, adverse, always`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: credibility, central, findings, above, acceptable, adverse, always Rule/authority context: [42] Some of the relevant principles concerning adverse credibility findings were set out in Mohacsi v Canada (Minister of Citizenship and Immigration), 2003 FCT 429: Evidence spans paragraphs 45-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5140026` offsets `34-42`; context: [7] If there is a valid reason to question the claimant’s credibility, the Board may draw a negative inference from a failure to provide corroborative evidence that would reasonably be expected.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140026` offsets `151-159`; context: [7] If there is a valid reason to question the claimant’s credibility, the Board may draw a negative inference from a failure to provide corroborative evidence that would reasonably be expected.
- Evidence: `governing_rule` cue `principles` at chunk `5140028` offsets `26-36`; context: [42] Some of the relevant principles concerning adverse credibility findings were set out in Mohacsi v Canada (Minister of Citizenship and Immigration), 2003 FCT 429:

#### 24255:3:subtheme:3 · paragraphs 48-49

- Raw key terms: `board, claimant, credibility, affecting, arbitrarily, based, bazelais, because`
- Display key terms: `credibility, affecting, arbitrarily, based, bazelais, because`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: credibility, affecting, arbitrarily, based, bazelais, because Rule/authority context: (Also see Lubana v Canada (Minister of Citizenship and Immigration) 2003 FCT 116; Hilo v Canada (Minister of Employment and Immigration) (1992), 15 Imm LR (2d) 199 (FCA), which held that where the Board finds that the cl Application context: [19] Second, the Board is entitled to conclude that a claimant is not credible because of implausibilities in his or her evidence as long as its inferences are not unreasonable and its reasons are set out in “clear and u Evidence spans paragraphs 48-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `however` at chunk `5140029` offsets `299-306`; context: No decision-maker, however can act arbitrarily or in a capricious manner.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140030` offsets `121-129`; context: [19] Second, the Board is entitled to conclude that a claimant is not credible because of implausibilities in his or her evidence as long as its inferences are not unreasonable and its reasons are set out in “clear and unmistakable terms”.
- Evidence: `governing_rule` cue `under` at chunk `5140030` offsets `807-812`; context: (Also see Lubana v Canada (Minister of Citizenship and Immigration) 2003 FCT 116; Hilo v Canada (Minister of Employment and Immigration) (1992), 15 Imm LR (2d) 199 (FCA), which held that where the Board finds that the claimant’s testimony is lacking in credibility, the Board is under a duty to state in clear, unambiguous terms the reason for casting doubt upon the claimant’s testimony; Younes v Canada (Citizenship and Immigration), 2013 FC 1122 at para 2; Bazelais v Canada (Citizenship and Immigration), 2013 FC 316 at para 40).
- Evidence: `reasoning_application` cue `conclude` at chunk `5140030` offsets `38-46`; context: [19] Second, the Board is entitled to conclude that a claimant is not credible because of implausibilities in his or her evidence as long as its inferences are not unreasonable and its reasons are set out in “clear and unmistakable terms”.

#### 24255:3:subtheme:4 · paragraphs 50-51

- Raw key terms: `case, corroborative, evidence, whether, against, appearing, applicant, board`
- Display key terms: `case, corroborative, whether, against, appearing`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: case, corroborative, whether, against, appearing Evidence spans paragraphs 50-51. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5140031` offsets `343-348`; context: Thus, there is an issue as to whether a valid reason for doubting the Applicant’s credibility existed which opened the door to a requirement to provide corroborative evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140031` offsets `190-198`; context: It does not cite any internal contradictions or inconsistencies in the Applicant’s evidence or state why his evidence is implausible.
- Evidence: `issue` cue `whether` at chunk `5140032` offsets `342-349`; context: [44] Against this is the principle that uncontradicted evidence may be rejected if it is inconsistent with the probabilities of the case as a whole (Cooper v Canada (Minister of Citizenship and Immigration), 2012 FC 118 at para 4) and, as stated in Lopera v Canada (Minister of Citizenship and Immigration), 2011 FC 653 at para 31 [Lopera]), whether corroborative evidence can reasonably be demanded depends upon the facts of each case.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140032` offsets `55-63`; context: [44] Against this is the principle that uncontradicted evidence may be rejected if it is inconsistent with the probabilities of the case as a whole (Cooper v Canada (Minister of Citizenship and Immigration), 2012 FC 118 at para 4) and, as stated in Lopera v Canada (Minister of Citizenship and Immigration), 2011 FC 653 at para 31 [Lopera]), whether corroborative evidence can reasonably be demanded depends upon the facts of each case.

#### 24255:3:subtheme:5 · paragraphs 52-53

- Raw key terms: `board, justice, above, absence, ahortor, applicant, canada, common`
- Display key terms: `justice, above, absence, ahortor, common`
- Argument roles: `evidence_fact, party_position`
- Explanation: Observed roles: evidence_fact, party_position Display terms: justice, above, absence, ahortor, common Position/evidence statements: The applicant, relying on Ahortor v Canada (Minister of Employment & Immigration), (1993), 65 FTR 137 (TD), submitted that the Board could not draw a negative inference from the mere fact that the applicant failed to pro Evidence spans paragraphs 52-53. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submitted` at chunk `5140033` offsets `278-287`; context: The applicant, relying on Ahortor v Canada (Minister of Employment & Immigration), (1993), 65 FTR 137 (TD), submitted that the Board could not draw a negative inference from the mere fact that the applicant failed to produce any extrinsic documents to corroborate his story.
- Evidence: `evidence_fact` cue `found that` at chunk `5140034` offsets `19-29`; context: [46] Justice Kelen found that it was reasonable for the Board to expect some corroborating evidence and that:

#### 24255:3:subtheme:6 · paragraphs 54-55

- Raw key terms: `applicant, board, found, provided, above, absence, ahortor, apparent`
- Display key terms: `provided, above, absence, ahortor, apparent`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: provided, above, absence, ahortor, apparent Evidence spans paragraphs 54-55. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `5140035` offsets `5-12`; context: [31] Whether corroborative evidence can reasonably be demanded depends upon the facts of each case.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140035` offsets `27-35`; context: [31] Whether corroborative evidence can reasonably be demanded depends upon the facts of each case.
- Evidence: `evidence_fact` cue `found that` at chunk `5140036` offsets `200-210`; context: The Board found that the applicant had provided many documents to establish his credentials as a doctor and his employment record but no documents to corroborate his claim to have treated and counselled homosexuals beyond such records that would be normal for any physician.
- Evidence: `counterargument_limitation` cue `but` at chunk `5140036` offsets `320-323`; context: The Board found that the applicant had provided many documents to establish his credentials as a doctor and his employment record but no documents to corroborate his claim to have treated and counselled homosexuals beyond such records that would be normal for any physician.

#### Section text

[28] The Applicant did not provide any corroborative evidence and the Board did not err in drawing a negative inference from his unwillingness to do so. A lack of an effort to obtain corroborative evidence may undermine a claim (Muthiyansa v Canada (Minister of Citizenship and Immigration), 2001 FCT 17 at paras 12-13 [Muthiyansa]). Corroborating evidence may be expected where it is reasonably available (Wokwera v Canada (Minister of Citizenship and Immigration), 2012 FC 132 at para 39 [Wokwera]). As the Applicant failed to explain why he could not obtain documents as to his divorce or hotel bills, which were reasonably available to him, or to explain why his brother would not provide an affidavit, it was not unreasonable for the Board to find that the lack of any form of corroborating documentation undermined the Applicant’s credibility.

[29] The Board referred to the 2011 US DOS Report for Oman which was released in 2012. This confirms that the most recent year for which official statistics are available was 2009 and that there were nine prosecutions for sodomy in that year; the report makes no statement about 2010; and, it states that there were no reports of prosecutions in 2011. While the Board may have erred in stating that the US DOS Report indicated that there were no reports of prosecution in 2010, the essence of the argument is the same as there were no reports of recent prosecutions for homosexual conduct in Oman. This information was put to the Applicant who did not produce his own evidence of recent prosecutions. The Applicant was determined to not be a credible witness and failed to provide corroborate evidence.

[30] The Respondent submits that it was not unreasonable for the Board to doubt the credibility of the Applicant’s claim that he was being persecuted for homosexual conduct. Credibility findings are the “heartland” of its expertise (Francis v Canada (Minister of Citizenship and Immigration), 2011 FC 1078 at para 7; Cato v Canada (Minister of Citizenship and Immigration), 2010 FC 1313 at para 27). The Board is entitled to weigh the evidence and the Court can only interfere where there was clearly no credible evidence upon which the Board could have come to its conclusion (Khosa v Canada (Minister of Citizenship and Immigration), 2009 SCC 12, [2009] 1 SCR 339 at paras 59-62 [Khosa]; Yang v Canada (Minister of Citizenship and Immigration), 2006 FC 1013 at para 5; Hernandez Perez v Canada (Minister of Citizenship and Immigration), 2009 FC 1065 at paras 12-14).
Analysis

[31] When an applicant swears to the truth of certain allegations, this creates a presumption that those allegations are true unless there is reason to doubt their truthfulness (Maldonado, above, at para 4).

[32] However, the onus is always upon the claimant to prove its claim. As Justice Pinard stated in Samseen v Canada (Minister of Citizenship and Immigration), 2006 FC 542 at para 14 [Samseen], “it is trite law that the applicant bears the onus of establishing the elements of his claim for protection” (Gill v Canada (Minister of Citizenship and Immigration), 2004 FC 1498).

[33] And, in evaluating the merit of a refugee claim, “[…] the Board [is] entitled to take into account the applicant's lack of effort to obtain corroborative evidence to establish [elements of his claim] and to draw a negative inference of his credibility based on this” (Samseen, above, at para 30).

[34] This flows directly from Rule 7 of the Rules (now Rule 11) which states that:

[7] …The claimant must provide acceptable documents establishing identity and other elements of the claim. A claimant who does not provide acceptable documents must explain why they were not provided and what steps were taken to obtain them.

[35] Jurisprudence concerning Rule 7 makes it clear that the Board can take into account an applicant’s lack of efforts to obtain corroborative evidence where it should be available and that the presumption of truth is always reviewable (Nagy v Canada (Citizenship and Immigration), 2013 FC 640 at para 66 [Nagy]; Samseen, above, at para 30).

[36] The Respondent submits that where a claimant’s story is found to be implausible or lacking in credibility, a lack of documentary evidence can be a valid consideration for the purposes of assessing credibility (Byaje and Ortiz Juarez, both above). This is an accurate principle. However, to be applicable, there must be a valid reason to doubt the Applicant’s credibility or the Board must have found the Applicant’s story to be implausible.

[37] In Byaje, above, the Board clearly stated the reasons why it did not believe the applicant’s story. Justice Mosley agreed that the applicant’s actions were not consistent with the events of her story. And, for that reason, it was not an error for the Board to require corroborating documents in circumstances where it had credibility concerns. Similarly, in Ortiz Juarez, the Board drew adverse conclusions as to credibility because the applicants’ oral evidence raised significant new information not included in their PIF’s, they had failed to provide satisfactory explanations for those omissions, and, there was an absence of corroborating documentary evidence.

[38] In Amarapala v Canada (Minister of Citizenship and Immigration), 2004 FC 12, [2004] FCJ No 62 (TD) at para 10 (QL), Justice Kelen addressed this principle when he stated that:

[10] It is well established that a panel cannot make negative inferences solely from the fact that a refugee claimant failed to produce any extrinsic documents to corroborate a claim. But where there are valid reasons to doubt a claimant's credibility, a failure to provide corroborating documentation is a proper consideration for a panel if the Board does not accept the applicant's explanation for failing to produce that evidence.

[39] In Dundar v Canada (Citizenship and Immigration), 2007 FC 1026 at para 22, Justice Tremblay-Lamer concurred with Justice Kelen’s approach and found the following:

[22] …Where valid reasons to doubt a claimant’s credibility exist, the Board may draw negative credibility inferences from a failure to provide supporting evidence. However, in my opinion, these inferences may only be drawn where the applicant has also been unable to provide a reasonable explanation for his or her lack of corroborating material.

[40] In Ndjavera v Canada (Minister of Citizenship and Immigration), 2013 FC 452, Justice Rennie stated the following:

[6] There is no general requirement for corroboration and it would be an error to make a credibility finding based on the absence of corroborative evidence alone: Dundar v Canada (Citizenship and Immigration), 2007 FC 1026 at paras 19-22.

[7] If there is a valid reason to question the claimant’s credibility, the Board may draw a negative inference from a failure to provide corroborative evidence that would reasonably be expected. Much depends on the type of evidence at issue and whether it relates to a central aspect of the claim. Corroborative evidence is most valuable, when it is independently generated by a neutral source…

[41] Of course, it must also always be kept in mind that the Board’s credibility analysis is central to its role as a trier of fact. As such, these findings are to be given significant deference by the reviewing Court and should stand unless the Board’s reasoning process was flawed and the resulting decision falls outside the range of possible, acceptable outcomes which are defensible in respect of the facts and the law (Dunsmuir, above, at para 47).

[42] Some of the relevant principles concerning adverse credibility findings were set out in Mohacsi v Canada (Minister of Citizenship and Immigration), 2003 FCT 429:

[18] First, the determination of a claimant’s credibility is the heartland of the Board’s jurisdiction. It has a well-established expertise in the determination of questions of fact, particularly the evaluation of the credibility and subjective fear of persecution of a claimant. No decision-maker, however can act arbitrarily or in a capricious manner.

[19] Second, the Board is entitled to conclude that a claimant is not credible because of implausibilities in his or her evidence as long as its inferences are not unreasonable and its reasons are set out in “clear and unmistakable terms”. Furthermore, the Board is entitled to make reasonable findings based on implausibilities, common sense and rationality. It may reject uncontradicted evidence if it is not consistent with the probabilities affecting the case as a whole, or where inconsistencies are found in the evidence.
(Also see Lubana v Canada (Minister of Citizenship and Immigration) 2003 FCT 116; Hilo v Canada (Minister of Employment and Immigration) (1992), 15 Imm LR (2d) 199 (FCA), which held that where the Board finds that the claimant’s testimony is lacking in credibility, the Board is under a duty to state in clear, unambiguous terms the reason for casting doubt upon the claimant’s testimony; Younes v Canada (Citizenship and Immigration), 2013 FC 1122 at para 2; Bazelais v Canada (Citizenship and Immigration), 2013 FC 316 at para 40).

[43] In the present case, the Board does not specify any reasons for doubting the Applicant’s credibility. It does not cite any internal contradictions or inconsistencies in the Applicant’s evidence or state why his evidence is implausible. It makes no reference to the Applicant’s demeanour when appearing before the Board. Thus, there is an issue as to whether a valid reason for doubting the Applicant’s credibility existed which opened the door to a requirement to provide corroborative evidence.

[44] Against this is the principle that uncontradicted evidence may be rejected if it is inconsistent with the probabilities of the case as a whole (Cooper v Canada (Minister of Citizenship and Immigration), 2012 FC 118 at para 4) and, as stated in Lopera v Canada (Minister of Citizenship and Immigration), 2011 FC 653 at para 31 [Lopera]), whether corroborative evidence can reasonably be demanded depends upon the facts of each case.

[45] In Lopera, above, the Board had sought the applicant’s explanation for the absence of any documentary corroboration and rejected those explanations as not credible. The applicant, relying on Ahortor v Canada (Minister of Employment & Immigration), (1993), 65 FTR 137 (TD), submitted that the Board could not draw a negative inference from the mere fact that the applicant failed to produce any extrinsic documents to corroborate his story. The respondent submitted that it was open to the Board to draw a negative inference from the fact that the applicant did not have documents that he could be expected to have, nor did he have satisfactory explanations for their absence. The respondent relied on Ortiz Juarez, above, at paragraph 7, where Justice Phelan stated that, “The requirement for corroboration is only a matter of common sense.”

[46] Justice Kelen found that it was reasonable for the Board to expect some corroborating evidence and that:

[31] Whether corroborative evidence can reasonably be demanded depends upon the facts of each case. In Juarez, Justice Phelan found that the corroborative evidence could reasonably have been expected to be available to the applicants in that case, and so the Board in that case was reasonable to draw a negative inference as a result of its absence. In contrast, in Ahortor the Board impugned the applicant’s credibility on the basis of inconsistencies that were not supported by the evidence in that case. The Board in Ahortor failed to consider the applicant’s explanations for the apparent inconsistencies, and Justice Teitelbaum found that the Board had provided no valid reason for doubting the applicant’s credibility: Ahortor at paragraphs 43 and 44.

[47] I would also note Wokwera, above, where the Board rejected the applicant’s claim for persecution based on an imputed political opinion as a person sympathetic to homosexuals in Uganda. The Board found that the applicant had provided many documents to establish his credentials as a doctor and his employment record but no documents to corroborate his claim to have treated and counselled homosexuals beyond such records that would be normal for any physician.

## 24255:4 · paragraphs 56-74

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `cd0801337c86876c02a998e4ed896fa0e86cec41bb4297e084a951f7563921f8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24255:4:subtheme:1 · paragraphs 56-67

- Raw key terms: `board, evidence, canada, applicant, immigration, minister, case, corroborating`
- Display key terms: `case, corroborating`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: case, corroborating Rule/authority context: [49] Justice Boivin found the decision under review to be reasonable based, in part, on a finding that the Board reasonably assumed that there were sources from which the applicant, who was highly educated with legal rep | [50] In this case, the Board began its analysis by stating that it was aware that testimony given under oath is presumed to be true unless there is a valid reason to doubt truthfulness. Evidence spans paragraphs 56-67. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5140038` offsets `46-51`; context: [39] The Court further notes that the central issue in this case is whether it was reasonable for the Board to expect that the applicant could and should have provided corroborating evidence, and whether it was open to the Board to draw a negative inference from the failure to produce any.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140038` offsets `182-190`; context: [39] The Court further notes that the central issue in this case is whether it was reasonable for the Board to expect that the applicant could and should have provided corroborating evidence, and whether it was open to the Board to draw a negative inference from the failure to produce any.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140039` offsets `294-302`; context: [49] Justice Boivin found the decision under review to be reasonable based, in part, on a finding that the Board reasonably assumed that there were sources from which the applicant, who was highly educated with legal representation and family connections in Uganda, could acquire corroborating evidence in the form of affidavits or letters other than from individuals who would be put in danger.
- Evidence: `governing_rule` cue `under` at chunk `5140039` offsets `39-44`; context: [49] Justice Boivin found the decision under review to be reasonable based, in part, on a finding that the Board reasonably assumed that there were sources from which the applicant, who was highly educated with legal representation and family connections in Uganda, could acquire corroborating evidence in the form of affidavits or letters other than from individuals who would be put in danger.
- Evidence: `counterargument_limitation` cue `but` at chunk `5140039` offsets `451-454`; context: Further, he had been in Canada since the fall of 2009, but had not sought to obtain affidavits or other supporting documentation.
- Evidence: `evidence_fact` cue `testimony` at chunk `5140040` offsets `82-91`; context: [50] In this case, the Board began its analysis by stating that it was aware that testimony given under oath is presumed to be true unless there is a valid reason to doubt truthfulness.
- Evidence: `governing_rule` cue `under` at chunk `5140040` offsets `98-103`; context: [50] In this case, the Board began its analysis by stating that it was aware that testimony given under oath is presumed to be true unless there is a valid reason to doubt truthfulness.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5140040` offsets `447-453`; context: The Board also found that it cannot be satisfied that “the evidence is credible or trustworthy unless satisfied that it is probably so, not just possibly so” (Orelien v Canada (Minister of Employment and Immigration) (1991), 15 Imm LR (2nd) 1 (FCA)).
- Evidence: `evidence_fact` cue `record` at chunk `5140041` offsets `32-38`; context: [51] The Board was faced with a record that contained no evidence as to the Applicant’s sexual orientation or the relationship and the events that transpired in Oman other than the Applicant’s PIF and oral testimony.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140042` offsets `187-195`; context: [52] Faced with this factual situation, if the Board had a valid reason for doubting the Applicant’s credibility, then it would not have been unreasonable for it to request corroborating evidence to prove this crucial element of the Applicant’s claim, such as proof of his divorce as his testimony was that it resulted from his homosexual relationship, hotel receipts or an affidavit from his brother who he claimed assisted him after the arrest.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140043` offsets `92-100`; context: [53] However, the Board cannot base a credibility finding solely on a lack of corroborative evidence, which seems to be what it did in this case.
- Evidence: `evidence_fact` cue `testimony` at chunk `5140045` offsets `350-359`; context: If the Board engages in such reasoning, it circumvents the presumption that sworn testimony is truthful (see Maldonado v Canada (Minister of Employment and Immigration), [1994] FCJ No 72) by analyzing the applicant’s reasons for a lack of documents without addressing the credibility or plausibility of the applicant’s allegations as described in oral testimony.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140046` offsets `118-126`; context: [28] The reasons do not disclose any credibility concern other than those concerns relating to the failure to produce evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140048` offsets `174-182`; context: [19] The Respondent is accurate in relying on the jurisprudence of this court to state that the onus is on the refugee claimant to adduce sufficient credible and trustworthy evidence to establish that there is a reasonable chance that the claimant would be persecuted if returned to his country of origin.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5140048` offsets `50-63`; context: [19] The Respondent is accurate in relying on the jurisprudence of this court to state that the onus is on the refugee claimant to adduce sufficient credible and trustworthy evidence to establish that there is a reasonable chance that the claimant would be persecuted if returned to his country of origin.
- Evidence: `counterargument_limitation` cue `However` at chunk `5140048` offsets `441-448`; context: However, I do find the Board’s logic puzzling with respect to the lack of documentation corroborating either the existence of the farm, or the grandfather’s ownership of the farm, which I agree was central to the narrative in terms of setting the scene of and motive for the alleged persecution.

#### 24255:4:subtheme:2 · paragraphs 68-72

- Raw key terms: `evidence, claimant, claimants, farc, panel, alleged, case, claim`
- Display key terms: `farc, alleged, case`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: farc, alleged, case Position/evidence statements: As the Respondent argues, a lack of documentary evidence can be a valid consideration where a claimant’s story has been found to otherwise lack credibility. Application context: [13] Therefore, based on the evidence adduced, the panel disbelieves that the claimant’s grandfather owned a farm in Sonora as alleged and, therefore, it disbelieves that the alleged incidents of December 1994 and mid-Ju | It was therefore open to the CRDD to consider his failure to produce corroborating evidence in further assessing his credibility […] Evidence spans paragraphs 68-72. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5140049` offsets `121-128`; context: [12] The claimant’s failure to provide the farm ownership documents raises a serious disbelief in the panel’s mind as to whether his grandfather owned the alleged farm in Sonora.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140049` offsets `214-222`; context: There is no persuasive documentary evidence from reliable sources that suggests that the claimants’ grandfather owned a farm in Sonora where his problems with the FARC took place.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140050` offsets `29-37`; context: [13] Therefore, based on the evidence adduced, the panel disbelieves that the claimant’s grandfather owned a farm in Sonora as alleged and, therefore, it disbelieves that the alleged incidents of December 1994 and mid-June 1995 ever took place.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5140050` offsets `5-14`; context: [13] Therefore, based on the evidence adduced, the panel disbelieves that the claimant’s grandfather owned a farm in Sonora as alleged and, therefore, it disbelieves that the alleged incidents of December 1994 and mid-June 1995 ever took place.
- Evidence: `party_position` cue `argues` at chunk `5140052` offsets `387-393`; context: As the Respondent argues, a lack of documentary evidence can be a valid consideration where a claimant’s story has been found to otherwise lack credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140052` offsets `180-188`; context: [20] This reasoning is out of line with the body of case law of this Court and is unreasonable in that it plants as the seed of incredibility the lack of corroborating documentary evidence instead of using the lack of documentary evidence to buttress an existing adverse credibility finding.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140053` offsets `212-220`; context: It was therefore open to the CRDD to consider his failure to produce corroborating evidence in further assessing his credibility […]
- Evidence: `reasoning_application` cue `therefore` at chunk `5140053` offsets `136-145`; context: It was therefore open to the CRDD to consider his failure to produce corroborating evidence in further assessing his credibility […]

#### 24255:4:subtheme:3 · paragraphs 73-74

- Raw key terms: `basis, board, above, absence, applicant, applicants, based, case`
- Display key terms: `basis, above, absence, based, case`
- Argument roles: `counterargument_limitation, evidence_fact, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position Display terms: basis, above, absence, based, case Position/evidence statements: But the Board was not entitled to discredit the Applicants’ entire claim solely on the basis of this failure. Evidence spans paragraphs 73-74. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claim` at chunk `5140054` offsets `182-187`; context: But the Board was not entitled to discredit the Applicants’ entire claim solely on the basis of this failure.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140055` offsets `314-322`; context: Rather, the Board impugns the Applicant’s credibility based on the absence of corroborative evidence.
- Evidence: `counterargument_limitation` cue `however` at chunk `5140055` offsets `434-441`; context: Significantly, however, the Board misinterpreted that documentary evidence.

#### Section text

[48] Justice Boivin stated:

[39] The Court further notes that the central issue in this case is whether it was reasonable for the Board to expect that the applicant could and should have provided corroborating evidence, and whether it was open to the Board to draw a negative inference from the failure to produce any. In this analysis, the Court refers to Lopera v Canada (Minister of Citizenship and Immigration), 2011 FC 653, [2011] FCJ No 828 [Lopera], which relied on Ortiz Juarez v Canada (Minister of Citizenship and Immigration), 2006 FC 288, 146 ACWS (3d) 705. In Lopera, above, the Court states at para 31 that: “Whether corroborative evidence can reasonably be demanded depends upon the facts of each case”. Both cases stand for the proposition that it is reasonable for the Board to demand corroborating evidence where the applicant can be reasonably expected to have such evidence available to them.

[49] Justice Boivin found the decision under review to be reasonable based, in part, on a finding that the Board reasonably assumed that there were sources from which the applicant, who was highly educated with legal representation and family connections in Uganda, could acquire corroborating evidence in the form of affidavits or letters other than from individuals who would be put in danger. Further, he had been in Canada since the fall of 2009, but had not sought to obtain affidavits or other supporting documentation.

[50] In this case, the Board began its analysis by stating that it was aware that testimony given under oath is presumed to be true unless there is a valid reason to doubt truthfulness. Further, that the real test of the truth of a story is that it is in harmony with the preponderance of probabilities which a practical and informed person would readily recognize as reasonable in that place and in those conditions. The Board also found that it cannot be satisfied that “the evidence is credible or trustworthy unless satisfied that it is probably so, not just possibly so” (Orelien v Canada (Minister of Employment and Immigration) (1991), 15 Imm LR (2nd) 1 (FCA)).

[51] The Board was faced with a record that contained no evidence as to the Applicant’s sexual orientation or the relationship and the events that transpired in Oman other than the Applicant’s PIF and oral testimony. His evidence was that he had one homosexual relationship in Oman and that when it was discovered he had no further contact with his partner and had no documentary evidence of the relationship. He also had not had a homosexual relationship since arriving in Canada and provided no oral or other evidence to suggest that he was part of the gay community here such as supporting letters from community organizations or otherwise.

[52] Faced with this factual situation, if the Board had a valid reason for doubting the Applicant’s credibility, then it would not have been unreasonable for it to request corroborating evidence to prove this crucial element of the Applicant’s claim, such as proof of his divorce as his testimony was that it resulted from his homosexual relationship, hotel receipts or an affidavit from his brother who he claimed assisted him after the arrest. Similarly, to reject the Applicant’s explanation for failing to provide such evidence, being that he had not kept in touch with anyone in Oman since his departure and did not want them to know where he is.

[53] However, the Board cannot base a credibility finding solely on a lack of corroborative evidence, which seems to be what it did in this case.

[54] In Dayebga v Canada (Minister of Citizenship and Immigration), 2013 FC 842, Justice O’Keefe stated the following:

[27] The respondent’s approach would reverse engineer the principle from Ahortor above. [T]he applicant’s failure to produce documents would create a credibility concern allowing the Board to consider his failure to produce documents as a reason to doubt credibility. If the Board engages in such reasoning, it circumvents the presumption that sworn testimony is truthful (see Maldonado v Canada (Minister of Employment and Immigration), [1994] FCJ No 72) by analyzing the applicant’s reasons for a lack of documents without addressing the credibility or plausibility of the applicant’s allegations as described in oral testimony.

[28] The reasons do not disclose any credibility concern other than those concerns relating to the failure to produce evidence. In the absence of such a credibility concern or any doubts about the applicant’s story other than those pertaining to documentary evidence, it was an error for the Board to reject the claim solely on the basis of a lack of corroborative evidence.

[55] This is similarly stated in Ayala v Canada (Minister of Citizenship and Immigration), 2011 FC 611 at paras 19-21:

[19] The Respondent is accurate in relying on the jurisprudence of this court to state that the onus is on the refugee claimant to adduce sufficient credible and trustworthy evidence to establish that there is a reasonable chance that the claimant would be persecuted if returned to his country of origin. Certainly in this case, it was open to the Board to come to the conclusion that the Applicants had failed to satisfy this requirement. However, I do find the Board’s logic puzzling with respect to the lack of documentation corroborating either the existence of the farm, or the grandfather’s ownership of the farm, which I agree was central to the narrative in terms of setting the scene of and motive for the alleged persecution. The Board reasoned, starting at para 12 of the reasons:

[12] The claimant’s failure to provide the farm ownership documents raises a serious disbelief in the panel’s mind as to whether his grandfather owned the alleged farm in Sonora. There is no persuasive documentary evidence from reliable sources that suggests that the claimants’ grandfather owned a farm in Sonora where his problems with the FARC took place. The documentary evidence does not indicated that their family’s problems with the FARC took place at their grandfather’s farm. The onus is on the claimants to establish their claim.

[13] Therefore, based on the evidence adduced, the panel disbelieves that the claimant’s grandfather owned a farm in Sonora as alleged and, therefore, it disbelieves that the alleged incidents of December 1994 and mid-June 1995 ever took place. Since the panel disbelieves that the claimant’s grandfather owned a farm, it disbelieves that the FARC demanded vacuna from the claimants’ family and as a result, it disbelieves that the claimants’ family received threats from the FARC for failing to pay vacuna.

[14] The panel finds that the claimants have fabricated their story about their fear of persecution at the hands of the FARC guerrillas in Colombia.

[20] This reasoning is out of line with the body of case law of this Court and is unreasonable in that it plants as the seed of incredibility the lack of corroborating documentary evidence instead of using the lack of documentary evidence to buttress an existing adverse credibility finding. The Board points to no other reason to disbelieve the Applicants’ testimony. As the Respondent argues, a lack of documentary evidence can be a valid consideration where a claimant’s story has been found to otherwise lack credibility. For example, in Bin, above, cited by the Respondent, Justice Denis Pelletier went on to say at para 22:

[22] In the present case, the applicant's claim had been discredited by a number of internal contradictions and inconsistencies. It was therefore open to the CRDD to consider his failure to produce corroborating evidence in further assessing his credibility […]

[21] The Board was entitled to find the Applicants’ explanation for failing to produce the documents unreasonable. But the Board was not entitled to discredit the Applicants’ entire claim solely on the basis of this failure. To do so would be to ignore the oft-cited ratio of Maldonado, above.

[56] In this case, the Board has similarly fallen into error. The Decision does not identify any credibility concerns or state that the Board found the Applicant’s story to be implausible and the reasons for that finding. Rather, the Board impugns the Applicant’s credibility based on the absence of corroborative evidence. Further, on the basis of its finding that the documentary evidence contradicted his testimony. Significantly, however, the Board misinterpreted that documentary evidence.

## 24255:5 · paragraphs 75-84

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7b073a60f0eb84a5200964046f6c9635f1c4b2b000ed31318c44523a4456f3e9`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24255:5:subtheme:1 · paragraphs 75-79

- Raw key terms: `board, applicant, conduct, documentary, evidence, year, against, appears`
- Display key terms: `conduct, documentary, year, against, appears`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: conduct, documentary, year, against, appears Position/evidence statements: [61] The Applicant submits that in appropriate cases, the Board is required to conduct a separate analysis for section 96 and 97 (Balakumar v Canada (Minister of Citizenship and Immigration), 2008 FC 20 at para 13; Kandi Rule/authority context: [58] In fact, that document states that the most recent year for which statistics are available was for 2009: Gay, lesbian, bisexual, and transgender (LGBT) persons faced discrimination under the law and in practice. | A claimant found to be not credible under section 96 may nevertheless obtain status under section 97 if the claimant’s profile is sufficient to establish risk (Asu v Canada (Minister of Citizenship and Immigration), 2005 Application context: Therefore, in these circumstances, there were no valid reasons to doubt the Applicant’s credibility. Evidence spans paragraphs 75-79. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140056` offsets `125-133`; context: [57] The Board refers to the US DOS Report and states:
The claimant was asked to give his comments regarding the documentary evidence from independent and reliable sources that indicate that there were no reports of prosecution for homosexual conduct in Oman during the year 2010.
- Evidence: `governing_rule` cue `under` at chunk `5140057` offsets `186-191`; context: [58] In fact, that document states that the most recent year for which statistics are available was for 2009:
Gay, lesbian, bisexual, and transgender (LGBT) persons faced discrimination under the law and in practice.
- Evidence: `counterargument_limitation` cue `although` at chunk `5140057` offsets `453-461`; context: There were no reports of prosecutions for during the year, although nine prosecutions for sodomy occurred in 2009, the most recent year for which statistics are available.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140058` offsets `46-54`; context: [59] The Board misapprehended the documentary evidence in finding that there were no prosecutions for 2010, when in fact the most recent year for which statistics were available was in 2009.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140059` offsets `198-206`; context: [60] If the Board had provided valid reasons for doubting the Applicant’s credibility, then it would have been entirely reasonable for it to have expected the Applicant to have provided documentary evidence to corroborate his claim, such as his divorce documents or an affidavit from his brother; to have rejected his explanation for having failed to do so; and, to have drawn a negative inference from the failure to provide such evidence.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5140059` offsets `875-884`; context: Therefore, in these circumstances, there were no valid reasons to doubt the Applicant’s credibility.
- Evidence: `counterargument_limitation` cue `However` at chunk `5140059` offsets `441-448`; context: However, the Decision did not contain an adverse credibility finding based on inconsistencies or contradictions in the Applicant’s evidence or any similar finding.
- Evidence: `party_position` cue `submits` at chunk `5140060` offsets `19-26`; context: [61] The Applicant submits that in appropriate cases, the Board is required to conduct a separate analysis for section 96 and 97 (Balakumar v Canada (Minister of Citizenship and Immigration), 2008 FC 20 at para 13; Kandiah v Canada (Minister of Citizenship and Immigration), 2005 FC 181 at para 18).
- Evidence: `governing_rule` cue `under` at chunk `5140060` offsets `336-341`; context: A claimant found to be not credible under section 96 may nevertheless obtain status under section 97 if the claimant’s profile is sufficient to establish risk (Asu v Canada (Minister of Citizenship and Immigration), 2005 FC 1693 at para 9).
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `5140060` offsets `357-369`; context: A claimant found to be not credible under section 96 may nevertheless obtain status under section 97 if the claimant’s profile is sufficient to establish risk (Asu v Canada (Minister of Citizenship and Immigration), 2005 FC 1693 at para 9).

#### 24255:5:subtheme:2 · paragraphs 80-84

- Raw key terms: `applicant, board, risk, submits, above, analysis, basis, canada`
- Display key terms: `risk, submits, above, analysis, basis`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: risk, submits, above, analysis, basis Position/evidence statements: [62] The Applicant submits that his risk profile arises from his identity as a homosexual which subjects him to prosecution. | [63] The Applicant submits that the same documentary evidence relied on by the Board supports the conclusion that the Applicant faces a serious risk of harm in Oman on an objective basis given his sexual identity. Rule/authority context: It also makes no reference to the evidence of criminalization of homosexuality under Omani penal legislation, or the reinforcement of social norms by discriminatory practices. Application context: The Board’s reliance on this document is therefore perverse and capricious. Operative outcome context: [66] For the above reasons this application for judicial review is granted. Evidence spans paragraphs 80-84. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5140061` offsets `169-177`; context: The Board does not make a finding as to the question of the Applicant’s sexual orientation.
- Evidence: `party_position` cue `submits` at chunk `5140061` offsets `19-26`; context: [62] The Applicant submits that his risk profile arises from his identity as a homosexual which subjects him to prosecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140061` offsets `251-259`; context: It also makes no reference to the evidence of criminalization of homosexuality under Omani penal legislation, or the reinforcement of social norms by discriminatory practices.
- Evidence: `governing_rule` cue `under` at chunk `5140061` offsets `296-301`; context: It also makes no reference to the evidence of criminalization of homosexuality under Omani penal legislation, or the reinforcement of social norms by discriminatory practices.
- Evidence: `party_position` cue `submits` at chunk `5140062` offsets `19-26`; context: [63] The Applicant submits that the same documentary evidence relied on by the Board supports the conclusion that the Applicant faces a serious risk of harm in Oman on an objective basis given his sexual identity.
- Evidence: `evidence_fact` cue `evidence` at chunk `5140062` offsets `53-61`; context: [63] The Applicant submits that the same documentary evidence relied on by the Board supports the conclusion that the Applicant faces a serious risk of harm in Oman on an objective basis given his sexual identity.
- Evidence: `reasoning_application` cue `therefore` at chunk `5140062` offsets `255-264`; context: The Board’s reliance on this document is therefore perverse and capricious.
- Evidence: `party_position` cue `submits` at chunk `5140063` offsets `20-27`; context: [64] The Respondent submits that the Board was not required to conduct a separate section 97 analysis as it made very clear findings that it found the Applicant’s story to be false.
- Evidence: `evidence_fact` cue `found that` at chunk `5140063` offsets `729-739`; context: In this case, the Board clearly did not believe that the Applicant was in a homosexual relationship and found that he fabricated his story to support a false claim.
- Evidence: `disposition` cue `granted` at chunk `5140065` offsets `67-74`; context: [66] For the above reasons this application for judicial review is granted.

#### Section text

[57] The Board refers to the US DOS Report and states:
The claimant was asked to give his comments regarding the documentary evidence from independent and reliable sources that indicate that there were no reports of prosecution for homosexual conduct in Oman during the year 2010.

[58] In fact, that document states that the most recent year for which statistics are available was for 2009:
Gay, lesbian, bisexual, and transgender (LGBT) persons faced discrimination under the law and in practice. Social norms also re-enforced discrimination against LGBT persons. The penal code criminalizes consensual same-sex sexual conduct with a jail term of six months to three years. There were no reports of prosecutions for during the year, although nine prosecutions for sodomy occurred in 2009, the most recent year for which statistics are available.(Emphasis added)

[59] The Board misapprehended the documentary evidence in finding that there were no prosecutions for 2010, when in fact the most recent year for which statistics were available was in 2009. The Board then appears to have used this error to impugn the Applicant’s credibility. The transcript of the hearing before the Board reads as follows:
Q It does state, the document, that people are discriminated and prosecuted for homosexual behaviour in Oman and there is a penal court---or penal court that criminalizes homosexual but there is no report that anybody was prosecuted for that in the year 2010.
Now, sir, had you brought –had you brought [a] copy of the warrant of arrest, a copy of the charges against you I would have understood. I would give more weight to those documents that this document but I have no documents, sir.
Sir, how am I going to believe you that you—you are being wanted in Oman for homosexual charges, 2010?
A All I can confirm is that is what happened to me and I’m telling the truth, that is what happened to me and why would I will leave my country, I have lived there for a very long time, why would I leave my kids, why would I leave everything that I own for such a long time, and like, you know, just leave everything just – if I didn’t have any problems, just for the sake of it.

[60] If the Board had provided valid reasons for doubting the Applicant’s credibility, then it would have been entirely reasonable for it to have expected the Applicant to have provided documentary evidence to corroborate his claim, such as his divorce documents or an affidavit from his brother; to have rejected his explanation for having failed to do so; and, to have drawn a negative inference from the failure to provide such evidence. However, the Decision did not contain an adverse credibility finding based on inconsistencies or contradictions in the Applicant’s evidence or any similar finding. Nor was there any finding that the Applicant’s story was in whole implausible with reasons supporting such a finding. Further, and in particular, the reason for attacking the Applicant’s credibility appears to be the Board’s misapprehension of the documentary evidence. Therefore, in these circumstances, there were no valid reasons to doubt the Applicant’s credibility. Accordingly, it was not reasonable for the Board to draw an adverse inference regarding the Applicant’s credibility nor to then use this to ground a demand for corroborating documentation and, ultimately, to deny his claim based on the failure to provide such evidence.
Did the Board consider the Applicant’s section 97(1) claim?
Applicant’s Position

[61] The Applicant submits that in appropriate cases, the Board is required to conduct a separate analysis for section 96 and 97 (Balakumar v Canada (Minister of Citizenship and Immigration), 2008 FC 20 at para 13; Kandiah v Canada (Minister of Citizenship and Immigration), 2005 FC 181 at para 18). A claimant found to be not credible under section 96 may nevertheless obtain status under section 97 if the claimant’s profile is sufficient to establish risk (Asu v Canada (Minister of Citizenship and Immigration), 2005 FC 1693 at para 9). The Board engaged in a perfunctory reference to section 97 which was insufficient to discharge its duty to conduct a separate analysis (Amare v Canada (Minister of Citizenship and Immigration), 2008 FC 228 at paras 12-13).

[62] The Applicant submits that his risk profile arises from his identity as a homosexual which subjects him to prosecution. The Board does not make a finding as to the question of the Applicant’s sexual orientation. It also makes no reference to the evidence of criminalization of homosexuality under Omani penal legislation, or the reinforcement of social norms by discriminatory practices.

[63] The Applicant submits that the same documentary evidence relied on by the Board supports the conclusion that the Applicant faces a serious risk of harm in Oman on an objective basis given his sexual identity. The Board’s reliance on this document is therefore perverse and capricious. If the Board correctly appreciated the facts and applied the law accordingly, it would have reached a different conclusion (Moagi v Canada (Minister of Employment and Immigration) (1986), 69 NR 229 (CA)).
Respondent’s Submissions

[64] The Respondent submits that the Board was not required to conduct a separate section 97 analysis as it made very clear findings that it found the Applicant’s story to be false. While case law has held that there may be circumstances where a separate section 97 is appropriate (Kilic v Canada (Minister of Citizenship and Immigration), 2004 FC 84 at para 29; Sanchez v Canada (Minister of Citizenship and Immigration), 2007 FCA 99 at para 15), it is not necessary where the applicant has been found to be not credible (Plancher v Canada (Minister of Citizenship and Immigration), 2007 FC 1283 at paras 16-17 [Plancher]). In this case, the Board clearly did not believe that the Applicant was in a homosexual relationship and found that he fabricated his story to support a false claim. Having rejected the Applicant’s story outright, there was no remaining basis upon which a claim of risk was made out.

[65] Given my finding above as to the credibility analysis, I agree with the Applicant’s position.

[66] For the above reasons this application for judicial review is granted.


## 24255:6 · paragraphs 85-86

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7d25e1701b39d1b91d477dcefec234ca70e7dbed8a852531f2adbc2525bce3f7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24255:6:subtheme:1 · paragraphs 85-86

- Raw key terms: `allowed, application, arises, aside, back, board, cause, cecily`
- Display key terms: `allowed, arises, aside, back, cecily`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: allowed, arises, aside, back, cecily Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that this application for judicial review is allowed, the Board’s decision is set aside and the matter is remitted back for re-determination by a differently constituted panel of the Boa Evidence spans paragraphs 85-86. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5140065` offsets `303-311`; context: No question of general importance for certification has been proposed and none arises.
- Evidence: `disposition` cue `allowed` at chunk `5140065` offsets `155-162`; context: JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is allowed, the Board’s decision is set aside and the matter is remitted back for re-determination by a differently constituted panel of the Board.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is allowed, the Board’s decision is set aside and the matter is remitted back for re-determination by a differently constituted panel of the Board. No question of general importance for certification has been proposed and none arises.
"Cecily Y. Strickland"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-10401-12
STYLE OF CAUSE:
ALI SALEH ZAHRAN AL ISMAILI v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
October 10, 2013
REASONS FOR 

## 24255:7 · paragraphs 87-87

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5bffbfdf378ae7116f0fd604cf926bad061441c90aed927b42cf916f73958007`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24255:7:subtheme:1 · paragraphs 87-87

- Raw key terms: `appearances, applicant, attorney, barristers, brodzky, canada, cullen, dated`
- Display key terms: `barristers, brodzky, cullen, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barristers, brodzky, cullen, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 87-87. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND JUDGMENT:
STRICKLAND J.
DATED:
January 24, 2014
APPEARANCES:
Michael Brodzky
For The Applicant
Nicole Rahaman
For The Respondent
SOLICITORS OF RECORD:
Petrykanyn Cullen
Barristers & Solicitors
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
