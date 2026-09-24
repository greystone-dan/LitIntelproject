# Discussion Units: case 13412

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **60**
- Continuity pairs: **59**
- Discussion Units: **4**
- Paragraph source hashes: **60**
- Sub-themes: **15**

## 13412:1 · paragraphs 0-37

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `99ab87a64706b8545155c7e2f27efeec1f9c22710cf48fe8725ac052a2a828ae`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13412:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `applicant, decision, immigration, appeal, april, basis, board, canada`
- Display key terms: `april, basis`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: april, basis Operative outcome context: [1] The applicant seeks judicial review of the decision of the Refugee Appeal Division of the Immigration and Refugee Board [RAD] dated April 16, 2015 which dismissed his appeal of the decision of the Refugee Protection  Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4660856` offsets `157-166`; context: [1] The applicant seeks judicial review of the decision of the Refugee Appeal Division of the Immigration and Refugee Board [RAD] dated April 16, 2015 which dismissed his appeal of the decision of the Refugee Protection Division [RPD] decision.

#### 13412:1:subtheme:2 · paragraphs 2-20

- Raw key terms: `applicant, documents, identity, fraudulent, evidence, found, credibility, card`
- Display key terms: `documents, identity, fraudulent, credibility, card`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: documents, identity, fraudulent, credibility, card Position/evidence statements: Because of his involvement with the SCNC, he claims that he was arrested, detained and tortured by the police on several occasions. | The RPD noted that the applicant was uncertain about the order of his names, as in Africa, first and last names are not differentiated, and found that the order of his name differed between the names provided at the RPD  Rule/authority context: [2] The application for judicial review raises several issues including the role of the RAD in assessing credibility without an oral hearing, the need to reconcile the requirement for a refugee claimant to provide credib | [3] The determinative issue is the RAD’s error in basing its primary credibility finding on the applicant’s use of false documents to exit Cameroon, contrary to the principles in the jurisprudence, which the RAD then rel Application context: Because of his involvement with the SCNC, he claims that he was arrested, detained and tortured by the police on several occasions. Operative outcome context: As a result, the application for judicial review is allowed. | [15] The RAD denied the request for an oral hearing, noting that the new evidence could not independently establish the applicant’s identity and did not meet the test set out in subsection 110(6) to permit an oral hearin Evidence spans paragraphs 2-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4660857` offsets `55-61`; context: [2] The application for judicial review raises several issues including the role of the RAD in assessing credibility without an oral hearing, the need to reconcile the requirement for a refugee claimant to provide credible and trustworthy evidence of their identity with the principle that adverse credibility findings should not be based on a refugee claimant’s need to flee their country with false documents, and whether a finding that a refugee claimant has failed to establish their identity disposes of any obligation on the RAD or RPD to assess a refugee claimant’s risk upon return to their country pursuant to section 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] on the basis of objective evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660857` offsets `239-247`; context: [2] The application for judicial review raises several issues including the role of the RAD in assessing credibility without an oral hearing, the need to reconcile the requirement for a refugee claimant to provide credible and trustworthy evidence of their identity with the principle that adverse credibility findings should not be based on a refugee claimant’s need to flee their country with false documents, and whether a finding that a refugee claimant has failed to establish their identity disposes of any obligation on the RAD or RPD to assess a refugee claimant’s risk upon return to their country pursuant to section 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] on the basis of objective evidence.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4660857` offsets `607-618`; context: [2] The application for judicial review raises several issues including the role of the RAD in assessing credibility without an oral hearing, the need to reconcile the requirement for a refugee claimant to provide credible and trustworthy evidence of their identity with the principle that adverse credibility findings should not be based on a refugee claimant’s need to flee their country with false documents, and whether a finding that a refugee claimant has failed to establish their identity disposes of any obligation on the RAD or RPD to assess a refugee claimant’s risk upon return to their country pursuant to section 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] on the basis of objective evidence.
- Evidence: `issue` cue `issue` at chunk `4660858` offsets `22-27`; context: [3] The determinative issue is the RAD’s error in basing its primary credibility finding on the applicant’s use of false documents to exit Cameroon, contrary to the principles in the jurisprudence, which the RAD then relied on to draw additional negative credibility inferences.
- Evidence: `party_position` cue `claims` at chunk `4660858` offsets `619-625`; context: Because of his involvement with the SCNC, he claims that he was arrested, detained and tortured by the police on several occasions.
- Evidence: `governing_rule` cue `principles` at chunk `4660858` offsets `165-175`; context: [3] The determinative issue is the RAD’s error in basing its primary credibility finding on the applicant’s use of false documents to exit Cameroon, contrary to the principles in the jurisprudence, which the RAD then relied on to draw additional negative credibility inferences.
- Evidence: `reasoning_application` cue `Because` at chunk `4660858` offsets `574-581`; context: Because of his involvement with the SCNC, he claims that he was arrested, detained and tortured by the police on several occasions.
- Evidence: `disposition` cue `allowed` at chunk `4660858` offsets `331-338`; context: As a result, the application for judicial review is allowed.
- Evidence: `evidence_fact` cue `found that` at chunk `4660860` offsets `270-280`; context: The CBSA found that the birth certificate was unverifiable and the National Identity Card was probably counterfeit.
- Evidence: `party_position` cue `Claim` at chunk `4660861` offsets `356-361`; context: The RPD noted that the applicant was uncertain about the order of his names, as in Africa, first and last names are not differentiated, and found that the order of his name differed between the names provided at the RPD hearing, his other documents and his Basis of Claim form.
- Evidence: `evidence_fact` cue `found that` at chunk `4660861` offsets `12-22`; context: [8] The RPD found that the applicant’s testimony regarding his identity was not credible.
- Evidence: `party_position` cue `Claim` at chunk `4660862` offsets `188-193`; context: [9] The RPD found that the applicant’s explanation for failing to disclose his prior visa applications using the name “Gawum” was not reasonable, noting he could have amended his Basis of Claim form to be truthful.
- Evidence: `evidence_fact` cue `found that` at chunk `4660862` offsets `12-22`; context: [9] The RPD found that the applicant’s explanation for failing to disclose his prior visa applications using the name “Gawum” was not reasonable, noting he could have amended his Basis of Claim form to be truthful.
- Evidence: `evidence_fact` cue `record` at chunk `4660863` offsets `104-110`; context: [10] The RPD placed little weight on the applicant’s birth certificate given the other documents on the record admitted to be fraudulent, the anomalies in the documents and the credibility concerns.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660864` offsets `30-38`; context: [12] The RAD admitted the new evidence in accordance with subsection 110(4) of the Act.
- Evidence: `party_position` cue `submitted` at chunk `4660865` offsets `120-129`; context: [13] However, the RAD gave the affidavit of the applicant’s uncle little weight given that the applicant had repeatedly submitted fraudulent documents and his uncle had been the conduit for several of these fraudulent documents.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4660865` offsets `31-40`; context: [13] However, the RAD gave the affidavit of the applicant’s uncle little weight given that the applicant had repeatedly submitted fraudulent documents and his uncle had been the conduit for several of these fraudulent documents.
- Evidence: `evidence_fact` cue `record` at chunk `4660866` offsets `135-141`; context: [14] The RAD accepted the applicant’s explanation for the inconsistencies in the order of his first and last names in documents on the record based on the article provided.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660867` offsets `73-81`; context: [15] The RAD denied the request for an oral hearing, noting that the new evidence could not independently establish the applicant’s identity and did not meet the test set out in subsection 110(6) to permit an oral hearing.
- Evidence: `disposition` cue `denied` at chunk `4660867` offsets `13-19`; context: [15] The RAD denied the request for an oral hearing, noting that the new evidence could not independently establish the applicant’s identity and did not meet the test set out in subsection 110(6) to permit an oral hearing.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660868` offsets `197-205`; context: [16] The RAD noted that in accordance with Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799, [2014] 4 FCR 811 [Huruglica] it would conduct an independent assessment of the evidence.
- Evidence: `evidence_fact` cue `found that` at chunk `4660869` offsets `134-144`; context: [17] The RAD accepted that the different order of names in the applicant’s documentation cannot be used as an indicator of fraud, but found that the RPD did not err by inquiring into the reliability of the applicant’s documents given his propensity for relying on fraudulent documents.
- Evidence: `evidence_fact` cue `found that` at chunk `4660870` offsets `13-23`; context: [18] The RAD found that the RPD had erred by finding that it was implausible that the applicant’s US visa and his denied Canadian visa application used his girlfriend’s last name and were fraudulent.
- Evidence: `counterargument_limitation` cue `However` at chunk `4660870` offsets `200-207`; context: However, the RAD again found that the applicant’s repeated reliance on fraudulent documents in his interactions with the US and Canadian authorities exhibits his propensity to rely on such documents and assume a fraudulent identity and that this detracts from his credibility.
- Evidence: `disposition` cue `denied` at chunk `4660870` offsets `114-120`; context: [18] The RAD found that the RPD had erred by finding that it was implausible that the applicant’s US visa and his denied Canadian visa application used his girlfriend’s last name and were fraudulent.
- Evidence: `evidence_fact` cue `found that` at chunk `4660873` offsets `125-135`; context: However, the RAD found that, in this case, it was open to the RPD, in light of the credibility concerns and the fraudulent National Identity Card, to look for more reliable and probative documents and to give the secondary identity documents little weight.
- Evidence: `counterargument_limitation` cue `However` at chunk `4660873` offsets `108-115`; context: However, the RAD found that, in this case, it was open to the RPD, in light of the credibility concerns and the fraudulent National Identity Card, to look for more reliable and probative documents and to give the secondary identity documents little weight.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660874` offsets `256-264`; context: [22] The RAD rejected the applicant’s argument that he should not be held responsible for his uncle’s actions in sending him fraudulent documents which he had not previously seen, noting that the onus was on him to establish, with credible and trustworthy evidence, on a balance of probabilities, that he is who he says he is.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660875` offsets `250-258`; context: Based on the totality of the evidence, the RAD found that he had not provided sufficient reliable and probative evidence to establish his identity on a balance of probabilities.

