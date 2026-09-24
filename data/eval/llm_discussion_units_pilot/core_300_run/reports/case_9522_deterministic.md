# Discussion Units: case 9522

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **84**
- Continuity pairs: **83**
- Discussion Units: **11**
- Paragraph source hashes: **84**
- Sub-themes: **26**

## 9522:1 · paragraphs 0-8

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f3cf4a947d5123928eefe7804c95430fc1d2167f0dd78d88af33200eb0a8eb85`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9522:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicant, decision, appeal, application, august, canada, dated, denied`
- Display key terms: `august, dated, denied`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: august, dated, denied Rule/authority context: [1] This is an application under s 18. | [2] The Applicant applied for a disability pension under the Canada Pension Plan, SC 1985, c C-8 [CPP] on February 28, 2012. Application context: [2] The Applicant applied for a disability pension under the Canada Pension Plan, SC 1985, c C-8 [CPP] on February 28, 2012. Operative outcome context: 1 of the Federal Courts Act, RSC 1985, c F-7 [Act] for judicial review of a decision of the Appeal Division of the Social Security Tribunal [AD], dated August 27, 2015 [Decision], which denied the Applicant’s application | The application was initially denied on June 21, 2012 and, upon reconsideration, was again denied on October 16, 2012. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4481502` offsets `27-32`; context: [1] This is an application under s 18.
- Evidence: `disposition` cue `denied` at chunk `4481502` offsets `224-230`; context: 1 of the Federal Courts Act, RSC 1985, c F-7 [Act] for judicial review of a decision of the Appeal Division of the Social Security Tribunal [AD], dated August 27, 2015 [Decision], which denied the Applicant’s application for leave to appeal a decision of the General Division of the Social Security Tribunal [GD].
- Evidence: `evidence_fact` cue `found that` at chunk `4481503` offsets `335-345`; context: The GD found that the Applicant did not meet the criteria for payment of a CPP disability pension on the basis that he had not demonstrated, on a balance of probabilities, that he had a severe and prolonged disability on or before December 31, 2011, which is the Applicant’s minimum qualifying period [MQP].
- Evidence: `governing_rule` cue `under` at chunk `4481503` offsets `51-56`; context: [2] The Applicant applied for a disability pension under the Canada Pension Plan, SC 1985, c C-8 [CPP] on February 28, 2012.
- Evidence: `reasoning_application` cue `applied` at chunk `4481503` offsets `18-25`; context: [2] The Applicant applied for a disability pension under the Canada Pension Plan, SC 1985, c C-8 [CPP] on February 28, 2012.
- Evidence: `disposition` cue `denied` at chunk `4481503` offsets `155-161`; context: The application was initially denied on June 21, 2012 and, upon reconsideration, was again denied on October 16, 2012.
- Evidence: `governing_rule` cue `UNDER` at chunk `4481504` offsets `102-107`; context: DECISION UNDER REVIEW

#### 9522:1:subtheme:2 · paragraphs 5-8

- Raw key terms: `applicant, appeal, concluded, decision, although, application, chance, considered`
- Display key terms: `concluded, although, chance, considered`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: concluded, although, chance, considered Position/evidence statements: Although the Applicant had submitted that insufficient weight was given to Dr. Application context: In addition to this issue, the AD also considered whether the appeal would have a reasonable chance of success, which is the test to be applied when considering leave to appeal. Evidence spans paragraphs 5-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4481506` offsets `376-381`; context: In addition to this issue, the AD also considered whether the appeal would have a reasonable chance of success, which is the test to be applied when considering leave to appeal.
- Evidence: `reasoning_application` cue `applied` at chunk `4481506` offsets `492-499`; context: In addition to this issue, the AD also considered whether the appeal would have a reasonable chance of success, which is the test to be applied when considering leave to appeal.
- Evidence: `issue` cue `whether` at chunk `4481507` offsets `376-383`; context: The AD found that the Applicant challenged the weight placed on the medical evidence but did not set out how the GD erred in law or fact, or whether a breach of natural justice had occurred and in what manner.
- Evidence: `evidence_fact` cue `found that` at chunk `4481507` offsets `11-21`; context: [6] The AD found that the Applicant’s submissions were no more than statements disagreeing with the outcome of the GD’s decision and expressing the continued belief that the Applicant met the requirements for a CPP disability pension.
- Evidence: `counterargument_limitation` cue `but` at chunk `4481507` offsets `320-323`; context: The AD found that the Applicant challenged the weight placed on the medical evidence but did not set out how the GD erred in law or fact, or whether a breach of natural justice had occurred and in what manner.
- Evidence: `party_position` cue `submitted` at chunk `4481508` offsets `208-217`; context: Although the Applicant had submitted that insufficient weight was given to Dr.
- Evidence: `evidence_fact` cue `found that` at chunk `4481508` offsets `26-36`; context: [7] In its review, the AD found that the GD had considered and addressed both the objective medical evidence as well as the Applicant’s oral testimony about his medical conditions.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4481508` offsets `181-189`; context: Although the Applicant had submitted that insufficient weight was given to Dr.

#### Section text

Joseph v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2017-04-21
Neutral citation
2017 FC 391
File numbers
T-1674-15
Decision Content
Date: 20170421
Docket: T-1674-15
Citation: 2017 FC 391
Ottawa, Ontario, April 21, 2017
PRESENT: The Honourable Mr. Justice Russell
BETWEEN:
PETER JOSEPH
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS
I. INTRODUCTION

[1] This is an application under s 18.1 of the Federal Courts Act, RSC 1985, c F-7 [Act] for judicial review of a decision of the Appeal Division of the Social Security Tribunal [AD], dated August 27, 2015 [Decision], which denied the Applicant’s application for leave to appeal a decision of the General Division of the Social Security Tribunal [GD].
II. BACKGROUND

[2] The Applicant applied for a disability pension under the Canada Pension Plan, SC 1985, c C-8 [CPP] on February 28, 2012. The application was initially denied on June 21, 2012 and, upon reconsideration, was again denied on October 16, 2012. The matter was then heard by the GD, which denied the application on July 17, 2015. The GD found that the Applicant did not meet the criteria for payment of a CPP disability pension on the basis that he had not demonstrated, on a balance of probabilities, that he had a severe and prolonged disability on or before December 31, 2011, which is the Applicant’s minimum qualifying period [MQP].

[3] The Applicant then sought to appeal the GD’s denial to the AD on imprecise grounds.
III. DECISION UNDER REVIEW

[4] In a Decision dated August 27, 2015, the AD refused the Applicant’s application for leave to appeal the GD’s decision to deny the Applicant a CPP disability pension.

[5] Although the Applicant had not identified grounds of appeal in his application, the AD concluded that the Applicant had sought leave to appeal to the AD on the grounds that the GD decision should be characterized as based upon an erroneous finding of fact which it made in a perverse or capricious manner, or without regard for the material before it. In addition to this issue, the AD also considered whether the appeal would have a reasonable chance of success, which is the test to be applied when considering leave to appeal.

[6] The AD found that the Applicant’s submissions were no more than statements disagreeing with the outcome of the GD’s decision and expressing the continued belief that the Applicant met the requirements for a CPP disability pension. The AD found that the Applicant challenged the weight placed on the medical evidence but did not set out how the GD erred in law or fact, or whether a breach of natural justice had occurred and in what manner. Thus, the AD concluded that the Applicant’s submissions invited the AD to reweigh the evidence, which is not the function of the AD.

[7] In its review, the AD found that the GD had considered and addressed both the objective medical evidence as well as the Applicant’s oral testimony about his medical conditions. Although the Applicant had submitted that insufficient weight was given to Dr. Samuels’ medical evidence, the AD found that this evidence had been appropriately addressed in the GD’s decision. Furthermore, the AD found that the GD had appropriately analyzed the content of the other medical reports in its decision. Overall, the Applicant’s disagreements with the conclusions of the GD were found to be insufficient to ground an appeal.

[8] The AD concluded that it was not persuaded that the Applicant’s submissions disclosed a ground of appeal that would have a reasonable chance of success, and refused the application for leave to appeal.


## 9522:2 · paragraphs 9-10

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `28ba99ad8c66bd713005173a71fa864bf0359c57f1894c5c503e5ebcb99d10c0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9522:2:subtheme:1 · paragraphs 9-10

- Raw key terms: `appears, applicant, application, apply, appropriate, arrive, based, capricious`
- Display key terms: `appears, apply, appropriate, arrive, based, capricious`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: appears, apply, appropriate, arrive, based, capricious Position/evidence statements: [9] Based on the oral and written submissions, it appears the Applicant submits that the following are at issue in this application: Did the Applicant have a severe and prolonged physical disability as defined in s 42(2) Rule/authority context: Did the GD and the AD fail to apply the appropriate legal test to arrive at their decisions to reject the Applicant’s application for payment of a disability pension under the CPP as a result of his permanent disability? Application context: Did the GD and the AD fail to apply the appropriate legal test to arrive at their decisions to reject the Applicant’s application for payment of a disability pension under the CPP as a result of his permanent disability? Evidence spans paragraphs 9-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4481510` offsets `106-111`; context: [9] Based on the oral and written submissions, it appears the Applicant submits that the following are at issue in this application:
Did the Applicant have a severe and prolonged physical disability as defined in s 42(2)(a) of the CPP to qualify for a disability pension?
- Evidence: `party_position` cue `submits` at chunk `4481510` offsets `72-79`; context: [9] Based on the oral and written submissions, it appears the Applicant submits that the following are at issue in this application:
Did the Applicant have a severe and prolonged physical disability as defined in s 42(2)(a) of the CPP to qualify for a disability pension?
- Evidence: `evidence_fact` cue `Record` at chunk `4481510` offsets `694-700`; context: Is the Certified Record deficient?
- Evidence: `governing_rule` cue `legal test` at chunk `4481510` offsets `324-334`; context: Did the GD and the AD fail to apply the appropriate legal test to arrive at their decisions to reject the Applicant’s application for payment of a disability pension under the CPP as a result of his permanent disability?
- Evidence: `reasoning_application` cue `apply` at chunk `4481510` offsets `302-307`; context: Did the GD and the AD fail to apply the appropriate legal test to arrive at their decisions to reject the Applicant’s application for payment of a disability pension under the CPP as a result of his permanent disability?

#### Section text

IV. ISSUES

[9] Based on the oral and written submissions, it appears the Applicant submits that the following are at issue in this application:
Did the Applicant have a severe and prolonged physical disability as defined in s 42(2)(a) of the CPP to qualify for a disability pension?
Did the GD and the AD fail to apply the appropriate legal test to arrive at their decisions to reject the Applicant’s application for payment of a disability pension under the CPP as a result of his permanent disability?
Was the GD’s decision based upon an error of fact made in a perverse or capricious manner or without regard for the materials before it?
Are the decisions of the GD and AD reasonable?
Is the Certified Record deficient?

## 9522:3 · paragraphs 11-11

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1015fce5f08cc66c83223541c0803aff5b68aded7821d909ded8f2c3d0eef4db`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9522:3:subtheme:1 · paragraphs 11-11

