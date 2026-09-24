# Discussion Units: case 1439

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **50**
- Continuity pairs: **49**
- Discussion Units: **3**
- Paragraph source hashes: **50**
- Sub-themes: **12**

## 1439:1 · paragraphs 0-3

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `08b1afb9805ce7214a60b091d7520d2bfe9c01179862c58b86b02f36b79507c6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1439:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `review, azenabor, based, concerns, decision, documents, evidence, filed`
- Display key terms: `review, azenabor, based, concerns, documents, filed`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, reasoning_application Display terms: review, azenabor, based, concerns, documents, filed Application context: [2] I conclude that the RAD’s decision was fair and reasonable. | [3] The application for judicial review is therefore dismissed. Operative outcome context: [3] The application for judicial review is therefore dismissed. Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4140487` offsets `203-211`; context: They argue the RAD’s finding that they filed fraudulent evidence was unreasonable since it was based on microscopic concerns about the documents and ignored available information about authentication of Nigerian affidavits.
- Evidence: `evidence_fact` cue `evidence` at chunk `4140488` offsets `332-340`; context: However, the RAD relied on a series of reasonable and clearly identified concerns that were grounded in the evidence and were based on its review of the original documents.
- Evidence: `reasoning_application` cue `conclude` at chunk `4140488` offsets `6-14`; context: [2] I conclude that the RAD’s decision was fair and reasonable.
- Evidence: `counterargument_limitation` cue `However` at chunk `4140488` offsets `224-231`; context: However, the RAD relied on a series of reasonable and clearly identified concerns that were grounded in the evidence and were based on its review of the original documents.
- Evidence: `reasoning_application` cue `therefore` at chunk `4140489` offsets `43-52`; context: [3] The application for judicial review is therefore dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4140489` offsets `53-62`; context: [3] The application for judicial review is therefore dismissed.

#### Section text

Azenabor v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2020-12-16
Neutral citation
2020 FC 1160
File numbers
IMM-5214-19
Decision Content
Date: 20201216
Docket: IMM-5214-19
Citation: 2020 FC 1160
Ottawa, Ontario, December 16, 2020
PRESENT: Mr. Justice McHaffie
BETWEEN:
OGECHUKWU AZENABOR
MIRABELLA EBEHIREMEN IGHODARO-AZENABOR
OSEDEBAMEN MICHAEL IGHODARO
Applicants
and
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Overview

[1] Ms. Ogechukwu Azenabor and her two children seek judicial review of the dismissal of their refugee claim by the Refugee Appeal Division (RAD). They argue the RAD’s finding that they filed fraudulent evidence was unreasonable since it was based on microscopic concerns about the documents and ignored available information about authentication of Nigerian affidavits. They also say that it was unfair for the RAD to discount a police report based on concerns they did not have the chance to respond to, and that the RAD improperly discounted the affidavit of Ms. Azenabor’s husband.

[2] I conclude that the RAD’s decision was fair and reasonable. The concerns with the documents identified by the RAD may not have individually been sufficient to find the documents fraudulent, as the RAD itself recognized. However, the RAD relied on a series of reasonable and clearly identified concerns that were grounded in the evidence and were based on its review of the original documents. The RAD was also not required to give greater or more specific notice to the Azenabors about each of its ultimate concerns with the authenticity of the police report before concluding that the document was not genuine. The RAD’s finding that the Azenabors had filed fraudulent documents, and its consequent conclusion that the Azenabors were not Convention refugees or persons in need of protection within the meaning of sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], was reasonable.

[3] The application for judicial review is therefore dismissed.


## 1439:2 · paragraphs 4-47

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `590ddc0f8450482c827b75d5f6f0319c3c8ba28a0f6363069f16658116a3ed24`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1439:2:subtheme:1 · paragraphs 4-5

- Raw key terms: `issues, affidavit, affidavits, application, arguments, authenticity, azenabor, azenabors`
- Display key terms: `issues, affidavit, affidavits, arguments, authenticity, azenabor, azenabors`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: issues, affidavit, affidavits, arguments, authenticity, azenabor, azenabors Position/evidence statements: [4] The Azenabors’ arguments on this application raise three main issues: Did the RAD err in its determination that the affidavits submitted by the Azenabors were fraudulent? Evidence spans paragraphs 4-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4140490` offsets `66-72`; context: [4] The Azenabors’ arguments on this application raise three main issues:
Did the RAD err in its determination that the affidavits submitted by the Azenabors were fraudulent?
- Evidence: `party_position` cue `submitted` at chunk `4140490` offsets `131-140`; context: [4] The Azenabors’ arguments on this application raise three main issues:
Did the RAD err in its determination that the affidavits submitted by the Azenabors were fraudulent?
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140490` offsets `389-398`; context: Azenabor’s affidavit?

#### 1439:2:subtheme:2 · paragraphs 6-7

- Raw key terms: `canada, citizenship, court, decision, immigration, justified, minister, para`
- Display key terms: `justified, para`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: justified, para Rule/authority context: This does not change the reasonableness standard of review, but emphasizes that within the reasonableness framework, decision makers are given considerable latitude in making credibility findings, which should not be dis Evidence spans paragraphs 6-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4140491` offsets `61-67`; context: [5] The parties are agreed that the first and third of these issues are reviewable on the reasonableness standard: Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at paras 16–17, 23–25.
- Evidence: `evidence_fact` cue `evidence` at chunk `4140492` offsets `179-187`; context: The Supreme Court in Vavilov reiterated that reviewing courts should not reweigh or reassess evidence: Vavilov at para 125.
- Evidence: `governing_rule` cue `standard of review` at chunk `4140492` offsets `397-415`; context: This does not change the reasonableness standard of review, but emphasizes that within the reasonableness framework, decision makers are given considerable latitude in making credibility findings, which should not be disturbed lightly: Amador Ordonez v Canada (Citizenship and Immigration), 2019 FC 1216 at para 6; Vavilov at paras 88–90.
- Evidence: `counterargument_limitation` cue `but` at chunk `4140492` offsets `417-420`; context: This does not change the reasonableness standard of review, but emphasizes that within the reasonableness framework, decision makers are given considerable latitude in making credibility findings, which should not be disturbed lightly: Amador Ordonez v Canada (Citizenship and Immigration), 2019 FC 1216 at para 6; Vavilov at paras 88–90.

