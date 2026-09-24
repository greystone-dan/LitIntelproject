# Discussion Units: case 2660

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **44**
- Continuity pairs: **43**
- Discussion Units: **4**
- Paragraph source hashes: **44**
- Sub-themes: **12**

## 2660:1 · paragraphs 0-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b472fe48eae6b466ae124928fab7754798e52357123760f701659b0c34f1b5a3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2660:1:subtheme:1 · paragraphs 0-8

- Raw key terms: `chhabu, canada, october, august, england, april, development, human`
- Display key terms: `chhabu, october, august, england, april, development, human`
- Argument roles: `disposition, evidence_fact, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, reasoning_application Display terms: chhabu, october, august, england, april, development, human Application context: Her son states that she has not travelled since 1998 because of her health. Operative outcome context: She re-entered Canada on August 31, 1987 and was granted landed immigrant status for a second time on October 22, 1987, based on a ten-year family class sponsorship by her son. Evidence spans paragraphs 0-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4189746` offsets `192-207`; context: [1] The Minister of Human Resources Development (the Minister) seeks judicial review of a decision of the Canada Pension Plan/Old Age Security Review Tribunal (the Review Tribunal) wherein it determined that the applicant, Mrs.
- Evidence: `disposition` cue `granted` at chunk `4189748` offsets `146-153`; context: She re-entered Canada on August 31, 1987 and was granted landed immigrant status for a second time on October 22, 1987, based on a ten-year family class sponsorship by her son.
- Evidence: `reasoning_application` cue `because` at chunk `4189751` offsets `226-233`; context: Her son states that she has not travelled since 1998 because of her health.
- Evidence: `evidence_fact` cue `determined that` at chunk `4189753` offsets `148-163`; context: As a result of this review, it was determined that Mrs.

#### 2660:1:subtheme:2 · paragraphs 9-11

- Raw key terms: `account, bank, chhabu, concluded, government, home, india, indian`
- Display key terms: `account, bank, chhabu, concluded, government, home, india, indian`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: account, bank, chhabu, concluded, government, home, india, indian Application context: The investigation officer's report (the investigation report) states that because she was landed in October 1987, on a ten-year family sponsorship by her son, she was not to receive assistance from the government by way  Operative outcome context: Her appeal was allowed. Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4189754` offsets `661-669`; context: Additionally, the fact that an Indian address was listed as her permanent residence in her passport brought her residency in Canadainto question.
- Evidence: `reasoning_application` cue `because` at chunk `4189754` offsets `181-188`; context: The investigation officer's report (the investigation report) states that because she was landed in October 1987, on a ten-year family sponsorship by her son, she was not to receive assistance from the government by way of pensions or social assistance until after the expiry of the sponsorship period.
- Evidence: `disposition` cue `allowed` at chunk `4189756` offsets `578-585`; context: Her appeal was allowed.

#### 2660:1:subtheme:3 · paragraphs 12-16

- Raw key terms: `canada, security, resident, application, curit, defined, established, home`
- Display key terms: `security, resident, curit, defined, established, home`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: security, resident, curit, defined, established, home Rule/authority context: [14] The circumstances under which a partial OAS pension is payable to an individual are set out in subsection 3(2) of the Act. | "Review Tribunal" means a Canada Pension Plan - Old Age Security Review Tribunal established under section 82 of the Canada Pension Plan; 2. Application context: The Minister concludes that Ms. Evidence spans paragraphs 12-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4189757` offsets `40-45`; context: [12] The Review Tribunal identified the issue as "whether [Mrs.
- Evidence: `evidence_fact` cue `evidence` at chunk `4189757` offsets `887-895`; context: We are sure that this residence is not evidence of a greater connection with India.
- Evidence: `reasoning_application` cue `concludes` at chunk `4189757` offsets `411-420`; context: The Minister concludes that Ms.
- Evidence: `counterargument_limitation` cue `but` at chunk `4189757` offsets `2004-2007`; context: She was clear that she lived with her son and daughter-in-law, but details were sometimes beyond her.
- Evidence: `governing_rule` cue `under` at chunk `4189759` offsets `23-28`; context: [14] The circumstances under which a partial OAS pension is payable to an individual are set out in subsection 3(2) of the Act.
- Evidence: `governing_rule` cue `under` at chunk `4189761` offsets `152-157`; context: "Review Tribunal" means a Canada Pension Plan - Old Age Security Review Tribunal established under section 82 of the Canada Pension Plan;
2.

#### 2660:1:subtheme:4 · paragraphs 17-18

- Raw key terms: `applicable, application, fact, mixed, questions, review, standard, acts`
- Display key terms: `applicable, fact, mixed, questions, review, standard, acts`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: applicable, fact, mixed, questions, review, standard, acts Rule/authority context: Therefore, there is no issue regarding the application of a standard of review by the Review Tribunal with respect to the decision under appeal. | As such, she claims that the applicable standard of review is that of reasonableness simpliciter. Application context: Therefore, there is no issue regarding the application of a standard of review by the Review Tribunal with respect to the decision under appeal. Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4189762` offsets `111-116`; context: Therefore, there is no issue regarding the application of a standard of review by the Review Tribunal with respect to the decision under appeal.
- Evidence: `governing_rule` cue `standard of review` at chunk `4189762` offsets `148-166`; context: Therefore, there is no issue regarding the application of a standard of review by the Review Tribunal with respect to the decision under appeal.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4189762` offsets `88-97`; context: Therefore, there is no issue regarding the application of a standard of review by the Review Tribunal with respect to the decision under appeal.
- Evidence: `issue` cue `whether` at chunk `4189763` offsets `52-59`; context: Chhabu contends that the determination of whether a person is resident in Canada involves questions of mixed fact and law.
- Evidence: `governing_rule` cue `standard of review` at chunk `4189763` offsets `356-374`; context: As such, she claims that the applicable standard of review is that of reasonableness simpliciter.

#### 2660:1:subtheme:5 · paragraphs 19-20

- Raw key terms: `canada, decision, however, review, tribunal, able, analysis, appeal`
- Display key terms: `however, review, able, analysis`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: however, review, able, analysis Position/evidence statements: I do note that the Minister, as the applicant in Ding, supra, argued that the question ought to be examined on a reasonableness standard (paragraph 22 of Ding). Rule/authority context: [19] It has been determined that where a Review Tribunal bases its decision as to residency on an individual's "intention", it has applied the wrong legal test and its decision will be reviewed on a standard of correctne | Rather, as noted earlier, the Review Tribunal is established under section 82 of the Canada Pension Plan, R. Application context: [19] It has been determined that where a Review Tribunal bases its decision as to residency on an individual's "intention", it has applied the wrong legal test and its decision will be reviewed on a standard of correctne Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4189764` offsets `507-515`; context: However, counsel have not pointed to, nor have I been able to find, any authority in which a pragmatic and functional analysis has been undertaken with respect to a decision of a Review Tribunal regarding the question of residency.
- Evidence: `party_position` cue `argued` at chunk `4189764` offsets `592-598`; context: I do note that the Minister, as the applicant in Ding, supra, argued that the question ought to be examined on a reasonableness standard (paragraph 22 of Ding).
- Evidence: `evidence_fact` cue `determined that` at chunk `4189764` offsets `17-32`; context: [19] It has been determined that where a Review Tribunal bases its decision as to residency on an individual's "intention", it has applied the wrong legal test and its decision will be reviewed on a standard of correctness: Canada(Minister of Human Resources Development) v.
- Evidence: `governing_rule` cue `legal test` at chunk `4189764` offsets `149-159`; context: [19] It has been determined that where a Review Tribunal bases its decision as to residency on an individual's "intention", it has applied the wrong legal test and its decision will be reviewed on a standard of correctness: Canada(Minister of Human Resources Development) v.
- Evidence: `reasoning_application` cue `applied` at chunk `4189764` offsets `131-138`; context: [19] It has been determined that where a Review Tribunal bases its decision as to residency on an individual's "intention", it has applied the wrong legal test and its decision will be reviewed on a standard of correctness: Canada(Minister of Human Resources Development) v.
- Evidence: `counterargument_limitation` cue `However` at chunk `4189764` offsets `298-305`; context: However, counsel have not pointed to, nor have I been able to find, any authority in which a pragmatic and functional analysis has been undertaken with respect to a decision of a Review Tribunal regarding the question of residency.
- Evidence: `governing_rule` cue `under` at chunk `4189765` offsets `130-135`; context: Rather, as noted earlier, the Review Tribunal is established under section 82 of the Canada Pension Plan, R.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4189765` offsets `419-425`; context: There is a privative clause of sorts, contained in subsection 84(1) of the CPP, the strength of which is bolstered by the fact that a decision of the Review Tribunal on an appeal under subsection 28(1) of the Act cannot be further appealed to a Pension Appeals Board (subsection 83(1) of the CPP).

#### 2660:1:subtheme:6 · paragraphs 21-22

- Raw key terms: `deference, however, thus, adjudication, administration, applicants, balanced, benefit`
- Display key terms: `deference, however, thus, adjudication, administration, balanced, benefit`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: deference, however, thus, adjudication, administration, balanced, benefit Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4189766` offsets `9-14`; context: [21] The issue of residency in relation to OAS eligibility is one that the Review Tribunal is regularly called upon to determine.
- Evidence: `counterargument_limitation` cue `however` at chunk `4189766` offsets `305-312`; context: In interpreting the definition of residency, however, the Court is equally or better positioned.
- Evidence: `counterargument_limitation` cue `however` at chunk `4189767` offsets `230-237`; context: The conferment of benefits, however, is balanced with the interests of fairness and financial responsibility.