- Raw key terms: `appeal, application, decision, following, issue, leave, reasonable, refusing`
- Display key terms: `following, leave, reasonable, refusing`
- Argument roles: `governing_rule, issue, party_position`
- Explanation: Observed roles: governing_rule, issue, party_position Display terms: following, leave, reasonable, refusing Position/evidence statements: [10] The Respondent submits that the following is at issue in this application: Was the AD’s Decision refusing the application for leave to appeal reasonable? Rule/authority context: STANDARD OF REVIEW Evidence spans paragraphs 11-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4481511` offsets `53-58`; context: [10] The Respondent submits that the following is at issue in this application:
Was the AD’s Decision refusing the application for leave to appeal reasonable?
- Evidence: `party_position` cue `submits` at chunk `4481511` offsets `20-27`; context: [10] The Respondent submits that the following is at issue in this application:
Was the AD’s Decision refusing the application for leave to appeal reasonable?
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `4481511` offsets `162-180`; context: STANDARD OF REVIEW

#### Section text

[10] The Respondent submits that the following is at issue in this application:
Was the AD’s Decision refusing the application for leave to appeal reasonable?
V. STANDARD OF REVIEW

## 9522:4 · paragraphs 12-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `261c8b0b50f0cfe64b5384860d03d4612c8899c79cc8d275ddbccc5d8664c4bb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9522:4:subtheme:1 · paragraphs 12-13

- Raw key terms: `canada, para, review, standard, adopt, agraira, analysis, appear`
- Display key terms: `para, review, standard, adopt, agraira, analysis, appear`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: para, review, standard, adopt, agraira, analysis, appear Rule/authority context: [11] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir] held that a standard of review analysis need not be conducted in every instance. | [12] The standard of review for any findings of fact by the Social Security Tribunal and for the interpretation of the Department of Employment and Social Development Act, SC 2005, c-34 [DESD Act] is reasonableness: Rein Evidence spans paragraphs 12-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4481512` offsets `230-238`; context: Instead, where the standard of review applicable to a particular question before the court is settled in a satisfactory manner by past jurisprudence, the reviewing court may adopt that standard of review.
- Evidence: `governing_rule` cue `standard of review` at chunk `4481512` offsets `96-114`; context: [11] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir] held that a standard of review analysis need not be conducted in every instance.
- Evidence: `governing_rule` cue `standard of review` at chunk `4481513` offsets `9-27`; context: [12] The standard of review for any findings of fact by the Social Security Tribunal and for the interpretation of the Department of Employment and Social Development Act, SC 2005, c-34 [DESD Act] is reasonableness: Reinhardt v Canada (Attorney General), 2016 FCA 158 at para 15.

#### 9522:4:subtheme:2 · paragraphs 14-14

- Raw key terms: `above, acceptable, analysis, another, canada, citizenship, concerned, court`
- Display key terms: `above, acceptable, analysis, another, concerned`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: above, acceptable, analysis, another, concerned Evidence spans paragraphs 14-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4481514` offsets `219-226`; context: [13] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.

#### Section text

[11] The Supreme Court of Canada in Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir] held that a standard of review analysis need not be conducted in every instance. Instead, where the standard of review applicable to a particular question before the court is settled in a satisfactory manner by past jurisprudence, the reviewing court may adopt that standard of review. Only where this search proves fruitless, or where the relevant precedents appear to be inconsistent with new developments in the common law principles of judicial review, must the reviewing court undertake a consideration of the four factors comprising the standard of review analysis: Agraira v Canada (Public Safety and Emergency Preparedness), 2013 SCC 36 at para 48.

[12] The standard of review for any findings of fact by the Social Security Tribunal and for the interpretation of the Department of Employment and Social Development Act, SC 2005, c-34 [DESD Act] is reasonableness: Reinhardt v Canada (Attorney General), 2016 FCA 158 at para 15.

[13] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.” See Dunsmuir, above, at para 47, and Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 59. Put another way, the Court should intervene only if the Decision was unreasonable in the sense that it falls outside the “range of possible, acceptable outcomes which are defensible in respect of the facts and law.”
VI. STATUTORY PROVISIONS

## 9522:5 · paragraphs 15-15

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ae7665b478b205695e39e84fe3dd4ca9daa02d9e171b943ce96f8d29dd2bacd0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9522:5:subtheme:1 · paragraphs 15-15

- Raw key terms: `abusive, accorde, acted, appeal, appears, appel, appeler, arbitraire`
- Display key terms: `abusive, accorde, acted, appears, appel, appeler, arbitraire`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: abusive, accorde, acted, appears, appel, appeler, arbitraire Evidence spans paragraphs 15-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4481515` offsets `542-549`; context: [14] The following provisions from the DESD Act are relevant in this proceeding:
Grounds of appeal
Moyens d’appel
58 (1) The only grounds of appeal are that
58 (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `record` at chunk `4481515` offsets `594-600`; context: [14] The following provisions from the DESD Act are relevant in this proceeding:
Grounds of appeal
Moyens d’appel
58 (1) The only grounds of appeal are that
58 (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.

#### Section text

[14] The following provisions from the DESD Act are relevant in this proceeding:
Grounds of appeal
Moyens d’appel
58 (1) The only grounds of appeal are that
58 (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
c) elle a fondé sa décision sur une conclusion de fait erronée, tirée de façon abusive ou arbitraire ou sans tenir compte des éléments portés à sa connaissance.
Criteria
Critère
(2) Leave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success.
(2) La division d’appel rejette la demande de permission d’en appeler si elle est convaincue que l’appel n’a aucune chance raisonnable de succès.
Decision
Décision
(3) The Appeal Division must either grant or refuse leave to appeal.
(3) Elle accorde ou refuse cette permission.

## 9522:6 · paragraphs 16-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `dfe2678167a50fccbee7184632e34081d2941b1a4b43ead8d2932b424aab3296`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9522:6:subtheme:1 · paragraphs 16-17

- Raw key terms: `applicant, application, disability, pension, actually, admissibilit, ajust, alin`
- Display key terms: `disability, pension, actually, admissibilit, ajust, alin`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: disability, pension, actually, admissibilit, ajust, alin Position/evidence statements: [16] In his written submissions, the Applicant submits that both the GD and AD failed to apply the appropriate legal test in their decisions to deny the Applicant’s application for the CPP disability pension because the  Rule/authority context: … … Benefits payable Prestations payables 44 (1) Subject to this Part, 44 (1) Sous réserve des autres dispositions de la présente partie : … … (b) a disability pension shall be paid to a contributor who has not reached s | [16] In his written submissions, the Applicant submits that both the GD and AD failed to apply the appropriate legal test in their decisions to deny the Applicant’s application for the CPP disability pension because the  Application context: [16] In his written submissions, the Applicant submits that both the GD and AD failed to apply the appropriate legal test in their decisions to deny the Applicant’s application for the CPP disability pension because the  Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4481516` offsets `3636-3641`; context: …
…
Benefits payable
Prestations payables
44 (1) Subject to this Part,
44 (1) Sous réserve des autres dispositions de la présente partie :
…
…
(b) a disability pension shall be paid to a contributor who has not reached sixty-five years of age, to whom who
b) une pension d’invalidité doit être payée à un cotisant qui n’a pas atteint l’âge de soixante-cinq ans, à qui aucune pension de retraite n’est payable, qui est invalide et qui :
(i) has made contributions for not less than the minimum qualifying period,
(i) soit a versé des cotisations pendant au moins la période minimale d’admissibilité,
(ii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if an application for a disability pension had been received before the contributor’s application for a disability pension was actually received, or
(ii) soit est un cotisant à qui une pension d’invalidité aurait été payable au moment où il est réputé être devenu invalide, si une demande de pension d’invalidité avait été reçue avant le moment où elle l’a effectivement été,
(iii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if a division of unadjusted pensionable earnings that was made under section 55 or 55.
- Evidence: `party_position` cue `submits` at chunk `4481517` offsets `47-54`; context: [16] In his written submissions, the Applicant submits that both the GD and AD failed to apply the appropriate legal test in their decisions to deny the Applicant’s application for the CPP disability pension because the Applicant’s disability qualifies and is verified by medical evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481517` offsets `280-288`; context: [16] In his written submissions, the Applicant submits that both the GD and AD failed to apply the appropriate legal test in their decisions to deny the Applicant’s application for the CPP disability pension because the Applicant’s disability qualifies and is verified by medical evidence.
- Evidence: `governing_rule` cue `legal test` at chunk `4481517` offsets `111-121`; context: [16] In his written submissions, the Applicant submits that both the GD and AD failed to apply the appropriate legal test in their decisions to deny the Applicant’s application for the CPP disability pension because the Applicant’s disability qualifies and is verified by medical evidence.
- Evidence: `reasoning_application` cue `apply` at chunk `4481517` offsets `89-94`; context: [16] In his written submissions, the Applicant submits that both the GD and AD failed to apply the appropriate legal test in their decisions to deny the Applicant’s application for the CPP disability pension because the Applicant’s disability qualifies and is verified by medical evidence.

#### 9522:6:subtheme:2 · paragraphs 18-20

- Raw key terms: `applicant, decision, evidence, ignores, july, medical, says, able`
- Display key terms: `ignores, july, medical, says, able`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: ignores, july, medical, says, able Rule/authority context: Furthermore, the decision incorrectly applies case law in the interpretation of s 42(2)(a)(i) of the CPP, as the legal test is not whether the Applicant is able to pursue any employment, but whether the Applicant is able Application context: The decision wrongly concludes that the Applicant should have sought work opportunities despite being on an unpaid leave of absence. Evidence spans paragraphs 18-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4481518` offsets `824-831`; context: Furthermore, the decision incorrectly applies case law in the interpretation of s 42(2)(a)(i) of the CPP, as the legal test is not whether the Applicant is able to pursue any employment, but whether the Applicant is able to regularly pursue “any substantially gainful occupation”: Villani v Canada (Attorney General), 2001 FCA 248 [Villani].
- Evidence: `evidence_fact` cue `evidence` at chunk `4481518` offsets `284-292`; context: This conclusion disregards the medical evidence and encourages a breach of employment law.
- Evidence: `governing_rule` cue `legal test` at chunk `4481518` offsets `806-816`; context: Furthermore, the decision incorrectly applies case law in the interpretation of s 42(2)(a)(i) of the CPP, as the legal test is not whether the Applicant is able to pursue any employment, but whether the Applicant is able to regularly pursue “any substantially gainful occupation”: Villani v Canada (Attorney General), 2001 FCA 248 [Villani].
- Evidence: `reasoning_application` cue `concludes` at chunk `4481518` offsets `133-142`; context: The decision wrongly concludes that the Applicant should have sought work opportunities despite being on an unpaid leave of absence.
- Evidence: `counterargument_limitation` cue `but` at chunk `4481518` offsets `880-883`; context: Furthermore, the decision incorrectly applies case law in the interpretation of s 42(2)(a)(i) of the CPP, as the legal test is not whether the Applicant is able to pursue any employment, but whether the Applicant is able to regularly pursue “any substantially gainful occupation”: Villani v Canada (Attorney General), 2001 FCA 248 [Villani].
- Evidence: `evidence_fact` cue `evidence` at chunk `4481519` offsets `132-140`; context: [18] As for the GD’s July 17 decision regarding the prolonged “criterion,” the Applicant says that the decision ignores the medical evidence that demonstrates the Applicant had a 27% permanent disability in March 2011 during the MQP.

#### Section text

[15] The following provisions from the CPP are relevant in this proceeding:
When person deemed disabled
Personne déclarée invalide
42 (2) For the purposes of this Act,
42 (2) Pour l’application de la présente loi :
(a) a person shall be considered to be disabled only if he is determined in prescribed manner to have a severe and prolonged mental or physical disability, and for the purposes of this paragraph,
a) une personne n’est considérée comme invalide que si elle est déclarée, de la manière prescrite, atteinte d’une invalidité physique ou mentale grave et prolongée, et pour l’application du présent alinéa :
(i) a disability is severe only if by reason thereof the person in respect of whom the determination is made is incapable regularly of pursuing any substantially gainful occupation, and
(i) une invalidité n’est grave que si elle rend la personne à laquelle se rapporte la déclaration régulièrement incapable de détenir une occupation véritablement rémunératrice,
(ii) a disability is prolonged only if it is determined in prescribed manner that the disability is likely to be long continued and of indefinite duration or is likely to result in death; and
(ii) une invalidité n’est prolongée que si elle est déclarée, de la manière prescrite, devoir vraisemblablement durer pendant une période longue, continue et indéfinie ou devoir entraîner vraisemblablement le décès;
(b) a person is deemed to have become or to have ceased to be disabled at the time that is determined in the prescribed manner to be the time when the person became or ceased to be, as the case may be, disabled, but in no case shall a person — including a contributor referred to in subparagraph 44(1)(b)(ii) — be deemed to have become disabled earlier than fifteen months before the time of the making of any application in respect of which the determination is made.
b) une personne est réputée être devenue ou avoir cessé d’être invalide à la date qui est déterminée, de la manière prescrite, être celle où elle est devenue ou a cessé d’être, selon le cas, invalide, mais en aucun cas une personne — notamment le cotisant visé au sousalinéa 44(1)b)(ii) — n’est réputée être devenue invalide à une date antérieure de plus de quinze mois à la date de la présentation d’une demande à l’égard de laquelle la détermination a été faite.
…
…
Benefits payable
Prestations payables
44 (1) Subject to this Part,
44 (1) Sous réserve des autres dispositions de la présente partie :
…
…
(b) a disability pension shall be paid to a contributor who has not reached sixty-five years of age, to whom who
b) une pension d’invalidité doit être payée à un cotisant qui n’a pas atteint l’âge de soixante-cinq ans, à qui aucune pension de retraite n’est payable, qui est invalide et qui :
(i) has made contributions for not less than the minimum qualifying period,
(i) soit a versé des cotisations pendant au moins la période minimale d’admissibilité,
(ii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if an application for a disability pension had been received before the contributor’s application for a disability pension was actually received, or
(ii) soit est un cotisant à qui une pension d’invalidité aurait été payable au moment où il est réputé être devenu invalide, si une demande de pension d’invalidité avait été reçue avant le moment où elle l’a effectivement été,
(iii) is a contributor to whom a disability pension would have been payable at the time the contributor is deemed to have become disabled if a division of unadjusted pensionable earnings that was made under section 55 or 55.1 had not been made;
(iii) soit est un cotisant à qui une pension d’invalidité aurait été payable au moment où il est réputé être devenu invalide, si un partage des gains non ajustés ouvrant droit à pension n’avait pas été effectué en application des articles 55 et 55.1;
…
…
Calculation of minimum qualifying period in case of disability pension and disabled contributor’s child’s benefit
Calcul de la période minimale d’admissibilité dans le cas d’une pension d’invalidité et d’une prestation d’enfant de cotisant invalide
(2) For the purposes of paragraphs (1)(b) and (e),
(2) Pour l’application des alinéas (1)b) et e) :
(a) a contributor shall be considered to have made contributions for not less than the minimum qualifying period only if the contributor has made contributions during the contributor’s contributory period on earnings that are not less than the contributor’s basic exemption, calculated without regard to subsection 20(2),
a) le cotisant n’est réputé avoir versé des cotisations pendant au moins la période minimale d’admissibilité que s’il a versé des cotisations au cours de sa période cotisable sur des gains qui sont au moins égaux à son exemption de base, compte non tenu du paragraphe 20(2), selon le cas :
(i) for at least four of the last six calendar years included either wholly or partly in the contributor’s contributory period or, where there are fewer than six calendar years included either wholly or partly in the contributor’s contributory period, for at least four years,
(i) soit, pendant au moins quatre des six dernières années civiles comprises, en tout ou en partie, dans sa période cotisable, soit, lorsqu’il y a moins de six années civiles entièrement ou partiellement comprises dans sa période cotisable, pendant au moins quatre années,
(i.1) for at least 25 calendar years included either wholly or partly in the contributor’s contributory period, of which at least three are in the last six calendar years included either wholly or partly in the contributor’s contributory period, or
(i.1) pendant au moins vingt-cinq années civiles comprises, en tout ou en partie, dans sa période cotisable, dont au moins trois dans les six dernières années civiles comprises, en tout ou en partie, dans sa période cotisable,
(ii) for each year after the month of cessation of the contributor’s previous disability benefit; and
(ii) pour chaque année subséquente au mois de la cessation de la pension d’invalidité;
(b) the contributory period of a contributor shall be the period
b) la période cotisable d’un cotisant est la période qui :
(i) commencing January 1, 1966 or when he reaches eighteen years of age, whichever is the later, and
(i) commence le 1er janvier 1966 ou au moment où il atteint l’âge de dix-huit ans, en choisissant celle de ces deux dates qui est postérieure à l’autre,
(ii) ending with the month in which he is determined to have become disabled for the purpose of paragraph (1)(b),
(ii) se termine avec le mois au cours duquel il est déclaré invalide dans le cadre de l’alinéa (1)b),
but excluding
mais ne comprend pas :
(iii) any month that was excluded from the contributor’s contributory period under this Act or under a provincial pension plan by reason of disability, and
(iii) un mois qui, en raison d’une invalidité, a été exclu de la période cotisable de ce cotisant conformément à la présente loi ou à un régime provincial de pensions,
(iv) in relation to any benefits payable under this Act for any month after December, 1977, any month for which the contributor was a family allowance recipient in a year for which the contributor’s unadjusted pensionable earnings are less than the basic exemption of the contributor for the year, calculated without regard to subsection 20(2).
(iv) en ce qui concerne une prestation payable en application de la présente loi à l’égard d’un mois postérieur à décembre 1977, un mois relativement auquel il était bénéficiaire d’une allocation familiale dans une année à l’égard de laquelle ses gains non ajustés ouvrant droit à pension étaient inférieurs à son exemption de base pour l’année, compte non tenu du paragraphe 20(2).
VII. ARGUMENT
A. Applicant