#### 1439:2:subtheme:3 · paragraphs 8-13

- Raw key terms: `azenabors, evidence, nigeria, refugee, affidavits, azenabor, documentary, documents`
- Display key terms: `azenabors, nigeria, refugee, affidavits, azenabor, documentary, documents`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: azenabors, nigeria, refugee, affidavits, azenabor, documentary, documents Position/evidence statements: The Azenabors challenged these findings on appeal to the RAD and argued that the RPD had failed to consider the documentary evidence submitted. Rule/authority context: This standard is best reflected in the correctness standard, although strictly speaking it does not involve the application of a standard of review: Canadian Pacific at para 54; Canada (Citizenship and Immigration) v Kho Application context: [7] The second issue is a matter of procedural fairness, and is therefore reviewed on a “fairness” standard, that is to say, by assessing whether the procedure was fair in all the circumstances: Canadian Pacific Railway  Evidence spans paragraphs 8-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4140493` offsets `15-20`; context: [7] The second issue is a matter of procedural fairness, and is therefore reviewed on a “fairness” standard, that is to say, by assessing whether the procedure was fair in all the circumstances: Canadian Pacific Railway Company v Canada (Attorney General), 2018 FCA 69 at para 54.
- Evidence: `evidence_fact` cue `evidence` at chunk `4140493` offsets `759-767`; context: The RAD’s Conclusion Regarding Fraudulent Documents was Reasonable
(1) The Azenabors’ documentary evidence
- Evidence: `governing_rule` cue `standard of review` at chunk `4140493` offsets `410-428`; context: This standard is best reflected in the correctness standard, although strictly speaking it does not involve the application of a standard of review: Canadian Pacific at para 54; Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 43; Canadian Association of Refugee Lawyers v Canada (Immigration, Refugees and Citizenship), 2020 FCA 196 at para 35.
- Evidence: `reasoning_application` cue `therefore` at chunk `4140493` offsets `64-73`; context: [7] The second issue is a matter of procedural fairness, and is therefore reviewed on a “fairness” standard, that is to say, by assessing whether the procedure was fair in all the circumstances: Canadian Pacific Railway Company v Canada (Attorney General), 2018 FCA 69 at para 54.
- Evidence: `counterargument_limitation` cue `although` at chunk `4140493` offsets `342-350`; context: This standard is best reflected in the correctness standard, although strictly speaking it does not involve the application of a standard of review: Canadian Pacific at para 54; Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 43; Canadian Association of Refugee Lawyers v Canada (Immigration, Refugees and Citizenship), 2020 FCA 196 at para 35.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140495` offsets `86-95`; context: [9] The Azenabors filed a number of documents in support of their claim, including an affidavit from Mr.
- Evidence: `party_position` cue `argued` at chunk `4140496` offsets `204-210`; context: The Azenabors challenged these findings on appeal to the RAD and argued that the RPD had failed to consider the documentary evidence submitted.
- Evidence: `evidence_fact` cue `testimony` at chunk `4140496` offsets `128-137`; context: Azenabor based on three aspects of her testimony.
- Evidence: `evidence_fact` cue `evidence` at chunk `4140497` offsets `106-114`; context: [11] During the course of their review, the RAD had concerns about a number of aspects of the documentary evidence, including the affidavits and the police report, which had not been raised by the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `4140498` offsets `710-718`; context: The RAD accepted these documents for consideration, although it did not accept certain factual statements made in the submission in the absence of any evidence filed to support them.
- Evidence: `counterargument_limitation` cue `although` at chunk `4140498` offsets `611-619`; context: The RAD accepted these documents for consideration, although it did not accept certain factual statements made in the submission in the absence of any evidence filed to support them.

#### 1439:2:subtheme:4 · paragraphs 14-17

