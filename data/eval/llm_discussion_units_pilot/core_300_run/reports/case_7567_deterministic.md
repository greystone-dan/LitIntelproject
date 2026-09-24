# Discussion Units: case 7567

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **94**
- Continuity pairs: **93**
- Discussion Units: **2**
- Paragraph source hashes: **94**
- Sub-themes: **22**

## 7567:1 · paragraphs 0-85

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6866e1ee95132a97cf8e36564cbfedd3caa0424b9dd634efb16f217ecbb82f41`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7567:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `allergan, canada, counterclaim, defendant, order, patent, plaintiff, reasons`
- Display key terms: `allergan, counterclaim, order, patent`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: allergan, counterclaim, order, patent No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.

#### 7567:1:subtheme:2 · paragraphs 2-6

- Raw key terms: `allergan, sandoz, action, costs, disbursements, incurred, kissei, patent`
- Display key terms: `allergan, sandoz, action, costs, disbursements, incurred, kissei, patent`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue Display terms: allergan, sandoz, action, costs, disbursements, incurred, kissei, patent Rule/authority context: Allergan then commenced an infringement action against Sandoz pursuant to subsection 6(1) of the Regulations. Operative outcome context: In response, Sandoz filed a Statement of Defence and Counterclaim in which it denied that its product would infringe the ‘002 Patent and claimed that the patent is invalid on the grounds of obviousness, overbreadth and i Evidence spans paragraphs 2-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4401716` offsets `287-293`; context: The legal fees component of this award ($272,000) represents approximately 45% of the fees incurred by Sandoz in connection with the issues in this proceeding, as ultimately narrowed.
- Evidence: `counterargument_limitation` cue `However` at chunk `4401717` offsets `104-111`; context: However, it filed a brief defense to Sandoz’s Counterclaim and incurred certain additional costs, primarily in relation to the discovery process.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4401719` offsets `385-396`; context: Allergan then commenced an infringement action against Sandoz pursuant to subsection 6(1) of the Regulations.
- Evidence: `counterargument_limitation` cue `However` at chunk `4401719` offsets `729-736`; context: However, it ultimately narrowed its Counterclaim to a single allegation of invalidity based on obviousness.
- Evidence: `disposition` cue `denied` at chunk `4401719` offsets `573-579`; context: In response, Sandoz filed a Statement of Defence and Counterclaim in which it denied that its product would infringe the ‘002 Patent and claimed that the patent is invalid on the grounds of obviousness, overbreadth and insufficiency.

#### 7567:1:subtheme:3 · paragraphs 7-8

- Raw key terms: `allergan, counterclaim, first, issue, issues, kissei, sandoz, second`
- Display key terms: `allergan, counterclaim, first, issues, kissei, sandoz, second`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: allergan, counterclaim, first, issues, kissei, sandoz, second Rule/authority context: ) The second was whether representations that were made during the patent application process on behalf of Kissei could be introduced as evidence in this proceeding, pursuant to section 53. | In this regard, I encouraged them to attempt to reach a settlement on this issue, failing which to identify a lump sum amount that reflected certain identified factors as well as any additional relevant factors, includin Operative outcome context: After becoming aware that Kissei had incurred material cost beyond simply filing a brief defence to Sandoz’s Counterclaim, I also granted Kissei leave to make submissions on costs. Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4401721` offsets `210-216`; context: There were three principal issues addressed.
- Evidence: `evidence_fact` cue `evidence` at chunk `4401721` offsets `491-499`; context: ) The second was whether representations that were made during the patent application process on behalf of Kissei could be introduced as evidence in this proceeding, pursuant to section 53.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4401721` offsets `520-531`; context: ) The second was whether representations that were made during the patent application process on behalf of Kissei could be introduced as evidence in this proceeding, pursuant to section 53.
- Evidence: `issue` cue `issue` at chunk `4401722` offsets `57-62`; context: [8] Ultimately, I found in favour of Sandoz on the first issue and in favour of Allergan on the second and third issues.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4401722` offsets `465-478`; context: In this regard, I encouraged them to attempt to reach a settlement on this issue, failing which to identify a lump sum amount that reflected certain identified factors as well as any additional relevant factors, including those identified in Rule 400 of the Rules and the jurisprudence.
- Evidence: `disposition` cue `granted` at chunk `4401722` offsets `610-617`; context: After becoming aware that Kissei had incurred material cost beyond simply filing a brief defence to Sandoz’s Counterclaim, I also granted Kissei leave to make submissions on costs.

#### 7567:1:subtheme:4 · paragraphs 9-11

- Raw key terms: `award, disbursements, plus, requests, sandoz, total, allergan, alternative`
- Display key terms: `award, disbursements, plus, requests, sandoz, total, allergan, alternative`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: award, disbursements, plus, requests, sandoz, total, allergan, alternative Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4401723` offsets `249-255`; context: [9] Sandoz submits that in light of the fact that it prevailed in the infringement action initiated by Allergan, it is entitled to its costs, without any offset to reflect the fact that it was unsuccessful with respect to two of the three principal issues in the proceeding.

#### 7567:1:subtheme:5 · paragraphs 12-13

- Raw key terms: `allergan, costs, counterclaim, relation, sandoz, above, against, awarded`
- Display key terms: `allergan, costs, counterclaim, relation, sandoz, above, against, awarded`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: allergan, costs, counterclaim, relation, sandoz, above, against, awarded Evidence spans paragraphs 12-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4401726` offsets `317-322`; context: It maintains that such a set off is also warranted by the fact that it prevailed in relation to the issue Sandoz raised with respect to the prosecution history of the ’002 Patent.
- Evidence: `counterargument_limitation` cue `However` at chunk `4401726` offsets `124-131`; context: However, it seeks only to use that success as a set off against any costs payable to Sandoz.

#### 7567:1:subtheme:6 · paragraphs 14-17

- Raw key terms: `allergan, sandoz, invalidity, maintains, respect, appropriate, award, because`
- Display key terms: `allergan, sandoz, invalidity, maintains, respect, appropriate, award, because`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: allergan, sandoz, invalidity, maintains, respect, appropriate, award, because Rule/authority context: [17] Kissei was required to be added to Allergan’s action pursuant to subsection 6(2) of the Regulations. Application context: [15] More specifically, Allergan maintains that a lump sum award to Sandoz based on a percentage of actual legal fees would not be appropriate, essentially because Allergan prevailed with respect to two of the three main | Felton’s fees should be fully assessable, essentially because the bulk of her time was spent addressing Sandoz’s invalidity claims. Operative outcome context: [14] In the alternative, Allergan submits that any cost award granted to Sandoz should be discounted by two-thirds of what Sandoz has claimed, to reflect that Allergan prevailed in respect of two of the three principal i Evidence spans paragraphs 14-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4401728` offsets `219-225`; context: [14] In the alternative, Allergan submits that any cost award granted to Sandoz should be discounted by two-thirds of what Sandoz has claimed, to reflect that Allergan prevailed in respect of two of the three principal issues in dispute.
- Evidence: `disposition` cue `granted` at chunk `4401728` offsets `62-69`; context: [14] In the alternative, Allergan submits that any cost award granted to Sandoz should be discounted by two-thirds of what Sandoz has claimed, to reflect that Allergan prevailed in respect of two of the three principal issues in dispute.
- Evidence: `issue` cue `issues` at chunk `4401729` offsets `221-227`; context: [15] More specifically, Allergan maintains that a lump sum award to Sandoz based on a percentage of actual legal fees would not be appropriate, essentially because Allergan prevailed with respect to two of the three main issues in dispute between the parties.
- Evidence: `reasoning_application` cue `because` at chunk `4401729` offsets `156-163`; context: [15] More specifically, Allergan maintains that a lump sum award to Sandoz based on a percentage of actual legal fees would not be appropriate, essentially because Allergan prevailed with respect to two of the three main issues in dispute between the parties.
- Evidence: `evidence_fact` cue `evidence` at chunk `4401730` offsets `278-286`; context: Wilson’s fees should be assessed at 50%, because the Court found her evidence regarding the legislative history of section 53.
- Evidence: `reasoning_application` cue `because` at chunk `4401730` offsets `108-115`; context: Felton’s fees should be fully assessable, essentially because the bulk of her time was spent addressing Sandoz’s invalidity claims.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4401731` offsets `58-69`; context: [17] Kissei was required to be added to Allergan’s action pursuant to subsection 6(2) of the Regulations.
- Evidence: `counterargument_limitation` cue `However` at chunk `4401731` offsets `106-113`; context: However, it took no position in that action and did not participate in the trial.

#### 7567:1:subtheme:7 · paragraphs 18-23