#### 2660:1:subtheme:7 · paragraphs 23-24

- Raw key terms: `test, allegations, analysis, applicable, applying, arrived, brunswick, canada`
- Display key terms: `allegations, analysis, applicable, applying, arrived, brunswick`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: allegations, analysis, applicable, applying, arrived, brunswick Rule/authority context: [23] The nature of the question involves applying the correct legal test to various facts and is therefore one of mixed fact and law. | [24] Having regard to these factors, it is my view that the applicable standard of review is reasonableness. Application context: [23] The nature of the question involves applying the correct legal test to various facts and is therefore one of mixed fact and law. Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4189768` offsets `23-31`; context: [23] The nature of the question involves applying the correct legal test to various facts and is therefore one of mixed fact and law.
- Evidence: `evidence_fact` cue `determined that` at chunk `4189768` offsets `293-308`; context: ) wherein it was determined that residency is a question of fact to be determined in the particular circumstances).
- Evidence: `governing_rule` cue `legal test` at chunk `4189768` offsets `62-72`; context: [23] The nature of the question involves applying the correct legal test to various facts and is therefore one of mixed fact and law.
- Evidence: `reasoning_application` cue `therefore` at chunk `4189768` offsets `97-106`; context: [23] The nature of the question involves applying the correct legal test to various facts and is therefore one of mixed fact and law.
- Evidence: `evidence_fact` cue `evidence` at chunk `4189769` offsets `415-423`; context: 247 (Ryan) where he stated:
A decision will be unreasonable only if there is no line of analysis within the
given reasons that could reasonably lead the tribunal from the evidence before
it to the conclusion at which it arrived.
- Evidence: `governing_rule` cue `standard of review` at chunk `4189769` offsets `71-89`; context: [24] Having regard to these factors, it is my view that the applicable standard of review is reasonableness.

#### Section text

Canada (Minister of Human Resources Development) v. Chhabu
Court (s) Database
Federal Court Decisions
Date
2005-09-19
Neutral citation
2005 FC 1277
File numbers
T-2009-04
Decision Content
Date: 20050919
Docket: T-2009-04
Citation: 2005 FC 1277
Ottawa, Ontario, September 19, 2005
PRESENT: THE HONOURABLE MADAM JUSTICE LAYDEN-STEVENSON
BETWEEN:
MINISTER OF HUMAN RESOURCES DEVELOPMENT
Applicant
and
BIBI CHHABU
Respondent
REASONS FOR ORDER AND ORDER

[1] The Minister of Human Resources Development (the Minister) seeks judicial review of a decision of the Canada Pension Plan/Old Age Security Review Tribunal (the Review Tribunal) wherein it determined that the applicant, Mrs. Chhabu, for purposes of the Old Age Security Act, R.S.C. 1985, c. 0-9 (the Act), has been resident in Canada since October 4, 1986.
BACKGROUND

[2] Mrs. Chhabu is from India and she lives in Edmonton with her only son, Ismail Chhabu. She has been a Canadian citizen since April 2003. She first arrived in Canada as a landed immigrant on October 2, 1982. Over the next four years, she travelled between Canada, England (where two daughters reside) and Bombay, India. She stayed in India for more than two years (between July 1984 and October 1986) and re-entered Canada on a visitor's visa on October 4, 1986.

[3] Mrs. Chhabu left Canada again in June 1987 and travelled to Saudi Arabia, Egypt and England. She re-entered Canada on August 31, 1987 and was granted landed immigrant status for a second time on October 22, 1987, based on a ten-year family class sponsorship by her son.

[4] On April 29, 1992, Mrs. Chhabu yet again left Canadafor England. She left England on October 14, 1992. Her whereabouts in the years that followed are questioned by the Minister. The next stamp in her Canadian passport is a return stamp to Canada dated January 19, 1994. Her son states that she returned to Canada in October 1992 and left Canada in early January 1994, for a three-week visit to Chicago from which she returned on January 19, 1994. Her passport, according to her son, was simply not stamped to reflect her entry into Canada or the United States.

[5] On August 11, 1994, Mrs. Chhabu submitted an application for the Old Age Security (OAS) benefit. Her application did not reveal that she had obtained landed immigrant status for a second time in October 1987 and she was approved for a partial pension effective August 1994. As of October of the same year, she began receiving the Guaranteed Income Supplement (GIS).

[6] Mrs. Chhabu later visited South Africa and England and was absent from Canada from May to late August 1995. She visited England again between July and the fall of 1998. Her son states that she has not travelled since 1998 because of her health.

[7] During this time frame, Mrs. Chhabu held an Indian passport, which was issued in February 1982 and renewed in 1992. On March 3, 1992, she obtained a new Indian passport from the Consulate General of India in Vancouver on which it stated that she was a citizen of India. It listed her permanent residence as "Chabby St., Manipur, Broach, Guj, India". The passport was valid until February 16, 2002.

[8] Mrs. Chhabu's file was reviewed by Human Resources Development Canada (HRDC), as it then was, in April 1997. As a result of this review, it was determined that Mrs. Chhabu's earliest eligibility date was January 1995. She was notified by correspondence that she had been overpaid $2,739.40 for the period from August 1994 to December 1994 inclusive. This amount was recovered at the rate of $50.00 per month. A balance of $89.40 was still owing when her account was suspended in 2001 as a result of the review described in the paragraphs that follow.

[9] In November 2001, Mrs. Chhabu's file was again examined and her eligibility for benefits was reviewed. The investigation officer's report (the investigation report) states that because she was landed in October 1987, on a ten-year family sponsorship by her son, she was not to receive assistance from the government by way of pensions or social assistance until after the expiry of the sponsorship period. Thus, it was concluded that she was not eligible to receive government assistance until at least October 22, 1997. Additionally, the fact that an Indian address was listed as her permanent residence in her passport brought her residency in Canadainto question.

[10] The investigating officer requested an interview with Mrs. Chhabu. A government employee agreed to act as an interpreter. In response to the officer's questions, Mrs. Chhabu stated, among other things, that she, along with her son and daughters, owned the home in India that was listed as her permanent residence. She said that a tenant lived in the house from whom she received rent money that was placed in her Indian bank account. She also stated that she lived with her daughter in England for two years between April 1992 and January 1994. The translator expressed the belief that, at times, Mrs. Chhabu was being evasive with her answers and refused to answer some of the questions put to her. In the investigation report, the officer noted that "[f]or the questions that [Mrs. Chhabu] did answer, she was lucid and had no trouble recollecting dates and places she had been. At no time did she appear confused or ask for clarification".

[11] The investigator concluded that Mrs. Chhabu had not severed her ties from India as she still owned a home and other household effects and held a bank account there. Mrs. Chhabu was informed by HRDC correspondence dated June 6, 2002, that she was overpaid and was required to reimburse the sum of $73,507.70 in OAS and GIS for January 1995 to October 2001, inclusive. She requested that the Minister reconsider that determination. The HRDC's review by the ministerial delegate maintained the original decision and Mrs. Chhabu appealed to the Review Tribunal. Her appeal was allowed.
THE DECISION

[12] The Review Tribunal identified the issue as "whether [Mrs. Chhabu] has ever established residence in Canada and if so, when". It concluded that she "became a resident of Canada in October 1986 and has remained a resident of Canada since that time. Her eligibility for OAS and GIS should be recalculated on that basis". The salient portions of the Review Tribunal's findings are set out below.
The Minister concludes that Ms. Chhabu was not a resident of Canada for Income Security purposes as her ties with India were greater than her ties with Canada as she had not given up her residence in India. The property in India is not owned by the Appellant. She is one of the titleholders of a property originally owned by 4 brothers, one of whom was her husband. It is held as a family property for any member's use during visits to the homeland. We are sure that this residence is not evidence of a greater connection with India. In Canada, she resides with her only son and his family. Two daughters live in England, while the other lives near the family home in India.
Mr. Chhabu testifies that his mother always intended to make Canada her home from the time that she first came in October 1982. Certainly it was Mr. Chhabu's intention to have his widowed mother as a member of his household from that time forward. The Appellant was unable to understand our questions despite the interpreter's able assistance. She would sometimes go into her religious language.
The investigator reports similar occurrences during the interview conducted with the Appellant in May 2002. The clear subtext to the report of the investigation (pages 75-83, hearing case file) and interview (pages 85-95) was that the evasion was intentional and dishonest. Based on the testimony before us, we conclude that the Appellant is not always aware of her condition. She was unable to explain the purpose of the proceedings or comprehend more complex questions. She was clear that she lived with her son and daughter-in-law, but details were sometimes beyond her. We are convinced that theses aspects of dementia were also at the root of the evasion during the interview.
We are convinced that the Appellant has been resident in Canada as defined by the Act since her entry October 4, 1986. She abandoned her wavering on residence at that time in Canada's favour and has not interrupted it since. Her trips out of country were temporary and limited in duration. The lack of tax returns and SIN until collecting OAS and GIS is easily understood in light of her age (67) when she established residence. Aside from the continuing presence of family in India, there are no strong ties to that country.
RELEVANT STATUTORY PROVISIONS

[13] The relevant statutory provisions are attached to these reasons as Schedule "A". For ease of reference, the most pertinent provisions are discussed and reproduced here.

[14] The circumstances under which a partial OAS pension is payable to an individual are set out in subsection 3(2) of the Act.
Old Age Security Act,
R.S.C. 1985, c. 0-9
3.(2) Subject to this Act and the regulations, a partial monthly pension may be paid for any month in a payment quarter to every person who is not eligible for a full monthly pension under subsection (1) and
(a) has attained sixty-five years of age; and
(b) has resided in Canada after attaining eighteen years of age and prior to the day on which that person's application is approved for an aggregate period of at least ten years but less than forty years and, where that aggregate period is less than twenty years, was resident in Canada on the day preceding the day on which that person's application is approved.
Loi sur la sécurité de la vieillesse,
L.R.C. (1985), ch. O-9
3. (2) Sous réserve des autres dispositions de la présente loi et de ses règlements, une pension partielle est payable aux personnes qui ne peuvent bénéficier de la pleine pension et qui, à la fois :
a) ont au moins soixante-cinq ans;
b) ont, après l'âge de dix-huit ans, résidé en tout au Canada pendant au moins dix ans mais moins de quarante ans avant la date d'agrément de leur demande et, si la période totale de résidence est inférieure à vingt ans, résidaient au Canada le jour précédant la date d'agrément de leur demande.

[15] The term "resided", as it is used in paragraph 3(2)(b) of the Act, is not defined in the Act but is described in the Old Age Security Regulations, C.R.C., c. 1246 as:
21. (1) For the purposes of the Act and these Regulations,
(a) a person resides in Canada if he makes his home and ordinarily lives in any part of Canada; and
(b) a person is present in Canada when he is physically present in any part of Canada.
[...]
(4) Any interval of absence from Canada of a person resident in Canada that is
(a) of a temporary nature and does not exceed one year,
(b) for the purpose of attending a school or university, or
(c) specified in subsection (5)
shall be deemed not to have interrupted that person's residence or presence in Canada.
21. (1) Aux fins de la Loi et du présent règlement,
a) une personne réside au Canada si elle établit sa demeure et vit ordinairement dans une région du Canada; et
b) une personne est présente au Canada lorsqu'elle se trouve physiquement dans une région du Canada.
[...]
(4) Lorsqu'une personne qui réside au Canada s'absente du Canada et que son absence
a) est temporaire et ne dépasse pas un an,
b) a pour motif la fréquentation d'une école ou d'une université, ou
c) compte parmi les absences mentionnées au paragraphe (5),
cette absence est réputée n'avoir pas interrompu la résidence ou la présence de cette personne au Canada.

[16] Section 2 of the Act defines "Review Tribunal" as:
2. "Review Tribunal" means a Canada Pension Plan - Old Age Security Review Tribunal established under section 82 of the Canada Pension Plan;
2. « tribunal de révision » Tribunal de révision Régime de pensions du Canada - Sécurité de la vieillesse constitué en application de l'article 82 du Régime de pensions du Canada.
THE STANDARD OF REVIEW

[17] The parties agree that the appeal before the Review Tribunal is a de novo hearing. Therefore, there is no issue regarding the application of a standard of review by the Review Tribunal with respect to the decision under appeal. Regarding the Review Tribunal's decision that is the subject of this application, the Minister urges me to apply the same standard of review that is applicable to matters involving the Pension Appeals Board. The Minister maintains that the Review Tribunal is analogous to the Pension Appeals Board and the two Acts interrelate. Thus, it is said that the appropriate standard of review is correctness for questions of law and patent unreasonableness for questions of mixed fact and law.

[18] Mrs. Chhabu contends that the determination of whether a person is resident in Canada involves questions of mixed fact and law. She submits that it involves both an assessment of the facts surrounding an individual's circumstances and the application of the legal definition of residence as set out in the Act. As such, she claims that the applicable standard of review is that of reasonableness simpliciter.

[19] It has been determined that where a Review Tribunal bases its decision as to residency on an individual's "intention", it has applied the wrong legal test and its decision will be reviewed on a standard of correctness: Canada(Minister of Human Resources Development) v. Ding2005 FC 76 (Ding). However, counsel have not pointed to, nor have I been able to find, any authority in which a pragmatic and functional analysis has been undertaken with respect to a decision of a Review Tribunal regarding the question of residency. I do note that the Minister, as the applicant in Ding, supra, argued that the question ought to be examined on a reasonableness standard (paragraph 22 of Ding).

[20] The powers of the Review Tribunal are not contained in the Act. Rather, as noted earlier, the Review Tribunal is established under section 82 of the Canada Pension Plan, R.S.C. 1985,
c. C-8 (the CPP). There is a privative clause of sorts, contained in subsection 84(1) of the CPP, the strength of which is bolstered by the fact that a decision of the Review Tribunal on an appeal under subsection 28(1) of the Act cannot be further appealed to a Pension Appeals Board (subsection 83(1) of the CPP). Subsection 84(1) of the CPP and subsection 28(3) of the Act do, however, explicitly recognize judicial review of a Review Tribunal's decision. Nonetheless, the presence of this privative clause does suggest deference to a Review Tribunal's decision determining an appeal under the Act.

[21] The issue of residency in relation to OAS eligibility is one that the Review Tribunal is regularly called upon to determine. The factual circumstances of each case call for findings that fall within its expertise and thus militate in favour of deference. In interpreting the definition of residency, however, the Court is equally or better positioned.

[22] The Act confers a benefit to certain individuals and establishes who is entitled to the receipt of benefits and to what extent. To that end, it involves the adjudication of an individual's rights. The conferment of benefits, however, is balanced with the interests of fairness and financial responsibility. The Minister is charged with the administration and integrity of the Act and the public interest in ensuring that applicants are not paid benefits to which they are not entitled. Thus, the Act provides for the adjudication of individual rights but is also polycentric in nature. This factor results in neither a high nor a low degree of deference.

[23] The nature of the question involves applying the correct legal test to various facts and is therefore one of mixed fact and law. It is more factually than legally driven (see: Ding, supra and Perera v. Canada(Minister of Health and Welfare)(1994), 75 F.T.R. 310 (F.C.T.D.) wherein it was determined that residency is a question of fact to be determined in the particular circumstances). This factor favours more deference.

[24] Having regard to these factors, it is my view that the applicable standard of review is reasonableness. Consequently, I must have regard to the test set out by Mr. Justice Iacobocci in Law Society of New Brunswick v. Ryan, [2003] 1 S.C.R. 247 (Ryan) where he stated:
A decision will be unreasonable only if there is no line of analysis within the
given reasons that could reasonably lead the tribunal from the evidence before
it to the conclusion at which it arrived. If any of the reasons that are sufficient
to support the conclusion are tenable in the sense that they can stand up to a
somewhat probing examination, then the decision will not be unreasonable and
a reviewing court must not interfere (see Southam, [1997] 1 S.C.R. 748 at para.
56). This means that a decision may satisfy the reasonableness standard if it is
supported by a tenable explanation even if this explanation is not one that the
reviewing court finds compelling (see Southam, at para. 79).
THE ALLEGATIONS OF ERROR

## 2660:2 · paragraphs 25-40

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0282af8b96cf04c348138ad87673f4bb12cde0a2fdb299cd21f721f066958d47`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2660:2:subtheme:1 · paragraphs 25-26