#### 13412:1:subtheme:3 · paragraphs 21-22

- Raw key terms: `credibility, findings, reviewed, standard, applicant, application, argues, assess`
- Display key terms: `credibility, findings, reviewed, standard, argues, assess`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: credibility, findings, reviewed, standard, argues, assess Position/evidence statements: The Issues [25] The applicant argues that: 1. Rule/authority context: The RAD erred by failing to conduct an assessment, pursuant to section 97 of the Act, of the risk the applicant would face upon return to Cameroon. Application context: The RAD reached the same conclusion based on finding that the applicant’s identity had not been established and, therefore, it was not required to assess his risk. Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4660876` offsets `350-356`; context: The Issues [25] The applicant argues that:
1.
- Evidence: `party_position` cue `argues` at chunk `4660876` offsets `376-382`; context: The Issues [25] The applicant argues that:
1.
- Evidence: `evidence_fact` cue `found that` at chunk `4660876` offsets `21-31`; context: [24] The RAD further found that the RPD did not breach the applicant’s section 7 Charter rights by failing to conduct any assessment of his risk upon return to his home country.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4660876` offsets `762-773`; context: The RAD erred by failing to conduct an assessment, pursuant to section 97 of the Act, of the risk the applicant would face upon return to Cameroon.
- Evidence: `reasoning_application` cue `therefore` at chunk `4660876` offsets `291-300`; context: The RAD reached the same conclusion based on finding that the applicant’s identity had not been established and, therefore, it was not required to assess his risk.

#### 13412:1:subtheme:4 · paragraphs 23-27

