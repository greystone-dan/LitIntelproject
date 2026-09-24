# Discussion Units: case 11273

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **31**
- Continuity pairs: **30**
- Discussion Units: **3**
- Paragraph source hashes: **31**
- Sub-themes: **7**

## 11273:1 · paragraphs 0-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `03f991fb5c92078b2cd888958fad59af7d663ab168c4db25ae5051c2b9ceb0dc`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11273:1:subtheme:1 · paragraphs 0-12

- Raw key terms: `applicant, claim, claims, eritrea, identity, refugee, canada, credible`
- Display key terms: `claims, eritrea, identity, refugee, credible`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: claims, eritrea, identity, refugee, credible Position/evidence statements: [4] In 1998, a war broke out between Ethiopia and Eritrea, and the Applicant claims he was deported to Eritrea with his father and brother in 2000. | [5] The Applicant claims in his Basis of Claim [BOC] that he is a Pentecostal Christian, that he was raised in that religion, and that in May 2002, the Eritrean government banned the Pentecostal religion and made it ille Rule/authority context: Background [1] This application for judicial review, filed pursuant to section 18. | [13] Pursuant to subsection 111(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], the RAD confirmed the decision of the RPD, finding that the Applicant is neither a Convention refugee nor a perso Application context: His claim was denied, and because he feared being deported to Eritrea, he came to Canada on August 12, 2015 and made a refugee claim. | [9] The Applicant contends that he fears imprisonment and torture in Eritrea because of his escape from prison and because of his religion. Operative outcome context: His claim was denied, and because he feared being deported to Eritrea, he came to Canada on August 12, 2015 and made a refugee claim. | [13] Pursuant to subsection 111(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], the RAD confirmed the decision of the RPD, finding that the Applicant is neither a Convention refugee nor a perso Evidence spans paragraphs 0-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4567744` offsets `493-504`; context: Background [1] This application for judicial review, filed pursuant to section 18.
- Evidence: `issue` cue `issue` at chunk `4567745` offsets `22-27`; context: [2] The determinative issue in the underlying proceedings was the Applicant’s identity.
- Evidence: `evidence_fact` cue `evidence` at chunk `4567745` offsets `208-216`; context: Neither the RPD nor the RAD was satisfied that the Applicant had established his identity with credible and trustworthy evidence.
- Evidence: `party_position` cue `claims` at chunk `4567747` offsets `77-83`; context: [4] In 1998, a war broke out between Ethiopia and Eritrea, and the Applicant claims he was deported to Eritrea with his father and brother in 2000.
- Evidence: `party_position` cue `claims` at chunk `4567748` offsets `18-24`; context: [5] The Applicant claims in his Basis of Claim [BOC] that he is a Pentecostal Christian, that he was raised in that religion, and that in May 2002, the Eritrean government banned the Pentecostal religion and made it illegal to practice it.
- Evidence: `party_position` cue `claims` at chunk `4567749` offsets `18-24`; context: [6] The Applicant claims that in April 2005, he was detained at a Bible study meeting, and detained for 8 months in a prison camp, where he was interrogated and tortured.
- Evidence: `party_position` cue `claims` at chunk `4567751` offsets `18-24`; context: [8] The Applicant claims that in February 2014, he secured a false passport and flew to Mexico, and from there, he went to the United States [US] border where he made an asylum claim.
- Evidence: `reasoning_application` cue `because` at chunk `4567751` offsets `210-217`; context: His claim was denied, and because he feared being deported to Eritrea, he came to Canada on August 12, 2015 and made a refugee claim.
- Evidence: `disposition` cue `denied` at chunk `4567751` offsets `198-204`; context: His claim was denied, and because he feared being deported to Eritrea, he came to Canada on August 12, 2015 and made a refugee claim.
- Evidence: `party_position` cue `contends` at chunk `4567752` offsets `18-26`; context: [9] The Applicant contends that he fears imprisonment and torture in Eritrea because of his escape from prison and because of his religion.
- Evidence: `reasoning_application` cue `because` at chunk `4567752` offsets `77-84`; context: [9] The Applicant contends that he fears imprisonment and torture in Eritrea because of his escape from prison and because of his religion.
- Evidence: `evidence_fact` cue `found that` at chunk `4567755` offsets `13-23`; context: [12] The RPD found that the Applicant was unable to establish his identity with trustworthy and credible evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4567756` offsets `366-374`; context: [13] Pursuant to subsection 111(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], the RAD confirmed the decision of the RPD, finding that the Applicant is neither a Convention refugee nor a person in need of protection, and dismissed the Applicant’s appeal on the basis that he failed to establish his identity with credible and trustworthy evidence.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `4567756` offsets `5-16`; context: [13] Pursuant to subsection 111(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], the RAD confirmed the decision of the RPD, finding that the Applicant is neither a Convention refugee nor a person in need of protection, and dismissed the Applicant’s appeal on the basis that he failed to establish his identity with credible and trustworthy evidence.
- Evidence: `reasoning_application` cue `applies` at chunk `4567756` offsets `528-535`; context: Standard of Review [14] The role of the RAD is set out in Canada (Citizenship and Immigration) v Huruglica, 2016 FCA 93, [Huruglica] and this Court applies a reasonableness standard when reviewing the RAD’s conclusions.
- Evidence: `disposition` cue `dismissed` at chunk `4567756` offsets `249-258`; context: [13] Pursuant to subsection 111(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], the RAD confirmed the decision of the RPD, finding that the Applicant is neither a Convention refugee nor a person in need of protection, and dismissed the Applicant’s appeal on the basis that he failed to establish his identity with credible and trustworthy evidence.