- Raw key terms: `documents, azenabors, evidence, filed, fraudulent, genuine, testimony, affidavits`
- Display key terms: `documents, azenabors, filed, fraudulent, genuine, testimony, affidavits`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: documents, azenabors, filed, fraudulent, genuine, testimony, affidavits Position/evidence statements: Azenabor’s oral testimony, this does not mean that the RAD accepted her evidence to be credible, as the Azenabors claim. Rule/authority context: ” These included: the seal on one of the affidavits was “very clearly a colour photocopy which has been cut out and stuck on the affidavit as opposed to a genuine seal,” a conclusion the RAD reached on the basis of revie Application context: The RAD therefore did not rely on any particular findings arising from inconsistencies or implausibilities in Ms. | [14] In each case, the RAD referred to the identified concerns with the documents, which it considered “along with the prevalence of fraudulent documents in Nigeria” to conclude that the documents were not genuine on a b Evidence spans paragraphs 14-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4140499` offsets `881-887`; context: ” These included:
the seal on one of the affidavits was “very clearly a colour photocopy which has been cut out and stuck on the affidavit as opposed to a genuine seal,” a conclusion the RAD reached on the basis of review of the original affidavit;
another of the affidavits had three issues: (i) it identifies the deponent as living in Lagos, when the Azenabors alleged that she lived in Port Harcourt; (ii) the page where the affidavit was signed was in a different font than the first page, raising concerns that the two pages do not have the same provenance; and (iii) the affiant attached a work identification badge that had typographical errors, including listing the business address as being in “Portcourt” rather than “Port Harcourt”;
a further affidavit had two issues: (i) the stamp on the affidavit did not appear on the photograph attached to the affidavit nor underneath it and there was no evidence that the stamp was ever on the photo; and (ii) the affidavit identified the affiant as living in Lagos, while the Azenabors had alleged that she lived in Abuja;
the final two affidavits (i) attached photographs of the affiants, as required for affidavits in Lagos State, but the commissioner’s stamp on the top of each affidavit was placed under the photographs; and (ii) had identical title and signature blocks; and
the police report, which included the title “Crime Diary Extract,” did not conform with the information in the NDP about the availability or format of such documents, did not have the watermark expected for Lagos State police reports, and a number of other identified irregularities.
- Evidence: `evidence_fact` cue `testimony` at chunk `4140499` offsets `251-260`; context: Azenabor’s oral testimony.
- Evidence: `governing_rule` cue `under` at chunk `4140499` offsets `1851-1856`; context: ” These included:
the seal on one of the affidavits was “very clearly a colour photocopy which has been cut out and stuck on the affidavit as opposed to a genuine seal,” a conclusion the RAD reached on the basis of review of the original affidavit;
another of the affidavits had three issues: (i) it identifies the deponent as living in Lagos, when the Azenabors alleged that she lived in Port Harcourt; (ii) the page where the affidavit was signed was in a different font than the first page, raising concerns that the two pages do not have the same provenance; and (iii) the affiant attached a work identification badge that had typographical errors, including listing the business address as being in “Portcourt” rather than “Port Harcourt”;
a further affidavit had two issues: (i) the stamp on the affidavit did not appear on the photograph attached to the affidavit nor underneath it and there was no evidence that the stamp was ever on the photo; and (ii) the affidavit identified the affiant as living in Lagos, while the Azenabors had alleged that she lived in Abuja;
the final two affidavits (i) attached photographs of the affiants, as required for affidavits in Lagos State, but the commissioner’s stamp on the top of each affidavit was placed under the photographs; and (ii) had identical title and signature blocks; and
the police report, which included the title “Crime Diary Extract,” did not conform with the information in the NDP about the availability or format of such documents, did not have the watermark expected for Lagos State police reports, and a number of other identified irregularities.
- Evidence: `reasoning_application` cue `therefore` at chunk `4140499` offsets `129-138`; context: The RAD therefore did not rely on any particular findings arising from inconsistencies or implausibilities in Ms.
- Evidence: `counterargument_limitation` cue `However` at chunk `4140499` offsets `262-269`; context: However, it concluded that the documents from Nigeria the Azenabors filed—the five affidavits and the police report—were fraudulent, and that the Azenabors therefore lacked credibility.
- Evidence: `issue` cue `issue` at chunk `4140500` offsets `334-339`; context: Having reviewed each of the documents, the RAD reached the following conclusion:
Any one issue with any one of the above-mentioned documents would not be sufficient for me to conclude that the documents were not genuine.
- Evidence: `evidence_fact` cue `testimony` at chunk `4140500` offsets `786-795`; context: Accordingly, I place no weight on the testimony of the Principal Appellant.
- Evidence: `reasoning_application` cue `conclude` at chunk `4140500` offsets `169-177`; context: [14] In each case, the RAD referred to the identified concerns with the documents, which it considered “along with the prevalence of fraudulent documents in Nigeria” to conclude that the documents were not genuine on a balance of probabilities.
- Evidence: `counterargument_limitation` cue `However` at chunk `4140500` offsets `466-473`; context: However, taking all of the issues with all of the documents cumulatively, I find, on a balance of probabilities, the Appellants submitted six documents which are not genuine.
- Evidence: `party_position` cue `claim` at chunk `4140501` offsets `264-269`; context: Azenabor’s oral testimony, this does not mean that the RAD accepted her evidence to be credible, as the Azenabors claim.
- Evidence: `evidence_fact` cue `testimony` at chunk `4140501` offsets `166-175`; context: Azenabor’s oral testimony, this does not mean that the RAD accepted her evidence to be credible, as the Azenabors claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4140502` offsets `476-484`; context: They note that the Federal Court of Appeal has cautioned against being overly “microscopic” in analyzing the evidence of refugee claimants: Attakora v Canada (Minister of Employment & Immigration), [1989] FCJ No 444 (CA) at para 9.

#### 1439:2:subtheme:5 · paragraphs 18-20