[16] In his written submissions, the Applicant submits that both the GD and AD failed to apply the appropriate legal test in their decisions to deny the Applicant’s application for the CPP disability pension because the Applicant’s disability qualifies and is verified by medical evidence.

[17] With regards to the GD’s July 17 decision on severity, the Applicant says there are several errors of law. The decision wrongly concludes that the Applicant should have sought work opportunities despite being on an unpaid leave of absence. This conclusion disregards the medical evidence and encourages a breach of employment law. This conclusion also ignores the fact that, despite his employer’s accommodations, the Applicant was unable to complete even a four-hour work day due to his medical condition. The expectation that the Applicant could pursue employment, despite the medical evidence demonstrating that the Applicant was incapable of pursuing any employment, is unreasonable. Furthermore, the decision incorrectly applies case law in the interpretation of s 42(2)(a)(i) of the CPP, as the legal test is not whether the Applicant is able to pursue any employment, but whether the Applicant is able to regularly pursue “any substantially gainful occupation”: Villani v Canada (Attorney General), 2001 FCA 248 [Villani].

[18] As for the GD’s July 17 decision regarding the prolonged “criterion,” the Applicant says that the decision ignores the medical evidence that demonstrates the Applicant had a 27% permanent disability in March 2011 during the MQP. This finding is also contrary to subsequent decisions by the GD which have found that a period of three years is a prolonged period of “indefinite duration,” and that there is no requirement for objective medical evidence to be adduced to support a finding of severe disability.

[19] The Applicant asks the Court to amend the style of cause to name the appropriate Respondent in these proceedings.

## 9522:7 · paragraphs 21-36

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `894b7007914dd7d84e9c667e6dcfd5bc8f430c602faf802cc0569721503cd1dd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9522:7:subtheme:1 · paragraphs 21-24

- Raw key terms: `disability, according, appeal, court, leave, pension, plan, reasonable`
- Display key terms: `disability, according, leave, pension, plan, reasonable`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position Display terms: disability, according, leave, pension, plan, reasonable Position/evidence statements: [21] The Respondent submits that the AD’s Decision to deny leave to appeal was reasonable and this application should be dismissed. Rule/authority context: (2) Disability under the Plan Operative outcome context: [20] The Applicant seeks relief in the form of an order that sets aside the finding of the GD and finds in favour of the Applicant or, in the alternative, that the Court refer the matter back to a different tribunal and  | [21] The Respondent submits that the AD’s Decision to deny leave to appeal was reasonable and this application should be dismissed. Evidence spans paragraphs 21-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `granted` at chunk `4481521` offsets `249-256`; context: [20] The Applicant seeks relief in the form of an order that sets aside the finding of the GD and finds in favour of the Applicant or, in the alternative, that the Court refer the matter back to a different tribunal and direct that the Applicant be granted a CPP disability pension.
- Evidence: `party_position` cue `submits` at chunk `4481522` offsets `20-27`; context: [21] The Respondent submits that the AD’s Decision to deny leave to appeal was reasonable and this application should be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4481522` offsets `121-130`; context: [21] The Respondent submits that the AD’s Decision to deny leave to appeal was reasonable and this application should be dismissed.
- Evidence: `evidence_fact` cue `found that` at chunk `4481523` offsets `306-316`; context: The Federal Court of Appeal has found that a reasonable chance of success means an arguable case: Fancy v Canada (Attorney General), 2010 FCA 63.
- Evidence: `governing_rule` cue `under` at chunk `4481523` offsets `435-440`; context: (2) Disability under the Plan

#### 9522:7:subtheme:2 · paragraphs 25-28

- Raw key terms: `applicant, disability, chance, evidence, grounds, reasonable, respondent, success`
- Display key terms: `disability, chance, grounds, reasonable, success`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: disability, chance, grounds, reasonable, success Position/evidence statements: [25] The Respondent submits that the Applicant has argued grounds in this review application that were not raised in his leave to appeal before the AD. | The Applicant was represented by a paralegal with a specialization in CPP disability claims. Rule/authority context: In characterizing the sole issue as being whether the Applicant has a severe and prolonged disability under the CPP, the Applicant attempts to re-litigate the matter, which is not the purpose of judicial review. | [27] The first of these new grounds refers to the GD and AD’s application of the appropriate legal test to determine disability. Application context: These grounds do not have a reasonable chance of success because the evidence that the Applicant claims was disregarded is actually referred to in the decision. Evidence spans paragraphs 25-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4481525` offsets `141-148`; context: [24] A disability is considered “severe” only if the person is incapable regularly of pursuing any substantially gainful occupation, and not whether they are capable of performing their usual occupation: Canada (Minister of Human Resources Development) v Scott, 2003 FCA 34 at para 7.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481525` offsets `397-405`; context: An applicant who seeks to satisfy this definition must demonstrate a serious health problem and, where there is evidence of work capacity, that efforts at obtaining and maintaining employment have been unsuccessful by reason of the health condition: Klabouch v Canada (Social Development), 2008 FCA 33 at paras 14-17 [Klabouch].
- Evidence: `issue` cue `issue` at chunk `4481526` offsets `179-184`; context: In characterizing the sole issue as being whether the Applicant has a severe and prolonged disability under the CPP, the Applicant attempts to re-litigate the matter, which is not the purpose of judicial review.
- Evidence: `party_position` cue `submits` at chunk `4481526` offsets `20-27`; context: [25] The Respondent submits that the Applicant has argued grounds in this review application that were not raised in his leave to appeal before the AD.
- Evidence: `governing_rule` cue `under` at chunk `4481526` offsets `254-259`; context: In characterizing the sole issue as being whether the Applicant has a severe and prolonged disability under the CPP, the Applicant attempts to re-litigate the matter, which is not the purpose of judicial review.
- Evidence: `party_position` cue `claims` at chunk `4481527` offsets `294-300`; context: The Applicant was represented by a paralegal with a specialization in CPP disability claims.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481527` offsets `90-98`; context: [26] In its consideration of leave to appeal, the AD is not obliged to scrutinize all the evidence before it, but only the grounds raised on leave: Mohamed v Canada (Attorney General), 2016 FC 482 at para 12.
- Evidence: `counterargument_limitation` cue `but` at chunk `4481527` offsets `110-113`; context: [26] In its consideration of leave to appeal, the AD is not obliged to scrutinize all the evidence before it, but only the grounds raised on leave: Mohamed v Canada (Attorney General), 2016 FC 482 at para 12.
- Evidence: `party_position` cue `argues` at chunk `4481528` offsets `144-150`; context: The Respondent argues that the GD clearly set out the appropriate legal test for disability in its July 17 decision and considered multiple factors, including the Applicant’s age, language skills, education, work history, and medical conditions.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481528` offsets `571-579`; context: The second of the new grounds refers to the contention that the GD’s conclusion that the Applicant should have sought other employment opportunities indicates a complete disregard for the medical evidence.
- Evidence: `governing_rule` cue `legal test` at chunk `4481528` offsets `93-103`; context: [27] The first of these new grounds refers to the GD and AD’s application of the appropriate legal test to determine disability.
- Evidence: `reasoning_application` cue `because` at chunk `4481528` offsets `638-645`; context: These grounds do not have a reasonable chance of success because the evidence that the Applicant claims was disregarded is actually referred to in the decision.
- Evidence: `counterargument_limitation` cue `However` at chunk `4481528` offsets `742-749`; context: However, the conclusion based on the evidence is simply not favourable to the Applicant; that is, the GD did not agree with the medical reports that the Applicant was “totally disabled from any employment.