- Raw key terms: `credibility, canada, citizenship, findings, immigration, minister, para, respect`
- Display key terms: `credibility, findings, para, respect`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: credibility, findings, para, respect Rule/authority context: [29] With respect to questions of credibility, the jurisprudence has generally established that the RAD may or should defer to the RPD because the RPD has heard the witnesses directly, has had an opportunity to probe the Application context: [29] With respect to questions of credibility, the jurisprudence has generally established that the RAD may or should defer to the RPD because the RPD has heard the witnesses directly, has had an opportunity to probe the | [30] However, in Khachatourian v Canada (Minister of Citizenship and Immigration), 2015 FC 182 at paras 31-32, [2015] FCJ No 156 (QL), Justice Noël noted that the RAD should assume its appellate role and, therefore, the  Evidence spans paragraphs 23-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4660878` offsets `161-168`; context: [28] The reasonableness standard focuses on “the existence of justification, transparency and intelligibility within the decision-making process” and considers “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir at para 47).
- Evidence: `evidence_fact` cue `testimony` at chunk `4660879` offsets `223-232`; context: [29] With respect to questions of credibility, the jurisprudence has generally established that the RAD may or should defer to the RPD because the RPD has heard the witnesses directly, has had an opportunity to probe their testimony or has had some advantage not enjoyed by the RAD; see, for example, Huruglica at para 55; Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 at para 39, [2014] FCJ No 1116 (QL); Nahal v Canada (Minister of Citizenship and Immigration), 2014 FC 1208 at para 25, [2014] FCJ No 1254 (QL).
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4660879` offsets `51-64`; context: [29] With respect to questions of credibility, the jurisprudence has generally established that the RAD may or should defer to the RPD because the RPD has heard the witnesses directly, has had an opportunity to probe their testimony or has had some advantage not enjoyed by the RAD; see, for example, Huruglica at para 55; Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 at para 39, [2014] FCJ No 1116 (QL); Nahal v Canada (Minister of Citizenship and Immigration), 2014 FC 1208 at para 25, [2014] FCJ No 1254 (QL).
- Evidence: `reasoning_application` cue `because` at chunk `4660879` offsets `135-142`; context: [29] With respect to questions of credibility, the jurisprudence has generally established that the RAD may or should defer to the RPD because the RPD has heard the witnesses directly, has had an opportunity to probe their testimony or has had some advantage not enjoyed by the RAD; see, for example, Huruglica at para 55; Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 at para 39, [2014] FCJ No 1116 (QL); Nahal v Canada (Minister of Citizenship and Immigration), 2014 FC 1208 at para 25, [2014] FCJ No 1254 (QL).
- Evidence: `evidence_fact` cue `evidence` at chunk `4660880` offsets `388-396`; context: [30] However, in Khachatourian v Canada (Minister of Citizenship and Immigration), 2015 FC 182 at paras 31-32, [2015] FCJ No 156 (QL), Justice Noël noted that the RAD should assume its appellate role and, therefore, the same level of deference may not be warranted with respect to credibility findings in an appeal as in a judicial review; an independent assessment or an analysis of the evidence would be necessary to permit some level of deference.
- Evidence: `reasoning_application` cue `therefore` at chunk `4660880` offsets `205-214`; context: [30] However, in Khachatourian v Canada (Minister of Citizenship and Immigration), 2015 FC 182 at paras 31-32, [2015] FCJ No 156 (QL), Justice Noël noted that the RAD should assume its appellate role and, therefore, the same level of deference may not be warranted with respect to credibility findings in an appeal as in a judicial review; an independent assessment or an analysis of the evidence would be necessary to permit some level of deference.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660882` offsets `118-126`; context: The RAD stated that it conducted its own assessment of the evidence.

#### 13412:1:subtheme:5 · paragraphs 28-29

- Raw key terms: `certain, hearing, held, hold, however, oral, provides, subsection`
- Display key terms: `certain, hearing, hold, however, oral, provides, subsection`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: certain, hearing, hold, however, oral, provides, subsection Position/evidence statements: The RAD did not breach its duty of procedural fairness [34] The applicant acknowledges that subsection 110(6) of the Act provides that the RAD may hold a hearing if certain conditions are met, but submits that the common Application context: The RAD did not breach its duty of procedural fairness [34] The applicant acknowledges that subsection 110(6) of the Act provides that the RAD may hold a hearing if certain conditions are met, but submits that the common Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4660883` offsets `29-34`; context: [33] On judicial review, the issue is whether the RAD’s credibility findings are reasonable.
- Evidence: `party_position` cue `submits` at chunk `4660883` offsets `840-847`; context: The RAD did not breach its duty of procedural fairness [34] The applicant acknowledges that subsection 110(6) of the Act provides that the RAD may hold a hearing if certain conditions are met, but submits that the common law duty of procedural fairness continues to apply and an oral hearing should have been held to provide him with an opportunity to respond to the RAD’s credibility concerns and to know the case he had to meet.
- Evidence: `evidence_fact` cue `testimony` at chunk `4660883` offsets `268-277`; context: It is well settled that credibility findings of boards and tribunals are owed significant deference on judicial review, given that they are in the best position to assess the testimony and the evidence.
- Evidence: `reasoning_application` cue `apply` at chunk `4660883` offsets `909-914`; context: The RAD did not breach its duty of procedural fairness [34] The applicant acknowledges that subsection 110(6) of the Act provides that the RAD may hold a hearing if certain conditions are met, but submits that the common law duty of procedural fairness continues to apply and an oral hearing should have been held to provide him with an opportunity to respond to the RAD’s credibility concerns and to know the case he had to meet.
- Evidence: `counterargument_limitation` cue `However` at chunk `4660883` offsets `296-303`; context: However, in the present case, the RAD did not conduct an oral hearing and did not hear first-hand from the applicant.
- Evidence: `counterargument_limitation` cue `However` at chunk `4660884` offsets `120-127`; context: However, subsection 110(6) provides an exception where a hearing may be held where certain criteria are met.

#### 13412:1:subtheme:6 · paragraphs 30-31

- Raw key terms: `applicant, credibility, accepted, allowing, canada, case, central, citizenship`
- Display key terms: `credibility, accepted, allowing, case, central`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: credibility, accepted, allowing, case, central Evidence spans paragraphs 30-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4660885` offsets `132-137`; context: [36] The applicant interprets the exception to mean that when any of the evidence relied on by the RAD raises a serious credibility issue that is central to the decision and that, if accepted, would justify allowing or rejecting the refugee claim, the criteria are met.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660885` offsets `73-81`; context: [36] The applicant interprets the exception to mean that when any of the evidence relied on by the RAD raises a serious credibility issue that is central to the decision and that, if accepted, would justify allowing or rejecting the refugee claim, the criteria are met.

#### 13412:1:subtheme:7 · paragraphs 32-33

- Raw key terms: `findings, further, give, record, adequacy, agreed, alphabet, applicant`
- Display key terms: `findings, further, give, adequacy, agreed, alphabet`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: findings, further, give, adequacy, agreed, alphabet Evidence spans paragraphs 32-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4660887` offsets `878-886`; context: The comments by the RAD as to the differences in the spelling of the Applicant’s name in the US proceedings versus the Canadian proceedings is nonsense: of course, there will be differences where a different alphabet and language is in question such as Somali and English.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660887` offsets `176-184`; context: Had the RAD simply reviewed the findings of the RPD as to the adequacy of the Applicant’s evidence and agreed with it, that would have ended the matter.
- Evidence: `evidence_fact` cue `record` at chunk `4660888` offsets `80-86`; context: [10] The point is that if the RAD chooses to take a frolic and venture into the record to make further substantive findings, it should give some sort of notice to the parties and give them an opportunity to make submissions.

#### 13412:1:subtheme:8 · paragraphs 34-37