- Raw key terms: `affidavits, azenabors, verification, affidavit, assistant, authorities, genuineness, nigeria`
- Display key terms: `affidavits, azenabors, verification, affidavit, assistant, authorities, genuineness, nigeria`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: affidavits, azenabors, verification, affidavit, assistant, authorities, genuineness, nigeria Position/evidence statements: I conclude that the RAD articulated reasonable grounds for its findings that the documents submitted were not genuine, and thus for finding Ms. Application context: I conclude that the RAD articulated reasonable grounds for its findings that the documents submitted were not genuine, and thus for finding Ms. Evidence spans paragraphs 18-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submitted` at chunk `4140503` offsets `165-174`; context: I conclude that the RAD articulated reasonable grounds for its findings that the documents submitted were not genuine, and thus for finding Ms.
- Evidence: `reasoning_application` cue `conclude` at chunk `4140503` offsets `76-84`; context: I conclude that the RAD articulated reasonable grounds for its findings that the documents submitted were not genuine, and thus for finding Ms.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4140504` offsets `274-283`; context: 2 in the NDP for Nigeria [the Affidavit RIR].
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4140505` offsets `44-53`; context: [19] The Azenabors point to passages in the Affidavit RIR that state that in Nigeria, authenticity of an affidavit is verified by checking the records of the authority who administered the affidavit.

#### 1439:2:subtheme:6 · paragraphs 21-28

- Raw key terms: `affidavit, authenticity, affidavits, azenabors, cannot, court, appearance, based`
- Display key terms: `affidavit, authenticity, affidavits, azenabors, cannot, appearance, based`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: affidavit, authenticity, affidavits, azenabors, cannot, appearance, based Position/evidence statements: ” They argue since a seal does not establish an affidavit’s authenticity, it was wrong for the RAD to rely on the appearance of the seal on one of the affidavits. Rule/authority context: As the Minister points out, the onus is on a refugee claimant to demonstrate through credible evidence that they meet the definitions of a Convention refugee or a person in need of protection under section 96 or 97 of th Application context: The fact that a fraudulent affidavit may have what appears to be a genuine seal does not mean that the RAD cannot conclude that an affidavit with an apparently fraudulent seal is fraudulent. | There is therefore no possible way for the Court to assess the Azenabors’ argument that the RAD’s conclusion that the seal was apparently simply a colour photocopy was unreasonable. Evidence spans paragraphs 21-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4140506` offsets `854-859`; context: In any event, I cannot accept the Azenabors’ submission on this issue for three reasons.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4140506` offsets `594-603`; context: While the Azenabors correctly note that they presented the Affidavit RIR to the RAD and made arguments on it, the elements of the Affidavit RIR they relied on pertained to the formalities of affidavits, not the RAD’s ability to assess their authenticity.
- Evidence: `evidence_fact` cue `evidence` at chunk `4140507` offsets `48-56`; context: [21] First, I do not read the country condition evidence as indicating that it is never possible, either as a practical matter or as a matter of Nigerian law, to find an affidavit inauthentic based on its facial features.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4140508` offsets `61-70`; context: [22] In context, I cannot take this or other passages in the Affidavit RIR to indicate that an affidavit may not show itself to be inauthentic based on elements of its appearance or contents, even without conducting a verification with the notary public or court registry.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140509` offsets `99-108`; context: [23] Second, even if Nigerian authorities say it can be difficult to verify the authenticity of an affidavit by a facial assessment, this cannot mean that the RAD is precluded from making an assessment of the authenticity of the evidence before it based on their expertise, judgment, and reference to the country condition information.
- Evidence: `evidence_fact` cue `evidence` at chunk `4140510` offsets `289-297`; context: As the Minister points out, the onus is on a refugee claimant to demonstrate through credible evidence that they meet the definitions of a Convention refugee or a person in need of protection under section 96 or 97 of the IRPA: Németh v Canada (Justice), 2010 SCC 56 at para 98; Boateng v Canada (Minister of Citizenship and Immigration), 2003 FCT 632 at para 9.
- Evidence: `governing_rule` cue `under` at chunk `4140510` offsets `387-392`; context: As the Minister points out, the onus is on a refugee claimant to demonstrate through credible evidence that they meet the definitions of a Convention refugee or a person in need of protection under section 96 or 97 of the IRPA: Németh v Canada (Justice), 2010 SCC 56 at para 98; Boateng v Canada (Minister of Citizenship and Immigration), 2003 FCT 632 at para 9.
- Evidence: `party_position` cue `argue` at chunk `4140511` offsets `228-233`; context: ” They argue since a seal does not establish an affidavit’s authenticity, it was wrong for the RAD to rely on the appearance of the seal on one of the affidavits.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4140511` offsets `50-59`; context: [25] The Azenabors next point to a passage in the Affidavit RIR that quotes the Assistant Superintendent as noting that “the seal does not establish [an affidavit’s] authenticity as all fake ones also do carry [the] seal.
- Evidence: `reasoning_application` cue `conclude` at chunk `4140511` offsets `517-525`; context: The fact that a fraudulent affidavit may have what appears to be a genuine seal does not mean that the RAD cannot conclude that an affidavit with an apparently fraudulent seal is fraudulent.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140512` offsets `99-108`; context: [26] The Azenabors also argued that the RAD’s conclusion regarding the quality of the seal on this affidavit was unreasonable, asserting that review of the original, which had been returned to the Azenabors, was at odds with the RAD’s conclusions.
- Evidence: `reasoning_application` cue `therefore` at chunk `4140512` offsets `398-407`; context: There is therefore no possible way for the Court to assess the Azenabors’ argument that the RAD’s conclusion that the seal was apparently simply a colour photocopy was unreasonable.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4140513` offsets `9-18`; context: [27] The Affidavit RIR indicates that the Federal High Courts in Nigeria require the deponent to attach two copies of a passport-sized photograph to the affidavit, and that notary publics in Lagos state similarly require a passport photo to be affixed to the affidavit.

#### 1439:2:subtheme:7 · paragraphs 29-31