- Raw key terms: `assessment, canada, chhabu's, complete, factors, intention, minister, reasons`
- Display key terms: `assessment, chhabu's, complete, factors, intention`
- Argument roles: `counterargument_limitation, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, reasoning_application Display terms: assessment, chhabu's, complete, factors, intention Application context: The Minister asserts that because the notion of "intention" was worthy of mention in the Review Tribunal's reasons, it constitutes an indication that intention was the primary factor in its determination. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4189770` offsets `743-750`; context: The Minister asserts that because the notion of "intention" was worthy of mention in the Review Tribunal's reasons, it constitutes an indication that intention was the primary factor in its determination.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4189770` offsets `562-568`; context: It is argued that Ding stands for the proposition that "intention" cannot be regarded as the basis for a determination of residency.
- Evidence: `evidence_fact` cue `evidence` at chunk `4189771` offsets `124-132`; context: Chhabu's evidence was that he always intended for his mother to make Canada her home from the time she first landed in October 1982.

#### 2660:2:subtheme:2 · paragraphs 27-35

- Raw key terms: `review, tribunal, minister, finding, chhabu, evidence, reasons, tribunal's`
- Display key terms: `review, finding, chhabu, tribunal's`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: review, finding, chhabu, tribunal's Rule/authority context: The Review Tribunal is, by virtue of subsection 82(11) of the CPP, under a statutory duty to provide reasons. Application context: R 869 (the reasoning regarding the content of reasons has been applied in the context of administrative law), the Supreme Court stated that an unsuccessful party should not be left in doubt as to why that party was not s | [32] The Minister urges me to conclude that Ding, supra, and Thomson v. Evidence spans paragraphs 27-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4189772` offsets `24-29`; context: [27] The Minister takes issue with the Review Tribunal's finding that Mrs.
- Evidence: `evidence_fact` cue `evidence` at chunk `4189772` offsets `111-119`; context: Chhabu's residence in India "is not evidence of a greater connection with India".
- Evidence: `governing_rule` cue `under` at chunk `4189775` offsets `156-161`; context: The Review Tribunal is, by virtue of subsection 82(11) of the CPP, under a statutory duty to provide reasons.
- Evidence: `reasoning_application` cue `applied` at chunk `4189776` offsets `118-125`; context: R 869 (the reasoning regarding the content of reasons has been applied in the context of administrative law), the Supreme Court stated that an unsuccessful party should not be left in doubt as to why that party was not successful.
- Evidence: `reasoning_application` cue `conclude` at chunk `4189777` offsets `30-38`; context: [32] The Minister urges me to conclude that Ding, supra, and Thomson v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4189778` offsets `112-120`; context: Chhabu] is supported by the evidence.
- Evidence: `reasoning_application` cue `conclude` at chunk `4189778` offsets `340-348`; context: It was not unreasonable for the Review Tribunal to conclude that the home was a shared property used by various family members to hang their hats while visiting India.
- Evidence: `evidence_fact` cue `record` at chunk `4189779` offsets `391-397`; context: Although it is not evident on the record, at the hearing of the judicial review application counsel advised that, at the outset of the appeal, the Review Tribunal conducted a voir dire to determine Mrs.
- Evidence: `reasoning_application` cue `because` at chunk `4189779` offsets `40-47`; context: [34] The "dementia" is more problematic because of the retroactivity the Review Tribunal assigned to its finding.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4189779` offsets `357-365`; context: Although it is not evident on the record, at the hearing of the judicial review application counsel advised that, at the outset of the appeal, the Review Tribunal conducted a voir dire to determine Mrs.
- Evidence: `evidence_fact` cue `testimony` at chunk `4189780` offsets `100-109`; context: Chhabu's testimony before it, "these aspects of dementia were also at the root of the evasion during the interview".
- Evidence: `counterargument_limitation` cue `However` at chunk `4189780` offsets `823-830`; context: However, the Review Tribunal had a duty to provide reasons or some form of analysis for its ruling.

