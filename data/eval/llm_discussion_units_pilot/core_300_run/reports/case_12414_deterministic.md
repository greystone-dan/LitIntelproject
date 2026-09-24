# Discussion Units: case 12414

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **16**
- Continuity pairs: **15**
- Discussion Units: **3**
- Paragraph source hashes: **16**
- Sub-themes: **8**

## 12414:1 · paragraphs 0-8

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b0eeaf60f2553a957d01f0f41c959e50985015fc16aaa1b0a5cdca6abb79f1e7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12414:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `applicant, decision, immigration, meilina, yani, alternative, although, appeal`
- Display key terms: `meilina, yani, alternative, although`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position Display terms: meilina, yani, alternative, although Position/evidence statements: Although the RPD found that the applicant was a victim of gender-based persecution at the hands of her ex-husband, it also found that the availability of an internal flight alternative [IFA] was determinative of all clai Rule/authority context: Although the RPD found that the applicant was a victim of gender-based persecution at the hands of her ex-husband, it also found that the availability of an internal flight alternative [IFA] was determinative of all clai Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `4619956` offsets `552-558`; context: Although the RPD found that the applicant was a victim of gender-based persecution at the hands of her ex-husband, it also found that the availability of an internal flight alternative [IFA] was determinative of all claims under either section 96 or subsection 97(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act].
- Evidence: `evidence_fact` cue `found that` at chunk `4619956` offsets `353-363`; context: Although the RPD found that the applicant was a victim of gender-based persecution at the hands of her ex-husband, it also found that the availability of an internal flight alternative [IFA] was determinative of all claims under either section 96 or subsection 97(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act].
- Evidence: `governing_rule` cue `under` at chunk `4619956` offsets `559-564`; context: Although the RPD found that the applicant was a victim of gender-based persecution at the hands of her ex-husband, it also found that the availability of an internal flight alternative [IFA] was determinative of all claims under either section 96 or subsection 97(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act].
- Evidence: `counterargument_limitation` cue `Although` at chunk `4619956` offsets `336-344`; context: Although the RPD found that the applicant was a victim of gender-based persecution at the hands of her ex-husband, it also found that the availability of an internal flight alternative [IFA] was determinative of all claims under either section 96 or subsection 97(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act].

#### 12414:1:subtheme:2 · paragraphs 2-3