#### 9522:7:subtheme:3 · paragraphs 29-32

- Raw key terms: `applicant, appeal, chance, reasonable, severe, success, application, appropriate`
- Display key terms: `chance, reasonable, severe, success, appropriate`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: chance, reasonable, severe, success, appropriate Position/evidence statements: [28] The Applicant also maintains that there was a failure to apply the standard of reasonableness, but the Respondent submits that both the GD and AD applied the appropriate standard in assessing the applications. | The Applicant argues that the medical evidence of Dr. Application context: [28] The Applicant also maintains that there was a failure to apply the standard of reasonableness, but the Respondent submits that both the GD and AD applied the appropriate standard in assessing the applications. | Thus, it was reasonable for the AD to conclude that this ground did not have a reasonable chance of success on appeal. Operative outcome context: [31] Overall, the decisions by the GD and AD demonstrate clear justification for why the application was denied. Evidence spans paragraphs 29-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4481529` offsets `233-240`; context: The GD determined whether the Applicant had a severe and prolonged disability on or before the MQP on a balance of probabilities, and the AD determined whether the appeal had a reasonable chance of success.
- Evidence: `party_position` cue `submits` at chunk `4481529` offsets `119-126`; context: [28] The Applicant also maintains that there was a failure to apply the standard of reasonableness, but the Respondent submits that both the GD and AD applied the appropriate standard in assessing the applications.
- Evidence: `reasoning_application` cue `apply` at chunk `4481529` offsets `62-67`; context: [28] The Applicant also maintains that there was a failure to apply the standard of reasonableness, but the Respondent submits that both the GD and AD applied the appropriate standard in assessing the applications.
- Evidence: `party_position` cue `argues` at chunk `4481530` offsets `117-123`; context: The Applicant argues that the medical evidence of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481530` offsets `141-149`; context: The Applicant argues that the medical evidence of Dr.
- Evidence: `counterargument_limitation` cue `but` at chunk `4481530` offsets `199-202`; context: Samuels was not given appropriate weight, but the GD referred overtly to Dr.
- Evidence: `party_position` cue `argued` at chunk `4481531` offsets `55-61`; context: [30] In his leave to appeal application, the Applicant argued that he had medical conditions that qualified as severe and prolonged in nature and that are sufficient to render him unemployable in any capacity.
- Evidence: `reasoning_application` cue `conclude` at chunk `4481531` offsets `387-395`; context: Thus, it was reasonable for the AD to conclude that this ground did not have a reasonable chance of success on appeal.
- Evidence: `counterargument_limitation` cue `but` at chunk `4481531` offsets `281-284`; context: The AD noted that these statements did not identify errors in Decision but rather expressed disagreement with the outcome of the Decision.
- Evidence: `party_position` cue `submits` at chunk `4481532` offsets `128-135`; context: The Respondent submits that these proceedings are merely an attempt to re-litigate the Applicant’s appeals.
- Evidence: `disposition` cue `denied` at chunk `4481532` offsets `105-111`; context: [31] Overall, the decisions by the GD and AD demonstrate clear justification for why the application was denied.

#### 9522:7:subtheme:4 · paragraphs 33-36

- Raw key terms: `respondent, applicant, attorney, canada, court, decision, general, judicial`
- Display key terms: `judicial`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: judicial Position/evidence statements: The Respondent submits that the Court should only consider the AD’s denial of the leave to appeal and that the Decision does not warrant judicial intervention. Rule/authority context: [32] Furthermore, the Applicant implies that he may have been entitled to benefits under other insurance regimes and that this should favour his position as qualifying for a CPP disability pension. Evidence spans paragraphs 33-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4481533` offsets `331-336`; context: However, this Court has determined that qualification for a benefit provided under provincial legislation does not raise an arguable issue concerning a decision that similar evidence does not qualify for benefit under another statute such as the Plan: Callihoo v Canada (Attorney General), 2000 FCJ No 612 at para 12.
- Evidence: `evidence_fact` cue `determined that` at chunk `4481533` offsets `222-237`; context: However, this Court has determined that qualification for a benefit provided under provincial legislation does not raise an arguable issue concerning a decision that similar evidence does not qualify for benefit under another statute such as the Plan: Callihoo v Canada (Attorney General), 2000 FCJ No 612 at para 12.
- Evidence: `governing_rule` cue `under` at chunk `4481533` offsets `83-88`; context: [32] Furthermore, the Applicant implies that he may have been entitled to benefits under other insurance regimes and that this should favour his position as qualifying for a CPP disability pension.
- Evidence: `counterargument_limitation` cue `However` at chunk `4481533` offsets `198-205`; context: However, this Court has determined that qualification for a benefit provided under provincial legislation does not raise an arguable issue concerning a decision that similar evidence does not qualify for benefit under another statute such as the Plan: Callihoo v Canada (Attorney General), 2000 FCJ No 612 at para 12.
- Evidence: `issue` cue `whether` at chunk `4481534` offsets `60-67`; context: [33] The Respondent maintains that although it is not clear whether the Applicant seeks to set aside the decision of the GD or AD, it is clear the relief sought is inappropriate as the Applicant seeks a directed verdict on the merits that would substitute the Court’s opinion for the GD’s.
- Evidence: `party_position` cue `submits` at chunk `4481534` offsets `305-312`; context: The Respondent submits that the Court should only consider the AD’s denial of the leave to appeal and that the Decision does not warrant judicial intervention.

#### Section text

[20] The Applicant seeks relief in the form of an order that sets aside the finding of the GD and finds in favour of the Applicant or, in the alternative, that the Court refer the matter back to a different tribunal and direct that the Applicant be granted a CPP disability pension. The Applicant also requests any other relief that the Court may deem just as well as the costs of these proceedings on a substantial indemnity basis, including the proceedings before the GD.
B. Respondent

[21] The Respondent submits that the AD’s Decision to deny leave to appeal was reasonable and this application should be dismissed.
(1) Leave to Appeal

[22] According to s 58(2) of the DESD Act, leave to appeal is refused if the appeal has no reasonable chance of success, which can only be found if it is based on one of the enumerated grounds in s 58(1): Belo-Alves v Canada (Attorney General), 2014 FC 1100 at paras 70-73. The Federal Court of Appeal has found that a reasonable chance of success means an arguable case: Fancy v Canada (Attorney General), 2010 FCA 63.
(2) Disability under the Plan

[23] According to ss 42(2), 44(1)(b), and 44(2) of the CPP, a person must satisfy three requirements to be entitled to a disability pension. They must: meet the contributory requirements; be disabled within the meaning of the Plan when the contributory requirements were met; and be so disabled continuously and indefinitely. Subsection 42(2) of the CPP also provides that a person shall be considered to be disabled only if he or she is determined to have a severe and prolonged mental or physical disability.

[24] A disability is considered “severe” only if the person is incapable regularly of pursuing any substantially gainful occupation, and not whether they are capable of performing their usual occupation: Canada (Minister of Human Resources Development) v Scott, 2003 FCA 34 at para 7. An applicant who seeks to satisfy this definition must demonstrate a serious health problem and, where there is evidence of work capacity, that efforts at obtaining and maintaining employment have been unsuccessful by reason of the health condition: Klabouch v Canada (Social Development), 2008 FCA 33 at paras 14-17 [Klabouch]. This must be demonstrated by medical evidence and evidence of employment efforts and possibilities: Villani, above, at para 50; Klabouch, above, at para 16. An applicant must also prove that the disability existed prior to the expiry of the MQP and continuously thereafter: Granovsky v Canada (Minister of Employment and Immigration), 2000 SCC 28 at para 28.
(3) Reasonableness

[25] The Respondent submits that the Applicant has argued grounds in this review application that were not raised in his leave to appeal before the AD. In characterizing the sole issue as being whether the Applicant has a severe and prolonged disability under the CPP, the Applicant attempts to re-litigate the matter, which is not the purpose of judicial review. The Applicant also fails to address how the grounds presented before the AD raised a reasonable chance of success and how the AD erred in refusing to grant leave to appeal. Instead, the Applicant raises an alleged error in the application of a legal test that was not before the AD.

[26] In its consideration of leave to appeal, the AD is not obliged to scrutinize all the evidence before it, but only the grounds raised on leave: Mohamed v Canada (Attorney General), 2016 FC 482 at para 12. The Applicant was represented by a paralegal with a specialization in CPP disability claims. Thus, the Applicant should have advanced the relevant grounds in seeking leave to appeal, and the new ground advanced before the Court should not render the Decision unreasonable. Furthermore, even if the Applicant had advanced this ground before the AD, the Respondent submits that this would not have demonstrated a reasonable chance of success on appeal, or warrant a grant of leave to appeal.

[27] The first of these new grounds refers to the GD and AD’s application of the appropriate legal test to determine disability. The Respondent argues that the GD clearly set out the appropriate legal test for disability in its July 17 decision and considered multiple factors, including the Applicant’s age, language skills, education, work history, and medical conditions. The second of the new grounds refers to the contention that the GD’s conclusion that the Applicant should have sought other employment opportunities indicates a complete disregard for the medical evidence. These grounds do not have a reasonable chance of success because the evidence that the Applicant claims was disregarded is actually referred to in the decision. However, the conclusion based on the evidence is simply not favourable to the Applicant; that is, the GD did not agree with the medical reports that the Applicant was “totally disabled from any employment.”

[28] The Applicant also maintains that there was a failure to apply the standard of reasonableness, but the Respondent submits that both the GD and AD applied the appropriate standard in assessing the applications. The GD determined whether the Applicant had a severe and prolonged disability on or before the MQP on a balance of probabilities, and the AD determined whether the appeal had a reasonable chance of success.

[29] In particular, the AD reasonably assessed the grounds that were put before it on leave to appeal. The Applicant argues that the medical evidence of Dr. Samuels was not given appropriate weight, but the GD referred overtly to Dr. Samuels’ medical report and reasonably analyzed that it did not reveal severe conditions that would prevent the Applicant from seeking employment. The GD also noted that the May 2015 letter which did reveal Dr. Samuels’ opinion that the Applicant had severe conditions that would prevent employment was written well past the relevant MQP. As such, the GD was obligated to accord that letter less weight than the evidence up to the date of the MQP. In light of these considerations, the AD found that the GD did not disregard the medical evidence. Since the function of the AD is not to reweigh evidence on leave to appeal, it did not do so. Instead, the AD reasonably concluded that the GD’s consideration and weighing of the medical evidence had been reasonable and, consequently, this ground did not have a reasonable chance of success on appeal.

[30] In his leave to appeal application, the Applicant argued that he had medical conditions that qualified as severe and prolonged in nature and that are sufficient to render him unemployable in any capacity. The AD noted that these statements did not identify errors in Decision but rather expressed disagreement with the outcome of the Decision. Thus, it was reasonable for the AD to conclude that this ground did not have a reasonable chance of success on appeal.

[31] Overall, the decisions by the GD and AD demonstrate clear justification for why the application was denied. The Respondent submits that these proceedings are merely an attempt to re-litigate the Applicant’s appeals.

[32] Furthermore, the Applicant implies that he may have been entitled to benefits under other insurance regimes and that this should favour his position as qualifying for a CPP disability pension. However, this Court has determined that qualification for a benefit provided under provincial legislation does not raise an arguable issue concerning a decision that similar evidence does not qualify for benefit under another statute such as the Plan: Callihoo v Canada (Attorney General), 2000 FCJ No 612 at para 12.
(4) Order Sought

[33] The Respondent maintains that although it is not clear whether the Applicant seeks to set aside the decision of the GD or AD, it is clear the relief sought is inappropriate as the Applicant seeks a directed verdict on the merits that would substitute the Court’s opinion for the GD’s. The Respondent submits that the Court should only consider the AD’s denial of the leave to appeal and that the Decision does not warrant judicial intervention.

[34] The Respondent also requests that the style of cause to be amended to reflect the Respondent as the Attorney General of Canada.

[35] The Respondent seeks an order dismissing the application for judicial review without costs.


## 9522:8 · paragraphs 37-41

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ead34cfb59b1d05f6c3e3383be7214995d53742eaa4228defb2703185c260efb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9522:8:subtheme:1 · paragraphs 37-38

- Raw key terms: `issues, raised, analysis, applicant, argument, court, deal, disability`
- Display key terms: `issues, raised, analysis, argument, deal, disability`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: issues, raised, analysis, argument, deal, disability Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4481537` offsets `92-98`; context: [36] In writing and in oral argument before the Court, the Applicant has raised a series of issues for review, and I will deal with each of them in turn.