#### 2660:2:subtheme:3 · paragraphs 36-40

- Raw key terms: `review, evidence, tribunal, adequately, chhabu's, tribunal's, without, address`
- Display key terms: `review, adequately, chhabu's, tribunal's, without, address`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: review, adequately, chhabu's, tribunal's, without, address Rule/authority context: In short, the reasons under scrutiny do not withstand a somewhat probing examination. | [40] Finally, should I be in error in my pragmatic and functional analysis regarding the applicable standard of review, I would arrive at the same result were the applicable standard that of patent unreasonableness. Application context: The reasons do not adequately discharge the Review Tribunal's statutory duty to analyse the evidence before it and are therefore unreasonable. | Absent guidance, I am left to speculate and again, I find that the Review Tribunal's failure to adequately analyse the evidence in relation to this issue renders its finding unreasonable. Evidence spans paragraphs 36-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4189781` offsets `101-107`; context: [36] The error in this respect is further compounded by the Review Tribunal's failure to address the issues surrounding Mrs.
- Evidence: `evidence_fact` cue `evidence` at chunk `4189781` offsets `329-337`; context: Again, there was evidence, from both sides, relevant to these factors and it may well be that the 1992 passport and alleged Indian bank accounts would have had no impact on the Review Tribunal's ultimate conclusion.
- Evidence: `reasoning_application` cue `therefore` at chunk `4189781` offsets `820-829`; context: The reasons do not adequately discharge the Review Tribunal's statutory duty to analyse the evidence before it and are therefore unreasonable.
- Evidence: `counterargument_limitation` cue `However` at chunk `4189781` offsets `528-535`; context: However, it was not, in my view, open to the Review Tribunal to simply ignore these factors relied on by the Minister without some explanation as to why it discounted them.
- Evidence: `issue` cue `issue` at chunk `4189782` offsets `743-748`; context: Absent guidance, I am left to speculate and again, I find that the Review Tribunal's failure to adequately analyse the evidence in relation to this issue renders its finding unreasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4189782` offsets `540-548`; context: Am I to assume that the Review Tribunal accepted the evidence of Mr.
- Evidence: `reasoning_application` cue `I find` at chunk `4189782` offsets `646-652`; context: Absent guidance, I am left to speculate and again, I find that the Review Tribunal's failure to adequately analyse the evidence in relation to this issue renders its finding unreasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4189783` offsets `532-540`; context: While that may well be so, it does not trump the test enunciated in Ryan, supra, for there must be a line of analysis within the given reasons that could reasonably lead the tribunal, from the evidence before it, to the conclusion at which it arrived (emphasis added).
- Evidence: `governing_rule` cue `under` at chunk `4189783` offsets `709-714`; context: In short, the reasons under scrutiny do not withstand a somewhat probing examination.
- Evidence: `evidence_fact` cue `evidence` at chunk `4189784` offsets `378-386`; context: Chhabu were the unsuccessful party, she would have every right to complain that the Review Tribunal had not adequately explained the basis of its decision and that her submissions and evidence had not been properly considered.
- Evidence: `counterargument_limitation` cue `However` at chunk `4189784` offsets `141-148`; context: However, if the shoe were on the other foot and Mrs.
- Evidence: `governing_rule` cue `standard of review` at chunk `4189785` offsets `100-118`; context: [40] Finally, should I be in error in my pragmatic and functional analysis regarding the applicable standard of review, I would arrive at the same result were the applicable standard that of patent unreasonableness.