- Raw key terms: `application, applied, reasonableness, standard, analysis, apply, applying, available`
- Display key terms: `applied, reasonableness, standard, analysis, apply, applying, available`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: applied, reasonableness, standard, analysis, apply, applying, available Position/evidence statements: [4] The respondent submits that even if I find the RAD committed a reviewable error by applying the reasonableness standard, I should dismiss the application since the RPD would have reached the same conclusion if it had Rule/authority context: [2] As superior courts of justice do in similar circumstances, the RAD engaged in a standard of review analysis and found that the reasonableness standard applied to the RPD’s finding of fact and mixed fact and law. Application context: [2] As superior courts of justice do in similar circumstances, the RAD engaged in a standard of review analysis and found that the reasonableness standard applied to the RPD’s finding of fact and mixed fact and law. | [4] The respondent submits that even if I find the RAD committed a reviewable error by applying the reasonableness standard, I should dismiss the application since the RPD would have reached the same conclusion if it had Evidence spans paragraphs 2-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4619957` offsets `363-369`; context: Issues and standard of review [3] This application for judicial review raises a single issue:
• Whether the RAD erred by holding that it should apply the reasonableness standard to the RPD’s findings of fact and mixed fact and law.
- Evidence: `evidence_fact` cue `found that` at chunk `4619957` offsets `116-126`; context: [2] As superior courts of justice do in similar circumstances, the RAD engaged in a standard of review analysis and found that the reasonableness standard applied to the RPD’s finding of fact and mixed fact and law.
- Evidence: `governing_rule` cue `standard of review` at chunk `4619957` offsets `84-102`; context: [2] As superior courts of justice do in similar circumstances, the RAD engaged in a standard of review analysis and found that the reasonableness standard applied to the RPD’s finding of fact and mixed fact and law.
- Evidence: `reasoning_application` cue `applied` at chunk `4619957` offsets `155-162`; context: [2] As superior courts of justice do in similar circumstances, the RAD engaged in a standard of review analysis and found that the reasonableness standard applied to the RPD’s finding of fact and mixed fact and law.
- Evidence: `party_position` cue `submits` at chunk `4619958` offsets `19-26`; context: [4] The respondent submits that even if I find the RAD committed a reviewable error by applying the reasonableness standard, I should dismiss the application since the RPD would have reached the same conclusion if it had applied the correctness standard.
- Evidence: `reasoning_application` cue `I find` at chunk `4619958` offsets `40-46`; context: [4] The respondent submits that even if I find the RAD committed a reviewable error by applying the reasonableness standard, I should dismiss the application since the RPD would have reached the same conclusion if it had applied the correctness standard.

#### 12414:1:subtheme:3 · paragraphs 4-5

- Raw key terms: `court, question, reasonableness, standard, above, adduced, adjudicator, agree`
- Display key terms: `question, reasonableness, standard, above, adduced, adjudicator, agree`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: question, reasonableness, standard, above, adduced, adjudicator, agree Application context: [5] With respect, I do not agree with the respondent that this Court should substitute its own assessment of the evidence adduced before the RAD, and, as this application does not raise a pure question of credibility, I  | This presumption applies unless the interpretation of the home statute is: 1) a constitutional question; 2) a question of law that is of central importance to the legal system as a whole and that is outside the adjudicat Operative outcome context: [5] With respect, I do not agree with the respondent that this Court should substitute its own assessment of the evidence adduced before the RAD, and, as this application does not raise a pure question of credibility, I  Evidence spans paragraphs 4-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4619959` offsets `193-201`; context: [5] With respect, I do not agree with the respondent that this Court should substitute its own assessment of the evidence adduced before the RAD, and, as this application does not raise a pure question of credibility, I am therefore of the view that if I am to find the RAD erred in applying the reasonableness standard, the application for judicial review should be granted and the matter sent back to the RAD for a new determination.
- Evidence: `evidence_fact` cue `evidence` at chunk `4619959` offsets `113-121`; context: [5] With respect, I do not agree with the respondent that this Court should substitute its own assessment of the evidence adduced before the RAD, and, as this application does not raise a pure question of credibility, I am therefore of the view that if I am to find the RAD erred in applying the reasonableness standard, the application for judicial review should be granted and the matter sent back to the RAD for a new determination.
- Evidence: `reasoning_application` cue `therefore` at chunk `4619959` offsets `223-232`; context: [5] With respect, I do not agree with the respondent that this Court should substitute its own assessment of the evidence adduced before the RAD, and, as this application does not raise a pure question of credibility, I am therefore of the view that if I am to find the RAD erred in applying the reasonableness standard, the application for judicial review should be granted and the matter sent back to the RAD for a new determination.
- Evidence: `disposition` cue `granted` at chunk `4619959` offsets `367-374`; context: [5] With respect, I do not agree with the respondent that this Court should substitute its own assessment of the evidence adduced before the RAD, and, as this application does not raise a pure question of credibility, I am therefore of the view that if I am to find the RAD erred in applying the reasonableness standard, the application for judicial review should be granted and the matter sent back to the RAD for a new determination.
- Evidence: `issue` cue `question` at chunk `4619960` offsets `559-567`; context: This presumption applies unless the interpretation of the home statute is: 1) a constitutional question; 2) a question of law that is of central importance to the legal system as a whole and that is outside the adjudicator’s expertise; 3) a question regarding the jurisdictional lines between two or more competing specialized tribunals; or 4) a true question of jurisdiction or vires (Dunsmuir v New Brunswick, 2008 SCC 9, at paras 59-61; Alberta Teachers, above).
- Evidence: `reasoning_application` cue `applies` at chunk `4619960` offsets `481-488`; context: This presumption applies unless the interpretation of the home statute is: 1) a constitutional question; 2) a question of law that is of central importance to the legal system as a whole and that is outside the adjudicator’s expertise; 3) a question regarding the jurisdictional lines between two or more competing specialized tribunals; or 4) a true question of jurisdiction or vires (Dunsmuir v New Brunswick, 2008 SCC 9, at paras 59-61; Alberta Teachers, above).

#### 12414:1:subtheme:4 · paragraphs 6-8