#### 11273:1:subtheme:2 · paragraphs 13-14

- Raw key terms: `applicant, consider, failed, however, identity, national, reasons, submission`
- Display key terms: `consider, failed, however, identity, national, submission`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: consider, failed, however, identity, national, submission Position/evidence statements: [17] First, the Applicant submitted that after the RAD gave no weight to the identity documents consisting of the birth certificate and national identity card because they were photocopies of photocopies, it failed to co Application context: [15] The RAD will apply a standard of correctness to its consideration of the RPD’s decision, and it will conduct its own review of the evidence and undertake its own analysis of the question. | [17] First, the Applicant submitted that after the RAD gave no weight to the identity documents consisting of the birth certificate and national identity card because they were photocopies of photocopies, it failed to co Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4567757` offsets `183-191`; context: [15] The RAD will apply a standard of correctness to its consideration of the RPD’s decision, and it will conduct its own review of the evidence and undertake its own analysis of the question.
- Evidence: `evidence_fact` cue `evidence` at chunk `4567757` offsets `136-144`; context: [15] The RAD will apply a standard of correctness to its consideration of the RPD’s decision, and it will conduct its own review of the evidence and undertake its own analysis of the question.
- Evidence: `reasoning_application` cue `apply` at chunk `4567757` offsets `18-23`; context: [15] The RAD will apply a standard of correctness to its consideration of the RPD’s decision, and it will conduct its own review of the evidence and undertake its own analysis of the question.
- Evidence: `counterargument_limitation` cue `however` at chunk `4567757` offsets `202-209`; context: The RAD, however, will not interfere with the RPD’s findings where such conclusions result from the RPD’s distinct advantages or from an intelligible reasoning process whose premises are embedded in such advantages.
- Evidence: `party_position` cue `submitted` at chunk `4567758` offsets `26-35`; context: [17] First, the Applicant submitted that after the RAD gave no weight to the identity documents consisting of the birth certificate and national identity card because they were photocopies of photocopies, it failed to consider the reason why the Applicant was unable to produce the originals.
- Evidence: `reasoning_application` cue `because` at chunk `4567758` offsets `159-166`; context: [17] First, the Applicant submitted that after the RAD gave no weight to the identity documents consisting of the birth certificate and national identity card because they were photocopies of photocopies, it failed to consider the reason why the Applicant was unable to produce the originals.
- Evidence: `counterargument_limitation` cue `However` at chunk `4567758` offsets `293-300`; context: However, this was not the Applicant’s submission to the RAD.

#### 11273:1:subtheme:3 · paragraphs 15-18

- Raw key terms: `applicant, medical, provided, report, based, credible, evidence, found`
- Display key terms: `medical, provided, report, based, credible`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: medical, provided, report, based, credible Position/evidence statements: [19] Second, the Applicant submitted that the RAD failed to appropriately consider the medical evidence of the psychiatrist. Application context: He argued that the physicians report was intended “to explain possible discrepancies that may have arisen over the hearing because of the applicant’s psychological frailty”, citing Feleke v Canada (Citizenship and Immigr Evidence spans paragraphs 15-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4567759` offsets `85-90`; context: [18] In any event, there is no evidence of any error by the RPD with respect to this issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `4567759` offsets `31-39`; context: [18] In any event, there is no evidence of any error by the RPD with respect to this issue.
- Evidence: `issue` cue `issue` at chunk `4567760` offsets `395-400`; context: The RAD did not address this issue, instead concluding that the report deserved little weight because it was based on a history provided by the Applicant, who had been found to lack credibility.
- Evidence: `party_position` cue `submitted` at chunk `4567760` offsets `27-36`; context: [19] Second, the Applicant submitted that the RAD failed to appropriately consider the medical evidence of the psychiatrist.
- Evidence: `evidence_fact` cue `evidence` at chunk `4567760` offsets `95-103`; context: [19] Second, the Applicant submitted that the RAD failed to appropriately consider the medical evidence of the psychiatrist.
- Evidence: `reasoning_application` cue `because` at chunk `4567760` offsets `248-255`; context: He argued that the physicians report was intended “to explain possible discrepancies that may have arisen over the hearing because of the applicant’s psychological frailty”, citing Feleke v Canada (Citizenship and Immigration), 2007 FC 539.