- Raw key terms: `affidavit, affidavits, azenabors, court, however, para, photographs, stamp`
- Display key terms: `affidavit, affidavits, azenabors, however, para, photographs, stamp`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: affidavit, affidavits, azenabors, however, para, photographs, stamp Rule/authority context: [28] The Azenabors argue that since there is no requirement that the stamp on a Nigerian affidavit be in any particular place, it was unreasonable for the RAD to rely on the fact that the stamp was placed under the photo | However, the RAD clearly set out its understanding of the requirements based on the Affidavit RIR and the Stamp RIR, and its concerns arising from the placement of the notary’s stamp under the photographs, considered cum Evidence spans paragraphs 29-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4140514` offsets `437-445`; context: However, it relied on its common sense impression that the purpose of the stamp in question (which appears in the upper left corner of the affidavits, where the photographs are attached) is to confirm that no one has tampered with the affidavit and that the photos were attached at the time it was commissioned.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140514` offsets `89-98`; context: [28] The Azenabors argue that since there is no requirement that the stamp on a Nigerian affidavit be in any particular place, it was unreasonable for the RAD to rely on the fact that the stamp was placed under the photographs attached to two of the affidavits.
- Evidence: `governing_rule` cue `under` at chunk `4140514` offsets `205-210`; context: [28] The Azenabors argue that since there is no requirement that the stamp on a Nigerian affidavit be in any particular place, it was unreasonable for the RAD to rely on the fact that the stamp was placed under the photographs attached to two of the affidavits.
- Evidence: `counterargument_limitation` cue `However` at chunk `4140514` offsets `354-361`; context: However, it relied on its common sense impression that the purpose of the stamp in question (which appears in the upper left corner of the affidavits, where the photographs are attached) is to confirm that no one has tampered with the affidavit and that the photos were attached at the time it was commissioned.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140515` offsets `322-331`; context: I agree that caution should be exercised in relying on elements of affidavit formalities that are not required by law.
- Evidence: `governing_rule` cue `under` at chunk `4140515` offsets `557-562`; context: However, the RAD clearly set out its understanding of the requirements based on the Affidavit RIR and the Stamp RIR, and its concerns arising from the placement of the notary’s stamp under the photographs, considered cumulatively with other problems in the affidavits.
- Evidence: `counterargument_limitation` cue `However` at chunk `4140515` offsets `374-381`; context: However, the RAD clearly set out its understanding of the requirements based on the Affidavit RIR and the Stamp RIR, and its concerns arising from the placement of the notary’s stamp under the photographs, considered cumulatively with other problems in the affidavits.

#### 1439:2:subtheme:8 · paragraphs 32-39

- Raw key terms: `decision, azenabors, concerns, documents, nigeria, para, canada, citizenship`
- Display key terms: `azenabors, concerns, documents, nigeria, para`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: azenabors, concerns, documents, nigeria, para Application context: [31] Again, I find the RAD’s reliance on these issues as one element of its assessment of the documents to be reasonable. | , taken as a whole, can rightly lead the Board to conclude that an applicant’s credibility is fatally undermined”: Asashi v Canada (Minister of Citizenship and Immigration), 2005 FC 102 at para 8. Operative outcome context: At the same time, this Court has upheld findings that refer to the prevalence of fraudulent documents in a country, as part of broader reasons that assess the documents on their merits: see, e. Evidence spans paragraphs 32-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4140517` offsets `47-53`; context: [31] Again, I find the RAD’s reliance on these issues as one element of its assessment of the documents to be reasonable.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140517` offsets `1232-1241`; context: In my view, the concerns of the RAD on these issues may not alone be sufficient to find an affidavit to be non-genuine, but they were reasonable matters to consider along with other concerns and indicia in the RAD’s assessment of the documents.
- Evidence: `reasoning_application` cue `I find` at chunk `4140517` offsets `12-18`; context: [31] Again, I find the RAD’s reliance on these issues as one element of its assessment of the documents to be reasonable.
- Evidence: `issue` cue `issues` at chunk `4140518` offsets `35-41`; context: [32] In addition to the particular issues discussed above, the RAD in each case referred to “the prevalence of fraudulent documents in Nigeria,” citing a November 13, 2013 RIR entitled Nigeria: False documents available in Nigeria and from Nigeria, which was item 3.
- Evidence: `disposition` cue `upheld` at chunk `4140519` offsets `455-461`; context: At the same time, this Court has upheld findings that refer to the prevalence of fraudulent documents in a country, as part of broader reasons that assess the documents on their merits: see, e.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140521` offsets `726-735`; context: The same principle, in my view, applies to the RAD’s assessment of the Azenabors’ affidavit evidence in this case.
- Evidence: `reasoning_application` cue `conclude` at chunk `4140521` offsets `497-505`; context: , taken as a whole, can rightly lead the Board to conclude that an applicant’s credibility is fatally undermined”: Asashi v Canada (Minister of Citizenship and Immigration), 2005 FC 102 at para 8.
- Evidence: `counterargument_limitation` cue `but` at chunk `4140523` offsets `107-110`; context: [37] In its decision, the RAD relied on the absence of a watermark on the document filed by the Azenabors, but also on several concerns that were not set out in the letter.
- Evidence: `evidence_fact` cue `evidence` at chunk `4140524` offsets `330-338`; context: They refer to the general duty on the part of the RPD to confront claimants with inconsistencies in their evidence and give them an opportunity to respond: Mohamed v Canada (Citizenship and Immigration), 2015 FC 1379 at para 21.

#### 1439:2:subtheme:9 · paragraphs 40-46