- Raw key terms: `review, standard, appeal, apply, canada, case, citizenship, correctness`
- Display key terms: `review, standard, apply, case, correctness`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: review, standard, apply, case, correctness Rule/authority context: [7] Since this case was argued, this Court has issued several decisions on the subject and it has engaged in several standard of review analyses. | [8] However, in Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 [Akuffo], I reviewed the jurisprudence of the Supreme Court of Canada and found myself unable to agree with Justice Phelan. Application context: In Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 [Huruglica], relying on Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 and Halifax (Regional Municipality) v United Gulf Developme | [9] In the case at bar, the choice of standard of review to be applied is not determinative as I would arrive at the same conclusion should I apply either one. Evidence spans paragraphs 6-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4619961` offsets `424-429`; context: In Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 [Huruglica], relying on Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 and Halifax (Regional Municipality) v United Gulf Developments Ltd, 2009 NSCA 78, Justice Phelan found that, as “the issue of law is one of general interest to the legal system”, this Court should apply the correctness standard when reviewing the standard of intervention chosen by the RAD sitting in appeal of RPD decisions.
- Evidence: `evidence_fact` cue `found that` at chunk `4619961` offsets `404-414`; context: In Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 [Huruglica], relying on Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 and Halifax (Regional Municipality) v United Gulf Developments Ltd, 2009 NSCA 78, Justice Phelan found that, as “the issue of law is one of general interest to the legal system”, this Court should apply the correctness standard when reviewing the standard of intervention chosen by the RAD sitting in appeal of RPD decisions.
- Evidence: `governing_rule` cue `standard of review` at chunk `4619961` offsets `117-135`; context: [7] Since this case was argued, this Court has issued several decisions on the subject and it has engaged in several standard of review analyses.
- Evidence: `reasoning_application` cue `apply` at chunk `4619961` offsets `504-509`; context: In Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 [Huruglica], relying on Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 and Halifax (Regional Municipality) v United Gulf Developments Ltd, 2009 NSCA 78, Justice Phelan found that, as “the issue of law is one of general interest to the legal system”, this Court should apply the correctness standard when reviewing the standard of intervention chosen by the RAD sitting in appeal of RPD decisions.
- Evidence: `issue` cue `question` at chunk `4619962` offsets `325-333`; context: At paragraph 26, I express the view that “the interpretation of the RAD Provisions by the RAD does not involve a question of central importance to the legal system as a whole or any other special circumstances that would require review on a correctness standard.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4619962` offsets `113-126`; context: [8] However, in Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 [Akuffo], I reviewed the jurisprudence of the Supreme Court of Canada and found myself unable to agree with Justice Phelan.
- Evidence: `governing_rule` cue `standard of review` at chunk `4619963` offsets `38-56`; context: [9] In the case at bar, the choice of standard of review to be applied is not determinative as I would arrive at the same conclusion should I apply either one.
- Evidence: `reasoning_application` cue `applied` at chunk `4619963` offsets `63-70`; context: [9] In the case at bar, the choice of standard of review to be applied is not determinative as I would arrive at the same conclusion should I apply either one.

#### Section text

Meilina v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-12-18
Neutral citation
2014 FC 1233
File numbers
IMM-642-14
Decision Content
Date: 20141218
Docket: IMM-642-14
Citation: 2014 FC 1233
Ottawa (Ontario), December 18, 2014
PRESENT: The Honourable Madam Justice Gagné
BETWEEN:
YANI MEILINA
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Defendant
JUDGMENT AND REASONS

[1] Ms. Yani Meilina, a 58 year old Christian citizen of Indonesia, seeks judicial review of a decision of the Refugee Appeal Division [RAD] of the Immigration and Refugee Protection Board, dismissing her appeal of findings made by the Refugee Protection Division [RPD] that she is neither a refugee nor a person in need of protection. Although the RPD found that the applicant was a victim of gender-based persecution at the hands of her ex-husband, it also found that the availability of an internal flight alternative [IFA] was determinative of all claims under either section 96 or subsection 97(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act].

[2] As superior courts of justice do in similar circumstances, the RAD engaged in a standard of review analysis and found that the reasonableness standard applied to the RPD’s finding of fact and mixed fact and law. As such, it found that the RPD’s analysis of the available IFA was reasonable and that its findings fell within the range of possible outcomes.
I. Issues and standard of review [3] This application for judicial review raises a single issue:
• Whether the RAD erred by holding that it should apply the reasonableness standard to the RPD’s findings of fact and mixed fact and law.

[4] The respondent submits that even if I find the RAD committed a reviewable error by applying the reasonableness standard, I should dismiss the application since the RPD would have reached the same conclusion if it had applied the correctness standard.

[5] With respect, I do not agree with the respondent that this Court should substitute its own assessment of the evidence adduced before the RAD, and, as this application does not raise a pure question of credibility, I am therefore of the view that if I am to find the RAD erred in applying the reasonableness standard, the application for judicial review should be granted and the matter sent back to the RAD for a new determination.