- Raw key terms: `applicant, credibility, documents, findings, circumstances, evidence, false, fraudulent`
- Display key terms: `credibility, documents, findings, circumstances, false, fraudulent`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: credibility, documents, findings, circumstances, false, fraudulent Position/evidence statements: The RAD’s negative credibility findings were not reasonable [41] The applicant argues that refugees are often forced to flee using false documents and negative credibility inferences are not justified in such circumstanc Rule/authority context: [42] As the applicant points out, the jurisprudence has cautioned against drawing negative credibility findings from the use of false documents where refugee claimants have little choice but to use such documents to leav Evidence spans paragraphs 34-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4660889` offsets `162-168`; context: [38] Although the RAD did make credibility findings, unlike in Husian, the RAD did not ignore contradictory evidence on the record or make additional findings on issues unknown to the applicant.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660889` offsets `108-116`; context: [38] Although the RAD did make credibility findings, unlike in Husian, the RAD did not ignore contradictory evidence on the record or make additional findings on issues unknown to the applicant.
- Evidence: `issue` cue `issue` at chunk `4660890` offsets `295-300`; context: The applicant was well aware that the only issue before the RAD was his identity and his use of fraudulent documents to establish his identity.
- Evidence: `party_position` cue `argues` at chunk `4660891` offsets `385-391`; context: The RAD’s negative credibility findings were not reasonable [41] The applicant argues that refugees are often forced to flee using false documents and negative credibility inferences are not justified in such circumstances (Rasheed v Canada (Minister of Citizenship and Immigration), 2004 FC 587 at para 18, [2004] FCJ No 715 (QL) [Rasheed]; Gulamsakhi v Canada (Minister of Citizenship and Immigration), 2015 FC 105 at para 9, [2015] FCJ No 271 (QL) [Gulamsakhi]); The applicant submits that all the credibility findings of the RAD stem from his use of fraudulent documents to escape persecution in Cameroon and which he presented upon arrival to seek refugee protection in Canada.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660891` offsets `101-109`; context: [40] However, as noted above, the RAD made credibility findings of its own, based on the documentary evidence and without hearing directly from the applicant.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4660892` offsets `38-51`; context: [42] As the applicant points out, the jurisprudence has cautioned against drawing negative credibility findings from the use of false documents where refugee claimants have little choice but to use such documents to leave their country.

#### Section text

Koffi v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2016-01-04
Neutral citation
2016 FC 4
File numbers
IMM-2285-15
Decision Content
Date: 20160104
Docket: IMM-2285-15
Citation: 2016 FC 4
Ottawa, Ontario, January 4, 2016
PRESENT: The Honourable Madam Justice Kane
BETWEEN:
VALANTINE MOBOH KOFFI
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] The applicant seeks judicial review of the decision of the Refugee Appeal Division of the Immigration and Refugee Board [RAD] dated April 16, 2015 which dismissed his appeal of the decision of the Refugee Protection Division [RPD] decision. The RAD confirmed that the applicant is neither a Convention refugee nor a person in need of protection on the basis that he did not establish his identity.

[2] The application for judicial review raises several issues including the role of the RAD in assessing credibility without an oral hearing, the need to reconcile the requirement for a refugee claimant to provide credible and trustworthy evidence of their identity with the principle that adverse credibility findings should not be based on a refugee claimant’s need to flee their country with false documents, and whether a finding that a refugee claimant has failed to establish their identity disposes of any obligation on the RAD or RPD to assess a refugee claimant’s risk upon return to their country pursuant to section 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the Act] on the basis of objective evidence.

[3] The determinative issue is the RAD’s error in basing its primary credibility finding on the applicant’s use of false documents to exit Cameroon, contrary to the principles in the jurisprudence, which the RAD then relied on to draw additional negative credibility inferences. As a result, the application for judicial review is allowed.
I. Background [4] The applicant is a citizen of Cameroon. He recounts that he is an active member of the Southern Cameroon National Council [SCNC], a political organization advocating for political independence for Southern Cameroon. Because of his involvement with the SCNC, he claims that he was arrested, detained and tortured by the police on several occasions. He fears death, persecution and torture upon return to Cameroon. In March 2014, aided by a smuggler and with false documents, he left Cameroon and travelled via France and Brazil to Canada and sought refugee protection.

[5] Upon arrival, he provided a false Cameroonian passport. When confronted by an immigration officer who had reason to doubt his identity, he disclosed that his name was Valantine Moboh Koffi. He had no documentation to support this identity and was detained until June 2014.

[6] While the applicant was in detention, the applicant’s mother and uncle sent additional documentation to Mr. Kamwa, a family friend in Canada, including the applicant’s birth certificate and National Identity Card. Mr. Kamwa submitted the documents to CBSA. The CBSA found that the birth certificate was unverifiable and the National Identity Card was probably counterfeit. The applicant acknowledged, after being presented with the card, that it was fraudulent.
II. The RPD Decision [7] The RPD found that the applicant had failed to meet the onus upon him to provide sufficient evidence to establish his identity.

[8] The RPD found that the applicant’s testimony regarding his identity was not credible. The RPD noted that the applicant was uncertain about the order of his names, as in Africa, first and last names are not differentiated, and found that the order of his name differed between the names provided at the RPD hearing, his other documents and his Basis of Claim form.

[9] The RPD found that the applicant’s explanation for failing to disclose his prior visa applications using the name “Gawum” was not reasonable, noting he could have amended his Basis of Claim form to be truthful. The RPD also found that it was not plausible that he had a fraudulent passport in the name “Gawum” which was coincidentally his girlfriend’s and child’s last name.

[10] The RPD placed little weight on the applicant’s birth certificate given the other documents on the record admitted to be fraudulent, the anomalies in the documents and the credibility concerns.
III. The RAD Decision [11] The applicant appealed to the RAD, seeking to rely on new evidence, in particular an affidavit from his uncle in Cameroon explaining that the fraudulent National Identity Card was sent without the applicant’s knowledge and an article on common practices regarding first and last names in Cameroon. He also requested an oral hearing.

[12] The RAD admitted the new evidence in accordance with subsection 110(4) of the Act.

[13] However, the RAD gave the affidavit of the applicant’s uncle little weight given that the applicant had repeatedly submitted fraudulent documents and his uncle had been the conduit for several of these fraudulent documents.

[14] The RAD accepted the applicant’s explanation for the inconsistencies in the order of his first and last names in documents on the record based on the article provided.

[15] The RAD denied the request for an oral hearing, noting that the new evidence could not independently establish the applicant’s identity and did not meet the test set out in subsection 110(6) to permit an oral hearing.

[16] The RAD noted that in accordance with Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799, [2014] 4 FCR 811 [Huruglica] it would conduct an independent assessment of the evidence.

[17] The RAD accepted that the different order of names in the applicant’s documentation cannot be used as an indicator of fraud, but found that the RPD did not err by inquiring into the reliability of the applicant’s documents given his propensity for relying on fraudulent documents.

[18] The RAD found that the RPD had erred by finding that it was implausible that the applicant’s US visa and his denied Canadian visa application used his girlfriend’s last name and were fraudulent. However, the RAD again found that the applicant’s repeated reliance on fraudulent documents in his interactions with the US and Canadian authorities exhibits his propensity to rely on such documents and assume a fraudulent identity and that this detracts from his credibility.