- Raw key terms: `above, award, canada, costs, para, band, indian, justice`
- Display key terms: `above, award, costs, para, band, indian, justice`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: above, award, costs, para, band, indian, justice Rule/authority context: General Principles | However, that discretion must be exercised in accordance with established principles pertaining to costs, unless the circumstances justify a different approach: Okanagan Indian Band, above, at para 22; Nova Chemicals Cor Application context: [18] In the alternative, if it does not succeed in obtaining a cost award, Kissei maintains that no costs should be assessed against it, either in the main action or the Counterclaim, because it was successful on the iss Evidence spans paragraphs 18-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4401732` offsets `217-223`; context: [18] In the alternative, if it does not succeed in obtaining a cost award, Kissei maintains that no costs should be assessed against it, either in the main action or the Counterclaim, because it was successful on the issues in which it engaged.
- Evidence: `governing_rule` cue `Principles` at chunk `4401732` offsets `272-282`; context: General Principles
- Evidence: `reasoning_application` cue `because` at chunk `4401732` offsets `184-191`; context: [18] In the alternative, if it does not succeed in obtaining a cost award, Kissei maintains that no costs should be assessed against it, either in the main action or the Counterclaim, because it was successful on the issues in which it engaged.
- Evidence: `governing_rule` cue `principles` at chunk `4401735` offsets `369-379`; context: However, that discretion must be exercised in accordance with established principles pertaining to costs, unless the circumstances justify a different approach: Okanagan Indian Band, above, at para 22; Nova Chemicals Corporation v Dow Chemical Company, 2017 FCA 25 at para 19 [Nova v Dow].
- Evidence: `counterargument_limitation` cue `However` at chunk `4401735` offsets `295-302`; context: However, that discretion must be exercised in accordance with established principles pertaining to costs, unless the circumstances justify a different approach: Okanagan Indian Band, above, at para 22; Nova Chemicals Corporation v Dow Chemical Company, 2017 FCA 25 at para 19 [Nova v Dow].
- Evidence: `governing_rule` cue `under` at chunk `4401736` offsets `534-539`; context: This trend is in part attributable to the Court’s desire to reduce the significant time and effort typically associated with preparing and reviewing the type of detailed bill of costs that is required for the purposes of an assessment under Tariff B: Consorzio del Prosciutto di Parma v Maple Leaf Meats Inc, 2002 FCA 417 at para 12 [Consorzio]; Venngo Inc v Concierge Connection Inc, 2017 FCA 96 at paras 85-86 [Venngo], leave to appeal ref’d [2017] SCCA No 302.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4401736` offsets `1185-1197`; context: Nevertheless, a lump sum award of costs may not be appropriate in all cases: Consorzio, above.

#### 7567:1:subtheme:8 · paragraphs 24-30

- Raw key terms: `above, costs, court, tariff, award, canada, cases, para`
- Display key terms: `above, costs, tariff, award, cases, para`
- Argument roles: `counterargument_limitation, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue Display terms: above, costs, tariff, award, cases, para Rule/authority context: [28] In recognition of the fact that Tariff B no longer provides an adequate level of partial indemnification, the Federal Courts Rules Committee decided in 2016 that the amount recoverable under Tariff B should be incre Evidence spans paragraphs 24-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4401738` offsets `19-26`; context: [24] Regardless of whether parties favour a lump sum award or an amount fixed in accordance with Tariff B, counsel are encouraged to be prepared to address costs, ideally on consent, at the conclusion of the proceeding or shortly thereafter: Consorzio, above.
- Evidence: `governing_rule` cue `under` at chunk `4401742` offsets `190-195`; context: [28] In recognition of the fact that Tariff B no longer provides an adequate level of partial indemnification, the Federal Courts Rules Committee decided in 2016 that the amount recoverable under Tariff B should be increased by approximately 25%: Minutes of the October 28, 2016 Meeting of the Rules Committee.
- Evidence: `counterargument_limitation` cue `However` at chunk `4401744` offsets `288-295`; context: However, the Court may depart from this approach in cases of truly “divided success” or “mixed results”: Eurocopter v Bell Helicopter Textron Canada Ltée, 2012 FC 842 at paras 23 and 56 [Eurocopter FC] aff’d 2013 FCA 220 at paras 10 and 15; Sanofi, above, at paras 8-9; Apotex v Sanofi-Aventis, above, at para 11; Bristol-Myers Squibb Canada Co v Teva Canada Limited, 2016 FC 991 at paras 9-14.

#### 7567:1:subtheme:9 · paragraphs 31-36

- Raw key terms: `award, para, range, above, case, court, lump, mid-point`
- Display key terms: `award, para, range, above, case, lump, mid-point`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: award, para, range, above, case, lump, mid-point Rule/authority context: [31] The jurisprudence is split on the issue of whether the successful defence of a patent infringement action, or success with respect to only some grounds of invalidity, constitutes “divided success” when the defendant | [34] In my view, there are very good reasons for beginning with the mid-point of the 25%-50% range in complex drug patent proceedings under the Regulations. Application context: In a second line of cases, it has been explicitly held that this type of outcome does not constitute “divided success” or “mixed results” and that therefore the defendant is entitled to its costs: Raydan, above; Illinois | However, in Seedlings, this was because neither party had demonstrated that a greater or lesser award was justified (Seedlings, above, at para 24), and in Bauer the Court adopted the 25% starting threshold “[i]n the inte Evidence spans paragraphs 31-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4401745` offsets `39-44`; context: [31] The jurisprudence is split on the issue of whether the successful defence of a patent infringement action, or success with respect to only some grounds of invalidity, constitutes “divided success” when the defendant in the main action is not successful with respect to one or more other allegations of invalidity.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4401745` offsets `9-22`; context: [31] The jurisprudence is split on the issue of whether the successful defence of a patent infringement action, or success with respect to only some grounds of invalidity, constitutes “divided success” when the defendant in the main action is not successful with respect to one or more other allegations of invalidity.
- Evidence: `reasoning_application` cue `therefore` at chunk `4401745` offsets `828-837`; context: In a second line of cases, it has been explicitly held that this type of outcome does not constitute “divided success” or “mixed results” and that therefore the defendant is entitled to its costs: Raydan, above; Illinois Tool Works Inc v Cobra Anchors Co, 2003 FCA 358 at paras 10-11; Betser-Zilevitch v Petrochina Canada Ltd, 2021 FC 151 at para 11 [Betser-Zilevitch 2]; Johnson & Johnson Inc v Boston Scientific Ltd, 2008 FC 817 at para 4.
- Evidence: `counterargument_limitation` cue `Notwithstanding` at chunk `4401745` offsets `1334-1349`; context: Notwithstanding my sympathy for the approach taken in the first line of cases, I consider myself bound by this second line of cases.
- Evidence: `reasoning_application` cue `because` at chunk `4401747` offsets `282-289`; context: However, in Seedlings, this was because neither party had demonstrated that a greater or lesser award was justified (Seedlings, above, at para 24), and in Bauer the Court adopted the 25% starting threshold “[i]n the interests of consistency and predictability”: Bauer, above, at para 14.
- Evidence: `counterargument_limitation` cue `However` at chunk `4401747` offsets `250-257`; context: However, in Seedlings, this was because neither party had demonstrated that a greater or lesser award was justified (Seedlings, above, at para 24), and in Bauer the Court adopted the 25% starting threshold “[i]n the interests of consistency and predictability”: Bauer, above, at para 14.
- Evidence: `governing_rule` cue `under` at chunk `4401748` offsets `134-139`; context: [34] In my view, there are very good reasons for beginning with the mid-point of the 25%-50% range in complex drug patent proceedings under the Regulations.
- Evidence: `governing_rule` cue `principles` at chunk `4401750` offsets `42-52`; context: [36] In addition to the foregoing general principles applicable to legal fees, disbursements are typically assessed in full, provided they are reasonable: MediaTube Corp v Bell Canada, 2017 FC 495, at para 21.

#### 7567:1:subtheme:10 · paragraphs 37-38

- Raw key terms: `appropriate, award, case, costs, lump, parties, proceeding, tariff`
- Display key terms: `appropriate, award, case, costs, lump, proceeding, tariff`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: appropriate, award, case, costs, lump, proceeding, tariff Rule/authority context: (1) Lump sum versus assessment pursuant to Tariff B Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4401751` offsets `198-203`; context: [37] I have considered all of the circumstances of this proceeding, including the various submissions made by each of the parties with respect to costs, in determining the appropriate cost award to issue in this case.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4401751` offsets `337-348`; context: (1) Lump sum versus assessment pursuant to Tariff B

#### 7567:1:subtheme:11 · paragraphs 39-40

- Raw key terms: `proceeding, respect, sandoz, above, action, allegation, allergan, appropriate`
- Display key terms: `proceeding, respect, sandoz, above, action, allegation, allergan, appropriate`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: proceeding, respect, sandoz, above, action, allegation, allergan, appropriate Evidence spans paragraphs 39-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4401753` offsets `433-438`; context: Coincidentally, this is also the approximate proportion (36%) of the overall legal fees claimed by Sandoz (before HST) that relate to the claim construction issue, in respect of which it prevailed.
- Evidence: `issue` cue `issues` at chunk `4401754` offsets `185-191`; context: However, it was unsuccessful with respect to the other two principal issues in dispute, namely, its Counterclaim based on obviousness and the relevance of the prosecution history of the ‘002 Patent.
- Evidence: `counterargument_limitation` cue `However` at chunk `4401754` offsets `116-123`; context: However, it was unsuccessful with respect to the other two principal issues in dispute, namely, its Counterclaim based on obviousness and the relevance of the prosecution history of the ‘002 Patent.

#### 7567:1:subtheme:12 · paragraphs 41-42

- Raw key terms: `allergan, costs, entitled, issue, para, sandoz, above, achieved`
- Display key terms: `allergan, costs, entitled, para, sandoz, above, achieved`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: allergan, costs, entitled, para, sandoz, above, achieved Rule/authority context: [41] I am sympathetic to Allergan’s position that it should be entitled to a set-off for its costs incurred in (i) successfully defending Sandoz’s Counterclaim, which was a distinct action under subsection 60(1) of the A Evidence spans paragraphs 41-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4401755` offsets `331-336`; context: [41] I am sympathetic to Allergan’s position that it should be entitled to a set-off for its costs incurred in (i) successfully defending Sandoz’s Counterclaim, which was a distinct action under subsection 60(1) of the Act (Farmobile, LLC v Farmers Edge Inc, 2018 FC 1269 at para 46), and (ii) dealing with the prosecution history issue.
- Evidence: `governing_rule` cue `under` at chunk `4401755` offsets `189-194`; context: [41] I am sympathetic to Allergan’s position that it should be entitled to a set-off for its costs incurred in (i) successfully defending Sandoz’s Counterclaim, which was a distinct action under subsection 60(1) of the Act (Farmobile, LLC v Farmers Edge Inc, 2018 FC 1269 at para 46), and (ii) dealing with the prosecution history issue.
- Evidence: `issue` cue `issues` at chunk `4401756` offsets `102-108`; context: [42] In my view, there should be consequences for having advanced and then failed to succeed on these issues.