#### 11273:1:subtheme:4 · paragraphs 19-22

- Raw key terms: `court, applicant, concerning, decision, deferential, documents, identity, issues`
- Display key terms: `concerning, deferential, documents, identity, issues`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: concerning, deferential, documents, identity, issues Application context: [25] It is in this light that the Court concludes it must be cautious in branding the RAD as being too deferential to the RPD in adopting some of its reasons. Evidence spans paragraphs 19-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4567763` offsets `246-252`; context: [22] As a final point, the Court does not agree with the Applicant’s submission that the RAD was overly deferential to the RPD and paid lip service to it by failing to carry out its own analysis, as demonstrated by failing to address some of the issues he raised concerning the RPD decision.
- Evidence: `issue` cue `issues` at chunk `4567764` offsets `76-82`; context: [23] With respect to the RAD carrying out its own assessment on the various issues, the Court finds that it relied upon different reasons from those of the RPD, regarding the reliability of the identity documents, the Applicant’s medical evidence and that concerning his evidence on the war between Ethiopia and Eritrea, thereby demonstrating that it carried out its own assessment in rejecting these aspects of his identity evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4567764` offsets `238-246`; context: [23] With respect to the RAD carrying out its own assessment on the various issues, the Court finds that it relied upon different reasons from those of the RPD, regarding the reliability of the identity documents, the Applicant’s medical evidence and that concerning his evidence on the war between Ethiopia and Eritrea, thereby demonstrating that it carried out its own assessment in rejecting these aspects of his identity evidence.
- Evidence: `evidence_fact` cue `record` at chunk `4567766` offsets `523-529`; context: The Court should not be overly critical of the RAD for arriving at many of the same conclusions reached by the RPD by applying the same reasoning to the same record, if the reasoning is sound.
- Evidence: `reasoning_application` cue `concludes` at chunk `4567766` offsets `40-49`; context: [25] It is in this light that the Court concludes it must be cautious in branding the RAD as being too deferential to the RPD in adopting some of its reasons.

#### 11273:1:subtheme:5 · paragraphs 23-27