#### Section text

[25] The Minister contends that the Review Tribunal erred:
(a) when it considered Mrs. Chhabu's "intention" to reside in Canada with her son as a factor in determining her place of residence; and
(b) in failing to undertake a complete assessment of the relevant factors.
ANALYSIS
Intention
Relying on Ding, supra, the Minister submits that the Review Tribunal erred when it considered Mrs. Chhabu's "intention" to reside in Canada with her son as a factor in determining her place of residence. It is argued that Ding stands for the proposition that "intention" cannot be regarded as the basis for a determination of residency. Rather, residence depends upon objective factors external to the individual's intention. The Minister asserts that because the notion of "intention" was worthy of mention in the Review Tribunal's reasons, it constitutes an indication that intention was the primary factor in its determination.

[26] I do not view the Review Tribunal's comments regarding "intention" through the same lens as the Minister. Mr. Chhabu's evidence was that he always intended for his mother to make Canada her home from the time she first landed in October 1982. The Review Tribunal was merely describing that evidence. It is implicit in its reasons that it did not take the son's intention to be determinative since it concluded that Mrs. Chhabu did not become a resident until 1986.
Failure to undertake a complete assessment of relevant factors

[27] The Minister takes issue with the Review Tribunal's finding that Mrs. Chhabu's residence in India "is not evidence of a greater connection with India". In this respect it is said that the Review Tribunal failed to have regard to other important and relevant factors such as Mrs. Chhabu's furniture, her bank accounts, her passports and her absences from Canada (particularly her absence of more than a year when she left England in October, 1992 and appeared to have returned to Canada on January 19, 1994).

[28] Additionally, the Minister takes exception to the Review Tribunal's observations with respect to Mrs. Chhabu suffering from "aspects of dementia" and asserts that there were no documents filed upon which such a finding could be made.

[29] In sum, the Minister claims that the Review Tribunal totally disregarded the contents of the investigation report. That approach was not available to it in the absence of a clear analysis outlining its reasons for rejecting it.