#### 9522:8:subtheme:2 · paragraphs 39-40

- Raw key terms: `applicant, court, appeal, appropriately, august, decide, decision, defined`
- Display key terms: `appropriately, august, decide, defined`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: appropriately, august, decide, defined Evidence spans paragraphs 39-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4481538` offsets `56-63`; context: [37] The Applicant says that the Court should determine whether he has a severe and prolonged physical disability as defined in s 42(2)(a) of the CPP to qualify for a CPP disability pension.
- Evidence: `issue` cue `issue` at chunk `4481539` offsets `20-25`; context: [38] This is not an issue that is appropriately before the Court.

#### 9522:8:subtheme:3 · paragraphs 41-41

- Raw key terms: `applicant, asking, court, decision, issue, jurisdiction, substitute, test`
- Display key terms: `asking, jurisdiction, substitute`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: asking, jurisdiction, substitute Evidence spans paragraphs 41-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4481540` offsets `74-79`; context: [39] The Applicant is asking the Court to substitute its decision on this issue for that of the GD.

#### Section text

VIII. ANALYSIS
A. Issues Raised

[36] In writing and in oral argument before the Court, the Applicant has raised a series of issues for review, and I will deal with each of them in turn.
B. Severe and Prolonged Disability

[37] The Applicant says that the Court should determine whether he has a severe and prolonged physical disability as defined in s 42(2)(a) of the CPP to qualify for a CPP disability pension.

[38] This is not an issue that is appropriately before the Court. This issue was for the GD to decide, which it did. The Court is not reviewing the GD’s decision. The Court is reviewing the AD’s Decision of August 27, 2015 which refused the Applicant leave to appeal the GD’s decision of July 17, 2015.

[39] The Applicant is asking the Court to substitute its decision on this issue for that of the GD. The Court has no jurisdiction to do this.
C. The Wrong Test

## 9522:9 · paragraphs 42-54

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2801fcb6b8bc552d93e8c0241fcf6a18df17f4bf8bce0e545cdc5d2cf9a02bed`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9522:9:subtheme:1 · paragraphs 42-46

- Raw key terms: `appeal, decision, applicant, division, general, disability, evidence, issue`
- Display key terms: `division, disability`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: division, disability Rule/authority context: It is respectfully submitted that the Board (General Division – Jackie Laidlaw on July 17, 2015 and Hazelyn Ross – Appeal Division – August 27, 2015 (sic) failed to apply the appropriate legal test to arrive at their dec Application context: It is respectfully submitted that the Board (General Division – Jackie Laidlaw on July 17, 2015 and Hazelyn Ross – Appeal Division – August 27, 2015 (sic) failed to apply the appropriate legal test to arrive at their dec | [42] The AD’s Decision sets out and applies the correct test for a leave to appeal: Evidence spans paragraphs 42-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4481541` offsets `45-50`; context: [40] The Applicant also raises the following issue:
19.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481541` offsets `442-450`; context: It is respectfully submitted that the Board (General Division – Jackie Laidlaw on July 17, 2015 and Hazelyn Ross – Appeal Division – August 27, 2015 (sic) failed to apply the appropriate legal test to arrive at their decision to reject the applicant’s application for payment of CPP disability benefit as a result of his permanent disability verified by appropriate medical documentary evidence as shown in paragraphs 4-13 [inclusive] above.
- Evidence: `governing_rule` cue `legal test` at chunk `4481541` offsets `243-253`; context: It is respectfully submitted that the Board (General Division – Jackie Laidlaw on July 17, 2015 and Hazelyn Ross – Appeal Division – August 27, 2015 (sic) failed to apply the appropriate legal test to arrive at their decision to reject the applicant’s application for payment of CPP disability benefit as a result of his permanent disability verified by appropriate medical documentary evidence as shown in paragraphs 4-13 [inclusive] above.
- Evidence: `reasoning_application` cue `apply` at chunk `4481541` offsets `221-226`; context: It is respectfully submitted that the Board (General Division – Jackie Laidlaw on July 17, 2015 and Hazelyn Ross – Appeal Division – August 27, 2015 (sic) failed to apply the appropriate legal test to arrive at their decision to reject the applicant’s application for payment of CPP disability benefit as a result of his permanent disability verified by appropriate medical documentary evidence as shown in paragraphs 4-13 [inclusive] above.
- Evidence: `issue` cue `issue` at chunk `4481542` offsets `58-63`; context: [41] As in most applications of this nature, the critical issue was the severity of the Applicant’s disability, and what the medical evidence adduced by the Applicant had to say on this central point.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481542` offsets `133-141`; context: [41] As in most applications of this nature, the critical issue was the severity of the Applicant’s disability, and what the medical evidence adduced by the Applicant had to say on this central point.
- Evidence: `reasoning_application` cue `applies` at chunk `4481543` offsets `36-43`; context: [42] The AD’s Decision sets out and applies the correct test for a leave to appeal:

#### 9522:9:subtheme:2 · paragraphs 47-50

- Raw key terms: `canada, attorney, decision, evidence, general, leave, medical, above`
- Display key terms: `leave, medical, above`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: leave, medical, above Rule/authority context: In cases like this, the Tribunal should examine the medical evidence and compare it to the decision under consideration. | It demonstrates that, on the plain meaning of the words in subparagraph 42(2)(a)(i), Parliament must have intended that the legal test for severity be applied with some degree of reference to the "real world" . Application context: Nevertheless, the requirements of subsection 58(1) should not be applied mechanically or in a perfunctory manner. | However all of this failed and as of September 21, 2009 - because of his constant pain - he was unable to return to work. Operative outcome context: If important evidence has been arguably overlooked or possibly misconstrued, leave to appeal should ordinarily be granted notwithstanding the presence of technical deficiencies in the application for leave. | It is further respectfully submitted that during the Minimum Qualifying Period (MQP) the , applicant on March 2011 was found to have a 27% permanent disability as a result of the assessment of a WSIB independent medical  Evidence spans paragraphs 47-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4481546` offsets `652-659`; context: On the contrary, the Appeal Division should review the underlying record and determine whether the decision failed to properly account for any of the evidence: Karadeolian v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481546` offsets `245-253`; context: [43] Justice Boswell provided guidance as to how the AD should go about its task in Griffin v Canada (Attorney General), 2016 FC 874 at para 20:
It is well established that the party seeking leave to appeal bears the onus of adducing all of the evidence and arguments required to meet the requirements of subsection 58(1): see, e.
- Evidence: `reasoning_application` cue `applied` at chunk `4481546` offsets `516-523`; context: Nevertheless, the requirements of subsection 58(1) should not be applied mechanically or in a perfunctory manner.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4481546` offsets `451-463`; context: Nevertheless, the requirements of subsection 58(1) should not be applied mechanically or in a perfunctory manner.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481547` offsets `437-445`; context: In cases like this, the Tribunal should examine the medical evidence and compare it to the decision under consideration.
- Evidence: `governing_rule` cue `under` at chunk `4481547` offsets `477-482`; context: In cases like this, the Tribunal should examine the medical evidence and compare it to the decision under consideration.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `4481547` offsets `620-635`; context: If important evidence has been arguably overlooked or possibly misconstrued, leave to appeal should ordinarily be granted notwithstanding the presence of technical deficiencies in the application for leave.
- Evidence: `disposition` cue `granted` at chunk `4481547` offsets `612-619`; context: If important evidence has been arguably overlooked or possibly misconstrued, leave to appeal should ordinarily be granted notwithstanding the presence of technical deficiencies in the application for leave.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481548` offsets `428-436`; context: has been unpaid leave of absence since 2009” but wrongly concluded that the applicant - while on unpaid leave of absence - should have gone to look for work elsewhere thereby completely disregarding the medical evidence at paragraph 6 above [the applicant was “totally disabled any employment”] and also committing a breach of the Employment Act.
- Evidence: `governing_rule` cue `legal test` at chunk `4481548` offsets `2474-2484`; context: It demonstrates that, on the plain meaning of the words in subparagraph 42(2)(a)(i), Parliament must have intended that the legal test for severity be applied with some degree of reference to the "real world" .
- Evidence: `reasoning_application` cue `because` at chunk `4481548` offsets `905-912`; context: However all of this failed and as of September 21, 2009 - because of his constant pain - he was unable to return to work.
- Evidence: `counterargument_limitation` cue `but` at chunk `4481548` offsets `262-265`; context: has been unpaid leave of absence since 2009” but wrongly concluded that the applicant - while on unpaid leave of absence - should have gone to look for work elsewhere thereby completely disregarding the medical evidence at paragraph 6 above [the applicant was “totally disabled any employment”] and also committing a breach of the Employment Act.
- Evidence: `disposition` cue `granted` at chunk `4481548` offsets `4035-4042`; context: It is further respectfully submitted that during the Minimum Qualifying Period (MQP) the , applicant on March 2011 was found to have a 27% permanent disability as a result of the assessment of a WSIB independent medical examiner and was granted a NEL award based upon this assessment but Ms Laidlaw erred in law when she completely disregarded this independent medical finding.

#### 9522:9:subtheme:3 · paragraphs 51-54

- Raw key terms: `decision, errors, tribunal, appeal, applicant, disability, evidence, finding`
- Display key terms: `errors, disability, finding`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: errors, disability, finding Position/evidence statements: [29] The Respondent submitted that there is insufficient Objective medical evidence to support a finding that the Appellant was disabled within the meaning of the CPP (Canada Pension Plan) by December 31, 2011. | Counsel submitted that the medical evidence supported such a finding and that in its decision the General Division failed to give significant weight to that evidence, notably that of Dr. Application context: [8] As stated earlier, the Tribunal concludes that Counsel for the Applicant was alleging that the General Division decision was based on errors of fact. Evidence spans paragraphs 51-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4481550` offsets `402-407`; context: The Tribunal notes that there is no requirement in the CPP (Canada Pension Plan) that objective medical evidence must be adduced to support a finding of severe disability In determining this issue, the Tribunal must assess all of the relevant evidence.
- Evidence: `party_position` cue `submitted` at chunk `4481550` offsets `20-29`; context: [29] The Respondent submitted that there is insufficient Objective medical evidence to support a finding that the Appellant was disabled within the meaning of the CPP (Canada Pension Plan) by December 31, 2011.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481550` offsets `75-83`; context: [29] The Respondent submitted that there is insufficient Objective medical evidence to support a finding that the Appellant was disabled within the meaning of the CPP (Canada Pension Plan) by December 31, 2011.
- Evidence: `counterargument_limitation` cue `but` at chunk `4481551` offsets `102-105`; context: [46] As the AD’s Decision makes clear, the Applicant was somewhat imprecise in his grounds of appeal, but the AD did decide what those grounds of appeal were:
ANALYSIS
- Evidence: `party_position` cue `submitted` at chunk `4481553` offsets `344-353`; context: Counsel submitted that the medical evidence supported such a finding and that in its decision the General Division failed to give significant weight to that evidence, notably that of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481553` offsets `371-379`; context: Counsel submitted that the medical evidence supported such a finding and that in its decision the General Division failed to give significant weight to that evidence, notably that of Dr.
- Evidence: `reasoning_application` cue `concludes` at chunk `4481553` offsets `36-45`; context: [8] As stated earlier, the Tribunal concludes that Counsel for the Applicant was alleging that the General Division decision was based on errors of fact.

