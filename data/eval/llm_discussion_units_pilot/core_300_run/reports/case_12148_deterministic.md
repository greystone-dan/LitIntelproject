# Discussion Units: case 12148

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **23**
- Continuity pairs: **22**
- Discussion Units: **1**
- Paragraph source hashes: **23**
- Sub-themes: **6**

## 12148:1 · paragraphs 0-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4bbcdd293c1e24283b01d32bb78e6c36e8e1645b4ff51a1273d7c6cfc1f5f48f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12148:1:subtheme:1 · paragraphs 0-6

- Raw key terms: `applicants, dowansingh, refugee, claim, credibility, decision, jamaica, reasons`
- Display key terms: `dowansingh, refugee, credibility, jamaica`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: dowansingh, refugee, credibility, jamaica Rule/authority context: Overview [1] This is the judicial review of the denial of the Applicants’ refugee appeal by the Refugee Appeal Division [RAD], pursuant to section 110 of the Immigration and Refugee Protection Act (SC 2001, c 27) [the Ac Application context: The Applicants, Rajiv and Tamara Dowansingh, are a married couple from Jamaica fearing persecution by supporters of the Jamaica Labour Party [JLP] because they refused to vote for the party in the 2011 national and local | [3] For the reasons below, I find the RAD’s decision [Decision] to be reasonable, and dismiss the judicial review. Operative outcome context: [2] The RAD upheld the rejection of the claim by the Refugee Protection Division [RPD], concluding that there were no “palpable and overriding errors” relating to the credibility findings by the RPD. Evidence spans paragraphs 0-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4608398` offsets `627-638`; context: Overview [1] This is the judicial review of the denial of the Applicants’ refugee appeal by the Refugee Appeal Division [RAD], pursuant to section 110 of the Immigration and Refugee Protection Act (SC 2001, c 27) [the Act].
- Evidence: `reasoning_application` cue `because` at chunk `4608398` offsets `871-878`; context: The Applicants, Rajiv and Tamara Dowansingh, are a married couple from Jamaica fearing persecution by supporters of the Jamaica Labour Party [JLP] because they refused to vote for the party in the 2011 national and local elections.
- Evidence: `disposition` cue `upheld` at chunk `4608399` offsets `12-18`; context: [2] The RAD upheld the rejection of the claim by the Refugee Protection Division [RPD], concluding that there were no “palpable and overriding errors” relating to the credibility findings by the RPD.
- Evidence: `reasoning_application` cue `I find` at chunk `4608400` offsets `27-33`; context: [3] For the reasons below, I find the RAD’s decision [Decision] to be reasonable, and dismiss the judicial review.
- Evidence: `counterargument_limitation` cue `but` at chunk `4608401` offsets `191-194`; context: He allegedly reported the incident to the police, but no action was taken.
- Evidence: `evidence_fact` cue `Record` at chunk `4608403` offsets `741-747`; context: Rather, the Applicants remained in the same house in the same district in which the assault had taken place, despite having immediate family living in other districts and sufficient financial means to remove themselves from danger (Application Record [AR], p.
- Evidence: `evidence_fact` cue `determined that` at chunk `4608404` offsets `124-139`; context: Dowansingh also submitted a police letter documenting the alleged assault he suffered in November 2012, but the RPD determined that this was “not a trustworthy document” for several reasons (AR, p.

#### 12148:1:subtheme:2 · paragraphs 7-10

- Raw key terms: `police, assessment, decision, independent, independently, report, accept, acknowledging`
- Display key terms: `police, assessment, independent, independently, report, accept, acknowledging`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: police, assessment, independent, independently, report, accept, acknowledging Application context: The RAD should not defer to the RPD’s conclusions on such matters, because the RPD is in no better a position to assess these documents than the RAD (Njeukam v Canada (Citizenship and Immigration), 2014 FC 859 at para 14 Evidence spans paragraphs 7-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4608405` offsets `167-174`; context: [10] More particularly, the decision maker should have conducted an independent assessment of the police letter submitted by the Applicants, and decided independently whether it was genuine.
- Evidence: `reasoning_application` cue `because` at chunk `4608406` offsets `180-187`; context: The RAD should not defer to the RPD’s conclusions on such matters, because the RPD is in no better a position to assess these documents than the RAD (Njeukam v Canada (Citizenship and Immigration), 2014 FC 859 at para 14; Kurtzmalaj v Canada (Citizenship and Immigration), 2014 FC 1072 at para 35; Sow v Canada (Citizenship and Immigration), 2015 FC 295 at para 13).
- Evidence: `evidence_fact` cue `evidence` at chunk `4608408` offsets `298-306`; context: The RAD has reviewed the evidence in this area concerning the police report, where the RPD found it to be riddled with anomalies, and those were identified clearly in its reasons; as such, the RAD finds the RPD finding regarding the value of the police report to be reasonable in this circumstance.

#### 12148:1:subtheme:3 · paragraphs 11-14

- Raw key terms: `assessment, detail, evidence, findings, authenticity, case, concerns, conclusions`
- Display key terms: `assessment, detail, findings, authenticity, case, concerns, conclusions`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: assessment, detail, findings, authenticity, case, concerns, conclusions Evidence spans paragraphs 11-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4608409` offsets `118-124`; context: [13] As a general practice, the more detail the RAD can provide in its reasons about its thoughts on the most salient issues pertaining to personalized documentation and country conditions, as well as including country condition evidence and whether it agrees with or differs from the RPD’s assessment, the more likely a reviewing Court is to find that such evidence was independently assessed by the RAD.
- Evidence: `evidence_fact` cue `evidence` at chunk `4608409` offsets `229-237`; context: [13] As a general practice, the more detail the RAD can provide in its reasons about its thoughts on the most salient issues pertaining to personalized documentation and country conditions, as well as including country condition evidence and whether it agrees with or differs from the RPD’s assessment, the more likely a reviewing Court is to find that such evidence was independently assessed by the RAD.
- Evidence: `evidence_fact` cue `evidence` at chunk `4608411` offsets `236-244`; context: [15] At the other end of the spectrum, if the RPD’s conclusions turn on other discrete observations, specialized expertise, and/or novel findings, then there is a greater need for the RAD to detail how it reached its conclusions on the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4608412` offsets `81-89`; context: [16] In this case, the RAD explicitly stated in its reasons that it reviewed the evidence regarding the police letter, and noted the RPD “identified clearly in its reasons” that the letter was “riddled with anomalies”.

#### 12148:1:subtheme:4 · paragraphs 15-17

- Raw key terms: `applicants, canada, credibility, findings, assessment, citizenship, conclusions, delay`
- Display key terms: `credibility, findings, assessment, conclusions, delay`
- Argument roles: `governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, party_position, reasoning_application Display terms: credibility, findings, assessment, conclusions, delay Position/evidence statements: [17] In any event, the RPD’s conclusions regarding the Applicants’ credibility rested on more pillars than merely the genuineness of the police report submitted. | [19] The Applicants argue that the RAD erred in assessing the RPD’s credibility findings on a “palpable and overriding error” standard. Rule/authority context: Negative credibility findings made under section 96 may also affect the validity of a claim under section 97, even though subjective fear is not part of the assessment for the latter section (Mahadeva v Canada (Minister  Application context: [18] I find the RAD’s conclusions to be reasonable. Evidence spans paragraphs 15-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submitted` at chunk `4608413` offsets `151-160`; context: [17] In any event, the RPD’s conclusions regarding the Applicants’ credibility rested on more pillars than merely the genuineness of the police report submitted.
- Evidence: `governing_rule` cue `under` at chunk `4608414` offsets `87-92`; context: Negative credibility findings made under section 96 may also affect the validity of a claim under section 97, even though subjective fear is not part of the assessment for the latter section (Mahadeva v Canada (Minister of Citizenship and Immigration), 2006 FC 415 at para 15).
- Evidence: `reasoning_application` cue `I find` at chunk `4608414` offsets `5-11`; context: [18] I find the RAD’s conclusions to be reasonable.
- Evidence: `party_position` cue `argue` at chunk `4608415` offsets `20-25`; context: [19] The Applicants argue that the RAD erred in assessing the RPD’s credibility findings on a “palpable and overriding error” standard.

#### 12148:1:subtheme:5 · paragraphs 18-19

- Raw key terms: `canada, case, credibility, error, overriding, palpable, para, applicants`
- Display key terms: `case, credibility, error, overriding, palpable, para`
- Argument roles: `issue, party_position`
- Explanation: Observed roles: issue, party_position Display terms: case, credibility, error, overriding, palpable, para Position/evidence statements: [21] The Applicants argue that the RAD should have been less deferential to the RPD’s credibility findings in this case. Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4608416` offsets `265-271`; context: [20] In what has become the pre-eminent case on the standard of intervention by the RAD, Justice Phelan in Huruglica v Canada (Citizenship and Immigration), 2014 FC 799 at para 55, concluded that the RAD may “recognize and respect the conclusion of the RPD on such issues as credibility” but is not limited to “to intervening on facts only where there is a ‘palpable and overriding error’.
- Evidence: `party_position` cue `argue` at chunk `4608417` offsets `20-25`; context: [21] The Applicants argue that the RAD should have been less deferential to the RPD’s credibility findings in this case.

#### 12148:1:subtheme:6 · paragraphs 20-22

- Raw key terms: `applicants, canada, citizenship, court, diner, immigration, judgment, able`
- Display key terms: `diner, able`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: diner, able Application context: I, therefore, dismiss this application for judicial review. Operative outcome context: This judicial review is dismissed. Evidence spans paragraphs 20-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4608418` offsets `135-141`; context: This Court has repeatedly held that RPD’s conclusions on issues of credibility based on testimony clearly warrant some measure of deference (Denbel v Canada (Citizenship and Immigration), 2015 FC 629 at para 31; Ali v Canada (Citizenship and Immigration), 2015 FC 500 at para 8; Ngandu v Canada (Citizenship and Immigration), 2015 FC 423 at para 31).
- Evidence: `evidence_fact` cue `testimony` at chunk `4608418` offsets `166-175`; context: This Court has repeatedly held that RPD’s conclusions on issues of credibility based on testimony clearly warrant some measure of deference (Denbel v Canada (Citizenship and Immigration), 2015 FC 629 at para 31; Ali v Canada (Citizenship and Immigration), 2015 FC 500 at para 8; Ngandu v Canada (Citizenship and Immigration), 2015 FC 423 at para 31).
- Evidence: `reasoning_application` cue `therefore` at chunk `4608419` offsets `196-205`; context: I, therefore, dismiss this application for judicial review.
- Evidence: `disposition` cue `dismissed` at chunk `4608419` offsets `319-328`; context: This judicial review is dismissed.

#### Section text

Dowansingh v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2015-07-30
Neutral citation
2015 FC 933
File numbers
IMM-6581-14
Decision Content
Date: 20150730
Docket: IMM-6581-14
Citation: 2015 FC 933
Toronto, Ontario, July 30, 2015
PRESENT: The Honourable Mr. Justice Diner
BETWEEN:
RAJIC CAVIN DOWANSINGH (A.K.A. RAJIV CAVIN DOWANSINGH) AND TAMARA DAMARIS DOWANSINGH
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Overview [1] This is the judicial review of the denial of the Applicants’ refugee appeal by the Refugee Appeal Division [RAD], pursuant to section 110 of the Immigration and Refugee Protection Act (SC 2001, c 27) [the Act]. The Applicants, Rajiv and Tamara Dowansingh, are a married couple from Jamaica fearing persecution by supporters of the Jamaica Labour Party [JLP] because they refused to vote for the party in the 2011 national and local elections.

[2] The RAD upheld the rejection of the claim by the Refugee Protection Division [RPD], concluding that there were no “palpable and overriding errors” relating to the credibility findings by the RPD.

[3] For the reasons below, I find the RAD’s decision [Decision] to be reasonable, and dismiss the judicial review.
II. Credibility Findings by the RPD [4] The Applicants are citizens of Jamaica who did not vote in the national election in Jamaica in December 2011, or the local election in March 2011. They allege that the neighbourhood in which they lived was beset by organized gangs associated with the JLP, which had lost the elections to the People’s National Party [PNP].

[5] Mr. Dowansingh claims that in November 2012, he was attacked by JLP thugs for failing to vote, thereby helping bring the PNP into power. He allegedly reported the incident to the police, but no action was taken.

[6] At first instance, the RPD noted several material irregularities in the Applicants’ narrative which undermined their credibility.

[7] For example, the claimants obtained Canadian temporary visas which they used to visit Canada from October 9-26, 2012, and March 22-April 14, 2013. The second visit, notably, came after the supposed attack on Mr. Dowansingh, but a refugee claim was not made until January 2014, a month after arriving in Canada for a third time. Further, when the Applicants returned to Jamaica after their second trip in April 2013, they did not relocate until their latest entry into Canada in December 2013. Rather, the Applicants remained in the same house in the same district in which the assault had taken place, despite having immediate family living in other districts and sufficient financial means to remove themselves from danger (Application Record [AR], p. 50-51).

[8] Mr. Dowansingh also submitted a police letter documenting the alleged assault he suffered in November 2012, but the RPD determined that this was “not a trustworthy document” for several reasons (AR, p.53). The document did not contain an original ink signature, did not contain a file number, the crest appeared to have been printed by an ink jet printer and the document’s date post-dated the e refugee claim (AR, p. 50).
III. Analysis [9] The Applicants’ argument that the RAD’s Decision was unreasonable rests on the following premise - the RAD erred by applying the standard of intervention of “palpable and overriding error” to its review of the RPD’s conclusions.

[10] More particularly, the decision maker should have conducted an independent assessment of the police letter submitted by the Applicants, and decided independently whether it was genuine. The fact that the RAD did not do so tainted the remaining credibility findings, as the RAD’s view of the Applicants’ narrative may have taken a different tone had it believed in the veracity of the November 2012 assault.

[11] I will begin by acknowledging that the genuineness of a document must be independently assessed by the RAD. The RAD should not defer to the RPD’s conclusions on such matters, because the RPD is in no better a position to assess these documents than the RAD (Njeukam v Canada (Citizenship and Immigration), 2014 FC 859 at para 14; Kurtzmalaj v Canada (Citizenship and Immigration), 2014 FC 1072 at para 35; Sow v Canada (Citizenship and Immigration), 2015 FC 295 at para 13).

[12] Notwithstanding the RAD’s use of the standard of “palpable and overriding error” in its review of the entirety of the RPD decision, the RAD appears to have examined and come to an independent assessment of the police report for itself:

[19] “….the RPD did not accept the police report as being trustworthy, due to the numerous inconsistencies within the body of the report and the quality of the report in general. The RPD, in its reasons, cited clearly the concerns it had when looking at the police report. The RAD has reviewed the evidence in this area concerning the police report, where the RPD found it to be riddled with anomalies, and those were identified clearly in its reasons; as such, the RAD finds the RPD finding regarding the value of the police report to be reasonable in this circumstance.” (AR, p.11, emphasis added)

[13] As a general practice, the more detail the RAD can provide in its reasons about its thoughts on the most salient issues pertaining to personalized documentation and country conditions, as well as including country condition evidence and whether it agrees with or differs from the RPD’s assessment, the more likely a reviewing Court is to find that such evidence was independently assessed by the RAD.

[14] However, this does not mean that the RAD is confined to a mechanistic process in which it must detail how it arrived at all of its independent conclusions. Where the RPD’s factual findings are numerous, plainly obvious, and well-articulated, as is the case here regarding the authenticity of a document, then the RAD’s succinct acknowledgment of these concerns may be enough to demonstrate that it has conducted independent assessment.

[15] At the other end of the spectrum, if the RPD’s conclusions turn on other discrete observations, specialized expertise, and/or novel findings, then there is a greater need for the RAD to detail how it reached its conclusions on the evidence. In such cases, merely stating that the evidence was examined and concurring with the RPD may not reflect that an independent assessment has actually been conducted (Cepeda-Guiterrez v Canada (Minster of Citizenship and Immigration), 157 FTR 35; Ali v Canada (Citizenship and Immigration), 2015 FC 500 at para 9; Mestre v Canada (Citizenship and Immigration), 2015 FC 375 at para 15; Shahini v Canada (Citizenship and Immigration), 2012 FC 211 at para 15).

[16] In this case, the RAD explicitly stated in its reasons that it reviewed the evidence regarding the police letter, and noted the RPD “identified clearly in its reasons” that the letter was “riddled with anomalies”. In the context of this case, I take this to mean that the RAD reviewed the evidence and had the same concerns as the RPD regarding its authenticity. There is neither any point nor requirement to parrot the words of the panel in arriving at the same credibility-based findings.

[17] In any event, the RPD’s conclusions regarding the Applicants’ credibility rested on more pillars than merely the genuineness of the police report submitted. The RAD found “there is [sic] no palpable and overriding errors relating to the credibility assessment by the RPD” and that “[t]he RPD considered the Appellants’ delay in departure, their travel to Canada, and their re-availment to Jamaica. It concluded that their actions speak to a lack of subjective fear” (AR, p.11). The RAD further held that the negative credibility findings made by the RPD extended to section 97, as they went “not only to subjective fear, but also to the non-subjective fear concerns”.

[18] I find the RAD’s conclusions to be reasonable. Negative credibility findings made under section 96 may also affect the validity of a claim under section 97, even though subjective fear is not part of the assessment for the latter section (Mahadeva v Canada (Minister of Citizenship and Immigration), 2006 FC 415 at para 15). While the RPD could have performed a separate section 97 analysis, it would not have made a material difference. Specifically, I agree with the RAD that the Applicants’ behaviour, including their delay in making a claim and their re-availment to Jamaica, as well as implausibilities and inconsistencies in their narrative, so seriously undermined their overall credibility that these findings were applicable to both section 96 and section 97. The negative section 96 credibility finding obviated the need to consider the claim under section 97 (Restrepo Mejia v Canada (Citizenship and Immigration); 2010 FC 410 at para 20; Reza Gorostieta v Canada (Citizenship and Immigration), 2011 FC 343 at para 32; Nyathi v Canada (Minister of Citizenship and Immigration), 2003 FC 1119 at paras 21-24; El Achkar v Canada (Citizenship and Immigration), 2013 FC 472 at paras 38, 43-44).

[19] The Applicants argue that the RAD erred in assessing the RPD’s credibility findings on a “palpable and overriding error” standard. I begin by noting that certain case law holds this is indeed the standard of intervention on which the RAD should review credibility findings (see for instance, Spasoja v Canada (Citizenship and Immigration), 2014 FC 913 at para 40).

[20] In what has become the pre-eminent case on the standard of intervention by the RAD, Justice Phelan in Huruglica v Canada (Citizenship and Immigration), 2014 FC 799 at para 55, concluded that the RAD may “recognize and respect the conclusion of the RPD on such issues as credibility” but is not limited to “to intervening on facts only where there is a ‘palpable and overriding error’.” I endorsed this approach in Brodrick v Canada (Citizenship and Immigration), 2015 FC 491 at para 34.

[21] The Applicants argue that the RAD should have been less deferential to the RPD’s credibility findings in this case. The RAD should have “recognized and respected” the credibility determinations by the RPD, not reviewed them for “palpable and overriding errors”. In other words, the RAD wasn’t aware that it could have intervened in circumstances where the RPD made an error in a credibility determination which wasn’t obvious (palpable) or of crucial importance (overriding) (Canada v South Yukon Forest Corporation, 2012 FCA 165 at para 46).

[22] However, I do not see what difference that would have made in this case. This Court has repeatedly held that RPD’s conclusions on issues of credibility based on testimony clearly warrant some measure of deference (Denbel v Canada (Citizenship and Immigration), 2015 FC 629 at para 31; Ali v Canada (Citizenship and Immigration), 2015 FC 500 at para 8; Ngandu v Canada (Citizenship and Immigration), 2015 FC 423 at para 31). As a result of the numerous inconsistencies and implausibilities in the Applicants’ narrative, I fail to see a reviewable error in the RAD’s Decision not to intervene.

[23] Despite the very able arguments of counsel for the Applicants and best efforts to convince me that the matter needs to be returned for reconsideration, I see no basis upon which to do so. I, therefore, dismiss this application for judicial review.
JUDGMENT
THIS COURT’S JUDGMENT is that
1. This judicial review is dismissed.
2. There are no questions for certification.
3. There is no award as to costs.
“Alan S. Diner”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-6581-14
STYLE OF CAUSE:
RAJIC CAVIN DOWANSINGH (A.K.A. RAJIV CAVIN DOWANSINGH) AND TAMARA DAMARIS DOWANSINGH v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
July 6, 2015
JUDGMENT AND reasons:
DINER J.
DATED:
july 30, 2015
APPEARANCES:
Anthony Navaneelan
For The Applicants
Alex C. Kam
For The respondent
SOLICITORS OF RECORD:
Mamann, Sandaluk & Kingwell
Barristers and Solicitors
Toronto, Ontario
For The Applicants
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The respondent