[30] The Minister's submissions, put another way, relate to the adequacy of the reasons.
The Review Tribunal is, by virtue of subsection 82(11) of the CPP, under a statutory duty to provide reasons. I agree that, here, its reasons are laconic. That said, it is not every failure or deficiency that will result in a successful application for judicial review. The reasons need only be sufficiently developed to understand the basis for the decision.

[31] In the criminal case R. v. Sheppard, [2002] 1 S.C.R 869 (the reasoning regarding the content of reasons has been applied in the context of administrative law), the Supreme Court stated that an unsuccessful party should not be left in doubt as to why that party was not successful. In Lai v. Canada (Minister of Citizenship and Immigration) (2000), 188 F.T.R. 113 (F.C.T.D.), Mr. Justice Pelletier, then of the Trial Division as it was then constituted, explained that the reasons of the tribunal must explain to the parties why the tribunal decided as it did and must also be sufficient to enable the reviewing court to discharge its function.

[32] The Minister urges me to conclude that Ding, supra, and Thomson v. Canada (Minister of National Revenue - M.N.R.), [1946] S.C.R. 209 dictate that a number of factors - ties in the form of personal property, regularity and length of stay in Canada, frequency and length of absences from Canada - must be considered in making a determination regarding residency. I agree that such factors are significant but they are not exhaustive and the ultimate determination must be made having regard to all the circumstances.

[33] The Review Tribunal's finding that the property in India is not owned by [Mrs. Chhabu] is supported by the evidence. The documentary evidence presented to the Review Tribunal demonstrates that the title to the house in India is held in her name along with eight other family members. It was not unreasonable for the Review Tribunal to conclude that the home was a shared property used by various family members to hang their hats while visiting India. The finding is further supported by the lack of evidence that Mrs. Chhabu spent any time in India after October 1986. While the Review Tribunal did not explicitly refer to the furniture contained within the house in India, in my view, it is fair to infer that the same reasoning applies to it.

[34] The "dementia" is more problematic because of the retroactivity the Review Tribunal assigned to its finding. I do not believe, as the Minister suggests, that the Review Tribunal attributed a medical diagnosis of "dementia" to Mrs. Chhabu. Rather, it used the term "dementia" to describe her lack of capacity to recall details and respond to questions. Although it is not evident on the record, at the hearing of the judicial review application counsel advised that, at the outset of the appeal, the Review Tribunal conducted a voir dire to determine Mrs. Chhabu's capacity. It is entirely within the purview of the Review Tribunal to assess the demeanour and the capacity of a witness before it. Moreover, there is evidence to the effect that when the Review Tribunal indicated that further questioning of Mrs. Chhabu would be futile, the Minister's representative was not opposed.

[35] The difficulty arises from the Review Tribunal's conclusion that, as a result of Mrs. Chhabu's testimony before it, "these aspects of dementia were also at the root of the evasion during the interview". The interview was conducted in May 2002 and the appeal was heard in September 2004. It appears that the Review Tribunal discounted Mrs. Chhabu's responses at the interview on the basis of her responses at the time of the hearing of the appeal. There is no explanation or analysis of the evidence relied upon by the Review Tribunal to arrive at this result. I do not suggest that it was not open to the Review Tribunal to find, on the evidence before it, that Mrs. Chhabu was likely incapacitated at the time of her interview. Indeed, it may well have arrived at the same determination had it analysed the evidence. However, the Review Tribunal had a duty to provide reasons or some form of analysis for its ruling. It came to a conclusion without explaining the factors upon which that conclusion was based. This renders the finding unreasonable.

[36] The error in this respect is further compounded by the Review Tribunal's failure to address the issues surrounding Mrs. Chhabu's 1992 passport and her Indian bank accounts. I presume that this omission has its genesis in the Review Tribunal's determination regarding Mrs. Chhabu's capacity or lack thereof. Again, there was evidence, from both sides, relevant to these factors and it may well be that the 1992 passport and alleged Indian bank accounts would have had no impact on the Review Tribunal's ultimate conclusion. However, it was not, in my view, open to the Review Tribunal to simply ignore these factors relied on by the Minister without some explanation as to why it discounted them. The reasons do not adequately discharge the Review Tribunal's statutory duty to analyse the evidence before it and are therefore unreasonable.

[37] I am also perplexed by the Review Tribunal's finding that Mrs. Chhabu's absences from Canada after 1986 were "temporary and limited in duration" without any further explanation. Of particular concern is its failure to address explicitly the matter of Mrs. Chhabu's whereabouts between October 1992 (when, according to her stamped passport, she left Manchester, England after a six-month stay there) and January 1994 (the next stamp in the passport reflecting an entry into Canada). Am I to assume that the Review Tribunal accepted the evidence of Mr. Chhabu to arrive at its determination? Absent guidance, I am left to speculate and again, I find that the Review Tribunal's failure to adequately analyse the evidence in relation to this issue renders its finding unreasonable.

[38] In coming to my conclusions, I have considered the articulate and forceful submissions of Mrs. Chhabu's counsel that both parties, by their respective representatives, were fully engaged in the process leading to the decision with the result that neither is left without knowing why the Review Tribunal came to the conclusion it did. While that may well be so, it does not trump the test enunciated in Ryan, supra, for there must be a line of analysis within the given reasons that could reasonably lead the tribunal, from the evidence before it, to the conclusion at which it arrived (emphasis added). That analysis is, for the most part, missing in the Review Tribunal's reasons. In short, the reasons under scrutiny do not withstand a somewhat probing examination.

[39] I also appreciate counsel's submission that Mrs. Chhabu has expended time and incurred expense in dealing with this proceeding to date. However, if the shoe were on the other foot and Mrs. Chhabu were the unsuccessful party, she would have every right to complain that the Review Tribunal had not adequately explained the basis of its decision and that her submissions and evidence had not been properly considered. The Minister, as a litigant, is no less entitled.

[40] Finally, should I be in error in my pragmatic and functional analysis regarding the applicable standard of review, I would arrive at the same result were the applicable standard that of patent unreasonableness.


## 2660:3 · paragraphs 41-42

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ce94f2ce5a998e7420593a131b8adb07ff4cb4f48371d8f29b88ca162d1f6ab0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2660:3:subtheme:1 · paragraphs 41-42