- Raw key terms: `azenabors, affidavit, azenabor, cannot, information, canada, decision, para`
- Display key terms: `azenabors, affidavit, azenabor, cannot, information, para`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: azenabors, affidavit, azenabor, cannot, information, para Application context: Azenabor’s affidavit, I cannot conclude that the RAD’s assessment was unreasonable. | The Court cannot conclude that the RAD’s decision was unreasonable based on assumptions or submissions regarding the source of information that were not put to the RAD and are not set out in the affidavit. Evidence spans paragraphs 40-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `4140525` offsets `376-383`; context: Whether a concern must be put explicitly to the claimant will depend on the facts of each case: Mohamed at para 21, citing Ongeldinov v Canada (Minister of Citizenship and Immigration), 2012 FC 656 at para 21.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4140527` offsets `427-436`; context: Azenabor’s Affidavit was Reasonable
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140528` offsets `69-78`; context: [42] At the conclusion of its reasons, the RAD briefly addressed the affidavit filed by Mr.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140529` offsets `36-45`; context: Azenabor’s affidavit, I cannot conclude that the RAD’s assessment was unreasonable.
- Evidence: `reasoning_application` cue `conclude` at chunk `4140529` offsets `56-64`; context: Azenabor’s affidavit, I cannot conclude that the RAD’s assessment was unreasonable.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140530` offsets `62-71`; context: [44] The Azenabors submit that some of the information in the affidavit derived from Mr.
- Evidence: `reasoning_application` cue `conclude` at chunk `4140530` offsets `220-228`; context: The Court cannot conclude that the RAD’s decision was unreasonable based on assumptions or submissions regarding the source of information that were not put to the RAD and are not set out in the affidavit.
- Evidence: `counterargument_limitation` cue `However` at chunk `4140530` offsets `125-132`; context: However, this is not set out in the affidavit either expressly or implicitly.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4140531` offsets `116-125`; context: Azenabor’s affidavit was rejected on the impermissible ground that he is the husband of Ms.

#### 1439:2:subtheme:10 · paragraphs 47-47

- Raw key terms: `agree, application, arises, certification, dismissed, judicial, matter, neither`
- Display key terms: `agree, arises, certification, dismissed, judicial, matter, neither`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: agree, arises, certification, dismissed, judicial, matter, neither Application context: [46] The application for judicial review is therefore dismissed. Operative outcome context: [46] The application for judicial review is therefore dismissed. Evidence spans paragraphs 47-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4140532` offsets `90-98`; context: Neither party proposed a question for certification and I agree that none arises in the matter.
- Evidence: `reasoning_application` cue `therefore` at chunk `4140532` offsets `44-53`; context: [46] The application for judicial review is therefore dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4140532` offsets `54-63`; context: [46] The application for judicial review is therefore dismissed.

#### Section text

II. Issues

[4] The Azenabors’ arguments on this application raise three main issues:
Did the RAD err in its determination that the affidavits submitted by the Azenabors were fraudulent?
Did the RAD err in making a finding about the authenticity of a police report without first raising its concern with the Azenabors and permitting them to respond?
Did the RAD err in its treatment of Mr. Azenabor’s affidavit?

[5] The parties are agreed that the first and third of these issues are reviewable on the reasonableness standard: Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at paras 16–17, 23–25. In conducting reasonableness review, the Court considers “the outcome of the administrative decision in light of its underlying rationale in order to ensure that the decision as a whole is transparent, intelligible and justified”: Vavilov at para 15. A reasonable decision is one “based on an internally coherent and rational chain of analysis” and that is “justified in relation to the facts and law that constrain the decision maker”: Vavilov at paras 85, 90, 99, 105–107.

[6] Assessments of credibility and authenticity are part of the fact-finding process. The Supreme Court in Vavilov reiterated that reviewing courts should not reweigh or reassess evidence: Vavilov at para 125. Credibility findings are described as being given “significant deference”: N’kuly v Canada (Citizenship and Immigration), 2016 FC 1121 at para 21. This does not change the reasonableness standard of review, but emphasizes that within the reasonableness framework, decision makers are given considerable latitude in making credibility findings, which should not be disturbed lightly: Amador Ordonez v Canada (Citizenship and Immigration), 2019 FC 1216 at para 6; Vavilov at paras 88–90. At the same time, credibility findings are not “immune from review,” and must be clearly articulated and justified on the evidence: N’kuly at para 24; Valère v Canada (Minister of Citizenship and Immigration), 2001 FCT 1200 at para 14.

[7] The second issue is a matter of procedural fairness, and is therefore reviewed on a “fairness” standard, that is to say, by assessing whether the procedure was fair in all the circumstances: Canadian Pacific Railway Company v Canada (Attorney General), 2018 FCA 69 at para 54. This standard is best reflected in the correctness standard, although strictly speaking it does not involve the application of a standard of review: Canadian Pacific at para 54; Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 43; Canadian Association of Refugee Lawyers v Canada (Immigration, Refugees and Citizenship), 2020 FCA 196 at para 35.
III. Analysis
A. The RAD’s Conclusion Regarding Fraudulent Documents was Reasonable
(1) The Azenabors’ documentary evidence

[8] The Azenabors’ claim for refugee protection is based on their stated fear of Mr. Azenabor’s uncle. They claim the uncle sexually assaulted Ms. Azenabor on several occasions in Lagos, Nigeria while Mr. Azenabor was studying in Canada, and plotted with the local Chief Priest to poison her as part of a plan to cover up his crimes. Ms. Azenabor alleges that the uncle continued to threaten her after she attempted to relocate within Nigeria so that she was ultimately required to flee the country.

[9] The Azenabors filed a number of documents in support of their claim, including an affidavit from Mr. Azenabor, affidavits from five individuals in Nigeria, and a police report allegedly showing Ms. Azenabor’s sexual abuse complaint against the uncle. The RAD’s treatment of these documents are at the heart of this application for judicial review.

[10] The Refugee Protection Division (RPD) made adverse credibility findings against Ms. Azenabor based on three aspects of her testimony. The Azenabors challenged these findings on appeal to the RAD and argued that the RPD had failed to consider the documentary evidence submitted.

[11] During the course of their review, the RAD had concerns about a number of aspects of the documentary evidence, including the affidavits and the police report, which had not been raised by the RPD. The RAD sent a letter to the Azenabors identifying these concerns and asking the Azenabors to address them. It also requested the original copies of the five affidavits said to have been sworn in Nigeria.

[12] The Azenabors filed a written response addressing the concerns identified by the RAD and enclosing the original affidavits as requested. They also filed three Response to Information Request (RIR) documents from the National Documentation Package (NDP) for Nigeria published by the Immigration and Refugee Board (IRB), copies of the sample police records from the Nigerian police obtained from the IRB, and a news article about a Nigerian lawyer suing the Lagos State Chief Judge alleging that the sale of seals in court registries was unconstitutional. The RAD accepted these documents for consideration, although it did not accept certain factual statements made in the submission in the absence of any evidence filed to support them.
(2) The RAD’s assessment of the documents

[13] The RAD concluded that the grounds on which the RPD had made its adverse credibility findings were not sustainable. The RAD therefore did not rely on any particular findings arising from inconsistencies or implausibilities in Ms. Azenabor’s oral testimony. However, it concluded that the documents from Nigeria the Azenabors filed—the five affidavits and the police report—were fraudulent, and that the Azenabors therefore lacked credibility. The RAD found that while some of its concerns had been satisfied, “on the whole, significant problems remained which were not sufficiently resolved.” These included:
the seal on one of the affidavits was “very clearly a colour photocopy which has been cut out and stuck on the affidavit as opposed to a genuine seal,” a conclusion the RAD reached on the basis of review of the original affidavit;
another of the affidavits had three issues: (i) it identifies the deponent as living in Lagos, when the Azenabors alleged that she lived in Port Harcourt; (ii) the page where the affidavit was signed was in a different font than the first page, raising concerns that the two pages do not have the same provenance; and (iii) the affiant attached a work identification badge that had typographical errors, including listing the business address as being in “Portcourt” rather than “Port Harcourt”;
a further affidavit had two issues: (i) the stamp on the affidavit did not appear on the photograph attached to the affidavit nor underneath it and there was no evidence that the stamp was ever on the photo; and (ii) the affidavit identified the affiant as living in Lagos, while the Azenabors had alleged that she lived in Abuja;
the final two affidavits (i) attached photographs of the affiants, as required for affidavits in Lagos State, but the commissioner’s stamp on the top of each affidavit was placed under the photographs; and (ii) had identical title and signature blocks; and
the police report, which included the title “Crime Diary Extract,” did not conform with the information in the NDP about the availability or format of such documents, did not have the watermark expected for Lagos State police reports, and a number of other identified irregularities.

[14] In each case, the RAD referred to the identified concerns with the documents, which it considered “along with the prevalence of fraudulent documents in Nigeria” to conclude that the documents were not genuine on a balance of probabilities. Having reviewed each of the documents, the RAD reached the following conclusion:
Any one issue with any one of the above-mentioned documents would not be sufficient for me to conclude that the documents were not genuine. However, taking all of the issues with all of the documents cumulatively, I find, on a balance of probabilities, the Appellants submitted six documents which are not genuine. I further find that this vitiates the presumption of truthfulness genuinely afforded to refugee claimants. Accordingly, I place no weight on the testimony of the Principal Appellant.

[15] I note in this regard that while the RAD did not make any credibility findings based on, for example, inconsistencies or implausibilities in Ms. Azenabor’s oral testimony, this does not mean that the RAD accepted her evidence to be credible, as the Azenabors claim. To the contrary, the RAD expressly found Ms. Azenabor’s evidence not to be credible, on the basis that it was given by someone who had filed multiple fraudulent documents. The RAD appropriately assessed the testimonial and documentary evidence as a whole, concluding that the problems with the genuineness of the documentary evidence meant that it could place no weight on the testimonial evidence.
(3) The RAD’s credibility conclusions were reasonable

[16] The Azenabors assert that the documents they filed were genuine and that the RAD’s contrary assessment was unreasonable. They argue that the RAD inappropriately seized on minor errors and discrepancies in the documents and relied on formalities that the objective country condition documents do not identify as prerequisites for affidavits sworn in Lagos State. They note that the Federal Court of Appeal has cautioned against being overly “microscopic” in analyzing the evidence of refugee claimants: Attakora v Canada (Minister of Employment & Immigration), [1989] FCJ No 444 (CA) at para 9.

[17] For the following reasons, I do not accept the Azenabors’ arguments. I conclude that the RAD articulated reasonable grounds for its findings that the documents submitted were not genuine, and thus for finding Ms. Azenabor not to be credible.
(a) The RAD could assess the genuineness of the affidavits without verification with Nigerian authorities

[18] The Azenabors referred to an RIR prepared by the Research Directorate of the IRB dated November 4, 2014, entitled Nigeria: Requirements and procedures for the issuance of affidavits; availability of fraudulent affidavits, which was item 9.2 in the NDP for Nigeria [the Affidavit RIR]. The Affidavit RIR sets out information regarding the governing legislation in Nigeria, procedures regarding the preparation and swearing of affidavits, and information regarding the verification of affidavits. The information is derived from a number of sources, notably several Nigerian law firms, a representative of the Nigerian Bar Association, a notary public, and an Assistant Superintendent of the Nigeria Police, Special Fraud Unit.

[19] The Azenabors point to passages in the Affidavit RIR that state that in Nigeria, authenticity of an affidavit is verified by checking the records of the authority who administered the affidavit. The Assistant Superintendent in particular stated that it is “almost impossible” to determine the authenticity of a document by an on-the-spot assessment, and that the only way that the court can determine the authenticity of an affidavit is to consult their records. The Azenabors argue that since authorities in Nigeria recognize that authenticity can not be determined based on a facial assessment, the RAD should not have assessed the genuineness of their affidavits on this basis. Instead, they argue, the RAD could and should have undertaken a verification with the relevant court registry if it had any concerns about the affidavits.

[20] As a preliminary matter, I agree with the Minister that the Azenabors did not argue before the RAD that it could not assess the authenticity of the affidavits based on their appearance, or that it was obliged to verify authenticity with the Nigerian court registries. As a general rule, an applicant is precluded from raising a new argument on judicial review that was not raised before the administrative decision maker: Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61 at paras 22–26. While the Azenabors correctly note that they presented the Affidavit RIR to the RAD and made arguments on it, the elements of the Affidavit RIR they relied on pertained to the formalities of affidavits, not the RAD’s ability to assess their authenticity. In any event, I cannot accept the Azenabors’ submission on this issue for three reasons.

[21] First, I do not read the country condition evidence as indicating that it is never possible, either as a practical matter or as a matter of Nigerian law, to find an affidavit inauthentic based on its facial features. Rather, the Affidavit RIR appears to note that the authenticity of a document cannot be confirmed simply through a quick assessment, since there are no security features that cannot be circumvented or forged. The passage referred to by the Azenabors reads as follows:
8. Verification of Affidavits
According to the Assistant Superintendent, the Police Special Fraud Unit relies on the “issuing authority to verify all documents,” including affidavits. Similarly, the Notary Public indicated that for affidavits sworn in the courts, the Assistant Chief Registrar of the court is “usually the authority to confirm genuineness of any purported affidavit” and that for affidavits sworn by notaries, the Notary Public who issued the affidavit can be contacted for confirmation of the genuineness of the document.
8.1 Security Features on Court-Issued Affidavits
Sources note that there are no security features on an affidavit. According to the Assistant Superintendent, it is “almost impossible” to determine the authencity [sic] of a document by an “[on the] spot assessment.”
[Citations omitted.]

[22] In context, I cannot take this or other passages in the Affidavit RIR to indicate that an affidavit may not show itself to be inauthentic based on elements of its appearance or contents, even without conducting a verification with the notary public or court registry. While the latter may be a conclusive basis on which to determine authenticity, this does not preclude consideration of other indicia.

[23] Second, even if Nigerian authorities say it can be difficult to verify the authenticity of an affidavit by a facial assessment, this cannot mean that the RAD is precluded from making an assessment of the authenticity of the evidence before it based on their expertise, judgment, and reference to the country condition information. The IRPA calls on the RAD to make its decision “on evidence that is adduced in the proceedings and considered credible or trustworthy in the circumstances”: IRPA, s 171(a.3). The RAD is not bound by legal or technical rules of evidence in making its determinations: IRPA, s 171(a.2). While the RAD’s assessments of authenticity must be grounded in the evidence before it, including relevant country condition evidence, it is entitled to assess the authenticity of documents as they are presented.

[24] Third, the Azenabors’ proposition that the RAD has an obligation to verify affidavits with the Nigerian authorities before it makes an adverse finding as to their authenticity is untenable. As the Minister points out, the onus is on a refugee claimant to demonstrate through credible evidence that they meet the definitions of a Convention refugee or a person in need of protection under section 96 or 97 of the IRPA: Németh v Canada (Justice), 2010 SCC 56 at para 98; Boateng v Canada (Minister of Citizenship and Immigration), 2003 FCT 632 at para 9. The RAD is under no obligation to undertake investigative steps to seek out information that might confirm the authenticity of a document. If the Azenabors considered that confirmation from a Nigerian court registry was necessary to demonstrate the authenticity of their affidavits, they could have taken steps to obtain and file such confirmation, particularly after the RAD had raised its concerns. The RAD had no obligation to do so.
(b) The RAD reasonably assessed the appearance of the seal

[25] The Azenabors next point to a passage in the Affidavit RIR that quotes the Assistant Superintendent as noting that “the seal does not establish [an affidavit’s] authenticity as all fake ones also do carry [the] seal.” They argue since a seal does not establish an affidavit’s authenticity, it was wrong for the RAD to rely on the appearance of the seal on one of the affidavits. Again, I disagree. The fact that a fraudulent affidavit may have what appears to be a genuine seal does not mean that the RAD cannot conclude that an affidavit with an apparently fraudulent seal is fraudulent.

[26] The Azenabors also argued that the RAD’s conclusion regarding the quality of the seal on this affidavit was unreasonable, asserting that review of the original, which had been returned to the Azenabors, was at odds with the RAD’s conclusions. This argument must fail, if for no other reason than that the original was not filed with the Court on this application for judicial review. There is therefore no possible way for the Court to assess the Azenabors’ argument that the RAD’s conclusion that the seal was apparently simply a colour photocopy was unreasonable.
(c) The RAD reasonably assessed the photographs and commissioners’ stamps

[27] The Affidavit RIR indicates that the Federal High Courts in Nigeria require the deponent to attach two copies of a passport-sized photograph to the affidavit, and that notary publics in Lagos state similarly require a passport photo to be affixed to the affidavit. The Affidavit RIR also states that affidavits issued in Nigeria by a notary public will carry the stamp of the notary, but it does not set out any particular requirements for the location of a stamp, particularly in relation to the photographs. A separate RIR dated November 23, 2017, entitled Nigeria: Requirement for lawyers to affix stamps on legal documents; validity of documents issued without stamps, which was item 9.3 in the NDP for Nigeria [the Stamp RIR], similarly notes that lawyers are required to affix their stamps on legal documents they prepare, but does not give any required location of the stamp on an affidavit.

[28] The Azenabors argue that since there is no requirement that the stamp on a Nigerian affidavit be in any particular place, it was unreasonable for the RAD to rely on the fact that the stamp was placed under the photographs attached to two of the affidavits. The RAD recognized that there was no explicit requirement for the stamp to be on the photo. However, it relied on its common sense impression that the purpose of the stamp in question (which appears in the upper left corner of the affidavits, where the photographs are attached) is to confirm that no one has tampered with the affidavit and that the photos were attached at the time it was commissioned. Since there is a requirement for affidavits to have a passport photo affixed, the RAD was concerned about the location of the stamp, since it could not confirm that the photo was of the person who signed the affidavit.

[29] I am satisfied that the RAD’s analysis of these affidavits is reasonable. The RAD had the opportunity to review the original affidavits and assess the role of the stamp, as well as other concerns with the title and signature blocks of the documents. I agree that caution should be exercised in relying on elements of affidavit formalities that are not required by law. However, the RAD clearly set out its understanding of the requirements based on the Affidavit RIR and the Stamp RIR, and its concerns arising from the placement of the notary’s stamp under the photographs, considered cumulatively with other problems in the affidavits. As the Supreme Court has held, “the decision maker may assess and evaluate the evidence before it” and a reviewing court must refrain from “reweighing and reassessing the evidence considered by the decision maker”: Vavilov at para 125.
(d) The RAD reasonably considered other features of the affidavits and supporting documents

[30] This Court has noted that minor typographical errors or other clerical e

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 1439:3 · paragraphs 48-49

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `aa5a6ae28d46f8f67abde4a4b7d8d7facddd5a1f8f90ad95fd4256eeee2dc788`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 1439:3:subtheme:1 · paragraphs 48-49

- Raw key terms: `court, imm-5214-19, judgment, mchaffie, appearances, applicants, application, attorney`
- Display key terms: `imm-5214-19, mchaffie`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: imm-5214-19, mchaffie Operative outcome context: JUDGMENT IN IMM-5214-19 THIS COURT’S JUDGMENT is that The application for judicial review is dismissed. Evidence spans paragraphs 48-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4140532` offsets `254-263`; context: JUDGMENT IN IMM-5214-19
THIS COURT’S JUDGMENT is that
The application for judicial review is dismissed.

#### Section text

JUDGMENT IN IMM-5214-19
THIS COURT’S JUDGMENT is that
The application for judicial review is dismissed.
“Nicholas McHaffie”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-5214-19
STYLE OF CAUSE:
OGECHUKWU AZENABOR ET AL v MINISTER OF CITIZENSHIP AND IMMIGRATION
HEARING HELD BY VIDEOCONFERENCE ON JUNE 17, 2020 FROM OTTAWA, ONTARIO (COURT) AND TORONTO, ONTARIO (PARTIES)
JUDGMENT AND REASONS:
MCHAFFIE J.
DATED:
December 16, 2020
APPEARANCES:
Pius L. Okoronkwo
For The ApplicantS
Jocelyn Espejo Clarke
For The Respondent
SOLICITORS OF RECORD:
Pius L. Okoronkwo
Barrister and Solicitor
Toronto, Ontario
For The ApplicantS
Attorney General of Canada
Toronto, Ontario
For The Respondent