- Raw key terms: `applicant, court, address, asylum, claim, evidence, finds, issues`
- Display key terms: `address, asylum, finds, issues`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: address, asylum, finds, issues Operative outcome context: Moreover, the RPD found that the Applicant was not credible in stating that he did not know why his asylum claim was denied, or that he could not obtain information regarding his claim from his lawyers who represented hi Evidence spans paragraphs 23-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4567767` offsets `91-97`; context: [26] This rule extends equally to situations where the RAD does not specifically deal with issues raised by the Applicant.
- Evidence: `evidence_fact` cue `record` at chunk `4567767` offsets `429-435`; context: It is trite law that (1) “a decision-maker is not required to make an explicit finding on each constituent element of the matter to address subordinate issues”, (2) “the court must first seek to supplement them [the reasons] before it seeks to subvert them” and (3) the reviewing Court should “look to the record for the purpose of assessing the reasonableness of the outcome”: Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 622 at paras 12 and14−15.
- Evidence: `issue` cue `issues` at chunk `4567768` offsets `103-109`; context: [27] It is in this perspective that the Court finds no error in the RAD not addressing the Applicant’s issues regarding the RPD rejecting or giving little weight to the letters of support of certain individuals, or dismissing the evidence from the Applicant’s US asylum claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4567768` offsets `230-238`; context: [27] It is in this perspective that the Court finds no error in the RAD not addressing the Applicant’s issues regarding the RPD rejecting or giving little weight to the letters of support of certain individuals, or dismissing the evidence from the Applicant’s US asylum claim.
- Evidence: `evidence_fact` cue `found that` at chunk `4567769` offsets `374-384`; context: Moreover, the RPD found that the Applicant was not credible in stating that he did not know why his asylum claim was denied, or that he could not obtain information regarding his claim from his lawyers who represented him in the matter.
- Evidence: `disposition` cue `denied` at chunk `4567769` offsets `473-479`; context: Moreover, the RPD found that the Applicant was not credible in stating that he did not know why his asylum claim was denied, or that he could not obtain information regarding his claim from his lawyers who represented him in the matter.
- Evidence: `evidence_fact` cue `evidence` at chunk `4567771` offsets `86-94`; context: [30] The RAD indicated that it carried out a “fulsome and independent analysis of the evidence adduced”.

#### Section text

Tekle v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2017-11-15
Neutral citation
2017 FC 1040
File numbers
IMM-1727-17
Decision Content
Date: 20171115
Docket: IMM-1727-17
Citation: 2017 FC 1040
Ottawa, Ontario, November 15, 2017
PRESENT: The Honourable Mr. Justice Annis
BETWEEN:
DAWIT ABRAHAM TEKLE
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Background [1] This application for judicial review, filed pursuant to section 18.1(1) of the Federal Courts Act, RSC 1985, c F-7, seeks to set aside a decision [the Decision] of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board from an earlier Refugee Protection Division [RPD] decision denying the Applicant’s claim for refugee protection.

[2] The determinative issue in the underlying proceedings was the Applicant’s identity. Neither the RPD nor the RAD was satisfied that the Applicant had established his identity with credible and trustworthy evidence.

[3] The Applicant, Dawit Abraham Tekle, was born on July 17, 1986 in Eritrea, and he allegedly moved to Addis Ababa, Ethiopia, when he was young.

[4] In 1998, a war broke out between Ethiopia and Eritrea, and the Applicant claims he was deported to Eritrea with his father and brother in 2000.

[5] The Applicant claims in his Basis of Claim [BOC] that he is a Pentecostal Christian, that he was raised in that religion, and that in May 2002, the Eritrean government banned the Pentecostal religion and made it illegal to practice it.

[6] The Applicant claims that in April 2005, he was detained at a Bible study meeting, and detained for 8 months in a prison camp, where he was interrogated and tortured.

[7] The Applicant allegedly escaped from the prison camp and fled to Sudan in the early hours of January 1, 2006, where he resided without status until November 2008. In the hopes of gaining entrance to Europe, he traveled to Libya, remaining there until May 2011 when the war in Libya worsened, at which time he returned to Sudan.

[8] The Applicant claims that in February 2014, he secured a false passport and flew to Mexico, and from there, he went to the United States [US] border where he made an asylum claim. His claim was denied, and because he feared being deported to Eritrea, he came to Canada on August 12, 2015 and made a refugee claim.

[9] The Applicant contends that he fears imprisonment and torture in Eritrea because of his escape from prison and because of his religion.

[10] In support of his claim, the Applicant submitted a “copy of a copy” of a birth certificate, a “copy of a copy” of a national identity card, a Texas driving license, letters from churches in Toronto and Texas, two witness letters, a psychiatric report and his US asylum claim documents.

[11] The Applicant’s application for refugee protection was heard by the RPD on October 12, 2016, and the negative decision was rendered in writing on October 20, 2016.

[12] The RPD found that the Applicant was unable to establish his identity with trustworthy and credible evidence.