[19] The RAD also agreed with the RPD’s finding that the applicant did not readily admit his identity until confronted, which detracts from his credibility.

[20] With respect to the RPD’s rejection of several other supporting identity documents including his birth certificate, arrest warrants, SCNC membership card and a newspaper article noting his involvement in the SCNC, the RAD again noted that the applicant had acquired several fraudulent identity documents in his name with the assistance of his uncle.

[21] The RAD noted that refugee claimants may not be in a position to provide authentic identity documents. However, the RAD found that, in this case, it was open to the RPD, in light of the credibility concerns and the fraudulent National Identity Card, to look for more reliable and probative documents and to give the secondary identity documents little weight. The RAD noted the prevalence of fraudulent documents in Cameroon and concluded, based on the totality of evidence, that it would give the secondary documents little weight.

[22] The RAD rejected the applicant’s argument that he should not be held responsible for his uncle’s actions in sending him fraudulent documents which he had not previously seen, noting that the onus was on him to establish, with credible and trustworthy evidence, on a balance of probabilities, that he is who he says he is.

[23] The RAD concluded that the only potentially probative document regarding the applicant’s identity as Valantine Moboh Koffi, his National Identity Card, was fraudulent and that his birth certificate was unverifiable. Based on the totality of the evidence, the RAD found that he had not provided sufficient reliable and probative evidence to establish his identity on a balance of probabilities.

[24] The RAD further found that the RPD did not breach the applicant’s section 7 Charter rights by failing to conduct any assessment of his risk upon return to his home country. The RAD reached the same conclusion based on finding that the applicant’s identity had not been established and, therefore, it was not required to assess his risk.
IV. The Issues [25] The applicant argues that:
1. The RAD breached procedural fairness by making negative credibility findings without convening an oral hearing.
2. The RAD’s negative credibility findings were not reasonable; specifically, the RAD erred by drawing a negative credibility inference because the applicant fled from Cameroon using false documentation.
3. The RAD erred by failing to conduct an assessment, pursuant to section 97 of the Act, of the risk the applicant would face upon return to Cameroon.
V. The Standard of Review [26] Issues of procedural fairness are reviewed on the standard of correctness.

[27] The application of the law to the facts of the case, the RAD’s credibility findings and the RAD’s decision regarding the RPD’s credibility findings are reviewed on the standard of reasonableness (Dunsmuir v New Brunswick, 2008 SCC 9 at paras 53-54, [2008] 1 SCR 190 [Dunsmuir]).

[28] The reasonableness standard focuses on “the existence of justification, transparency and intelligibility within the decision-making process” and considers “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir at para 47).

[29] With respect to questions of credibility, the jurisprudence has generally established that the RAD may or should defer to the RPD because the RPD has heard the witnesses directly, has had an opportunity to probe their testimony or has had some advantage not enjoyed by the RAD; see, for example, Huruglica at para 55; Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 at para 39, [2014] FCJ No 1116 (QL); Nahal v Canada (Minister of Citizenship and Immigration), 2014 FC 1208 at para 25, [2014] FCJ No 1254 (QL).

[30] However, in Khachatourian v Canada (Minister of Citizenship and Immigration), 2015 FC 182 at paras 31-32, [2015] FCJ No 156 (QL), Justice Noël noted that the RAD should assume its appellate role and, therefore, the same level of deference may not be warranted with respect to credibility findings in an appeal as in a judicial review; an independent assessment or an analysis of the evidence would be necessary to permit some level of deference.

[31] In Balde v Canada (Minister of Citizenship and Immigration), 2015 FC 624 at para 23, [2015] FCJ No 641 (QL), Justice Mosley agreed, noting that: “The Court has been consistent that the RAD ought to defer to findings of fact or credibility made by the RPD but must also conduct its own analysis of those findings.”

[32] In the present case, the RAD did a bit of everything. The RAD stated that it conducted its own assessment of the evidence. The RAD deferred to and confirmed some of the RPD’s credibility findings. The RAD found two of the RPD’s credibility findings to be in error, yet supported the adverse inferences arising from those findings (for other reasons). The RAD also made its own credibility findings regarding the documentary evidence.

[33] On judicial review, the issue is whether the RAD’s credibility findings are reasonable. It is well settled that credibility findings of boards and tribunals are owed significant deference on judicial review, given that they are in the best position to assess the testimony and the evidence. However, in the present case, the RAD did not conduct an oral hearing and did not hear first-hand from the applicant. The RAD’s credibility findings are based on its assessment of the evidence on the record. Despite the deference generally owed, credibility findings are not immune from review and must meet the Dunsmuir standard.
VI. Analysis 1. The RAD did not breach its duty of procedural fairness [34] The applicant acknowledges that subsection 110(6) of the Act provides that the RAD may hold a hearing if certain conditions are met, but submits that the common law duty of procedural fairness continues to apply and an oral hearing should have been held to provide him with an opportunity to respond to the RAD’s credibility concerns and to know the case he had to meet.

[35] The general rule is set out in subsection 110(3) which provides that the RAD must proceed without an oral hearing. However, subsection 110(6) provides an exception where a hearing may be held where certain criteria are met. Even if those criteria are met, the RAD still has the discretion to decline to hold an oral hearing.

[36] The applicant interprets the exception to mean that when any of the evidence relied on by the RAD raises a serious credibility issue that is central to the decision and that, if accepted, would justify allowing or rejecting the refugee claim, the criteria are met. In my view, for the purposes of this case, it is not necessary to determine how the exception should be interpreted as it remains a discretionary provision.

[37] With respect to the RAD’s common law duty of procedural fairness, the applicant relies on Husian v Canada (Minister of Citizenship and Immigration), 2015 FC 684 at paras 9-10, [2015] FCJ No 687 (QL) [Husian], where Justice Hughes highlighted the pitfalls of the RAD making credibility findings, which are then open to review, noting at paras 9-10:

[9] We come to the basis for sending the matter back to the RAD for re-determination. Had the RAD simply reviewed the findings of the RPD as to the adequacy of the Applicant’s evidence and agreed with it, that would have ended the matter. It did not. For whatever reason, the RAD went on to give further reasons, based on its own review of the record, as to why the Applicant’s evidence was not to be believed. It held, at paragraph 43, that it was unable to locate any evidence to support the Applicant’s claim to also being a member of the Dhawarawayne clan. That was wrong; there is such evidence in the Responses to Information Requests. The comments by the RAD as to the differences in the spelling of the Applicant’s name in the US proceedings versus the Canadian proceedings is nonsense: of course, there will be differences where a different alphabet and language is in question such as Somali and English. There are other errors.