#### 7567:1:subtheme:13 · paragraphs 43-45

- Raw key terms: `above, award, costs, discussion, issues, patent, sandoz, accordingly`
- Display key terms: `above, award, costs, discussion, issues, patent, sandoz, accordingly`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: above, award, costs, discussion, issues, patent, sandoz, accordingly Rule/authority context: [43] However, the controlling jurisprudence does not permit me to grant Allergan its costs in relation to the two issues on which it prevailed, or to reduce Sandoz’s award to reflect Allergan’s success on those issues: s Application context: Accordingly, it can legitimately be viewed as having been a successful party. Evidence spans paragraphs 43-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4401757` offsets `114-120`; context: [43] However, the controlling jurisprudence does not permit me to grant Allergan its costs in relation to the two issues on which it prevailed, or to reduce Sandoz’s award to reflect Allergan’s success on those issues: see discussion at paragraph 31 above.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4401757` offsets `30-43`; context: [43] However, the controlling jurisprudence does not permit me to grant Allergan its costs in relation to the two issues on which it prevailed, or to reduce Sandoz’s award to reflect Allergan’s success on those issues: see discussion at paragraph 31 above.
- Evidence: `issue` cue `issue` at chunk `4401758` offsets `256-261`; context: It did not take a position with respect to the patent infringement issue.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4401758` offsets `514-525`; context: Accordingly, it can legitimately be viewed as having been a successful party.

#### 7567:1:subtheme:14 · paragraphs 46-51

- Raw key terms: `offer, offers, rule, sandoz, allergan, judgment, trial, accepted`
- Display key terms: `offer, offers, rule, sandoz, allergan, trial, accepted`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: offer, offers, rule, sandoz, allergan, trial, accepted Rule/authority context: The jurisprudence has added that “the offer must be clear and unequivocal, must contain an element of compromise … and must bring the litigation to an end”: Venngo, above, at para 87. | [50] The essence of the first of the offers [Offer #1] was that Sandoz would not seek damages under section 8 of the Regulations in exchange for a discontinuance of the main action on a without cost basis and a payment t Application context: [51] Allergan maintains that Offer #1 does not trigger Rule 420 because there has been no determination of liability under section 8 of the Regulations. Evidence spans paragraphs 46-51. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4401760` offsets `359-365`; context: As this Court has observed, “[p]atent litigation is typically complex, and obviousness is typically among the most complex legal issues that are raised in patent litigation”: Teva Canada Limited v Janssen Inc, 2018 FC 1175 at para 14.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4401762` offsets `428-441`; context: The jurisprudence has added that “the offer must be clear and unequivocal, must contain an element of compromise … and must bring the litigation to an end”: Venngo, above, at para 87.
- Evidence: `governing_rule` cue `under` at chunk `4401764` offsets `94-99`; context: [50] The essence of the first of the offers [Offer #1] was that Sandoz would not seek damages under section 8 of the Regulations in exchange for a discontinuance of the main action on a without cost basis and a payment that increased over time from $3,000,000 (if it was accepted before or on September 1, 2020) to $12,000,000 (if it was accepted on or after January 15, 2021).
- Evidence: `governing_rule` cue `under` at chunk `4401765` offsets `117-122`; context: [51] Allergan maintains that Offer #1 does not trigger Rule 420 because there has been no determination of liability under section 8 of the Regulations.
- Evidence: `reasoning_application` cue `because` at chunk `4401765` offsets `64-71`; context: [51] Allergan maintains that Offer #1 does not trigger Rule 420 because there has been no determination of liability under section 8 of the Regulations.

#### 7567:1:subtheme:15 · paragraphs 52-56

- Raw key terms: `allergan, offer, sandoz, compromise, constituted, demand, proceeding, rather`
- Display key terms: `allergan, offer, sandoz, compromise, constituted, demand, proceeding, rather`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: allergan, offer, sandoz, compromise, constituted, demand, proceeding, rather Rule/authority context: In the absence of any evidence regarding the extent of Sandoz’s potential claims under section 8, let alone a judgment on those claims, it cannot be said that Allergan obtained a judgment less favourable than Offer #1. Application context: Offer #2 therefore met the requirements of Rule 420(2)(a), and I see no reason why Sandoz should not be entitled to its costs calculated at double the applicable rate, from the date of the offer to the date of the judgme Evidence spans paragraphs 52-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4401766` offsets `278-285`; context: In addition, it is not possible to ascertain whether Offer #1 met the element of compromise.
- Evidence: `evidence_fact` cue `evidence` at chunk `4401766` offsets `36-44`; context: In the absence of any evidence regarding the extent of Sandoz’s potential claims under section 8, let alone a judgment on those claims, it cannot be said that Allergan obtained a judgment less favourable than Offer #1.
- Evidence: `governing_rule` cue `under` at chunk `4401766` offsets `95-100`; context: In the absence of any evidence regarding the extent of Sandoz’s potential claims under section 8, let alone a judgment on those claims, it cannot be said that Allergan obtained a judgment less favourable than Offer #1.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4401766` offsets `153-159`; context: In the absence of any evidence regarding the extent of Sandoz’s potential claims under section 8, let alone a judgment on those claims, it cannot be said that Allergan obtained a judgment less favourable than Offer #1.
- Evidence: `evidence_fact` cue `evidence` at chunk `4401770` offsets `48-56`; context: [56] Unfortunately, Allergan did not adduce any evidence in that regard or to otherwise support its position.
- Evidence: `reasoning_application` cue `therefore` at chunk `4401770` offsets `641-650`; context: Offer #2 therefore met the requirements of Rule 420(2)(a), and I see no reason why Sandoz should not be entitled to its costs calculated at double the applicable rate, from the date of the offer to the date of the judgment on the merits.

#### 7567:1:subtheme:16 · paragraphs 57-58

- Raw key terms: `amount, award, case, court, discretion, including, lump, made`
- Display key terms: `amount, award, case, discretion, including, lump, made`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: amount, award, case, discretion, including, lump, made Rule/authority context: Such costs can either be the costs to which it would be entitled under the high end of Column IV of Tariff B, or such other costs as the Court may in its discretion allow: Canada (Attorney General) v Chrétien, 2011 FCA 5 Application context: Accordingly, I would have increased the cost award in favour of Sandoz to reflect Offer#2, even if I had concluded that the offer did not meet the requirements of Rule 420. Evidence spans paragraphs 57-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4401771` offsets `159-164`; context: Such costs can either be the costs to which it would be entitled under the high end of Column IV of Tariff B, or such other costs as the Court may in its discretion allow: Canada (Attorney General) v Chrétien, 2011 FCA 53 at para 3.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4401772` offsets `423-434`; context: Accordingly, I would have increased the cost award in favour of Sandoz to reflect Offer#2, even if I had concluded that the offer did not meet the requirements of Rule 420.

#### 7567:1:subtheme:17 · paragraphs 59-61