[13] Pursuant to subsection 111(1)(a) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], the RAD confirmed the decision of the RPD, finding that the Applicant is neither a Convention refugee nor a person in need of protection, and dismissed the Applicant’s appeal on the basis that he failed to establish his identity with credible and trustworthy evidence.
II. Standard of Review [14] The role of the RAD is set out in Canada (Citizenship and Immigration) v Huruglica, 2016 FCA 93, [Huruglica] and this Court applies a reasonableness standard when reviewing the RAD’s conclusions.

[15] The RAD will apply a standard of correctness to its consideration of the RPD’s decision, and it will conduct its own review of the evidence and undertake its own analysis of the question. The RAD, however, will not interfere with the RPD’s findings where such conclusions result from the RPD’s distinct advantages or from an intelligible reasoning process whose premises are embedded in such advantages. The standard is further elaborated upon by Justice Manson in Anel v Canada (Citizenship and Immigration ), 2016 FC 759 at para 25:
In Huruglica, above, the Federal Court of Appeal held that while the RAD must conduct its own analysis of a matter and review the RPD findings on the standard of correctness, the requirements insofar as deference to the RPD are to be evaluated on a case-by-case basis. Where a case involves considerations of credibility, the RAD must determine if the RPD was in fact better positioned to make a determination on that aspect of the claim. Where the error or lack thereof is easily identified by the RAD, the RPD may not have any real advantage; only where the RAD concludes the hearing of oral evidence by the RPD is essential should it remit the matter back to the RPD for redetermination.
III. Issues and Analysis [16] The Applicant argues that the RAD failed to consider the totality of the evidence in assessing whether his personal and national identity was established on a balance of probabilities. The Court rejects this submission for the following reasons.

[17] First, the Applicant submitted that after the RAD gave no weight to the identity documents consisting of the birth certificate and national identity card because they were photocopies of photocopies, it failed to consider the reason why the Applicant was unable to produce the originals. However, this was not the Applicant’s submission to the RAD. Rather, he argued that the RPD failed to provide reasons to explain why the birth certificate and national identity card were not valid documents in light of the presumption of validity of identity documents. The RAD provided reasons in response to this submission outlining why they lacked probative value, and therefore why they could not serve to identify the Applicant.

[18] In any event, there is no evidence of any error by the RPD with respect to this issue. The RPD provided several reasons to demonstrate that the Applicant’s explanations were not credible in describing his inability to produce the originals found at paragraphs 10 to 17 of its reasons. The Applicant advanced no specific submissions with respect to these reasons except that the RPD was “overly critical” of the identity evidence and had an “intent to find fault with whatever was presented rather than to take a fair and reasonable view of the material provided”.

[19] Second, the Applicant submitted that the RAD failed to appropriately consider the medical evidence of the psychiatrist. He argued that the physicians report was intended “to explain possible discrepancies that may have arisen over the hearing because of the applicant’s psychological frailty”, citing Feleke v Canada (Citizenship and Immigration), 2007 FC 539. The RAD did not address this issue, instead concluding that the report deserved little weight because it was based on a history provided by the Applicant, who had been found to lack credibility.

[20] With respect to the Applicant’s submission, it was pointed out that the medical report did not opine on the Applicant’s difficulties in recounting events. Rather, the report concluded that the Applicant “came across as a reliable historian” and that the author did “not anticipate that Mr. Tekle would have any difficulty representing himself at the refugee hearing”.

[21] Moreover, the Court agrees with the RAD’s conclusion that if the Applicant is not credible, a report based on a history provided by him would lack reliability. Apart from any testing conducted by the physician, the diagnosis, prognosis and treatment recommended in medical reports are based upon the initial factual summary contained in the patient’s history. If the history is false, it would detrimentally affect the reliability of the opinion portions of the medical report.

[22] As a final point, the Court does not agree with the Applicant’s submission that the RAD was overly deferential to the RPD and paid lip service to it by failing to carry out its own analysis, as demonstrated by failing to address some of the issues he raised concerning the RPD decision.

[23] With respect to the RAD carrying out its own assessment on the various issues, the Court finds that it relied upon different reasons from those of the RPD, regarding the reliability of the identity documents, the Applicant’s medical evidence and that concerning his evidence on the war between Ethiopia and Eritrea, thereby demonstrating that it carried out its own assessment in rejecting these aspects of his identity evidence.