[10] The point is that if the RAD chooses to take a frolic and venture into the record to make further substantive findings, it should give some sort of notice to the parties and give them an opportunity to make submissions.

[38] Although the RAD did make credibility findings, unlike in Husian, the RAD did not ignore contradictory evidence on the record or make additional findings on issues unknown to the applicant.

[39] In these circumstances, the RAD was not required to hold an oral hearing. First, the statute is clear that an oral hearing is discretionary even when the criteria are met. Second, the RAD did not breach the common law duty of procedural fairness. The applicant was well aware that the only issue before the RAD was his identity and his use of fraudulent documents to establish his identity. It cannot be said that he did not know the case he had to meet or that he did not have an opportunity to respond to credibility concerns in his submissions to the RAD.

[40] However, as noted above, the RAD made credibility findings of its own, based on the documentary evidence and without hearing directly from the applicant. In my view, this has a bearing on the deference generally owed to some of those credibility findings in the context of a reasonableness review.
2. The RAD’s negative credibility findings were not reasonable [41] The applicant argues that refugees are often forced to flee using false documents and negative credibility inferences are not justified in such circumstances (Rasheed v Canada (Minister of Citizenship and Immigration), 2004 FC 587 at para 18, [2004] FCJ No 715 (QL) [Rasheed]; Gulamsakhi v Canada (Minister of Citizenship and Immigration), 2015 FC 105 at para 9, [2015] FCJ No 271 (QL) [Gulamsakhi]); The applicant submits that all the credibility findings of the RAD stem from his use of fraudulent documents to escape persecution in Cameroon and which he presented upon arrival to seek refugee protection in Canada. The RAD’s repeated references to his propensity to use fraudulent documents must be viewed in this context.

[42] As the applicant points out, the jurisprudence has cautioned against drawing negative credibility findings from the use of false documents where refugee claimants have little choice but to use such documents to leave their country.

## 13412:2 · paragraphs 38-39

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `df20193a1b35d45f64ba075a8d3de70bb702a28a322a00fe5041e32781e325f1`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13412:2:subtheme:1 · paragraphs 38-39

- Raw key terms: `court, above, afghan, against, applicant, attakora, based, because`
- Display key terms: `above, afghan, against, attakora, based, because`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: above, afghan, against, attakora, based, because Application context: This is partly because it is not uncommon for a person fleeing persecution to follow the instructions of the person(s) organizing their escape: Rasheed v Canada (Minister of Citizenship and Immigration), 2004 FC 587 at p Evidence spans paragraphs 38-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660894` offsets `690-698`; context: This is consistent with the Applicant’s evidence regarding the fate of her Afghan passport as outlined above.
- Evidence: `reasoning_application` cue `because` at chunk `4660894` offsets `420-427`; context: This is partly because it is not uncommon for a person fleeing persecution to follow the instructions of the person(s) organizing their escape: Rasheed v Canada (Minister of Citizenship and Immigration), 2004 FC 587 at para 18, citing Attakora.

#### Section text

[43] In Gulamsakhi the Court noted:

[9] Moreover, this Court has repeatedly cautioned against drawing negative conclusions based on the use of smugglers and forged documents to escape violence and persecution. Travelling on false documents or destroying travel documents is of very limited value as a determination of the claimant’s credibility: Attakora v Canada (Minister of Employment and Immigration) (1989), 99 NR 168 (FCA) [Attakora]. This is partly because it is not uncommon for a person fleeing persecution to follow the instructions of the person(s) organizing their escape: Rasheed v Canada (Minister of Citizenship and Immigration), 2004 FC 587 at para 18, citing Attakora. This is consistent with the Applicant’s evidence regarding the fate of her Afghan passport as outlined above.

## 13412:3 · paragraphs 40-58

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `90438b01602340f6c2fa17efe7108edc5b846dcf3d8f3ff8ea44e2bbc2ce90c3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13412:3:subtheme:1 · paragraphs 40-46

- Raw key terms: `documents, applicant, arrival, authenticity, false, fraudulent, immigration, obtain`
- Display key terms: `documents, arrival, authenticity, false, fraudulent, obtain`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: documents, arrival, authenticity, false, fraudulent, obtain Position/evidence statements: [45] The respondent argues that there is little evidence that the applicant was forced to use a false document to flee his home country. | [48] The respondent also submits that the RAD reasonably relied on the applicant’s delay in revealing his identity as detracting from his credibility. Evidence spans paragraphs 40-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4660896` offsets `502-509`; context: Second, whether a person has told the truth about his or her travel documents has little direct bearing on whether the person is indeed a refugee (Attakora v.
- Evidence: `party_position` cue `argues` at chunk `4660897` offsets `20-26`; context: [45] The respondent argues that there is little evidence that the applicant was forced to use a false document to flee his home country.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660897` offsets `48-56`; context: [45] The respondent argues that there is little evidence that the applicant was forced to use a false document to flee his home country.
- Evidence: `counterargument_limitation` cue `However` at chunk `4660897` offsets `137-144`; context: However, the applicant’s narrative refers to his attempts to obtain documents to flee the country and his ultimate reliance on a smuggler to secure his travel out of Cameroon with a false passport, which he presented on arrival.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660899` offsets `95-103`; context: [7] […] Specifically, it was open to the board to consider the authenticity of the documentary evidence, the consistency of Mr.
- Evidence: `evidence_fact` cue `testimony` at chunk `4660900` offsets `425-434`; context: In addition, as is apparent from the passage above, the RPD noted inconsistencies in oral testimony and the applicants’ delay in claiming protection.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4660900` offsets `485-493`; context: Although there is no dispute that the RAD should scrutinise the authenticity of documents, the facts in Sertkaya differ from the present case.
- Evidence: `party_position` cue `submits` at chunk `4660901` offsets `25-32`; context: [48] The respondent also submits that the RAD reasonably relied on the applicant’s delay in revealing his identity as detracting from his credibility.
- Evidence: `evidence_fact` cue `found that` at chunk `4660901` offsets `215-225`; context: The RAD found that the applicant did not acknowledge his use of a false passport until confronted while in detention.
- Evidence: `counterargument_limitation` cue `However` at chunk `4660901` offsets `151-158`; context: However, the RAD appears to have overstated this delay.

#### 13412:3:subtheme:2 · paragraphs 47-50