- Raw key terms: `actions, consideration, costs, given, proceeding, abandoning, action, agreed`
- Display key terms: `actions, consideration, costs, given, proceeding, abandoning, action, agreed`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: actions, consideration, costs, given, proceeding, abandoning, action, agreed Evidence spans paragraphs 59-61. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4401773` offsets `276-282`; context: [59] Sandoz submits that it should be given credit for having: (i) cooperated with Allergan in settling all of the motions in this proceeding; (ii) agreed to the discontinuance of the action relating to the ‘780 Patent on a without costs basis; and (iii) agreed to narrow the issues for trial, including by abandoning its invalidity claims based on overbreadth and insufficiency.

#### 7567:1:subtheme:18 · paragraphs 62-64

- Raw key terms: `costs, fees, incurred, patent, respect, sandoz, abandoned, allergan`
- Display key terms: `costs, fees, incurred, patent, respect, sandoz, abandoned, allergan`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: costs, fees, incurred, patent, respect, sandoz, abandoned, allergan Application context: Accordingly, I will give this factor a neutral weighting in my assessment. Evidence spans paragraphs 62-64. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4401776` offsets `443-448`; context: I have also considered that the issue of overbreadth was effectively abandoned by Sandoz in December 2019, when Sandoz served the first report of Dr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4401776` offsets `830-838`; context: As a consequence, Allergan filed no evidence regarding the issue of overbreadth, and its evidence on the issue of insufficiency was limited to four paragraphs in Dr.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4401776` offsets `57-68`; context: Accordingly, I will give this factor a neutral weighting in my assessment.
- Evidence: `issue` cue `issues` at chunk `4401777` offsets `133-139`; context: [63] I will pause to observe that had Allergan incurred substantially greater costs in relation to the overbreadth and insufficiency issues, I may very well have made a significant downward adjustment in the lump sum amount awarded to Sandoz.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4401778` offsets `837-846`; context: For greater certainty, I have reviewed the detailed statement of those fees that is provided in Appendix A to the Second Wysokinski Affidavit, and I consider them all to be reasonable, notwithstanding the significant number of lawyers and clerks whose fees are being claimed by Sandoz.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `4401778` offsets `890-905`; context: For greater certainty, I have reviewed the detailed statement of those fees that is provided in Appendix A to the Second Wysokinski Affidavit, and I consider them all to be reasonable, notwithstanding the significant number of lawyers and clerks whose fees are being claimed by Sandoz.

#### 7567:1:subtheme:19 · paragraphs 65-70

- Raw key terms: `sandoz, disbursements, award, favour, fees, given, make, reasons`
- Display key terms: `sandoz, disbursements, award, favour, fees, given, make`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: sandoz, disbursements, award, favour, fees, given, make Application context: Accordingly, the fees component of the lump sum amount that will be awarded to Sandoz will be $225,000 + $47,000 = $272,000. | Accordingly, I do not consider it appropriate to make an award in favour of Sandoz in respect of Dr. Evidence spans paragraphs 65-70. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4401779` offsets `199-205`; context: [65] For the reasons I have explained, I will not make any downward adjustment or set off in favour of Allergan to reflect the fact that Allergan prevailed with respect to two of the three principal issues in this case.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4401780` offsets `174-185`; context: Accordingly, the fees component of the lump sum amount that will be awarded to Sandoz will be $225,000 + $47,000 = $272,000.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4401782` offsets `201-210`; context: In reaching this figure, Sandoz made various adjustments described in the Wysokinski Affidavit, in an effort to remove disbursements incurred in relation to the ‘780 Patent.
- Evidence: `evidence_fact` cue `evidence` at chunk `4401784` offsets `110-118`; context: Stewart’s evidence did not have any bearing on my decision on the merits.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4401784` offsets `174-185`; context: Accordingly, I do not consider it appropriate to make an award in favour of Sandoz in respect of Dr.

#### 7567:1:subtheme:20 · paragraphs 71-85

- Raw key terms: `kissei, sandoz, costs, total, accommodation, consider, disbursements, kirisawa`
- Display key terms: `kissei, sandoz, costs, total, accommodation, consider, disbursements, kirisawa`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: kissei, sandoz, costs, total, accommodation, consider, disbursements, kirisawa Rule/authority context: Allergan was required to add Kissei to the proceeding, pursuant to s. Application context: [72] Accordingly, I consider it appropriate to reduce the total disbursements of $124,605. | [73] Therefore, the total disbursements that will be awarded to Sandoz will be $77,145. Operative outcome context: This is because I granted Leave to Kissei to make submissions on costs after I became aware that it had incurred material costs in connection with this proceeding. | Sandoz submits that if any of Kissei’s accommodation claims are allowed, they should be limited to a maximum of four days for each of Messrs. Evidence spans paragraphs 71-85. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4401785` offsets `175-180`; context: Fassihi, Allergan submits that his fees should be discounted by 85%, to reflect the fact that the majority of his evidence was directed to the obviousness issue and that evidence was not accepted by the Court.
- Evidence: `evidence_fact` cue `evidence` at chunk `4401785` offsets `134-142`; context: Fassihi, Allergan submits that his fees should be discounted by 85%, to reflect the fact that the majority of his evidence was directed to the obviousness issue and that evidence was not accepted by the Court.
- Evidence: `counterargument_limitation` cue `but` at chunk `4401785` offsets `382-385`; context: Given the conclusions I reached in respect of his testimony (Allergan, above, at para 35), I consider that his fees should be substantially discounted, but not to the extent suggested by Allergan.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4401786` offsets `5-16`; context: [72] Accordingly, I consider it appropriate to reduce the total disbursements of $124,605.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4401787` offsets `5-14`; context: [73] Therefore, the total disbursements that will be awarded to Sandoz will be $77,145.
- Evidence: `counterargument_limitation` cue `However` at chunk `4401789` offsets `94-101`; context: However, it filed a defence to Sandoz’s Counterclaim and incurred some additional costs, primarily in respect of the examinations of one of its representatives (Yasuhiko Kirisawa) and one of the inventors of the ‘002 Patent (Mitsuo Muramatsu).
- Evidence: `reasoning_application` cue `Therefore` at chunk `4401790` offsets `145-154`; context: Therefore, it is entitled to the costs that it is seeking, with the following minor adjustments.
- Evidence: `reasoning_application` cue `because` at chunk `4401791` offsets `165-172`; context: [77] Sandoz relies on Pelletier v Canada, 2006 FCA 418 at para 9 [Pelletier] to support its assertion that Kissei is precluded from seeking costs in this proceeding because it failed to request costs in its pleadings or during the trial, which it did not attend.
- Evidence: `counterargument_limitation` cue `However` at chunk `4401791` offsets `263-270`; context: However, Sandoz’s reliance on Pelletier is misplaced.
- Evidence: `disposition` cue `granted` at chunk `4401791` offsets `335-342`; context: This is because I granted Leave to Kissei to make submissions on costs after I became aware that it had incurred material costs in connection with this proceeding.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4401792` offsets `471-482`; context: Allergan was required to add Kissei to the proceeding, pursuant to s.
- Evidence: `reasoning_application` cue `because` at chunk `4401792` offsets `103-110`; context: [78] Sandoz further submits that if Kissei is entitled to any costs, they should be borne by Allergan, because Allergan was the party who initially added Kissei as a Defendant in this proceeding, and because it is not uncommon for licencing agreements to include provisions for costs incurred by the licensor in defending impeachment actions.
- Evidence: `evidence_fact` cue `Affidavit` at chunk `4401793` offsets `236-245`; context: In brief, they relate to the preparation of Kissei’s defence and amended defence to Sandoz’s Counterclaim, the preparation of Kissei’s Affidavit of Documents, the preparation for examination of discovery of one of its representatives and one of the inventors of the ‘002 Patent, attendance at those examinations, and participation in various case management conferences.
- Evidence: `disposition` cue `allowed` at chunk `4401797` offsets `452-459`; context: Sandoz submits that if any of Kissei’s accommodation claims are allowed, they should be limited to a maximum of four days for each of Messrs.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4401798` offsets `14-25`; context: Accordingly, Kissei’s claims for accommodation will be adjusted downward to exclude the first nine days of hotel expenses claimed for Mr.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4401799` offsets `5-16`; context: [85] Accordingly, Sandoz will be required to indemnify Kissei for fees of $23,670 (assessed at the upper end of Column IV of Tariff B) plus reasonable disbursements of $16,626.

#### Section text

Allergan Inc. v. Sandoz Canada Inc.
Court (s) Database
Federal Court Decisions
Date
2021-02-26
Neutral citation
2021 FC 186
File numbers
T-2023-18
Notes
Reported Decision
Decision Content
Date: 20210226
Docket: T-2023-18
Citation: 2021 FC 186
Ottawa, Ontario, February 26, 2021
PRESENT: THE CHIEF JUSTICE
BETWEEN:
ALLERGAN INC.
Plaintiff
and
SANDOZ CANADA INC.
Defendant
and
KISSEI PHARMACEUTICAL CO., LTD.
Defendant/Patent Owner
AND BETWEEN:
SANDOZ CANADA INC.
Plaintiff by Counterclaim
and
ALLERGAN INC. and KISSEI PHARMACEUTICAL CO., LTD.
Defendants by Counterclaim
ORDER AND REASONS

[1] These reasons and the accompanying Order concern the costs claimed in relation to the patent infringement action filed by the plaintiff Allergan Inc. [Allergan] against the defendant Sandoz Canada Inc. [Sandoz], as well as the latter’s Counterclaim in this proceeding.

[2] For the reasons that follow, Allergan will be ordered to pay a lump sum amount of $384,505.69 to Sandoz, who ultimately prevailed in the main action. The legal fees component of this award ($272,000) represents approximately 45% of the fees incurred by Sandoz in connection with the issues in this proceeding, as ultimately narrowed. The other components are HST on those fees ($35,360), plus Sandoz’s reasonable disbursements ($77,145.69). Among other things, the fee award amount includes an upward adjustment to reflect the fact that Sandoz made a bona fide written offer to settle that would have provided Allergan with a more favourable outcome than what it ultimately achieved by continuing on to trial.

[3] The defendant Kissei Pharmaceutical Co. Ltd. [Kissei] did not take any position in the main action. However, it filed a brief defense to Sandoz’s Counterclaim and incurred certain additional costs, primarily in relation to the discovery process. Given that Kissei completely prevailed in its defence, it will be awarded its reasonable costs of $40,296.34. The fees component of this award ($23,670) has been calculated in accordance with the upper end of Column IV of Tariff B to the Federal Courts Rules, SOR/98-106 [the Rules]. The other component of this award is Kissei’s reasonable disbursements of $16,626.34.
I. Background

[4] Allergan is the exclusive licensee of Canadian Patent No. 2,507,002 [the ‘002 Patent]. That patent pertains to the prescription drug RAPAFLO®, which is indicated for the treatment of benign prostatic hyperplasia. Kissei is the owner of that patent.

[5] In 2018, Sandoz sought approval from Health Canada to market a generic alternative to RAPAFLO® in Canada [the Sandoz Product]. Soon thereafter, it served Allergan with a Notice of Allegation, as contemplated by subsection 5(3) of the Patented Medicines (Notice of Compliance) Regulations, SOR/93-133 [the Regulations]. Allergan then commenced an infringement action against Sandoz pursuant to subsection 6(1) of the Regulations. In its Statement of Claim, it named Kissei as a co-defendant. In response, Sandoz filed a Statement of Defence and Counterclaim in which it denied that its product would infringe the ‘002 Patent and claimed that the patent is invalid on the grounds of obviousness, overbreadth and insufficiency. However, it ultimately narrowed its Counterclaim to a single allegation of invalidity based on obviousness. Sandoz has confirmed that the costs it is now seeking do not include aspects of the Counterclaim that were not ultimately pursued (including the claims based on overbreadth and insufficiency). Indeed, Sandoz has also excluded the costs associated with the preparation of the Counterclaim itself.

[6] Allergan’s Statement of Claim also alleged that the Sandoz Product would infringe at least one of the claims in a second patent, namely, Canadian Patent No 2,496,780 [the ‘780 Patent]. Once again, Sandoz claimed that its product would not infringe the patent and alleged that the patent is invalid on several grounds. Approximately one week before the trial in this matter, the parties discontinued their dispute with respect to this second patent on consent, and on a without cost basis. They have confirmed that they are not seeking costs incurred in respect of the ‘780 Patent, and I am satisfied that the approach they have respectively taken to the calculation of their costs represents a reasonable attempt to exclude those costs (including disbursements). [1]

[7] In December 2020, I issued a Judgment and Reasons addressing the merits of Allergan’s action and Sandoz’s Counterclaim: Allergan Inc v Sandoz Canada Inc, 2020 FC 1189 [Allergan]. There were three principal issues addressed. The first was whether the Sandoz Product will infringe the ‘002 Patent. (This issue essentially turned on claims construction.) The second was whether representations that were made during the patent application process on behalf of Kissei could be introduced as evidence in this proceeding, pursuant to section 53.1 of the Patent Act, R.S.C. 1985, c. P-4 [the Act]. The third was whether the ‘002 Patent is invalid on the ground of obviousness.

[8] Ultimately, I found in favour of Sandoz on the first issue and in favour of Allergan on the second and third issues. I then invited Allergan and Sandoz to make submissions regarding costs. In this regard, I encouraged them to attempt to reach a settlement on this issue, failing which to identify a lump sum amount that reflected certain identified factors as well as any additional relevant factors, including those identified in Rule 400 of the Rules and the jurisprudence. After becoming aware that Kissei had incurred material cost beyond simply filing a brief defence to Sandoz’s Counterclaim, I also granted Kissei leave to make submissions on costs.
II. Overview of the Parties’ Submissions
A. Sandoz

[9] Sandoz submits that in light of the fact that it prevailed in the infringement action initiated by Allergan, it is entitled to its costs, without any offset to reflect the fact that it was unsuccessful with respect to two of the three principal issues in the proceeding. Given the complexity of the proceeding and the fact that Sandoz also made two offers to settle approximately two months prior to trial, it requests a lump sum award reflecting 50% of its assessable fees plus its reasonable disbursements and HST, for a total costs award of $462,876.45.

[10] In the alternative, Sandoz requests a lump sum award of 30% of its assessable fees plus its above-mentioned disbursements and HST, for a total award of $327,567.99.

[11] In the further alternative, Sandoz requests that costs be fixed at the high end of Column IV of Tariff B, with double costs awarded from the date of offer until the date of my judgment on the merits, plus its reasonable disbursements and HST, for a total costs award of $265,958.13.
B. Allergan

[12] Allergan submits that it should be awarded costs for having completely prevailed in relation to Sandoz’s Counterclaim. However, it seeks only to use that success as a set off against any costs payable to Sandoz. It maintains that such a set off is also warranted by the fact that it prevailed in relation to the issue Sandoz raised with respect to the prosecution history of the ’002 Patent. As discussed above, this was one of the three principal issues in dispute in this proceeding.

[13] The specific set off sought by Allergan is $201,277.73, which is the sum of its Bill of Costs for costs incurred in relation to Sandoz’s Counterclaim, calculated by reference to the upper end of Column IV of Tariff B.

[14] In the alternative, Allergan submits that any cost award granted to Sandoz should be discounted by two-thirds of what Sandoz has claimed, to reflect that Allergan prevailed in respect of two of the three principal issues in dispute. Allergan maintains that such a reduction is particularly appropriate given that this case was ultimately narrowed to three principal issues involving a single patent, and Sandoz narrowed its invalidity case to obviousness and one prior art document late in the day.

[15] More specifically, Allergan maintains that a lump sum award to Sandoz based on a percentage of actual legal fees would not be appropriate, essentially because Allergan prevailed with respect to two of the three main issues in dispute between the parties. Instead, Allergan insists that any cost award in favour of Sandoz should be calculated by reference to the high end of Column IV of Tariff B, and then discounted by two-thirds.

[16] Regarding expert fees, Allergan submits that Dr. Felton’s fees should be fully assessable, essentially because the bulk of her time was spent addressing Sandoz’s invalidity claims. Allergan adds that Ms. Wilson’s fees should be assessed at 50%, because the Court found her evidence regarding the legislative history of section 53.1 to be “straightforward and helpful”. Allegan further maintains that the fees of Dr. Stewart should not be assessable, and that Dr. Fassihi’s fees should be substantially reduced, as further discussed in part III.B.(7) of these reasons.
C. Kissei

[17] Kissei was required to be added to Allergan’s action pursuant to subsection 6(2) of the Regulations. However, it took no position in that action and did not participate in the trial. It simply filed a defence to Sandoz’s Counterclaim for declarations of invalidity of the ‘780 Patent and the ‘002 Patent. It also incurred some additional costs, primarily in respect of the examinations of one of its representatives and one of the inventors of the ‘002 Patent. Given that Sandoz’s Counterclaim was not successful, Kissei seeks its costs taxable at the upper end of Column IV of Tariff B ($23,670) together with “reasonable disbursements comprising business class airfare, accommodations and meals, translation services (if any) and transcript costs”. It has represented that none of those costs or disbursements pertain to the ‘780 Patent. [2]

[18] In the alternative, if it does not succeed in obtaining a cost award, Kissei maintains that no costs should be assessed against it, either in the main action or the Counterclaim, because it was successful on the issues in which it engaged.
III. Assessment
A. General Principles

[19] The principal objectives underlying an award of costs are to (i) provide indemnification for costs associated with successfully pursuing a valid legal right or defending an unfounded claim, (ii) penalize a party who has refused a reasonable settlement offer, and (iii) sanction behaviour that increases the duration and expense of litigation, or is otherwise unreasonable or vexatious: British Columbia (Minister of Forests) v Okanagan Indian Band, 2003 SCC 71 at para 25 [Okanagan Indian Band]; Air Canada v Thibodeau, 2007 FCA 115 at para 24 [Thibodeau]. In certain types of “special cases”, an award of costs can also facilitate access to justice: Okanagan Indian Band, above, at para 27.

[20] By virtue of being “a tool in the furtherance of the efficient and orderly administration of justice”, the power of courts to order cost awards can provide an important “disincentive to those who might be tempted to harass others with meritless claims”: Okanagan Indian Band, above, at paras 25-26.

[21] The Court has broad discretion over the amount and allocation of costs: Rule 400(1); Eli Lilly and Company v Teva Canada Limited, 2011 FCA 220 at para 55 [Eli Lilly v Teva]; Little Sisters Book and Art Emporium v Canada (Commissioner of Customs and Revenue), 2007 SCC 2 at paras 47 and 49. However, that discretion must be exercised in accordance with established principles pertaining to costs, unless the circumstances justify a different approach: Okanagan Indian Band, above, at para 22; Nova Chemicals Corporation v Dow Chemical Company, 2017 FCA 25 at para 19 [Nova v Dow].

[22] In this Court, costs may be fixed by reference to Tariff B of the Rules or by way of a lump sum: Rule 400(4). In recent years, the granting of a lump sum award has become increasingly common: Nova v Dow, above, at para 11; Philip Morris Products SA v Marlboro Canada Ltd, 2015 FCA 9 at para 4. This trend is in part attributable to the Court’s desire to reduce the significant time and effort typically associated with preparing and reviewing the type of detailed bill of costs that is required for the purposes of an assessment under Tariff B: Consorzio del Prosciutto di Parma v Maple Leaf Meats Inc, 2002 FCA 417 at para 12 [Consorzio]; Venngo Inc v Concierge Connection Inc, 2017 FCA 96 at paras 85-86 [Venngo], leave to appeal ref’d [2017] SCCA No 302. Given that submissions in support of a lump sum award can significantly decrease such time and effort for parties as well as the Court (if they are accepted), they facilitate access to justice. This is particularly so where such submissions reduce the legal costs that would otherwise be incurred in the preparation of the more detailed type of Bill of Costs that is required when costs are assessed pursuant to Tariff B. Nevertheless, a lump sum award of costs may not be appropriate in all cases: Consorzio, above.

[23] To the extent that a lump sum award can be expected to achieve the benefits mentioned above, it will further the objective of securing “the just, most expeditious and least expensive determination” of proceedings (Nova v Dow, above, at para 11, citing Rule 3) and should be favoured: Barzelex Inc v EBN Al Waleed (The), [1999] FCJ No 2002 at para 11 (TD), aff’d 2001 FCA 111; Pfizer Canada Inc v Novopharm Ltd, 2010 FC 668 at para 57.

[24] Regardless of whether parties favour a lump sum award or an amount fixed in accordance with Tariff B, counsel are encouraged to be prepared to address costs, ideally on consent, at the conclusion of the proceeding or shortly thereafter: Consorzio, above.

[25] The “default” level of costs in this Court is the mid-point of Column III in Tariff B: Rule 407; Sanofi-Aventis Canada Inc v Novopharm Limited, 2009 FC 1139 at para 4 [Sanofi-Novopharm FC], aff’d 2012 FCA 265; Apotex v Sanofi-Aventis, 2012 FC 318 at para 5 [Apotex v Sanofi-Aventis]; Dennis v Canada, 2017 FC 1011 at para 8; Bernard v Professional Institute of the Public Service of Canada, 2020 FCA 211 at para 38. Column III is intended to provide partial indemnification (as opposed to substantial or full indemnification) for “cases of average or usual complexity”: Thibodeau, above, at para 21; Novopharm Ltd v Eli Lilly and Co, 2010 FC 1154 at para 5 [Novopharm v Eli Lilly].

[26] In recognition of the particular attributes of intellectual property proceedings, it is common for increased costs to be awarded in those proceedings: see, e.g., Consorzio, above, at para 6; Lainco Inc c Commission scolaire des Bois-Francs, 2018 FC 186 at para 8(c). Those particular attributes include greater than average complexity, sophisticated parties, legal bills far in excess of what is contemplated by Column III of Tariff B, and “giving parties an incentive to litigate efficiently”: Seedlings Life Science Ventures, LLC v Pfizer Canada ULC, 2020 FC 505 at para 4 [Seedlings]. For cases that involve drug patent disputes and a cost award fixed by reference to the tariff, the high end of Column IV is often considered to be reasonable and appropriate: Sanofi-Novopharm FC, above, at para 13, aff’d 2012 FCA 265; Novopharm v Eli Lilly, above, at para 7; Apotex v Sanofi-Aventis, above. See also Federal Court of Appeal and Federal Court Rules Committee, Review of the Rules on Costs: Discussion Paper, October 5, 2015, at page 8.

[27] For essentially the same reasons identified immediately above, it is also increasingly common in intellectual property cases to award a significant lump sum amount “well in excess of the Tariff”: Vengo, above, at para 85; Bauer Hockey Ltd v Sport Maska Inc, 2020 FC 862 at para 12 [Bauer]. In this regard, a lump sum award in the range of 25-50% of actual fees, plus reasonable disbursements, is often made: Nova v Dow, above, at paras 17 and 21; Seedlings, above, at para 6; Bauer, above, at para 13. See also Loblaws Inc v Columbia Insurance Company, 2019 FC 1434 at para 15. In approaching this assessment, it should be kept in mind that determining the level of a lump sum award “is not an exact science”: Nova v Dow, above, at para 21.

[28] In recognition of the fact that Tariff B no longer provides an adequate level of partial indemnification, the Federal Courts Rules Committee decided in 2016 that the amount recoverable under Tariff B should be increased by approximately 25%: Minutes of the October 28, 2016 Meeting of the Rules Committee. Following a further consultation with the bar, a sub-committee of the Rules Committee is preparing proposed amendments for publication in Part I of the Canada Gazette and approval of the Governor in Council. In the meantime, it is relevant to bear in mind that the existing tariff “is considered particularly inadequate in Intellectual Property litigation [and in] maritime proceedings”: Report from the Federal Court of Appeal and Federal Court Rules sub-Committee on Costs (June 3, 2016), at section D.

[29] The principal factors the Court may consider in its determination of a cost award are set forth in a non-exhaustive list in Rule 400(3), which is reproduced in Appendix 1 below.

[30] The general rule is that the successful party is entitled to have its costs, even if it was not successful in respect of each and every argument it pursued: Okanagan Indian Band, above, at paras 20-21; Raydan Mfg Ltd v Emmanuel Simard & Fils Inc, 2006 FCA 293 at paras 2-5 [Raydan]. However, the Court may depart from this approach in cases of truly “divided success” or “mixed results”: Eurocopter v Bell Helicopter Textron Canada Ltée, 2012 FC 842 at paras 23 and 56 [Eurocopter FC] aff’d 2013 FCA 220 at paras 10 and 15; Sanofi, above, at paras 8-9; Apotex v Sanofi-Aventis, above, at para 11; Bristol-Myers Squibb Canada Co v Teva Canada Limited, 2016 FC 991 at paras 9-14.

[31] The jurisprudence is split on the issue of whether the successful defence of a patent infringement action, or success with respect to only some grounds of invalidity, constitutes “divided success” when the defendant in the main action is not successful with respect to one or more other allegations of invalidity. In one line of cases, the cost award in favour of the defendant who prevailed on the infringement issue was reduced to reflect the fact that it did not succeed with respect to some or all of its allegations of invalidity: see e.g., Fournier Pharma Inc v Canada (Health), 2012 FC 1121 at paras 4-6; GlaxoSmithKline Inc v Pharmascience Inc, 2008 FC 849 at para 4. In a second line of cases, it has been explicitly held that this type of outcome does not constitute “divided success” or “mixed results” and that therefore the defendant is entitled to its costs: Raydan, above; Illinois Tool Works Inc v Cobra Anchors Co, 2003 FCA 358 at paras 10-11; Betser-Zilevitch v Petrochina Canada Ltd, 2021 FC 151 at para 11 [Betser-Zilevitch 2]; Johnson & Johnson Inc v Boston Scientific Ltd, 2008 FC 817 at para 4. This is so regardless of whether the defendant’s allegations of invalidity were made in a defence to the main action or in a separate Counterclaim: Raydan, above, at paras 6-7; Eurocopter FC, above, at para 11. Notwithstanding my sympathy for the approach taken in the first line of cases, I consider myself bound by this second line of cases.

[32] With this in mind, I further consider that where a defendant in the main action prevails with respect to either the plaintiff’s allegation of infringement or one or more of its allegations of invalidity, an assessment of an appropriate lump sum award should begin at the mid-point of the 25%-50% range discussed at paragraph 27 above, plus reasonable disbursements. This would be subject to any adjustment to reflect factors that may support a departure from this level of award in such a case.

[33] I recognize that this Court has recently suggested that the proper method for determining a lump sum award based on a

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 7567:2 · paragraphs 86-93

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a17b609f1886c9be742144fe8963f9f2ca691d68c1fce8b3316efe77c3cf4385`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7567:2:subtheme:1 · paragraphs 86-87