[24] The Court acknowledges that the RAD did not comment on the Applicant’s submissions regarding documents issued to him by the US immigration authorities, or letters from friends, relatives and pastors intended to provide corroboration of his personal and national identity.

[25] It is in this light that the Court concludes it must be cautious in branding the RAD as being too deferential to the RPD in adopting some of its reasons. The reality is that when two competent decision-makers review the same factual circumstances, the first one should capture most of the relevant points that support a reasonable and well-explained decision. The Court should not be overly critical of the RAD for arriving at many of the same conclusions reached by the RPD by applying the same reasoning to the same record, if the reasoning is sound. Otherwise, this would amount to forcing the RAD to jump through differentiated reasoning hoops so as to provide a distinctive set of reasons from those of the RPD, even if there are no meaningful grounds of appeal for the RPD decision in the first place.

[26] This rule extends equally to situations where the RAD does not specifically deal with issues raised by the Applicant. It is trite law that (1) “a decision-maker is not required to make an explicit finding on each constituent element of the matter to address subordinate issues”, (2) “the court must first seek to supplement them [the reasons] before it seeks to subvert them” and (3) the reviewing Court should “look to the record for the purpose of assessing the reasonableness of the outcome”: Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 622 at paras 12 and14−15.

[27] It is in this perspective that the Court finds no error in the RAD not addressing the Applicant’s issues regarding the RPD rejecting or giving little weight to the letters of support of certain individuals, or dismissing the evidence from the Applicant’s US asylum claim.

[28] The RPD noted that none of the letters of support assisted in identifying the Applicant, apart from those which were handwritten and unsworn and that could have been presented by anyone. Similarly, with respect to the Applicant’s failed US asylum claim, the RPD noted that amongst all the documents produced, none related to the Applicant’s identity. Moreover, the RPD found that the Applicant was not credible in stating that he did not know why his asylum claim was denied, or that he could not obtain information regarding his claim from his lawyers who represented him in the matter.

[29] Not only should the RAD not be criticized for relying on these conclusions, but it is not required to address them when they speak for themselves from the RPD reasons.

[30] The RAD indicated that it carried out a “fulsome and independent analysis of the evidence adduced”. The Court finds no reason to discount this statement.


## 11273:2 · paragraphs 28-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `10c2c18039f984491bbef28c1c8882de3aeab5c876ba995b08580825621874be`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11273:2:subtheme:1 · paragraphs 28-29

- Raw key terms: `cause, imm-1727-17, style, abraham, amended, annis, appeal, application`
- Display key terms: `imm-1727-17, style, abraham, amended, annis`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: imm-1727-17, style, abraham, amended, annis Operative outcome context: Conclusion [31] The application is dismissed. Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4567771` offsets `359-367`; context: JUDGMENT FOR IMM-1727-17
THIS COURT’S JUDGMENT is that the application is dismissed, no question is certified for appeal and the style of cause is hereby amended.
- Evidence: `disposition` cue `dismissed` at chunk `4567771` offsets `198-207`; context: Conclusion [31] The application is dismissed.

#### Section text

IV. Conclusion [31] The application is dismissed. There were no questions suggested to be certified for appeal.
JUDGMENT FOR IMM-1727-17
THIS COURT’S JUDGMENT is that the application is dismissed, no question is certified for appeal and the style of cause is hereby amended.
"Peter Annis"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-1727-17
STYLE OF CAUSE:
DAWIT ABRAHAM TEKLE v THE MINISNTER OF IMMIGRATION, REFUGEES AND CITIZENSHIP
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
October 30, 2017


## 11273:3 · paragraphs 30-30

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c5237bb58cd8a2ae2088a6ae9c897e7bc5e071960bd2f86fd9efbb5902bdabb5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11273:3:subtheme:1 · paragraphs 30-30

- Raw key terms: `annis, appearances, applicant, attorney, barrister, canada, dated, deputy`
- Display key terms: `annis, barrister, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: annis, barrister, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 30-30. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT and REASONS:
ANNIS J.
DATED:
November xx, 2017
APPEARANCES:
Paul Vandervennen
For The Applicant
Stephen Jarvis
For The Respondent
SOLICITORS OF RECORD:
Paul Vandervennen
Barrister and Solicitor
Toronto, Ontario
For The Applicant
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