- Raw key terms: `applicant, country, documents, given, identity, little, secondary, weight`
- Display key terms: `country, documents, given, identity, little, secondary, weight`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: country, documents, given, identity, little, secondary, weight Rule/authority context: This ignores the principle from the jurisprudence that negative inferences should not be drawn from the use of false documents to flee a country or that the same false documents would be presented by an applicant upon ar Application context: Instead of acknowledging that negative inferences should not be drawn based on the use of false documents to flee a country, it relies on the use of the false documents to bolster its characterisation of the applicant ha Evidence spans paragraphs 47-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4660902` offsets `512-525`; context: This ignores the principle from the jurisprudence that negative inferences should not be drawn from the use of false documents to flee a country or that the same false documents would be presented by an applicant upon arrival.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660903` offsets `58-66`; context: [50] The RAD noted that it considered the totality of the evidence and clearly there were fraudulent documents among the identity documents provided by the applicant.
- Evidence: `counterargument_limitation` cue `However` at chunk `4660903` offsets `167-174`; context: However, the RAD accepted that the order of names on some of the identity documents was not an indicator of fraud, yet it appears that the RAD continued to give those documents little weight.
- Evidence: `reasoning_application` cue `because` at chunk `4660904` offsets `348-355`; context: Instead of acknowledging that negative inferences should not be drawn based on the use of false documents to flee a country, it relies on the use of the false documents to bolster its characterisation of the applicant having a propensity to use fraudulent documents and, in turn, to agree with the RPD that because of that propensity, the secondary documents should be given little weight.

#### 13412:3:subtheme:3 · paragraphs 51-54