- Raw key terms: `above, achieved, action, adjustment, allergan, among, amount, approximately`
- Display key terms: `above, achieved, action, adjustment, allergan, among, amount, approximately`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: above, achieved, action, adjustment, allergan, among, amount, approximately No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 86-87. This is a deterministic evidence summary, not a legal conclusion.

#### 7567:2:subtheme:2 · paragraphs 88-93

- Raw key terms: `patent, reduced, respect, sandoz, work, allergan, amount, approach`
- Display key terms: `patent, reduced, respect, sandoz, work, allergan, amount, approach`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: patent, reduced, respect, sandoz, work, allergan, amount, approach Position/evidence statements: Factors in awarding costs Facteurs à prendre en compte (3) In exercising its discretion under subsection (1), the Court may consider (3) Dans l’exercice de son pouvoir discrétionnaire en application du paragraphe (1), la Rule/authority context: Factors in awarding costs Facteurs à prendre en compte (3) In exercising its discretion under subsection (1), the Court may consider (3) Dans l’exercice de son pouvoir discrétionnaire en application du paragraphe (1), la Application context: Conditions Conditions (3) Subsections (1) and (2) do not apply unless the offer to settle (3) Les paragraphes (1) et (2) ne s’appliquent qu’à l’offre de règlement qui répond aux conditions suivantes : (a) is made at leas Operative outcome context: Factors in awarding costs Facteurs à prendre en compte (3) In exercising its discretion under subsection (1), the Court may consider (3) Dans l’exercice de son pouvoir discrétionnaire en application du paragraphe (1), la Evidence spans paragraphs 88-93. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4401801` offsets `1848-1854`; context: Factors in awarding costs
Facteurs à prendre en compte
(3) In exercising its discretion under subsection (1), the Court may consider
(3) Dans l’exercice de son pouvoir discrétionnaire en application du paragraphe (1), la Cour peut tenir compte de l’un ou l’autre des facteurs suivants :
(a) the result of the proceeding;
(a) le résultat de l’instance;
(b) the amounts claimed and the amounts recovered;
(b) les sommes réclamées et les sommes recouvrées;
(c) the importance and complexity of the issues;
(c) l’importance et la complexité des questions en litige;
(d) the apportionment of liability;
(d) le partage de la responsabilité;
(e) any written offer to settle;
(e) toute offre écrite de règlement;
(f) any offer to contribute made under rule 421;
(f) toute offre de contribution faite en vertu de la règle 421;
(g) the amount of work;
(g) la charge de travail;
(h) whether the public interest in having the proceeding litigated justifies a particular award of costs;
(h) le fait que l’intérêt public dans la résolution judiciaire de l’instance justifie une adjudication particulière des dépens;
(i) any conduct of a party that tended to shorten or unnecessarily lengthen the duration of the proceeding;
(i) la conduite d’une partie qui a eu pour effet d’abréger ou de prolonger inutilement la durée de l’instance;
(j) the failure by a party to admit anything that should have been admitted or to serve a request to admit;
(j) le défaut de la part d’une partie de signifier une demande visée à la règle 255 ou de reconnaître ce qui aurait dû être admis;
(k) whether any step in the proceeding was
(k) la question de savoir si une mesure prise au cours de l’instance, selon le cas :
(i) improper, vexatious or unnecessary, or
(i) était inappropriée, vexatoire ou inutile,
(ii) taken through negligence, mistake or excessive caution;
(ii) a été entreprise de manière négligente, par erreur ou avec trop de circonspection;
(l) whether more than one set of costs should be allowed, where two or more parties were represented by different solicitors or were represented by the same solicitor but separated their defence unnecessarily;
(l) la question de savoir si plus d’un mémoire de dépens devrait être accordé lorsque deux ou plusieurs parties sont représentées par différents avocats ou lorsque, étant représentées par le même avocat, elles ont scindé inutilement leur défense;
(m) whether two or more parties, represented by the same solicitor, initiated separate proceedings unnecessarily;
(m) la question de savoir si deux ou plusieurs parties représentées par le même avocat ont engagé inutilement des instances distinctes;
(n) whether a party who was successful in an action exaggerated a claim, including a counterclaim or third party claim, to avoid the operation of rules 292 to 299;
(n) la question de savoir si la partie qui a eu gain de cause dans une action a exagéré le montant de sa réclamation, notamment celle indiquée dans la demande reconventionnelle ou la mise en cause, pour éviter l’application des règles 292 à 299;
(n.
- Evidence: `party_position` cue `claimed` at chunk `4401801` offsets `1721-1728`; context: Factors in awarding costs
Facteurs à prendre en compte
(3) In exercising its discretion under subsection (1), the Court may consider
(3) Dans l’exercice de son pouvoir discrétionnaire en application du paragraphe (1), la Cour peut tenir compte de l’un ou l’autre des facteurs suivants :
(a) the result of the proceeding;
(a) le résultat de l’instance;
(b) the amounts claimed and the amounts recovered;
(b) les sommes réclamées et les sommes recouvrées;
(c) the importance and complexity of the issues;
(c) l’importance et la complexité des questions en litige;
(d) the apportionment of liability;
(d) le partage de la responsabilité;
(e) any written offer to settle;
(e) toute offre écrite de règlement;
(f) any offer to contribute made under rule 421;
(f) toute offre de contribution faite en vertu de la règle 421;
(g) the amount of work;
(g) la charge de travail;
(h) whether the public interest in having the proceeding litigated justifies a particular award of costs;
(h) le fait que l’intérêt public dans la résolution judiciaire de l’instance justifie une adjudication particulière des dépens;
(i) any conduct of a party that tended to shorten or unnecessarily lengthen the duration of the proceeding;
(i) la conduite d’une partie qui a eu pour effet d’abréger ou de prolonger inutilement la durée de l’instance;
(j) the failure by a party to admit anything that should have been admitted or to serve a request to admit;
(j) le défaut de la part d’une partie de signifier une demande visée à la règle 255 ou de reconnaître ce qui aurait dû être admis;
(k) whether any step in the proceeding was
(k) la question de savoir si une mesure prise au cours de l’instance, selon le cas :
(i) improper, vexatious or unnecessary, or
(i) était inappropriée, vexatoire ou inutile,
(ii) taken through negligence, mistake or excessive caution;
(ii) a été entreprise de manière négligente, par erreur ou avec trop de circonspection;
(l) whether more than one set of costs should be allowed, where two or more parties were represented by different solicitors or were represented by the same solicitor but separated their defence unnecessarily;
(l) la question de savoir si plus d’un mémoire de dépens devrait être accordé lorsque deux ou plusieurs parties sont représentées par différents avocats ou lorsque, étant représentées par le même avocat, elles ont scindé inutilement leur défense;
(m) whether two or more parties, represented by the same solicitor, initiated separate proceedings unnecessarily;
(m) la question de savoir si deux ou plusieurs parties représentées par le même avocat ont engagé inutilement des instances distinctes;
(n) whether a party who was successful in an action exaggerated a claim, including a counterclaim or third party claim, to avoid the operation of rules 292 to 299;
(n) la question de savoir si la partie qui a eu gain de cause dans une action a exagéré le montant de sa réclamation, notamment celle indiquée dans la demande reconventionnelle ou la mise en cause, pour éviter l’application des règles 292 à 299;
(n.
- Evidence: `evidence_fact` cue `evidence` at chunk `4401801` offsets `4462-4470`; context: 1) whether the expense required to have an expert witness give evidence was justified given
(n.
- Evidence: `governing_rule` cue `under` at chunk `4401801` offsets `1441-1446`; context: Factors in awarding costs
Facteurs à prendre en compte
(3) In exercising its discretion under subsection (1), the Court may consider
(3) Dans l’exercice de son pouvoir discrétionnaire en application du paragraphe (1), la Cour peut tenir compte de l’un ou l’autre des facteurs suivants :
(a) the result of the proceeding;
(a) le résultat de l’instance;
(b) the amounts claimed and the amounts recovered;
(b) les sommes réclamées et les sommes recouvrées;
(c) the importance and complexity of the issues;
(c) l’importance et la complexité des questions en litige;
(d) the apportionment of liability;
(d) le partage de la responsabilité;
(e) any written offer to settle;
(e) toute offre écrite de règlement;
(f) any offer to contribute made under rule 421;
(f) toute offre de contribution faite en vertu de la règle 421;
(g) the amount of work;
(g) la charge de travail;
(h) whether the public interest in having the proceeding litigated justifies a particular award of costs;
(h) le fait que l’intérêt public dans la résolution judiciaire de l’instance justifie une adjudication particulière des dépens;
(i) any conduct of a party that tended to shorten or unnecessarily lengthen the duration of the proceeding;
(i) la conduite d’une partie qui a eu pour effet d’abréger ou de prolonger inutilement la durée de l’instance;
(j) the failure by a party to admit anything that should have been admitted or to serve a request to admit;
(j) le défaut de la part d’une partie de signifier une demande visée à la règle 255 ou de reconnaître ce qui aurait dû être admis;
(k) whether any step in the proceeding was
(k) la question de savoir si une mesure prise au cours de l’instance, selon le cas :
(i) improper, vexatious or unnecessary, or
(i) était inappropriée, vexatoire ou inutile,
(ii) taken through negligence, mistake or excessive caution;
(ii) a été entreprise de manière négligente, par erreur ou avec trop de circonspection;
(l) whether more than one set of costs should be allowed, where two or more parties were represented by different solicitors or were represented by the same solicitor but separated their defence unnecessarily;
(l) la question de savoir si plus d’un mémoire de dépens devrait être accordé lorsque deux ou plusieurs parties sont représentées par différents avocats ou lorsque, étant représentées par le même avocat, elles ont scindé inutilement leur défense;
(m) whether two or more parties, represented by the same solicitor, initiated separate proceedings unnecessarily;
(m) la question de savoir si deux ou plusieurs parties représentées par le même avocat ont engagé inutilement des instances distinctes;
(n) whether a party who was successful in an action exaggerated a claim, including a counterclaim or third party claim, to avoid the operation of rules 292 to 299;
(n) la question de savoir si la partie qui a eu gain de cause dans une action a exagéré le montant de sa réclamation, notamment celle indiquée dans la demande reconventionnelle ou la mise en cause, pour éviter l’application des règles 292 à 299;
(n.
- Evidence: `reasoning_application` cue `apply` at chunk `4401801` offsets `8328-8333`; context: Conditions
Conditions
(3) Subsections (1) and (2) do not apply unless the offer to settle
(3) Les paragraphes (1) et (2) ne s’appliquent qu’à l’offre de règlement qui répond aux conditions suivantes :
(a) is made at least 14 days before the commencement of the hearing or trial; and
a) elle est faite au moins 14 jours avant le début de l’audience ou de l’instruction;
(b) is not withdrawn and does not expire before the commencement of the hearing or trial.
- Evidence: `disposition` cue `allowed` at chunk `4401801` offsets `3328-3335`; context: Factors in awarding costs
Facteurs à prendre en compte
(3) In exercising its discretion under subsection (1), the Court may consider
(3) Dans l’exercice de son pouvoir discrétionnaire en application du paragraphe (1), la Cour peut tenir compte de l’un ou l’autre des facteurs suivants :
(a) the result of the proceeding;
(a) le résultat de l’instance;
(b) the amounts claimed and the amounts recovered;
(b) les sommes réclamées et les sommes recouvrées;
(c) the importance and complexity of the issues;
(c) l’importance et la complexité des questions en litige;
(d) the apportionment of liability;
(d) le partage de la responsabilité;
(e) any written offer to settle;
(e) toute offre écrite de règlement;
(f) any offer to contribute made under rule 421;
(f) toute offre de contribution faite en vertu de la règle 421;
(g) the amount of work;
(g) la charge de travail;
(h) whether the public interest in having the proceeding litigated justifies a particular award of costs;
(h) le fait que l’intérêt public dans la résolution judiciaire de l’instance justifie une adjudication particulière des dépens;
(i) any conduct of a party that tended to shorten or unnecessarily lengthen the duration of the proceeding;
(i) la conduite d’une partie qui a eu pour effet d’abréger ou de prolonger inutilement la durée de l’instance;
(j) the failure by a party to admit anything that should have been admitted or to serve a request to admit;
(j) le défaut de la part d’une partie de signifier une demande visée à la règle 255 ou de reconnaître ce qui aurait dû être admis;
(k) whether any step in the proceeding was
(k) la question de savoir si une mesure prise au cours de l’instance, selon le cas :
(i) improper, vexatious or unnecessary, or
(i) était inappropriée, vexatoire ou inutile,
(ii) taken through negligence, mistake or excessive caution;
(ii) a été entreprise de manière négligente, par erreur ou avec trop de circonspection;
(l) whether more than one set of costs should be allowed, where two or more parties were represented by different solicitors or were represented by the same solicitor but separated their defence unnecessarily;
(l) la question de savoir si plus d’un mémoire de dépens devrait être accordé lorsque deux ou plusieurs parties sont représentées par différents avocats ou lorsque, étant représentées par le même avocat, elles ont scindé inutilement leur défense;
(m) whether two or more parties, represented by the same solicitor, initiated separate proceedings unnecessarily;
(m) la question de savoir si deux ou plusieurs parties représentées par le même avocat ont engagé inutilement des instances distinctes;
(n) whether a party who was successful in an action exaggerated a claim, including a counterclaim or third party claim, to avoid the operation of rules 292 to 299;
(n) la question de savoir si la partie qui a eu gain de cause dans une action a exagéré le montant de sa réclamation, notamment celle indiquée dans la demande reconventionnelle ou la mise en cause, pour éviter l’application des règles 292 à 299;
(n.
- Evidence: `issue` cue `question` at chunk `4401802` offsets `321-329`; context: In essence, where it was readily apparent that work was performed solely in respect of the ‘780 Patent, the time recorded on the docket in question was excluded from Sandoz’s calculations.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4401802` offsets `94-103`; context: [1] Sandoz’s approach in this regard is described in considerable detail at pages 3-13 of the affidavit of Marta Wysokinski, affirmed on January 27, 2021 [the Wysokinski Affidavit].