[6] That said, errors of law reviewed by this Court are generally governed by the correctness standard (Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 44). Questions which concern the interpretation of a tribunal’s own statute and the tribunal’s own function are presumed to be reviewable on the reasonableness standard (Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61 [Alberta Teachers]. This presumption applies unless the interpretation of the home statute is: 1) a constitutional question; 2) a question of law that is of central importance to the legal system as a whole and that is outside the adjudicator’s expertise; 3) a question regarding the jurisdictional lines between two or more competing specialized tribunals; or 4) a true question of jurisdiction or vires (Dunsmuir v New Brunswick, 2008 SCC 9, at paras 59-61; Alberta Teachers, above).

[7] Since this case was argued, this Court has issued several decisions on the subject and it has engaged in several standard of review analyses. In Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 [Huruglica], relying on Newton v Criminal Trial Lawyers’ Association, 2010 ABCA 399 and Halifax (Regional Municipality) v United Gulf Developments Ltd, 2009 NSCA 78, Justice Phelan found that, as “the issue of law is one of general interest to the legal system”, this Court should apply the correctness standard when reviewing the standard of intervention chosen by the RAD sitting in appeal of RPD decisions.

[8] However, in Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 [Akuffo], I reviewed the jurisprudence of the Supreme Court of Canada and found myself unable to agree with Justice Phelan. At paragraph 26, I express the view that “the interpretation of the RAD Provisions by the RAD does not involve a question of central importance to the legal system as a whole or any other special circumstances that would require review on a correctness standard. The issue of interpretation does not have significance outside the operation of these specific provisions, the very same provisions that only dictate the role and duties of the RAD.” I certified the question so that the parties have the opportunity to have the issue clarified by the Federal Court of Appeal.

[9] In the case at bar, the choice of standard of review to be applied is not determinative as I would arrive at the same conclusion should I apply either one.


## 12414:2 · paragraphs 9-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0963eb808b86aa65d67b10cf507074a86765633363e9e9d135a51f2d080fcad3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12414:2:subtheme:1 · paragraphs 9-9

- Raw key terms: `although, amongst, analysis, appeal, appeals, apply, case, consensus`
- Display key terms: `although, amongst, analysis, appeals, apply, case, consensus`
- Argument roles: `counterargument_limitation, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, reasoning_application Display terms: although, amongst, analysis, appeals, apply, case, consensus Application context: Analysis [10] Although the Federal Court of Appeal [FCA] has yet to hear a case involving a decision of the RPD, there is a consensus amongst the judges of this Court that the judicial review regime does not apply to app Evidence spans paragraphs 9-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `apply` at chunk `4619963` offsets `372-377`; context: Analysis [10] Although the Federal Court of Appeal [FCA] has yet to hear a case involving a decision of the RPD, there is a consensus amongst the judges of this Court that the judicial review regime does not apply to appeals of RPD decisions before the RAD.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4619963` offsets `178-186`; context: Analysis [10] Although the Federal Court of Appeal [FCA] has yet to hear a case involving a decision of the RPD, there is a consensus amongst the judges of this Court that the judicial review regime does not apply to appeals of RPD decisions before the RAD.

#### 12414:2:subtheme:2 · paragraphs 10-11