- Raw key terms: `identity, applicant, canada, citizenship, establish, immigration, minister, para`
- Display key terms: `identity, establish, para`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: identity, establish, para Evidence spans paragraphs 51-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4660906` offsets `289-296`; context: [53] In Jin v Canada (Minister of Citizenship and Immigration), 2006 FC 126 at para 13, [2006] FCJ No 181 (QL), Justice Barnes highlighted that identity is “a critical threshold decision for the Board” and that section 106 requires that the Board to determine, as a matter of credibility, whether the applicant has acceptable documentation to establish their identity.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660909` offsets `800-808`; context: Yet, he is still required to establish his personal identity with reliable and probative evidence in order to have his claim for protection determined.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4660909` offsets `235-243`; context: Although the RAD states that he is a citizen of Cameroon, the RAD was not satisfied that he has established his personal identity.

#### 13412:3:subtheme:4 · paragraphs 55-56

- Raw key terms: `applicant, assessed, cameroon, given, prra, risk, accordance, acws`
- Display key terms: `assessed, cameroon, given, prra, risk, accordance, acws`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: assessed, cameroon, given, prra, risk, accordance, acws Position/evidence statements: Assessment of the applicant’s risk pursuant to section 97 [57] Alternatively, the applicant submits that regardless of the RAD’s findings that he had not established his personal identity, the RAD should have assessed hi Rule/authority context: [56] The negative credibility finding arising from his use of false documents to exit Cameroon was unreasonable as it is not in accordance with the jurisprudence. Evidence spans paragraphs 55-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4660910` offsets `976-984`; context: For example, in Chen v Canada (Minister of Citizenship and Immigration), 2009 FC 379 at para 55, 176 ACWS (3d) 1120 [Chen], the Court found that PRRA officers are obliged to proceed beyond the question of personal identity where the national origin has been established and to assess country conditions and risk under section 97.
- Evidence: `party_position` cue `submits` at chunk `4660910` offsets `459-466`; context: Assessment of the applicant’s risk pursuant to section 97 [57] Alternatively, the applicant submits that regardless of the RAD’s findings that he had not established his personal identity, the RAD should have assessed his need for protection pursuant to section 97 based on the information that can be ascertained.
- Evidence: `evidence_fact` cue `found that` at chunk `4660910` offsets `917-927`; context: For example, in Chen v Canada (Minister of Citizenship and Immigration), 2009 FC 379 at para 55, 176 ACWS (3d) 1120 [Chen], the Court found that PRRA officers are obliged to proceed beyond the question of personal identity where the national origin has been established and to assess country conditions and risk under section 97.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4660910` offsets `148-161`; context: [56] The negative credibility finding arising from his use of false documents to exit Cameroon was unreasonable as it is not in accordance with the jurisprudence.

#### 13412:3:subtheme:5 · paragraphs 57-58

- Raw key terms: `allowed, appeal, applicant, application, appropriate, assessed, assessment, cannot`
- Display key terms: `allowed, appropriate, assessed, assessment, cannot`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: allowed, appropriate, assessed, assessment, cannot Operative outcome context: The application for judicial review is allowed and the applicant’s appeal of the RPD decision shall be re-determined by a different panel of the RAD. Evidence spans paragraphs 57-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4660912` offsets `22-27`; context: [59] In my view, this issue need not be determined, given that the RAD must re-determine the appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4660912` offsets `296-304`; context: The issue of whether a section 97 risk faced by an applicant who cannot establish their personal identity, but has established their national origin, should be assessed, as well as the objective evidence necessary to conduct such an assessment, remains to be determined in the appropriate case.
- Evidence: `disposition` cue `allowed` at chunk `4660912` offsets `478-485`; context: The application for judicial review is allowed and the applicant’s appeal of the RPD decision shall be re-determined by a different panel of the RAD.

#### Section text

[44] In Rasheed the Court noted:

[18] Where a claimant travels on false documents, destroys travel documents or lies about them upon arrival following an agent’s instructions, it has been held to be peripheral and of very limited value as a determination of general credibility. First, it is not uncommon for those who are fleeing from persecution not to have regular travel documents and, as a result of their fears and vulnerability, simply to act in accordance with the instructions of the agent who organized their escape. Second, whether a person has told the truth about his or her travel documents has little direct bearing on whether the person is indeed a refugee (Attakora v. Canada (Minister of Employment and Immigration), [1989] F.C.J. No. 444 (C.A) (QL); and Takhar v. Canada (Minister of Citizenship and Immigration), [1999] F.C.J. No. 240 at para. 14 (T.D.) (QL).

[45] The respondent argues that there is little evidence that the applicant was forced to use a false document to flee his home country. However, the applicant’s narrative refers to his attempts to obtain documents to flee the country and his ultimate reliance on a smuggler to secure his travel out of Cameroon with a false passport, which he presented on arrival. In my view, this falls within the category of cases where a negative inference should not be drawn from the use of false documents to flee.

[46] The respondent relies on Sertkaya v Canada (Minister of Citizenship and Immigration), 2004 FC 734 at para 7, 131 ACWS (3d) 729 [Sertkaya] to support its position that the RAD reasonably considered the authenticity of documents and the ability to obtain fraudulent documents in Cameroon:

[7] […] Specifically, it was open to the board to consider the authenticity of the documentary evidence, the consistency of Mr. Sertkaya’s story, the ability of the family to obtain and use fraudulent documents and the failure of the family to seek asylum during the five months spent in the United States. The applicants have failed to establish that any of these findings were in error and, in my view, they are sufficient to support the RPD’s findings. The error with regard to HADEP membership is not material to the overall conclusion.

[47] In Sertkaya, the RPD made a finding that it was improbable that fraudulent documents would have been required for the family to leave Turkey or that they would have been able to pass through passport control with such documents and that other documents were not authentic (a letter allegedly written by the applicant’s employer). In addition, as is apparent from the passage above, the RPD noted inconsistencies in oral testimony and the applicants’ delay in claiming protection. Although there is no dispute that the RAD should scrutinise the authenticity of documents, the facts in Sertkaya differ from the present case.

[48] The respondent also submits that the RAD reasonably relied on the applicant’s delay in revealing his identity as detracting from his credibility. However, the RAD appears to have overstated this delay. The RAD found that the applicant did not acknowledge his use of a false passport until confronted while in detention. The record shows that the applicant presented the false passport to an immigration officer upon arrival, but upon questioning by the officer, revealed his identity as Valantine Moboh Koffi without delay.

[49] Unlike Sertkaya, the RPD did not make any finding that the applicant did not need to rely on false documents to flee Cameroon. The RAD simply noted that “sometimes the refugee claimants cannot provide authentic probative identity documents.” The RAD went on to find that “[i]n the presence of credibility concerns” it was open to the RPD to look for more reliable documents to establish his identity and agreed that the secondary documents should be given little weight. This ignores the principle from the jurisprudence that negative inferences should not be drawn from the use of false documents to flee a country or that the same false documents would be presented by an applicant upon arrival.

[50] The RAD noted that it considered the totality of the evidence and clearly there were fraudulent documents among the identity documents provided by the applicant. However, the RAD accepted that the order of names on some of the identity documents was not an indicator of fraud, yet it appears that the RAD continued to give those documents little weight. The RAD also found that the applicant’s use of his girlfriend’s last name to obtain a US visa and to seek a Canadian visa was plausible, yet it did not acknowledge that these documents were intended to assist him to leave the country. In addition, it appears that the RAD did not independently assess the secondary documents at all; rather, it concurred with the RPD that these documents should be given little weight due to the applicant’s propensity to provide fraudulent documents.

[51] The RAD’s reasoning is problematic. Instead of acknowledging that negative inferences should not be drawn based on the use of false documents to flee a country, it relies on the use of the false documents to bolster its characterisation of the applicant having a propensity to use fraudulent documents and, in turn, to agree with the RPD that because of that propensity, the secondary documents should be given little weight.

[52] On the other hand, the legislation is clear that a refugee claimant must establish their identity.

[53] In Jin v Canada (Minister of Citizenship and Immigration), 2006 FC 126 at para 13, [2006] FCJ No 181 (QL), Justice Barnes highlighted that identity is “a critical threshold decision for the Board” and that section 106 requires that the Board to determine, as a matter of credibility, whether the applicant has acceptable documentation to establish their identity.

[54] In Su v Canada (Minister of Citizenship and Immigration), 2012 FC 743 at para 4, [2012] FCJ No 902 (QL), Justice Snider noted that the burden on a refugee claimant to establish their identity is a high one “as it should be” and, at para 3:

[3] Proof of identity is a pre-requisite for a person claiming refugee protection as without it there can “be no sound basis for testing or verifying the claims of persecution or, indeed for determining the Applicant’s true nationality” (Jin v Canada (Minister of Citizenship and Immigration), 2006 FC 126 at para 26, [2006] FCJ No 181 (QL); see also Liu v Canada (Minister of Citizenship and Immigration), 2007 FC 831 at para 18, [2007] FCJ No 1101 (QL)).

[55] Without diminishing the importance of establishing identity, given that it is not possible to assess an applicant’s claim for protection until their identity is established, this applicant finds himself in a challenging position. Although the RAD states that he is a citizen of Cameroon, the RAD was not satisfied that he has established his personal identity. He used false documents to flee and admits that a false National Identity Card was provided by his uncle, who also previously assisted him to obtain documents to flee. His secondary documents were given little weight largely due to the fraudulent primary documents and the RAD’s characterisation of his “propensity” to use fraudulent documents. Yet, he is still required to establish his personal identity with reliable and probative evidence in order to have his claim for protection determined.

[56] The negative credibility finding arising from his use of false documents to exit Cameroon was unreasonable as it is not in accordance with the jurisprudence. This finding then significantly influenced all the other credibility findings made by the RAD given the RAD’s characterisation of the applicant as a person with a propensity for using false documents.
3. Assessment of the applicant’s risk pursuant to section 97 [57] Alternatively, the applicant submits that regardless of the RAD’s findings that he had not established his personal identity, the RAD should have assessed his need for protection pursuant to section 97 based on the information that can be ascertained. The applicant draws an analogy to PRRA determinations where risk is assessed regardless of identity. For example, in Chen v Canada (Minister of Citizenship and Immigration), 2009 FC 379 at para 55, 176 ACWS (3d) 1120 [Chen], the Court found that PRRA officers are obliged to proceed beyond the question of personal identity where the national origin has been established and to assess country conditions and risk under section 97.

[58] The applicant points out that his risk has not been assessed at all and, given the limitations on his eligibility for a PRRA, he may not have his risk assessed before possible removal to Cameroon.

[59] In my view, this issue need not be determined, given that the RAD must re-determine the appeal. The issue of whether a section 97 risk faced by an applicant who cannot establish their personal identity, but has established their national origin, should be assessed, as well as the objective evidence necessary to conduct such an assessment, remains to be determined in the appropriate case.
JUDGMENT
THIS COURT’S JUDGMENT is that:
1. The application for judicial review is allowed and the applicant’s appeal of the RPD decision shall be re-determined by a different panel of the RAD.
2. No question is proposed for certification.
“Catherine M. Kane”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-2285-15
STYLE OF CAUSE:
VALANTINE MOBOH KOFFI v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
December 17, 2015


## 13412:4 · paragraphs 59-59

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3c2cf1de6cddebfa6e0f12aa054566474712a201f46870f0c7b047a2f0dd152a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13412:4:subtheme:1 · paragraphs 59-59

- Raw key terms: `alyssa, appearances, applicant, attorney, barristers, canada, dated, deputy`
- Display key terms: `alyssa, barristers, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alyssa, barristers, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 59-59. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND reasons:
KANE J.
DATED:
january 4, 2016
APPEARANCES:
Alyssa Manning
For The Applicant
Teresa Ramnarine
For The Respondent
SOLICITORS OF RECORD:
Refugee Law Office
Barristers and Solicitors
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