- Raw key terms: `bibi, cause, chhabu, date, development, human, minister, place`
- Display key terms: `bibi, chhabu, date, development, human, place`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: bibi, chhabu, date, development, human, place No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 41-42. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
THIS COURT ORDERS THAT the application for judicial review is allowed and the matter is remitted to a differently constituted Review Tribunal for redetermination.
"Carolyn Layden Stevenson"
Judge
SCHEDULE "A"
to the
Reasons for order dated September 19, 2005
In
MINISTER OF HUMAN RESOURCES DEVELOPMENT
and
BIBI CHHABU
T-2009-04
Old Age Security Act,
R.S.C. 1985, c. 0-9
2. "Review Tribunal" means a Canada Pension Plan - Old Age Security Review Tribunal established under section 82 of the Canada Pension Plan;
Loi sur la sécurité de la vieillesse,
L.R.C. (1985), c. 0-9
2. « tribunal de révision » Tribunal de révision Régime de pensions du Canada - Sécurité de la vieillesse constitué en application de l'article 82 du Régime de pensions du Canada.
3.(2) Subject to this Act and the regulations, a partial monthly pension may be paid for any month in a payment quarter to every person who is not eligible for a full monthly pension under subsection (1) and
(a) has attained sixty-five years of age; and
(b) has resided in Canada after attaining eighteen years of age and prior to the day on which that person's application is approved for an aggregate period of at least ten years but less than forty years and, where that aggregate period is less than twenty years, was resident in Canada on the day preceding the day on which that person's application is approved.
27.1 (1) A person who is dissatisfied with a decision or determination made under this Act that no benefit may be paid to that person, or respecting the amount of any benefit that may be paid to that person, may, within ninety days after the day on which the person is notified in the prescribed manner of the decision or determination, or within such longer period as the Minister may either before or after the expiration of those ninety days allow, make a request to the Minister in the prescribed form and manner for a reconsideration of that decision or determination.
(2) The Minister shall, without delay after receiving a request referred to in subsection (1), reconsider the decision or determination, as the case may be, and may confirm or vary it and may approve payment of a benefit, determine the amount of a benefit or determine that no benefit is payable and shall without delay notify the person who made the request in writing of the Minister's decision and of the reasons for the decision.
28.1 (1) Where an application for a benefit is made on behalf of a person and the Minister is satisfied, on the basis of evidence provided by or on behalf of that person, that the person was incapable of forming or expressing an intention to make an application on the person's own behalf on the day on which the application was actually made, the Minister may deem the application to have been made in the month preceding the first month in which the relevant benefit could have commenced to be paid or in the month that the Minister considers the person's last relevant period of incapacity to have commenced, whichever is the later.
[...]
(3) For the purposes of subsections (1) and (2), a period of incapacity must be a continuous period, except as otherwise prescribed.
CanadaPension Plan,
R.S.C. 1985, c. C-8
82. (1) A party who is dissatisfied with a decision of the Minister made under section 81 or subsection 84(2), or a person who is dissatisfied with a decision of the Minister made under subsection 27.1(2) of the Old Age Security Act, or, subject to the regulations, any person on their behalf, may appeal the decision to a Review Tribunal in writing within 90 days, or any longer period that the Commissioner of Review Tribunals may, either before or after the expiration of those 90 days, allow, after the day on which the party was notified in the prescribed manner of the decision or the person was notified in writing of the Minister's decision and of the reasons for it.
(2) A Review Tribunal shall be constituted in accordance with this section.
(3) The Governor in Council shall appoint a panel of between one hundred and four hundred persons resident in Canada, in such a way that, at any given time,
(a) at least twenty-five per cent of the members of the panel are members of the bar of a province;
(b) at least twenty-five per cent of the members of the panel are persons qualified to practise medicine or a prescribed related profession in a province; and
(c) there are members of the panel from every region of Canada.
(4) A person shall be appointed to the panel pursuant to subsection (3) for a term of at least two but not exceeding five years and is eligible for re-appointment on the expiration of his term.
(5) The Governor in Council shall appoint a Commissioner of Review Tribunals and a Deputy Commissioner of Review Tribunals, each for a term of at least two but not exceeding five years, and the Commissioner and Deputy Commissioner are eligible for re-appointment on the expiration of their respective terms.
(6) In the event of the absence or incapacity of the Commissioner of Review Tribunals or if the office of Commissioner is vacant, the Deputy Commissioner of Review Tribunals has all the powers of the Commissioner.
(7) Each Review Tribunal shall consist of three persons chosen by the Commissioner from among the members of the panel referred to in subsection (3), subject to the following requirements:
(a) the Commissioner must designate a member of the bar of a province as the Chairman of the Review Tribunal; and
(b) where the appeal to be heard involves a disability benefit, at least one member of the Review Tribunal must be a person qualified to practise medicine or a prescribed related profession in a province.
(8) An appeal to a Review Tribunal shall be heard at such place in Canada as is fixed by the Commissioner, having regard to the convenience of the appellant, the Minister, and any other person added as a party to the appeal pursuant to subsection (10).
[...]
(11) A Review Tribunal may confirm or vary a decision of the Minister made under section 81 or subsection 84(2) or under subsection 27.1(2) of the Old Age Security Act and may take any action in relation to any of those decisions that might have been taken by the Minister under that section or either of those subsections, and the Commissioner of Review Tribunals shall thereupon notify the Minister and the other parties to the appeal of the Review Tribunal's decision and of the reasons for its decision.
(12) A decision of the majority of the members of a Review Tribunal is a decision of the Tribunal.
83. (1) A party or, subject to the regulations, any person on behalf thereof, or the Minister, if dissatisfied with a decision of a Review Tribunal made under section 82, other than a decision made in respect of an appeal referred to in subsection 28(1) of the Old Age Security Act, or under subsection 84(2), may, within ninety days after the day on which that decision was communicated to the party or Minister, or within such longer period as the Chairman or Vice-Chairman of the Pension Appeals Board may either before or after the expiration of those ninety days allow, apply in writing to the Chairman or Vice-Chairman for leave to appeal that decision to the Pension Appeals Board.
84. (1) A Review Tribunal and the Pension Appeals Board have authority to determine any question of law or fact as to
(a) whether any benefit is payable to a person,
[...]
and the decision of a Review Tribunal, except as provided in this Act, or the decision of the Pension Appeals Board, except for judicial review under the Federal Courts Act, as the case may be, is final and binding for all purposes of this Act.
Old Age Security Regulations,
C.R.C., c. 1246
21. (1) For the purposes of the Act and these Regulations,
(a) a person resides in Canada if he makes his home and ordinarily lives in any part of Canada; and
(b) a person is present in Canada when he is physically present in any part of Canada.
[...]
(4) Any interval of absence from Canada of a person resident in Canada that is
(a) of a temporary nature and does not exceed one year,
(b) for the purpose of attending a school or university, or
(c) specified in subsection (5)
shall be deemed not to have interrupted that person's residence or presence in Canada.
3.(2) Sous réserve des autres dispositions de la présente loi et de ses règlements, une pension partielle est payable aux personnes qui ne peuvent bénéficier de la pleine pension et qui, à la fois :
a) ont au moins soixante-cinq ans;
b) ont, après l'âge de dix-huit ans, résidé en tout au Canada pendant au moins dix ans mais moins de quarante ans avant la date d'agrément de leur demande et, si la période totale de résidence est inférieure à vingt ans, résidaient au Canada le jour précédant la date d'agrément de leur demande.
27.1 (1) La personne qui se croit lésée par une décision de refus ou de liquidation de la prestation prise en application de la présente loi peut, dans les quatre-vingt-dix jours suivant la notification de la décision, selon les modalités réglementaires, ou dans le délai plus long que le ministre peut accorder avant ou après l'expiration du délai de quatre-vingt-dix jours, demander au ministre, selon les modalités réglementaires, de réviser sa décision.
(2) Le ministre étudie les demandes dès leur réception; il peut confirmer ou modifier sa décision soit en agréant le versement de la prestation ou en la liquidant, soit en décidant qu'il n'y a pas lieu de verser la prestation. Sans délai, il notifie sa décision et ses motifs.
28.1 (1) Dans le cas où il est convaincu, sur preuve présentée par une personne ou quiconque de sa part, qu'à la date à laquelle une demande de prestation a été faite, la personne n'avait pas la capacité de former ou d'exprimer l'intention de faire une demande de prestation, le ministre peut réputer la demande faite au cours du mois précédant le premier mois au cours duquel le versement de la prestation en question aurait pu commencer ou, s'il est postérieur, le mois au cours duquel, selon le ministre, la dernière période pertinente d'incapacité de la personne a commencé.
[...]
(3) Pour l'application des paragraphes (1) et (2), une période d'incapacité est continue, sous réserve des règlements.
Régime de pensions du Canada,
L.R.C. (1985), ch. C-8
82. (1) La personne qui se croit lésée par une décision du ministre rendue en application de l'article 81 ou du paragraphe 84(2) ou celle qui se croit lésée par une décision du ministre rendue en application du paragraphe 27.1(2) de la Loi sur la sécurité de la vieillesse ou, sous réserve des règlements, quiconque de sa part, peut interjeter appel par écrit auprès d'un tribunal de révision de la décision du ministre soit dans les quatre-vingt-dix jours suivant le jour où la première personne est, de la manière prescrite, avisée de cette décision, ou, selon le cas, suivant le jour où le ministre notifie à la deuxième personne sa décision et ses motifs, soit dans le délai plus long autorisé par le commissaire des tribunaux de révision avant ou après l'expiration des quatre-vingt-dix jours.
(2) Un tribunal de révision est constitué conformément au présent article.
(3) Le gouverneur en conseil nomme de cent à quatre cents personnes qui, résidant au Canada, feront partie d'une liste qui doit en tout temps répondre aux critères suivants :
a) au moins vingt-cinq pour cent de ceux qui font partie de la liste doivent appartenir à un barreau provincial;
b) au moins vingt-cinq pour cent de ceux qui font partie de la liste doivent être des personnes habiles à pratiquer la médecine ou une profession connexe prescrite dans une province;
c) il y a, dans cette liste, des représentants de chacune des régions du Canada.
(4) Une personne faisant partie de la liste établie en application du paragraphe (3) y est nommée pour une période qui peut varier entre deux et cinq ans et elle peut y être nommée de nouveau après l'expiration de cette période.
(5) Le gouverneur en conseil nomme, pour un mandat qui peut varier entre deux et cinq ans, un commissaire et un commissaire-adjoint des tribunaux de révision et, après l'expiration de leur mandat respectif, ceux-ci peuvent être nommés à nouveau.
(6) En cas d'absence ou d'empêchement du commissaire des tribunaux de révision, ou de vacance de son poste, le commissaire-adjoint assume les responsabilités du commissaire.
(7) Un tribunal de révision se compose de trois personnes qui, provenant de la liste visée au paragraphe (3), sont choisies par le commissaire en fonction des exigences suivantes :
a) le commissaire doit désigner, comme président du tribunal, un membre du barreau d'une province;
b) dans les cas où l'appel concerne une question se rapportant à une prestation d'invalidité, au moins un membre du tribunal doit être une personne habile à pratiquer la médecine ou une profession connexe prescrite dans une province.
(8) Un appel auprès d'un tribunal de révision est entendu à l'endroit du Canada que fixe le commissaire, compte tenu de ce qui convient à l'appelant, au ministre et aux mis en cause en application du paragraphe (10).
[...]
(11) Un tribunal de révision peut confirmer ou modifier une décision du ministre prise en vertu de l'article 81 ou du paragraphe 84(2) ou en vertu du paragraphe 27.1(2) de la Loi sur la sécurité de la vieillesse et il peut, à cet égard, prendre toute mesure que le ministre aurait pu prendre en application de ces dispositions; le commissaire des tribunaux de révision doit aussitôt donner un avis écrit de la décision du tribunal et des motifs la justifiant au ministre ainsi qu'aux parties à l'appel.
(12) Une décision de la majorité des membres d'un tribunal de révision emporte décision du tribunal.
83. (1) La personne qui se croit lésée par une décision du tribunal de révision rendue en application de l'article 82 - autre qu'une décision portant sur l'appel prévu au paragraphe 28(1) de la Loi sur la sécurité de la vieillesse - ou du paragraphe 84(2), ou, sous réserve des règlements, quiconque de sa part, de même que le ministre, peuvent présenter, soit dans les quatre-vingt-dix jours suivant le jour où la décision du tribunal de révision est transmise à la personne ou au ministre, soit dans tel délai plus long qu'autorise le président ou le vice-président de la Commission d'appel des pensions avant ou après l'expiration de ces quatre-vingt-dix jours, une demande écrite au président ou au vice-président de la Commission d'appel des pensions, afin d'obtenir la permission d'interjeter un appel de la décision du tribunal de révision auprès de la Commission.
84. (1) Un tribunal de révision et la Commission d'appel des pensions ont autorité pour décider des questions de droit ou de fait concernant :
a) la question de savoir si une prestation est payable à une personne;
[...]
La décision du tribunal de révision, sauf disposition contraire de la présente loi, ou celle de la Commission d'appel des pensions, sauf contrôle judiciaire dont elle peut faire l'objet aux termes de la Loi sur les Cours fédérales, est définitive et obligatoire pour l'application de la présente loi.
Règlement sur la sécurité de la vieillesse,
C.R.C., ch. 1246
21. (1) Aux fins de la Loi et du présent règlement,
a) une personne réside au Canada si elle établit sa demeure et vit ordinairement dans une région du Canada; et
b) une personne est présente au Canada lorsqu'elle se trouve physiquement dans une région du Canada.
[...]
(4) Lorsqu'une personne qui réside au Canada s'absente du Canada et que son absence
a) est temporaire et ne dépasse pas un an,
b) a pour motif la fréquentation d'une école ou d'une université, ou
c) compte parmi les absences mentionnées au paragraphe (5),
cette absence est réputée n'avoir pas interrompu la résidence ou la présence de cette personne au Canada.
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: T-2009-04

STYLE OF CAUSE: MINISTER OF HUMAN RESOURCES DEVELOPMENT v. BIBI CHHABU
PLACE OF HEARING: EDMONTON, AB
DATE OF HEARING: SEPTEMBER 7, 2005
REASONS FOR 

## 2660:4 · paragraphs 43-43

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9d074e0cbd55e6b4c667a4b719d5072f41d7f09e144f0f2fbd1a1ce3edcc12c2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2660:4:subtheme:1 · paragraphs 43-43

- Raw key terms: `appearances, applicant, attorney, canada, chotalia, dated, edmonton, general`
- Display key terms: `chotalia, dated, edmonton`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: chotalia, dated, edmonton No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 43-43. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER BY: LAYDEN-STEVENSON J.
DATED: SEPTEMBER 19, 2005
APPEARANCES:
Sandra Gruescu FOR APPLICANT
Shirish P. Chotalia FOR RESPONDENT
SOLICITORS OF RECORD:
John Sims
Attorney General of Canada
Ottawa, ON FOR APPLICANT
Pundit & Chotalia FOR RESPONDENT
Edmonton, AB