#### Section text

IV. Conclusion

[86] For the reasons set forth above, Allergan will be ordered to pay a lump sum amount of $384,505.69 to Sandoz, who ultimately prevailed in the main action. The fee component of this is $272,000, which represents approximately 45% of Sandoz’s Eligible Fees. The other components are HST on those legal fees, plus Sandoz’s reasonable disbursements. Among other things, the award for legal fees includes an upward adjustment to reflect the fact that Sandoz made a bona fide written offer to settle that would have provided Allergan with a more favourable outcome than what it ultimately achieved by continuing on to trial.

[87] Given that Kissei completely prevailed in its defence, it will be awarded its reasonable costs of $40,296.34, comprising $23,670 for legal fees calculated in accordance with the upper end of Column IV of Tariff B, plus reasonable disbursements of $16,626.34.
ORDER in T-2023-18
THIS COURT ORDERS that:
Allergan shall pay to Sandoz lump sum costs of $384,505.69, comprising reasonable fees of $272,000, HST on those fees of $35,360, plus reasonable disbursements of $77,145.69.
Sandoz shall pay to Kissei costs of $40,296.34, comprising fees of $23,670.00 assessed in accordance with the upper end of Column IV of Tariff B plus reasonable disbursements of $16,626.34.
“Paul S. Crampton”
Chief Justice
Appendix 1 – Relevant legislation
Federal Court Rules, SOR/98-106
COSTS
DÉPENS
Awarding of Costs Between Parties
Adjudication des dépens entre parties
Discretionary powers of Court
Pouvoir discrétionnaire de la Cour
400 (1) The Court shall have full discretionary power over the amount and allocation of costs and the determination of by whom they are to be paid.
400 (1) La Cour a le pouvoir discrétionnaire de déterminer le montant des dépens, de les répartir et de désigner les personnes qui doivent les payer.
Crown
La Couronne
(2) Costs may be awarded to or against the Crown.
(2) Les dépens peuvent être adjugés à la Couronne ou contre elle.
Factors in awarding costs
Facteurs à prendre en compte
(3) In exercising its discretion under subsection (1), the Court may consider
(3) Dans l’exercice de son pouvoir discrétionnaire en application du paragraphe (1), la Cour peut tenir compte de l’un ou l’autre des facteurs suivants :
(a) the result of the proceeding;
(a) le résultat de l’instance;
(b) the amounts claimed and the amounts recovered;
(b) les sommes réclamées et les sommes recouvrées;
(c) the importance and complexity of the issues;
(c) l’importance et la complexité des questions en litige;
(d) the apportionment of liability;
(d) le partage de la responsabilité;
(e) any written offer to settle;
(e) toute offre écrite de règlement;
(f) any offer to contribute made under rule 421;
(f) toute offre de contribution faite en vertu de la règle 421;
(g) the amount of work;
(g) la charge de travail;
(h) whether the public interest in having the proceeding litigated justifies a particular award of costs;
(h) le fait que l’intérêt public dans la résolution judiciaire de l’instance justifie une adjudication particulière des dépens;
(i) any conduct of a party that tended to shorten or unnecessarily lengthen the duration of the proceeding;
(i) la conduite d’une partie qui a eu pour effet d’abréger ou de prolonger inutilement la durée de l’instance;
(j) the failure by a party to admit anything that should have been admitted or to serve a request to admit;
(j) le défaut de la part d’une partie de signifier une demande visée à la règle 255 ou de reconnaître ce qui aurait dû être admis;
(k) whether any step in the proceeding was
(k) la question de savoir si une mesure prise au cours de l’instance, selon le cas :
(i) improper, vexatious or unnecessary, or
(i) était inappropriée, vexatoire ou inutile,
(ii) taken through negligence, mistake or excessive caution;
(ii) a été entreprise de manière négligente, par erreur ou avec trop de circonspection;
(l) whether more than one set of costs should be allowed, where two or more parties were represented by different solicitors or were represented by the same solicitor but separated their defence unnecessarily;
(l) la question de savoir si plus d’un mémoire de dépens devrait être accordé lorsque deux ou plusieurs parties sont représentées par différents avocats ou lorsque, étant représentées par le même avocat, elles ont scindé inutilement leur défense;
(m) whether two or more parties, represented by the same solicitor, initiated separate proceedings unnecessarily;
(m) la question de savoir si deux ou plusieurs parties représentées par le même avocat ont engagé inutilement des instances distinctes;
(n) whether a party who was successful in an action exaggerated a claim, including a counterclaim or third party claim, to avoid the operation of rules 292 to 299;
(n) la question de savoir si la partie qui a eu gain de cause dans une action a exagéré le montant de sa réclamation, notamment celle indiquée dans la demande reconventionnelle ou la mise en cause, pour éviter l’application des règles 292 à 299;
(n.1) whether the expense required to have an expert witness give evidence was justified given
(n.1) la question de savoir si les dépenses engagées pour la déposition d’un témoin expert étaient justifiées compte tenu de l’un ou l’autre des facteurs suivants :
(i) the nature of the litigation, its public significance and any need to clarify the law,
(i) la nature du litige, son importance pour le public et la nécessité de clarifier le droit,
(ii) the number, complexity or technical nature of the issues in dispute, or
(ii) le nombre, la complexité ou la nature technique des questions en litige,
(iii) the amount in dispute in the proceeding; and
(iii) la somme en litige;
(o) any other matter that it considers relevant.
(o) toute autre question qu’elle juge pertinente.
Tariff B
Tarif B
(4) The Court may fix all or part of any costs by reference to Tariff B and may award a lump sum in lieu of, or in addition to, any assessed costs.
(4) La Cour peut fixer tout ou partie des dépens en se reportant au tarif B et adjuger une somme globale au lieu ou en sus des dépens taxés.
[…]
[…]
Assessment according to Tariff B
Tarif B
407 Unless the Court orders otherwise, party-and-party costs shall be assessed in accordance with column III of the table to Tariff B.
407 Sauf ordonnance contraire de la Cour, les dépens partie-partie sont taxés en conformité avec la colonne III du tableau du tarif B.
[…]
[…]
Consequences of failure to accept plaintiff’s offer
Conséquences de la non-acceptation de l’offre du demandeur
420 (1) Unless otherwise ordered by the Court and subject to subsection (3), where a plaintiff makes a written offer to settle and obtains a judgment as favourable or more favourable than the terms of the offer to settle, the plaintiff is entitled to party-and-party costs to the date of service of the offer and costs calculated at double that rate, but not double disbursements, after that date.
420 (1) Sauf ordonnance contraire de la Cour et sous réserve du paragraphe (3), si le demandeur fait au défendeur une offre écrite de règlement, et que le jugement qu’il obtient est aussi avantageux ou plus avantageux que les conditions de l’offre, il a droit aux dépens partie-partie jusqu’à la date de signification de l’offre et, par la suite, au double de ces dépens mais non au double des débours.
Consequences of failure to accept defendant’s offer
Conséquences de la non-acceptation de l’offre du défendeur
(2) Unless otherwise ordered by the Court and subject to subsection (3), where a defendant makes a written offer to settle,
(2) Sauf ordonnance contraire de la Cour et sous réserve du paragraphe (3), si le défendeur fait au demandeur une offre écrite de règlement, les dépens sont alloués de la façon suivante :
(a) if the plaintiff obtains a judgment less favourable than the terms of the offer to settle, the plaintiff is entitled to party-and-party costs to the date of service of the offer and the defendant shall be entitled to costs calculated at double that rate, but not double disbursements, from that date to the date of judgment; or
a) si le demandeur obtient un jugement moins avantageux que les conditions de l’offre, il a droit aux dépens partie-partie jusqu’à la date de signification de l’offre et le défendeur a droit, par la suite et jusqu’à la date du jugement au double de ces dépens mais non au double des débours;
(b) if the plaintiff fails to obtain judgment, the defendant is entitled to party-and-party costs to the date of the service of the offer and to costs calculated at double that rate, but not double disbursements, from that date to the date of judgment.
b) si le demandeur n’a pas gain de cause lors du jugement, le défendeur a droit aux dépens partie-partie jusqu’à la date de signification de l’offre et, par la suite et jusqu’à la date du jugement, au double de ces dépens mais non au double des débours.
Conditions
Conditions
(3) Subsections (1) and (2) do not apply unless the offer to settle
(3) Les paragraphes (1) et (2) ne s’appliquent qu’à l’offre de règlement qui répond aux conditions suivantes :
(a) is made at least 14 days before the commencement of the hearing or trial; and
a) elle est faite au moins 14 jours avant le début de l’audience ou de l’instruction;
(b) is not withdrawn and does not expire before the commencement of the hearing or trial.
b) elle n’est pas révoquée et n’expire pas avant le début de l’audience ou de l’instruction.
FEDERAL COURT
SOLICITORS OF RECORD
DOCKET:
T-2023-18
STYLE OF CAUSE:
ALLERGAN INC v SANDOZ CANADA INC and KISSEI PHARMACEUTICAL CO., LTD.
SUBMISSIONS ON COSTS CONSIDERED AT OTTAWA, ONTARIO PURSUANT TO THIS COURT’S JUDGMENT IN 2020 FC 1189
ORDER AND reasons:
CRAMPTON C.J.
ORDER AND REASONS ISSUED:
February 26, 2021
WRITTEN SUBMISSSIONS BY:
David Tait
Steven Tanner
Sanjaya Mendis
Kendra Levasseur
For The Plaintiff
Carol Hitchman
Meghan Dureen
Rae Daddon
For The Defendant (SANDOZ cANADA iNC.)
J. Sheldon Hamilton
FOR THE DEFENDANT (KISSEI PHARMACEUTICAL CO., LTD.)
SOLICITORS OF RECORD:
McCarthy Tétrault LLP
Toronto, Ontario
For The Plaintiff
Sprigings IP
Toronto, Ontario
For The Defendant (SANDOZ cANADA iNC.)
Smart & Biggar LLP
Toronto, Ontario
FOR THE DEFENDANT (KISSEI PHARMACEUTICAL CO., LTD.)

[1] Sandoz’s approach in this regard is described in considerable detail at pages 3-13 of the affidavit of Marta Wysokinski, affirmed on January 27, 2021 [the Wysokinski Affidavit]. In essence, where it was readily apparent that work was performed solely in respect of the ‘780 Patent, the time recorded on the docket in question was excluded from Sandoz’s calculations. Where Sandoz was unable to proceed in that fashion, it simply reduced various categories of its actual fees by 50%. It took a similar approach to disbursements. For its part, Allergan simply reduced certain items by 50%.

[2] In this regard, it has reduced by 50% the costs incurred in respect of the examinations for discovery. I am satisfied that this represents a reasonable approach to excluding costs incurred in respect of the ‘780 Patent.

[3] Sandoz reduced the amount claimed in respect of three of Dr. Stewart’s four invoices by 50%, to exclude work performed in respect of the ‘780 Patent.

[4] $665.68 for the first two nights combined plus $471.75 per night for the next seven nights.

[5] $424.97 per night times five nights.