#### Section text

[40] The Applicant also raises the following issue:
19. It is respectfully submitted that the Board (General Division – Jackie Laidlaw on July 17, 2015 and Hazelyn Ross – Appeal Division – August 27, 2015 (sic) failed to apply the appropriate legal test to arrive at their decision to reject the applicant’s application for payment of CPP disability benefit as a result of his permanent disability verified by appropriate medical documentary evidence as shown in paragraphs 4-13 [inclusive] above.

[41] As in most applications of this nature, the critical issue was the severity of the Applicant’s disability, and what the medical evidence adduced by the Applicant had to say on this central point.

[42] The AD’s Decision sets out and applies the correct test for a leave to appeal:

[5] Leave to appeal a decision of the General Division of the Tribunal is a preliminary step to an appeal before the Appeal Division. To grant leave, the Appeal Division must be satisfied that the appeal would have a reasonable chance of success. In Canada (Minister of Human Resources Department) v. Hogerworst, 2007 FCA 41 as well as in Fancy v. Canada (Attorney General), 2010 FCA 63, the Federal Court of Appeal equated a reasonable chance of success to an arguable case.

[6] There are only three grounds on which an applicant may bring an appeal. These grounds are set out in section 58 of the DESD Act. They are,
(1) a breach of natural justice;
(2) that the General Division erred in law; and
(3) the General Division based its decision on an error of fact made in a perverse or capricious manner or without regard for the material before it.
(footnotes omitted)

[43] Justice Boswell provided guidance as to how the AD should go about its task in Griffin v Canada (Attorney General), 2016 FC 874 at para 20:
It is well established that the party seeking leave to appeal bears the onus of adducing all of the evidence and arguments required to meet the requirements of subsection 58(1): see, e.g., Tracey, above, at para 31; also see Auch v. Canada (Attorney General), 2016 FC 199 at para 52, [2016] F.C.J. No 155. Nevertheless, the requirements of subsection 58(1) should not be applied mechanically or in a perfunctory manner. On the contrary, the Appeal Division should review the underlying record and determine whether the decision failed to properly account for any of the evidence: Karadeolian v. Canada (Attorney General), 2016 FC 615 at para 10, [2016] F.C.J. No. 585.
(emphasis added)

[44] Likewise, in Karadeolian v Canada (Attorney General), 2016 FC 615 at paras 9-10, Justice Barnes wrote:
I do agree that the Tribunal must be wary of mechanistically applying the language of section 58 of the Act when it performs its gatekeeping function. It should not be trapped by the precise grounds for appeal advanced by a self-represented party like Ms. Karadeolian. In cases like this, the Tribunal should examine the medical evidence and compare it to the decision under consideration. If important evidence has been arguably overlooked or possibly misconstrued, leave to appeal should ordinarily be granted notwithstanding the presence of technical deficiencies in the application for leave.

[45] The Applicant elaborates in his written submissions what he means by the “wrong test”:
20. It is further respectfully submitted that Ms Laidlaw erred in law when at paragraph [46] of her decision she opined “....has been unpaid leave of absence since 2009” but wrongly concluded that the applicant - while on unpaid leave of absence - should have gone to look for work elsewhere thereby completely disregarding the medical evidence at paragraph 6 above [the applicant was “totally disabled any employment”] and also committing a breach of the Employment Act. She also completely ignored the fact that the applicant had a sedentary job - sitting all day before a computer and his employer Bell had not only accommodated him by allowing him to work a four hour day but had acquired a special chair to accommodate him and his medical condition. However all of this failed and as of September 21, 2009 - because of his constant pain - he was unable to return to work.
21. It is further respectfully submitted that Ms Laidlaw erred in law when she gave her version of the Villani v. Canada (AG) [2001] FCA 248 - because all the medical evidence points to the fact that the applicant was incapable at all times of pursuing any conceivable occupation:
At paragraph 38 of that decision the Court found reviewing the decision of the Barlow case:
“38. The analysis of subparagraph 42(2)(a)(i ) strongly suggests a legislative intention to apply the severity requirement in the “real world” context. Requiring that an applicant be incapable regularly of pursuing any conceivable occupation is quite different from requiring that an applicant be incapable at all times of pursuing any conceivable occupation. Each word in the subparagraph must be given meaning and when read in that way the subparagraph indicates, in my opinion that Parliament viewed as severe any disability which renders an applicant incapable of pursuing with consistent frequency any truly remunerative occupation. In my view, it follows from this that the hypothetical occupations which a decision maker must consider cannot be divorced from the particular circumstances of the applicant such as age, education level, language proficiency and past work and life experience.
“39. I agree with the conclusions in Barlow, supra and the reasons therefor in that case was brief and sound. It demonstrates that, on the plain meaning of the words in subparagraph 42(2)(a)(i), Parliament must have intended that the legal test for severity be applied with some degree of reference to the "real world" . It is difficult to understand what purpose the legislation would serve if it provided that disability benefits should be paid only to those applicants who were incapable of pursuing any form of occupation no matter how irregular, ungainful or insubstantial. Such an approach would defeat the objectives of the Plan and result in an analysis that is supportable on the plain language of the statute.”
22. It is further respectfully submitted that the Board has adopted the strict abstract approach in the interpretation of the “severity requirement” in subparagraph 42(2)(a)(i) without analyzing all of the legislative language - Villani above: see [42]
“[42] The explanation by the Deputy Minister of Welfare is unambiguous. The test for severity is not that a disability be “total”. In order to express the more lenient test for severity under the Plan therefore the drafters introduced the notion of severity as the inability regularly to pursue any substantially gainful occupation.”
23. It is further respectfully submitted that the Board failed to apply the standard of reasonableness when arriving at its decision to deny the applicant’s application for CPP disability benefit.
See: Villiani v Canada (Attorney General) supra.
24. It is further respectfully submitted that during the Minimum Qualifying Period (MQP) the , applicant on March 2011 was found to have a 27% permanent disability as a result of the assessment of a WSIB independent medical examiner and was granted a NEL award based upon this assessment but Ms Laidlaw erred in law when she completely disregarded this independent medical finding.
25. It is further respectfully submitted that the Tribunal in a subsequent matter concluded that a period of three years was a prolonged a period of “indefinite duration” and predictability and reliability in the workforce are of significant considerations - quite contrary to the finding against the applicant.
See: J.A. v. Minister of Human Resources and Skills Development ­ Reference GT-11746 February 3, 2014.

[11] The job she held when the medical problems made it impossible for her to keep working was in sales and marketing with the Rainbow Country Travel Association from January, 2009 until her contract ended in March, 2010. She was rehired by CRA (Canada Revenue Agency) at that time on another short term contract on another short term contract, but at the orientation session, she had an attack of muscle spasms, was driven home and could not continue on that contract. It was at this point she realized she could no longer work at any job.

[29] The Respondent submitted that there is insufficient Objective medical evidence to support a finding that the Appellant was disabled within the meaning of the CPP (Canada Pension Plan) by December 31, 2011. The Tribunal notes that there is no requirement in the CPP (Canada Pension Plan) that objective medical evidence must be adduced to support a finding of severe disability In determining this issue, the Tribunal must assess all of the relevant evidence.”
26. It is further respectfully submitted that in the interest of justice the decision of the Board [Jackie Laidlaw and Hazelyn Ross be set aside.
See: Kheiri v. Canada (Minister of Citizenship and Immigration), 2000 Can LII 1533 (FC).
[errors and emphasis in original]

[46] As the AD’s Decision makes clear, the Applicant was somewhat imprecise in his grounds of appeal, but the AD did decide what those grounds of appeal were:
ANALYSIS

[7] In order to grant leave to appeal the Tribunal must be satisfied that the appeal would have a reasonable chance of success. This means that the Tribunal must first find that, were the matter to proceed to a hearing,
(a) at least one of the grounds of the Application relate to a ground of appeal; and
(b) there is a reasonable chance that the appeal would succeed on this ground.
For the reasons set out below the Tribunal is not satisfied that this appeal would have a reasonable chance of success.
The Alleged Errors

[8] As stated earlier, the Tribunal concludes that Counsel for the Applicant was alleging that the General Division decision was based on errors of fact. In Counsel’s submission, the Applicant’s medical and mental conditions prior to the MQP were of such a nature that they brought him within the CPP definition of “severe” disability. Counsel submitted that the medical evidence supported such a finding and that in its decision the General Division failed to give significant weight to that evidence, notably that of Dr. Samuels.

## 9522:10 · paragraphs 55-82

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2e1bf2940fc4996f2dd2e73b0ba95f83d741c9c7cb43a012873ab970478cafb6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9522:10:subtheme:1 · paragraphs 55-56

- Raw key terms: `appeal, applicant, decision, evidence, medical, request, samuels, submissions`
- Display key terms: `medical, request, samuels, submissions`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule Display terms: medical, request, samuels, submissions Rule/authority context: [47] The AD’s Decision under review is a critique of the Applicant’s appeal submissions. Evidence spans paragraphs 55-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4481554` offsets `153-168`; context: [9] The following is the main portion of the submissions of Counsel for the Applicant:
According to the recent decision dated July 17, 2015 the Tribunal determined that the medical evidence on file does not establish that the appellant’s overall medical condition was severe prior to the MQP.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481555` offsets `163-171`; context: Essentially, the AD decided that the appeal was a request to “reweigh the evidence” which is not the AD’s function.
- Evidence: `governing_rule` cue `under` at chunk `4481555` offsets `23-28`; context: [47] The AD’s Decision under review is a critique of the Applicant’s appeal submissions.
- Evidence: `counterargument_limitation` cue `However` at chunk `4481555` offsets `354-361`; context: ” However, the AD appears to overlook the crucial fact that the Applicant’s doctors had indicated he could not work before Dr.

#### 9522:10:subtheme:2 · paragraphs 57-59

- Raw key terms: `medical, applicant, evidence, limitations, reference, report, samuels, treatment`
- Display key terms: `medical, limitations, reference, report, samuels, treatment`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: medical, limitations, reference, report, samuels, treatment Rule/authority context: Samuels’ Report of 2011 states that the Applicant has three diagnoses (chronic back pain, depression, and urine incontinence) and notes, under relevant physical findings and functional limitations, “limited lumbar [uncle Evidence spans paragraphs 57-59. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4481556` offsets `129-134`; context: [48] I think that while the Applicant’s counsel could have been more precise and should not have characterized this as simply an issue of “weight,” the GD did overlook crucial evidence that goes to the heart of the Applicant’s claim (which was that the medical evidence supported a severe disability that prevented him from returning to work) and, in so doing, based its decision on an error of fact made in a perverse and capricious manner and without regard for the materials before it.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481556` offsets `176-184`; context: [48] I think that while the Applicant’s counsel could have been more precise and should not have characterized this as simply an issue of “weight,” the GD did overlook crucial evidence that goes to the heart of the Applicant’s claim (which was that the medical evidence supported a severe disability that prevented him from returning to work) and, in so doing, based its decision on an error of fact made in a perverse and capricious manner and without regard for the materials before it.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481557` offsets `419-427`; context: The Tribunal is bound by the legislation and as such is required to give more weight to evidence up to the date of the MQP.
- Evidence: `counterargument_limitation` cue `however` at chunk `4481557` offsets `280-287`; context: ” The GD also says that, “His opinion in 2015 is that the Appellant is unemployable, however that was not his opinion prior to the MQP.
- Evidence: `governing_rule` cue `under` at chunk `4481558` offsets `146-151`; context: Samuels’ Report of 2011 states that the Applicant has three diagnoses (chronic back pain, depression, and urine incontinence) and notes, under relevant physical findings and functional limitations, “limited lumbar [unclear], difficulty with prolonged sitting/standing/walking.

#### 9522:10:subtheme:3 · paragraphs 60-63

- Raw key terms: `applicant, evidence, gordon, medical, samuels, work, appears, aspects`
- Display key terms: `gordon, medical, samuels, work, appears, aspects`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: gordon, medical, samuels, work, appears, aspects Position/evidence statements: The Applicant argues that all of this medical evidence was before the GD and was overlooked. Application context: Gordon had come to in 2009 and that the Applicant could not return to work because of the pain and mobility problems that affected all aspects of daily living. Evidence spans paragraphs 60-63. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4481559` offsets `440-448`; context: This has to include work and, in my view, must reasonably be taken as a response to the question “What are the limiting factors preventing your patient from returning to work?
- Evidence: `evidence_fact` cue `Evidence` at chunk `4481560` offsets `656-664`; context: Other Evidence
- Evidence: `reasoning_application` cue `because` at chunk `4481560` offsets `562-569`; context: Gordon had come to in 2009 and that the Applicant could not return to work because of the pain and mobility problems that affected all aspects of daily living.
- Evidence: `party_position` cue `argues` at chunk `4481561` offsets `486-492`; context: The Applicant argues that all of this medical evidence was before the GD and was overlooked.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481561` offsets `187-195`; context: This evidence includes reports from Dr.
- Evidence: `evidence_fact` cue `Record` at chunk `4481562` offsets `31-37`; context: [54] However, as the Certified Record shows, much of this evidence was not before the GD and so could not be taken into account by the AD.

#### 9522:10:subtheme:4 · paragraphs 64-67

- Raw key terms: `applicant, certified, record, hearing, application, counsel, court, evidence`
- Display key terms: `certified, hearing`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: certified, hearing Position/evidence statements: The Applicant appears to have submitted medical evidence in this application that was not before either the GD or the AD. Rule/authority context: The Court has before it the Certificate of the Tribunal which says: Pursuant to Rule 318(1) of the Federal Courts Rules, the Social Security Tribunal is forwarding certified copies of the following material as requested  Evidence spans paragraphs 64-67. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4481563` offsets `225-230`; context: [55] At the hearing before me on December 8, 2016, Applicant’s counsel suggested that the Certified Record did not contain all of the evidence that the Applicant had produced before the GD and the AD should have checked this issue.
- Evidence: `evidence_fact` cue `Record` at chunk `4481563` offsets `100-106`; context: [55] At the hearing before me on December 8, 2016, Applicant’s counsel suggested that the Certified Record did not contain all of the evidence that the Applicant had produced before the GD and the AD should have checked this issue.
- Evidence: `issue` cue `whether` at chunk `4481564` offsets `276-283`; context: In addition, the Applicant produced nothing (an affidavit would have helped) that the Court could rely upon to determine whether the Certified Record is incomplete, or in what ways it is incomplete.
- Evidence: `evidence_fact` cue `Record` at chunk `4481564` offsets `79-85`; context: [56] The Applicant had some 14 months to raise any problems with the Certified Record but only did so on the eve of the hearing and at the hearing itself.
- Evidence: `evidence_fact` cue `Record` at chunk `4481565` offsets `105-111`; context: [57] On the other hand, it would have been obvious to Applicant’s counsel when preparing the Applicant’s Record and the Applicant’s Memorandum of Argument if there was anything missing from the Certified Record.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `4481565` offsets `280-291`; context: The Court has before it the Certificate of the Tribunal which says:
Pursuant to Rule 318(1) of the Federal Courts Rules, the Social Security Tribunal is forwarding certified copies of the following material as requested by the Applicant.
- Evidence: `party_position` cue `submitted` at chunk `4481566` offsets `116-125`; context: The Applicant appears to have submitted medical evidence in this application that was not before either the GD or the AD.
- Evidence: `evidence_fact` cue `Record` at chunk `4481566` offsets `62-68`; context: [58] There is nothing before me to suggest that the Certified Record is not complete.

#### 9522:10:subtheme:5 · paragraphs 68-80

- Raw key terms: `medical, applicant, record, reports, certified, application, documents, reconsideration`
- Display key terms: `medical, reports, certified, documents, reconsideration`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: medical, reports, certified, documents, reconsideration Position/evidence statements: [62] The Applicant, without evidence, is simply asking the Court to accept that he submitted additional medical reports to the GD that were excluded from the Certified Record. | The Applicant claims these reports were submitted in his application for a CPP disability benefit on February 6, 2012. Rule/authority context: [64] In particular, the Applicant refers to the medical reports from October 2006 to June 2008 listed in his Application Record under Tab 3 [pre-2009 medical reports]. Evidence spans paragraphs 68-80. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4481567` offsets `679-684`; context: The Applicant has made further submissions on this issue but has failed to show that any such unreferenced reports appear in the Certified Record.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481567` offsets `69-77`; context: [59] A reading of the GD’s decision shows the Member setting out the evidence before her and dealing with it all in some detail.
- Evidence: `issue` cue `issue` at chunk `4481568` offsets `87-92`; context: [60] There is simply no evidence before me to support the Applicant’s position on this issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481568` offsets `24-32`; context: [60] There is simply no evidence before me to support the Applicant’s position on this issue.
- Evidence: `evidence_fact` cue `Record` at chunk `4481569` offsets `157-163`; context: [61] On the other hand, the Respondent’s affiant is clear that all of the materials in the Respondent’s possession were examined in assembling the Certified Record that was before the GD and the AD.
- Evidence: `party_position` cue `submitted` at chunk `4481570` offsets `83-92`; context: [62] The Applicant, without evidence, is simply asking the Court to accept that he submitted additional medical reports to the GD that were excluded from the Certified Record.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481570` offsets `28-36`; context: [62] The Applicant, without evidence, is simply asking the Court to accept that he submitted additional medical reports to the GD that were excluded from the Certified Record.
- Evidence: `evidence_fact` cue `Record` at chunk `4481571` offsets `209-215`; context: Gordon and others were submitted by the Applicant in 2012 but do not appear in the Certified Record.
- Evidence: `party_position` cue `claims` at chunk `4481572` offsets `182-188`; context: The Applicant claims these reports were submitted in his application for a CPP disability benefit on February 6, 2012.
- Evidence: `evidence_fact` cue `Record` at chunk `4481572` offsets `121-127`; context: [64] In particular, the Applicant refers to the medical reports from October 2006 to June 2008 listed in his Application Record under Tab 3 [pre-2009 medical reports].
- Evidence: `governing_rule` cue `under` at chunk `4481572` offsets `128-133`; context: [64] In particular, the Applicant refers to the medical reports from October 2006 to June 2008 listed in his Application Record under Tab 3 [pre-2009 medical reports].
- Evidence: `party_position` cue `claims` at chunk `4481576` offsets `24-30`; context: [68] The Applicant also claims that on August 1, 2012, he provided additional medical records from September 2009 to July 2012.
- Evidence: `evidence_fact` cue `Record` at chunk `4481576` offsets `166-172`; context: These records appear in the Certified Record and are referenced in the Tribunal’s reconsideration decision dated October 12, 2016:
We reviewed all the information and documents in your file, including all the reports you sent with your application and with your letter of August 1, 2012.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481578` offsets `24-32`; context: [70] Based on the above evidence, it appears that the pre-2009 medical reports that are alleged to be omitted from the Certified Record were not submitted by the Applicant either in the original application or in the request for reconsideration.
- Evidence: `party_position` cue `submit` at chunk `4481579` offsets `29-35`; context: [71] While the Applicant did submit additional medical reports on August 1, 2012, these medical reports were considered by the Tribunal and form part of the Certified Record.
- Evidence: `evidence_fact` cue `Record` at chunk `4481579` offsets `167-173`; context: [71] While the Applicant did submit additional medical reports on August 1, 2012, these medical reports were considered by the Tribunal and form part of the Certified Record.

#### 9522:10:subtheme:6 · paragraphs 81-82

- Raw key terms: `attorney, canada, cause, general, style, allowed, amended, appeal`
- Display key terms: `style, allowed, amended`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: style, allowed, amended Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that The application is allowed and the matter is returned for reconsideration by a differently constituted Appeal Division. Evidence spans paragraphs 81-82. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4481580` offsets `48-54`; context: [72] Notwithstanding these disputed evidentiary issues, I think the Applicant has identified a material error with the AD’s Decision in that the AD failed to notice that there were persuasive grounds for appeal on the basis of the medical evidence that was before the GD in that Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4481580` offsets `239-247`; context: [72] Notwithstanding these disputed evidentiary issues, I think the Applicant has identified a material error with the AD’s Decision in that the AD failed to notice that there were persuasive grounds for appeal on the basis of the medical evidence that was before the GD in that Dr.
- Evidence: `disposition` cue `allowed` at chunk `4481580` offsets `566-573`; context: JUDGMENT
THIS COURT’S JUDGMENT is that
The application is allowed and the matter is returned for reconsideration by a differently constituted Appeal Division.

#### Section text

[9] The following is the main portion of the submissions of Counsel for the Applicant:
According to the recent decision dated July 17, 2015 the Tribunal determined that the medical evidence on file does not establish that the appellant’s overall medical condition was severe prior to the MQP. The decision avers that while Mr. Joseph has limitations with his health conditions, he does not have a severe disability that would prevent him from partaking in gainful employment.
Contrary to the Tribunal’s decision, it remains this Firm's contention that Mr. Joseph’s physical medical conditions and psychological impairment are both severe and prolonged in nature prior and render him unemployable in any capacity. The medical evidence on file supports the severity of the appellant’s overall medical condition, which consists of a chronic low back pain and degenerative disc disease, with limited movement in all directions and spasms down to his legs, bladder incontinence and depression, which disables him from partaking in activities of daily living. He also has functional limitations of standing, sitting, walking, lifting, reaching and bending and difficulty with memory and concentration, due to his depressed state of mind and poor sleep caused by his severe pain, which is a significant barrier to him returning to any form of gainful employment since December 2011 and continuously thereafter.
It is respectfully submitted that the medical evidence on file from the appellant’s primary treating practitioners, most notably Dr. Samuels, was not given significant weight when rendering a decision in this claim. At this time we kindly request a Leave to Appeal as we remain confident in our belief that the medical evidence on file confirms our position that Mr. Joseph is totally and permanently disabled and that his overall physical and psychological conditions are both severe and prolonged in nature.” (AD-1 application for leave to appeal)

[47] The AD’s Decision under review is a critique of the Applicant’s appeal submissions. Essentially, the AD decided that the appeal was a request to “reweigh the evidence” which is not the AD’s function. It also points out that Dr. Samuels’ reports and medical conclusions were “specifically addressed at paragraph 39 of the General Division decision.” However, the AD appears to overlook the crucial fact that the Applicant’s doctors had indicated he could not work before Dr. Samuels’ opinion to that effect of 2015.

[48] I think that while the Applicant’s counsel could have been more precise and should not have characterized this as simply an issue of “weight,” the GD did overlook crucial evidence that goes to the heart of the Applicant’s claim (which was that the medical evidence supported a severe disability that prevented him from returning to work) and, in so doing, based its decision on an error of fact made in a perverse and capricious manner and without regard for the materials before it.

[49] In its treatment of Dr. Samuels’ medical report, the GD says, in reference to the 2011 report, that: “There is no mention of his ability to return to work or his limitations preventing work.” The GD also says that, “His opinion in 2015 is that the Appellant is unemployable, however that was not his opinion prior to the MQP. The Tribunal is bound by the legislation and as such is required to give more weight to evidence up to the date of the MQP.”

[50] Dr. Samuels’ Report of 2011 states that the Applicant has three diagnoses (chronic back pain, depression, and urine incontinence) and notes, under relevant physical findings and functional limitations, “limited lumbar [unclear], difficulty with prolonged sitting/standing/walking.” The report also states that the prognosis of the main medical condition is “guarded.” Guarded, in medical terminology, generally means the patient is acutely ill with questionable outlook and is often used by nurses and physicians to indicate that a patient is unlikely to recover from an illness. Dr. Samuels’ report also states, in reference to treatment type and response, “no sig[nificant] improvement.” See KT v AS, 2009 BCSC 1653 at para 141; Maldonado v Mooney, 2016 BCSC 558 at para 60; and Brough v Yipp, 2016 ABQB 559 at para 400.

[51] It is important to note that Dr. Samuels took over the Applicant’s care from Dr. Gordon, whose medical report in 2009 opined that the Applicant’s condition had deteriorated and, read in conjunction with the questions asked, appears to indicate that the Applicant’s condition has deteriorated in a way that affects all aspects of his daily living. This has to include work and, in my view, must reasonably be taken as a response to the question “What are the limiting factors preventing your patient from returning to work?”
Since Aug 18/09 last visit, has the medical condition improved or deteriorated? (1) What are the limiting factors preventing your patient from returning to work? Please elaborate on the functional capabilities. (2) What is preventing your patient from following the treatment plan and working at the same time? (3)
(1) - deteriorated
(2) - pain [uncertain if this is the word, the writing is difficult to read], mobility
(3) - generally affects all aspects of daily living

[52] In conjunction with the other medical history that demonstrates the Applicant’s condition had deteriorated since 2009, such as the MRIs that consistently showed his back to have mild degenerative changes with no progression noted, and Dr. Gordon’s medical opinion, it does not appear to be reasonable to infer that Dr. Samuels’ silence on the matter in 2011 indicated an opinion of employability. He appears to be confirming – “no significant improvement” – the conclusion that Dr. Gordon had come to in 2009 and that the Applicant could not return to work because of the pain and mobility problems that affected all aspects of daily living.
D. Other Evidence

[53] In his written submission, the Applicant refers to various pieces of documentation that he believes support his position that he was severely disabled and was not able to work. This evidence includes reports from Dr. Gordon, the Applicant’s family doctor prior to Dr. Samuels, reports of Dr. Germansky, the Workplace Safety and Insurance Board consultant and the March 21, 2011 decision of the Workplace Safety and Insurance Board, as well as other medical evidence. The Applicant argues that all of this medical evidence was before the GD and was overlooked.

[54] However, as the Certified Record shows, much of this evidence was not before the GD and so could not be taken into account by the AD.

[55] At the hearing before me on December 8, 2016, Applicant’s counsel suggested that the Certified Record did not contain all of the evidence that the Applicant had produced before the GD and the AD should have checked this issue. The Applicant requested an adjournment to give him time to check this matter out.

[56] The Applicant had some 14 months to raise any problems with the Certified Record but only did so on the eve of the hearing and at the hearing itself. In addition, the Applicant produced nothing (an affidavit would have helped) that the Court could rely upon to determine whether the Certified Record is incomplete, or in what ways it is incomplete.

[57] On the other hand, it would have been obvious to Applicant’s counsel when preparing the Applicant’s Record and the Applicant’s Memorandum of Argument if there was anything missing from the Certified Record. The Court has before it the Certificate of the Tribunal which says:
Pursuant to Rule 318(1) of the Federal Courts Rules, the Social Security Tribunal is forwarding certified copies of the following material as requested by the Applicant.
A. Decision of Hazelyn Ross, Member, Appeal Division
B. Application for Leave to Appeal to the Social Security Tribunal – AD1
C. Decision of Jackie Laidlaw, Member, General Division
D. General Division Letter – Appeal Ready to Proceed
E. Notice of Hearing for the General Division – GT0
F. Notice of Hearing – Administrative change of hearing date and type - GTOA
G. Legacy File – GT1
H. Notice of Readiness with Additional Documents – GT2
I. Claimant Submissions – Medical Documents – GT3
J. Respondent Submissions – GT4
K. Claimant Submissions – Medical Documents – GT5
L. Respondent Submissions – Record of Earnings – GT6
[emphasis in original]

[58] There is nothing before me to suggest that the Certified Record is not complete. The Applicant appears to have submitted medical evidence in this application that was not before either the GD or the AD.

[59] A reading of the GD’s decision shows the Member setting out the evidence before her and dealing with it all in some detail. The Applicant is suggesting she overlooked extensive evidence that he has now produced for this application. This is not convincing and there is nothing before me to suggest that the Court does not have the full Tribunal record. Given the Applicant’s assertions that the GD overlooked important medical evidence that supported his position, I requested the Applicant to file, post-hearing, a list of citations to show where any unreferenced medical reports could be located in the Certified Record. The Applicant has made further submissions on this issue but has failed to show that any such unreferenced reports appear in the Certified Record. Consequently, the Applicant now alleges that the reports were before the GD but were not included in the Certified Record.

[60] There is simply no evidence before me to support the Applicant’s position on this issue. The Applicant has not provided affidavit evidence on point or explained why his counsel did not, or could not, challenge the Certified Record when preparing his Memorandum of Fact and Law in July 2016, at the latest.

[61] On the other hand, the Respondent’s affiant is clear that all of the materials in the Respondent’s possession were examined in assembling the Certified Record that was before the GD and the AD. The Respondent’s affiant has also sworn an unchallenged affidavit saying that Exhibits A and B of the Applicant’s affidavit were not part of the Certified Record.

[62] The Applicant, without evidence, is simply asking the Court to accept that he submitted additional medical reports to the GD that were excluded from the Certified Record.

[63] Counsel for the Applicant now says in his post-hearing letter of December 19, 2016 that medical reports of Dr. Gordon and others were submitted by the Applicant in 2012 but do not appear in the Certified Record. But, as Respondent’s counsel points out, when the Applicant sought reconsideration on August 1, 2012, he referred to four reports that he said demonstrated that his medical condition worsened from September 2009 until July 2012. However, all of these reports can be found in the Certified Record.

[64] In particular, the Applicant refers to the medical reports from October 2006 to June 2008 listed in his Application Record under Tab 3 [pre-2009 medical reports]. The Applicant claims these reports were submitted in his application for a CPP disability benefit on February 6, 2012.

[65] The initial denial of the application, dated June 21, 2012, noted several documents that were reviewed, which ranged from November 2010 to February 2012.

[66] The Initial Adjudication Summary [IAS] refers to the information provided with the application as:
• (ISP 1151) Application dated Feb 6/12 Signed by Client
• (ISP 2507) Questionnaire dated Feb 6/12 Signed by Client
• (ISP 2502) Authorization to Disclose Information (yes) dated Feb 3/12 Signed by Client
• (ISP 2519) Medical Report dated Feb 25/12 Signed by Dr O Samuel Last visit Aug 21/11
• Enclosed Documents: As noted below
[emphasis in original]

[67] The IAS also notes the enclosed documents in the Medical Reports section, which include medical reports ranging from November 2010 to March 2011.

[68] The Applicant also claims that on August 1, 2012, he provided additional medical records from September 2009 to July 2012. These records appear in the Certified Record and are referenced in the Tribunal’s reconsideration decision dated October 12, 2016:
We reviewed all the information and documents in your file, including all the reports you sent with your application and with your letter of August 1, 2012. In addition to the reports listed in our letter of June 21, 2012, here are the new reports we have on file:
• Your urologist’s report dated June 2010
• Your orthopaedic surgeon’s report dated November 2010 and previously on file
• X-rays dated October 2009
[emphasis added]

[69] The Reconsideration Adjudication Summary [RAS] also refers to the enclosures in the request for reconsideration: “Enclosures: Specialists’ and test reports dated September 2009 to November 2010”. The Medical Reports section of the RAS refers to documents dated September 2009 to August 2011.

[70] Based on the above evidence, it appears that the pre-2009 medical reports that are alleged to be omitted from the Certified Record were not submitted by the Applicant either in the original application or in the request for reconsideration. There is no reference, in the initial denial or reconsideration, of any medical reports that are pre-2009.

[71] While the Applicant did submit additional medical reports on August 1, 2012, these medical reports were considered by the Tribunal and form part of the Certified Record. It is possible that the Applicant mistakenly believes he submitted the pre-2009 medical reports in the reconsideration request, but the reconsideration decision confirms all the additional information received and the pre-2009 medical reports are not included.
E. Conclusions

[72] Notwithstanding these disputed evidentiary issues, I think the Applicant has identified a material error with the AD’s Decision in that the AD failed to notice that there were persuasive grounds for appeal on the basis of the medical evidence that was before the GD in that Dr. Samuels’ opinion in 2015 that the Applicant could not work, which opinion confirmed earlier medical evidence that, as of the MQP, the Applicant had a severe and prolonged disability that prevented him from returning to work.
JUDGMENT
THIS COURT’S JUDGMENT is that
The application is allowed and the matter is returned for reconsideration by a differently constituted Appeal Division.
The style of cause is amended to reflect the Attorney General of Canada as the sole Respondent.
“James Russell”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-1674-15
STYLE OF CAUSE:
PETER JOSEPH v ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
TORONTO, Ontario
DATE OF HEARING:
December 8, 2016


## 9522:11 · paragraphs 83-83

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e2199362cf999006fea0994df06eb962a97cc8b404b31e4e9df09af4e519c986`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9522:11:subtheme:1 · paragraphs 83-83

- Raw key terms: `appearances, applicant, april, attorney, brampton, canada, chhina, dated`
- Display key terms: `april, brampton, chhina, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, brampton, chhina, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 83-83. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
RUSSELL J.
DATED:
APRIL 21, 2017
APPEARANCES:
Yuvraj Chhina
For The Applicant
Michael Stevenson
For The Respondent
SOLICITORS OF RECORD:
Fortis Law Practise
Brampton, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