- Raw key terms: `appeal, back, benefit, canada, case, citoyennet, clear, decided`
- Display key terms: `back, benefit, case, citoyennet, clear, decided`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: back, benefit, case, citoyennet, clear, decided Application context: [12] In any event, it seems clear in this case that the plaintiff did not benefit from the appeal she was entitled to and, as found by Justice Martineau in Djossou c Canada (Ministre de la Citoyenneté et de l’Immigration Evidence spans paragraphs 10-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4619964` offsets `22-28`; context: [11] However, several issues will need to be decided by the FCA, for example: What is the level of deference that is owed by the RAD to the RPD’s findings, if any and what is the scope of the questions of fact and questions of mixed fact and law for which deference would be owed?
- Evidence: `reasoning_application` cue `I find` at chunk `4619965` offsets `237-243`; context: [12] In any event, it seems clear in this case that the plaintiff did not benefit from the appeal she was entitled to and, as found by Justice Martineau in Djossou c Canada (Ministre de la Citoyenneté et de l’Immigration), 2014 CF 1080, I find that this is sufficient to quash the RAD’s decision, and to send the file back for re-determination.

#### 12414:2:subtheme:3 · paragraphs 12-14

- Raw key terms: `record, appeal, basis, case, certified, certify, deference, division`
- Display key terms: `basis, case, certified, certify, deference, division`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: basis, case, certified, certify, deference, division Operative outcome context: The application for judicial review is granted; 2. Evidence spans paragraphs 12-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4619966` offsets `68-76`; context: [13] At the hearing, both parties suggested that I certify the same question as was certified by Justice Phelan in Huruglica.
- Evidence: `evidence_fact` cue `record` at chunk `4619966` offsets `371-377`; context: However, to be consistent, I will certify the same question as I certified in Akuffo which, in my view, is better suited for this case:
Within the Refugee Appeal Division [RAD]’s statutory framework where the appeal proceeds on the basis of the record of the proceedings of the Refugee Protection Division [RPD], does the RAD owe deference to RPD findings of fact and of mixed fact and law?
- Evidence: `counterargument_limitation` cue `However` at chunk `4619966` offsets `126-133`; context: However, to be consistent, I will certify the same question as I certified in Akuffo which, in my view, is better suited for this case:
Within the Refugee Appeal Division [RAD]’s statutory framework where the appeal proceeds on the basis of the record of the proceedings of the Refugee Protection Division [RPD], does the RAD owe deference to RPD findings of fact and of mixed fact and law?
- Evidence: `issue` cue `question` at chunk `4619967` offsets `19-27`; context: [14] Although this question has been certified in several files and although the present case might not be the best case for the respondent to bring before the Federal Court of Appeal, I will nevertheless certify that question, as it is determinative of the case and would be determinative of an appeal.
- Evidence: `evidence_fact` cue `record` at chunk `4619967` offsets `723-729`; context: The following question is certified:
Within the Refugee Appeal Division [RAD]’s statutory framework where the appeal proceeds on the basis of the record of the proceedings of the Refugee Protection Division [RPD], does the RAD owe deference to RPD findings of fact and of mixed fact and law?
- Evidence: `disposition` cue `granted` at chunk `4619967` offsets `386-393`; context: The application for judicial review is granted;
2.

#### Section text

II. Analysis [10] Although the Federal Court of Appeal [FCA] has yet to hear a case involving a decision of the RPD, there is a consensus amongst the judges of this Court that the judicial review regime does not apply to appeals of RPD decisions before the RAD.

[11] However, several issues will need to be decided by the FCA, for example: What is the level of deference that is owed by the RAD to the RPD’s findings, if any and what is the scope of the questions of fact and questions of mixed fact and law for which deference would be owed?

[12] In any event, it seems clear in this case that the plaintiff did not benefit from the appeal she was entitled to and, as found by Justice Martineau in Djossou c Canada (Ministre de la Citoyenneté et de l’Immigration), 2014 CF 1080, I find that this is sufficient to quash the RAD’s decision, and to send the file back for re-determination.

[13] At the hearing, both parties suggested that I certify the same question as was certified by Justice Phelan in Huruglica. However, to be consistent, I will certify the same question as I certified in Akuffo which, in my view, is better suited for this case:
Within the Refugee Appeal Division [RAD]’s statutory framework where the appeal proceeds on the basis of the record of the proceedings of the Refugee Protection Division [RPD], does the RAD owe deference to RPD findings of fact and of mixed fact and law?

[14] Although this question has been certified in several files and although the present case might not be the best case for the respondent to bring before the Federal Court of Appeal, I will nevertheless certify that question, as it is determinative of the case and would be determinative of an appeal.
JUDGMENT
THIS COURT’S JUDGMENT is that:
1. The application for judicial review is granted;
2. The Refugee Appeal Division’s decision dated January 16, 2014 is set aside;
3. The file is remitted back to a different member of the Appeal Division for re-determination; and
4. The following question is certified:
Within the Refugee Appeal Division [RAD]’s statutory framework where the appeal proceeds on the basis of the record of the proceedings of the Refugee Protection Division [RPD], does the RAD owe deference to RPD findings of fact and of mixed fact and law?
"Jocelyne Gagné"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-642-14
STYLE OF CAUSE:
YANI MEILINA v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Vancouver, British Columbia
DATE OF HEARING:
July 24, 2014


## 12414:3 · paragraphs 15-15

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3d5dba2265015d50bce1893a83c093ce813b391c3d3d24cb0766fb3d3f9a0438`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12414:3:subtheme:1 · paragraphs 15-15

- Raw key terms: `appearances, applicant, associates, attorney, barristers, british, canada, cannon`
- Display key terms: `associates, barristers, british, cannon`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: associates, barristers, british, cannon No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 15-15. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
GAGNÉ J.
DATED:
December 18, 2014
APPEARANCES:
Leanna Krause
For The Applicant
R. Keith Reimer
For The Defendant
SOLICITORS OF RECORD:
Elgin, Cannon & Associates
Barristers and Solicitors
Vancouver, British Columbia
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Vancouver, British Columbia
For The Defendant
