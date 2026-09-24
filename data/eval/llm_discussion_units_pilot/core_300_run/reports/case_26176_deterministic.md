# Discussion Units: case 26176

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **30**
- Continuity pairs: **29**
- Discussion Units: **3**
- Paragraph source hashes: **30**
- Sub-themes: **10**

## 26176:1 · paragraphs 0-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `375ca835d8ae6d4338bd1fd9004e76808ecfc8f307cc4e0585d703d151786281`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26176:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, decision, immigration, aguilar, board, citizenship, claim, court`
- Display key terms: `aguilar`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: aguilar Rule/authority context: [1] This is an application for judicial review of the August 3, 2011 decision of the Refugee Protection Division of the Immigration and Refugee Board [the RPD or Board] denying the applicant’s claim for refugee protectio Application context: In a decision dated May 21, 2010, the RPD found the applicant to be a credible witness and accepted that he had been a victim of MS threats and extortion, but dismissed his claim, holding that section 96 of the IRPA was  Operative outcome context: In a decision dated May 21, 2010, the RPD found the applicant to be a credible witness and accepted that he had been a victim of MS threats and extortion, but dismissed his claim, holding that section 96 of the IRPA was  Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5231490` offsets `222-227`; context: [1] This is an application for judicial review of the August 3, 2011 decision of the Refugee Protection Division of the Immigration and Refugee Board [the RPD or Board] denying the applicant’s claim for refugee protection under section 96 and subsection 97(1)(b) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].
- Evidence: `evidence_fact` cue `found that` at chunk `5231491` offsets `555-565`; context: Justice Noël vacated that decision in Aguilar Zacarias v Minister of Citizenship and Immigration, 2011 FC 62, where he found that the Board had erred in its interpretation of section 97 of the IRPA because it failed to properly assess the personalized risk faced by the applicant.
- Evidence: `reasoning_application` cue `because` at chunk `5231491` offsets `396-403`; context: In a decision dated May 21, 2010, the RPD found the applicant to be a credible witness and accepted that he had been a victim of MS threats and extortion, but dismissed his claim, holding that section 96 of the IRPA was inapplicable as the victimization was not based on a Convention ground and that section 97 was inapplicable because the risk was a generalized one.
- Evidence: `counterargument_limitation` cue `but` at chunk `5231491` offsets `223-226`; context: In a decision dated May 21, 2010, the RPD found the applicant to be a credible witness and accepted that he had been a victim of MS threats and extortion, but dismissed his claim, holding that section 96 of the IRPA was inapplicable as the victimization was not based on a Convention ground and that section 97 was inapplicable because the risk was a generalized one.
- Evidence: `disposition` cue `dismissed` at chunk `5231491` offsets `227-236`; context: In a decision dated May 21, 2010, the RPD found the applicant to be a credible witness and accepted that he had been a victim of MS threats and extortion, but dismissed his claim, holding that section 96 of the IRPA was inapplicable as the victimization was not based on a Convention ground and that section 97 was inapplicable because the risk was a generalized one.

#### 26176:1:subtheme:2 · paragraphs 3-6

- Raw key terms: `applicant, chubby, claims, market, alleges, came, chain, collect`
- Display key terms: `chubby, claims, market, alleges, came, chain, collect`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: chubby, claims, market, alleges, came, chain, collect Position/evidence statements: [4] The applicant claims that he was a vendor in an open air market in Guatemala, where he sold chickens. | [5] The applicant claims that he and a fellow vendor, Evedardo Vicente, eventually reported Chubby’s extortion to the police. Application context: He also asserts that over time Chubby demonstrated increasing knowledge of the details of the applicant’s family, which led the applicant to conclude that he and his family were being watched. Operative outcome context: [3] In its August 3, 2011 decision that is the subject of the present application for judicial review, a different member of the RPD re-heard the case, decided that the applicant lacked credibility and dismissed the clai Evidence spans paragraphs 3-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5231492` offsets `349-354`; context: While it was certainly open to the member to have reached a different conclusion from the first member on the issue of credibility as the first decision was quashed for all purposes (see, e.
- Evidence: `evidence_fact` cue `determined that` at chunk `5231492` offsets `521-536`; context: Miah v Canada (Minister of Citizenship and Immigration), 2007 FC 2005 at para 8), I have determined that the reasoning in the second decision is so erroneous that it must be set aside.
- Evidence: `counterargument_limitation` cue `however` at chunk `5231492` offsets `745-752`; context: Given the deference which must be afforded to credibility determinations, it is exceptional that they will be overturned; this, however, is a case where an erroneous credibility finding requires intervention.
- Evidence: `disposition` cue `dismissed` at chunk `5231492` offsets `202-211`; context: [3] In its August 3, 2011 decision that is the subject of the present application for judicial review, a different member of the RPD re-heard the case, decided that the applicant lacked credibility and dismissed the claim for that reason.
- Evidence: `party_position` cue `claims` at chunk `5231493` offsets `18-24`; context: [4] The applicant claims that he was a vendor in an open air market in Guatemala, where he sold chickens.
- Evidence: `reasoning_application` cue `conclude` at chunk `5231493` offsets `665-673`; context: He also asserts that over time Chubby demonstrated increasing knowledge of the details of the applicant’s family, which led the applicant to conclude that he and his family were being watched.
- Evidence: `party_position` cue `claims` at chunk `5231494` offsets `18-24`; context: [5] The applicant claims that he and a fellow vendor, Evedardo Vicente, eventually reported Chubby’s extortion to the police.
- Evidence: `counterargument_limitation` cue `but` at chunk `5231494` offsets `149-152`; context: Chubby was imprisoned, but the applicant says the extortion continued and intensified, as did the threats: other members of the MS came to the market to collect payments and allegedly told the applicant that Chubby knew it was the applicant who had reported the extortion and that he and his friend, Vincente were “dead”.
- Evidence: `party_position` cue `claims` at chunk `5231495` offsets `137-143`; context: Vincente and the applicant to another market that the applicant claims they were visiting and shot and killed Mr.
- Evidence: `counterargument_limitation` cue `but` at chunk `5231495` offsets `333-336`; context: The applicant did not return to his market stall after this incident but continued working at his other job in a restaurant until approximately six months later when he alleges that Chubby came to the restaurant looking for him.

#### 26176:1:subtheme:3 · paragraphs 7-11

- Raw key terms: `canada, citizenship, immigration, minister, para, applicant, credibility, findings`
- Display key terms: `para, credibility, findings`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: para, credibility, findings Rule/authority context: Issues and Standard of Review Application context: The failure to conduct any analysis deprives these findings of transparency and they are therefore insufficient to overcome an otherwise deficient decision (Guney v Canada (Minister of Citizenship and Immigration), 2008  | A tribunal must be careful when rendering a decision based on a lack of plausibility because refugee claimants come from diverse cultures, and actions which appear implausible when judged from Canadian standards might be Evidence spans paragraphs 7-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5231496` offsets `314-320`; context: Issues and Standard of Review
- Evidence: `governing_rule` cue `Standard of Review` at chunk `5231496` offsets `325-343`; context: Issues and Standard of Review
- Evidence: `issue` cue `issues` at chunk `5231497` offsets `242-248`; context: [8] In the introduction to its decision, the Board made a passing reference to the fact that state protection and an internal flight alternative would have been available to the applicant but does not conduct any analysis whatsoever of these issues.
- Evidence: `reasoning_application` cue `therefore` at chunk `5231497` offsets `339-348`; context: The failure to conduct any analysis deprives these findings of transparency and they are therefore insufficient to overcome an otherwise deficient decision (Guney v Canada (Minister of Citizenship and Immigration), 2008 FC 1134 at para 21).
- Evidence: `counterargument_limitation` cue `but` at chunk `5231497` offsets `188-191`; context: [8] In the introduction to its decision, the Board made a passing reference to the fact that state protection and an internal flight alternative would have been available to the applicant but does not conduct any analysis whatsoever of these issues.
- Evidence: `counterargument_limitation` cue `However` at chunk `5231498` offsets `840-847`; context: However, as Justice Phelan noted in Njeri v Canada (Minister of Citizenship and Immigration), 2009 FC 291, [2009] FCJ No 350, “[D]eference is not a blank cheque.
- Evidence: `evidence_fact` cue `record` at chunk `5231499` offsets `302-308`; context: [10] Dealing more specifically with credibility findings that rest on plausibility determinations, this Court has often cautioned that such determinations are best limited to situations where events are clearly unlikely to have occurred in the manner asserted, based on common sense or the evidentiary record (see e.
- Evidence: `reasoning_application` cue `because` at chunk `5231499` offsets `1239-1246`; context: A tribunal must be careful when rendering a decision based on a lack of plausibility because refugee claimants come from diverse cultures, and actions which appear implausible when judged from Canadian standards might be plausible when considered from within the claimant’s milieu (at para 9) [citations omitted, emphasis added].
- Evidence: `counterargument_limitation` cue `However` at chunk `5231499` offsets `858-865`; context: However, plausibility findings should be made only in the clearest of cases, i.
- Evidence: `evidence_fact` cue `evidence` at chunk `5231500` offsets `99-107`; context: [11] An allegation may thus be found to be implausible when it does not make sense in light of the evidence before the Board or when (to borrow the language of Justice Muldoon in Vatchev) it is “outside the realm of what reasonably could be expected”.

#### 26176:1:subtheme:4 · paragraphs 12-18

- Raw key terms: `applicant, board, credibility, evidence, implausibility, implausible, market, chubby`
- Display key terms: `credibility, implausibility, implausible, market, chubby`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: credibility, implausibility, implausible, market, chubby Position/evidence statements: It is not implausible that the applicant was not targeted until the date he claims the extortion started and there is nothing in the evidence from which the Board could reasonably have concluded otherwise. Rule/authority context: [12] In this case, the Board did not respect these guiding principles and instead engaged in impermissible speculation in rejecting the credibility of the applicant’s claims. Application context: I find, on balance of probabilities, that the local Mara would have not begun extorting the claimant soon after he set up shop in 2004. | Accordingly, this implausibility finding is not reasonable. Evidence spans paragraphs 12-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `principles` at chunk `5231501` offsets `59-69`; context: [12] In this case, the Board did not respect these guiding principles and instead engaged in impermissible speculation in rejecting the credibility of the applicant’s claims.
- Evidence: `evidence_fact` cue `found that` at chunk `5231502` offsets `38-48`; context: [13] In the first instance, the Board found that it was implausible that the MS would not have begun extorting the applicant “soon after” he began selling chickens in the market.
- Evidence: `reasoning_application` cue `I find` at chunk `5231502` offsets `631-637`; context: I find, on balance of probabilities, that the local Mara would have not begun extorting the claimant soon after he set up shop in 2004.
- Evidence: `party_position` cue `claims` at chunk `5231503` offsets `367-373`; context: It is not implausible that the applicant was not targeted until the date he claims the extortion started and there is nothing in the evidence from which the Board could reasonably have concluded otherwise.
- Evidence: `evidence_fact` cue `evidence` at chunk `5231503` offsets `424-432`; context: It is not implausible that the applicant was not targeted until the date he claims the extortion started and there is nothing in the evidence from which the Board could reasonably have concluded otherwise.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5231503` offsets `497-508`; context: Accordingly, this implausibility finding is not reasonable.
- Evidence: `evidence_fact` cue `testimony` at chunk `5231504` offsets `186-195`; context: Vincente, stating:
The claimant’s own testimony, his exhibits, and the objective documentary evidence all state that the Mara gangs are ruthless, extremely, violent groups who take reprisals when crossed or betrayed.
- Evidence: `reasoning_application` cue `therefore` at chunk `5231504` offsets `367-376`; context: I therefore find it implausible that Mara members would approach the claimant at his stall in the market, after Chubby’s arrest and said that the claimant and his friend were “dead” and warn him that Chubby was “really pissed at him.
- Evidence: `reasoning_application` cue `conclude` at chunk `5231505` offsets `717-725`; context: This plausibility determination was certainly not one of the “clearest of cases” as set out by Justice Muldoon in Valtchev (cited above at para 10) and was an inappropriate basis upon which to conclude that the market encounter never occurred.
- Evidence: `evidence_fact` cue `evidence` at chunk `5231506` offsets `773-781`; context: In the circumstances, this is a further situation where the implausibility conclusion reached is far from clear and has no foundation in the evidence.
- Evidence: `reasoning_application` cue `therefore` at chunk `5231506` offsets `789-798`; context: It is therefore unreasonable.
- Evidence: `counterargument_limitation` cue `However` at chunk `5231507` offsets `136-143`; context: However, several of these other bases are without foundation.

#### 26176:1:subtheme:5 · paragraphs 19-21

- Raw key terms: `applicant, board, claim, however, report, authorities, complaints, evidence`
- Display key terms: `however, report, authorities, complaints`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: however, report, authorities, complaints Position/evidence statements: In support of its finding that the applicant could not have reported the extortion to the police, the Board referred to the documentation regarding typical police procedures in Guatemala, which indicated that the police  Application context: Therefore, the lack of a formal police report does not undercut the applicant’s claim to have reported the extortion to a member of the police, who was fulfilling the role of security guard on at the market on the day th Evidence spans paragraphs 19-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5231508` offsets `155-162`; context: [19] More specifically, the Board first noted that there were inconsistencies in the applicant’s evidence given at the first and second hearings regarding whether he and Mr.
- Evidence: `party_position` cue `claim` at chunk `5231508` offsets `1031-1036`; context: In support of its finding that the applicant could not have reported the extortion to the police, the Board referred to the documentation regarding typical police procedures in Guatemala, which indicated that the police typically took statements when formal complaints were made and reasoned that the complainant’s claim to have gone to the police was not credible as no statement was taken.
- Evidence: `evidence_fact` cue `evidence` at chunk `5231508` offsets `97-105`; context: [19] More specifically, the Board first noted that there were inconsistencies in the applicant’s evidence given at the first and second hearings regarding whether he and Mr.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5231508` offsets `1702-1711`; context: Therefore, the lack of a formal police report does not undercut the applicant’s claim to have reported the extortion to a member of the police, who was fulfilling the role of security guard on at the market on the day the report was made.
- Evidence: `evidence_fact` cue `testimony` at chunk `5231509` offsets `403-412`; context: This is consistent with the applicant’s testimony: he testified that he did not report the death threats to the police due to fear of the MS.
- Evidence: `counterargument_limitation` cue `However` at chunk `5231509` offsets `228-235`; context: However, one of the affidavits states that the applicant did not report the death threats (as opposed to the extortion) to the police.
- Evidence: `counterargument_limitation` cue `fails` at chunk `5231510` offsets `409-414`; context: The Board additionally highlighted the fact that the article fails to mention the applicant’s presence or the motive for the murder (i.

#### 26176:1:subtheme:6 · paragraphs 22-23

- Raw key terms: `because, board, credibility, determination, events, might, above-noted, acws`
- Display key terms: `because, credibility, determination, events, might, above-noted, acws`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: because, credibility, determination, events, might, above-noted, acws Application context: [22] Finally, the Board found that the applicant was not credible because his subjective fear was not well-founded. | In such circumstances, a decision may be set aside as unreasonable, even if peripheral points in the Board’s reasoning might withstand scrutiny, because the central bases for the Board’s credibility determination are unr Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5231511` offsets `797-804`; context: In addition, contrary to what the Board held, the fact that the MS did not threaten the applicant’s family following his departure does not undermine the credibility of the applicant’s version of events (although it might well be relevant to whether the applicant might be at risk if returned to El Salvador).
- Evidence: `evidence_fact` cue `found that` at chunk `5231511` offsets `24-34`; context: [22] Finally, the Board found that the applicant was not credible because his subjective fear was not well-founded.
- Evidence: `reasoning_application` cue `because` at chunk `5231511` offsets `66-73`; context: [22] Finally, the Board found that the applicant was not credible because his subjective fear was not well-founded.
- Evidence: `counterargument_limitation` cue `However` at chunk `5231511` offsets `354-361`; context: However, the record reveals that there was good reason for the family to have moved to that area because the applicant’s spouse and children would have the support of her family who lived in the town.
- Evidence: `reasoning_application` cue `because` at chunk `5231512` offsets `319-326`; context: In such circumstances, a decision may be set aside as unreasonable, even if peripheral points in the Board’s reasoning might withstand scrutiny, because the central bases for the Board’s credibility determination are unreasonable (see e.

#### 26176:1:subtheme:7 · paragraphs 24-25

- Raw key terms: `applicant, based, board, credibility, above, account, acws, additionally`
- Display key terms: `based, credibility, above, account, acws, additionally`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: based, credibility, above, account, acws, additionally Application context: [24] I would additionally note that I find the Board to have employed an inappropriate understanding of demeanour in its analysis. Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5231513` offsets `662-669`; context: While this Court has recognized that the Board is well-positioned to assess a claimant’s demeanour in its credibility determinations, demeanour is intended to encompass the way in which the claimant responds to questions, such as whether the claimant appears uncertain or hesitates.
- Evidence: `evidence_fact` cue `testimony` at chunk `5231513` offsets `969-978`; context: For instance, in Gjergo v Canada (Minister of Citizenship and Immigration), 2004 FC 303 at para 22, 131 ACWS (3d) 508, Justice Harrington wrote, “This Court has previously held that the panel may take into account the demeanor of an applicant during his testimony.
- Evidence: `reasoning_application` cue `I find` at chunk `5231513` offsets `36-42`; context: [24] I would additionally note that I find the Board to have employed an inappropriate understanding of demeanour in its analysis.

#### 26176:1:subtheme:8 · paragraphs 26-26

- Raw key terms: `above, allowed, application, arises, certification, completely, decision, facts`
- Display key terms: `above, allowed, arises, certification, completely, facts`
- Argument roles: `disposition, governing_rule, issue`
- Explanation: Observed roles: disposition, governing_rule, issue Display terms: above, allowed, arises, certification, completely, facts Rule/authority context: No question has been proposed for certification under section 74 of the IRPA and none arises as this decision turns completely on the facts. Operative outcome context: [26] For the above reasons, this application for judicial review is allowed. Evidence spans paragraphs 26-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5231515` offsets `80-88`; context: No question has been proposed for certification under section 74 of the IRPA and none arises as this decision turns completely on the facts.
- Evidence: `governing_rule` cue `under` at chunk `5231515` offsets `125-130`; context: No question has been proposed for certification under section 74 of the IRPA and none arises as this decision turns completely on the facts.
- Evidence: `disposition` cue `allowed` at chunk `5231515` offsets `68-75`; context: [26] For the above reasons, this application for judicial review is allowed.

#### Section text

Aguilar Zacarias v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-10-01
Neutral citation
2012 FC 1155
File numbers
IMM-9303-11
Decision Content
Date: 20121001
Docket: IMM-9303-11
Citation: 2012 FC 1155
Ottawa, Ontario, October 1, 2012
PRESENT: The Honourable Madam Justice Gleason
BETWEEN:
GABINO OLEGARIO AGUILAR ZACARIAS
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review of the August 3, 2011 decision of the Refugee Protection Division of the Immigration and Refugee Board [the RPD or Board] denying the applicant’s claim for refugee protection under section 96 and subsection 97(1)(b) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA]. The applicant is a citizen of Guatemala who alleges he was a victim of extortion and threats at the hands of the Mara Salvatrucha, or MS-13, gang [the MS].

[2] This is the second time this matter has been before this Court. In a decision dated May 21, 2010, the RPD found the applicant to be a credible witness and accepted that he had been a victim of MS threats and extortion, but dismissed his claim, holding that section 96 of the IRPA was inapplicable as the victimization was not based on a Convention ground and that section 97 was inapplicable because the risk was a generalized one. Justice Noël vacated that decision in Aguilar Zacarias v Minister of Citizenship and Immigration, 2011 FC 62, where he found that the Board had erred in its interpretation of section 97 of the IRPA because it failed to properly assess the personalized risk faced by the applicant. Justice Noël remitted the applicant’s claim to a different member of the RPD for re-determination.

[3] In its August 3, 2011 decision that is the subject of the present application for judicial review, a different member of the RPD re-heard the case, decided that the applicant lacked credibility and dismissed the claim for that reason. While it was certainly open to the member to have reached a different conclusion from the first member on the issue of credibility as the first decision was quashed for all purposes (see, e.g. Miah v Canada (Minister of Citizenship and Immigration), 2007 FC 2005 at para 8), I have determined that the reasoning in the second decision is so erroneous that it must be set aside. Given the deference which must be afforded to credibility determinations, it is exceptional that they will be overturned; this, however, is a case where an erroneous credibility finding requires intervention. As is more fully discussed below, the RPD’s findings in this case are based on impermissible conjecture and conclusions that contradict the evidence before the Board and thus cannot stand. To understand why this is so, it is necessary to review the applicant’s version of events and the Board’s decision.
Background

[4] The applicant claims that he was a vendor in an open air market in Guatemala, where he sold chickens. He says that he also worked at a restaurant chain in Guatemala. He alleges that a member of the MS, nicknamed “Gordo” or “Chubby” approached him at the market about two and one half years year after he opened his stall, demanded extortion payments, and thereafter visited him weekly to collect the payments. The applicant claims that Chubby told him that if he did not cooperate, someone close to him would be killed. He also asserts that over time Chubby demonstrated increasing knowledge of the details of the applicant’s family, which led the applicant to conclude that he and his family were being watched.

[5] The applicant claims that he and a fellow vendor, Evedardo Vicente, eventually reported Chubby’s extortion to the police. Chubby was imprisoned, but the applicant says the extortion continued and intensified, as did the threats: other members of the MS came to the market to collect payments and allegedly told the applicant that Chubby knew it was the applicant who had reported the extortion and that he and his friend, Vincente were “dead”.

[6] After Chubby was released from prison, members of the MS tracked Mr. Vincente and the applicant to another market that the applicant claims they were visiting and shot and killed Mr. Vicente. The applicant filed proof of Mr. Vincente’s execution with the RPD. The applicant did not return to his market stall after this incident but continued working at his other job in a restaurant until approximately six months later when he alleges that Chubby came to the restaurant looking for him. The applicant explained the situation to his manager, was assigned to work in the back of the restaurant and was eventually transferred to a different location of the restaurant chain. The applicant then learned from managers at various other restaurant locations that Chubby had come into their restaurants and asked about him. Finally in early 2008, the applicant saw Chubby sitting inside the restaurant while he was working. Scared, he never returned to work at the chain again.

[7] The applicant then moved his family to his in-laws’ village but continued to hear warnings about the presence of the MS in such villages and their ability to locate individuals. As a result, in May 2009, the applicant obtained a temporary work permit and came to Canada, where he filed for refugee protection.
Issues and Standard of Review

[8] In the introduction to its decision, the Board made a passing reference to the fact that state protection and an internal flight alternative would have been available to the applicant but does not conduct any analysis whatsoever of these issues. The failure to conduct any analysis deprives these findings of transparency and they are therefore insufficient to overcome an otherwise deficient decision (Guney v Canada (Minister of Citizenship and Immigration), 2008 FC 1134 at para 21). Thus, the only issue arising in this case is whether the Board’s credibility determination withstands scrutiny.

[9] As noted, it is incontrovertible that credibility findings are reviewable on the reasonableness standard and that significant deference is owed to credibility findings of the RPD given its ability to directly observe the witnesses’ demeanour, its expertise and its role as a finder of fact (see e.g. Aguebor v Canada (Minister of Employment and Immigration) (1993), 160 NR 315, [1993] FCJ No 732 (CA) [Aguebor] at para 4; Singh v Canada (Minister of Employment and Immigration) (1994), 169 NR 107, [1994] FCJ No 486 (CA) [Singh] at para 3; Hemmati v Canada (Minister of Citizenship and Immigration), 2008 FC 383 at para 41; Cetinkaya v Canada (Minister of Citizenship and Immigration), 2012 FC 8, [2012] FCJ No 13 at para 17; Rahal v Canada (Minister of Citizenship and Immigration), 2012 FC 319 at para 22, [2012] FCJ No 369 [Rahal]). However, as Justice Phelan noted in Njeri v Canada (Minister of Citizenship and Immigration), 2009 FC 291, [2009] FCJ No 350, “[D]eference is not a blank cheque. There must be reasoned reasons leading to a justifiable finding” (at para 12).

[10] Dealing more specifically with credibility findings that rest on plausibility determinations, this Court has often cautioned that such determinations are best limited to situations where events are clearly unlikely to have occurred in the manner asserted, based on common sense or the evidentiary record (see e.g. Giron v Canada (Minister of Employment and Immigration), 143 NR 238, [1992] FCJ No 481 (CA); Chavarro v Canada (Minister of Citizenship and Immigration), 2010 FC 1119 at paras 30-32; [2010] FCJ No 1397). As was articulated by Justice Muldoon in the oft-cited case of Valtchev v Canada (Minister of Citizenship and Immigration), 2001 FCT 776, [2001] FCJ No 1131 [Valchev]:
A tribunal may make adverse findings of credibility based on the implausibility of an applicant’s story provided the inferences drawn can be reasonably said to exist. However, plausibility findings should be made only in the clearest of cases, i.e., if the facts as presented are outside the realm of what could reasonably be expected, or where the documentary evidence demonstrates that the events could not have happened in the manner asserted by the claimant. A tribunal must be careful when rendering a decision based on a lack of plausibility because refugee claimants come from diverse cultures, and actions which appear implausible when judged from Canadian standards might be plausible when considered from within the claimant’s milieu (at para 9) [citations omitted, emphasis added].

[11] An allegation may thus be found to be implausible when it does not make sense in light of the evidence before the Board or when (to borrow the language of Justice Muldoon in Vatchev) it is “outside the realm of what reasonably could be expected”. In addition, this Court has held that the Board should provide “a reliable and verifiable evidentiary base against which the plausibility of the Applicants’ evidence might be judged”, otherwise a plausibility determination may be nothing more than “unfounded speculation” (Gjelaj v Canada (Minister of Citizenship and Immigration), 2010 FC 37 at para 4, [2010] FCJ No 31; see also Cao v Canada (Minister of Citizenship and Immigration), 2012 FC 694 at para 20, [2012] FCJ No 885 [Cao]).
Analysis

[12] In this case, the Board did not respect these guiding principles and instead engaged in impermissible speculation in rejecting the credibility of the applicant’s claims. To a significant extent, its credibility determination hinged on three implausibility findings it made. As discussed below, none of them was reasonable.

[13] In the first instance, the Board found that it was implausible that the MS would not have begun extorting the applicant “soon after” he began selling chickens in the market. From the applicant’s own account, the extortion began two and a half years after he started selling in the market. The Board reasoned:
The claimant began selling chicken as a market street vendor in [2004]. He testified that he had never seen Chubby before June 2006 when the extortion began. This is implausible given his own testimony that the Mara are everywhere in his country, and have been, according to the objective evidence, since the 1990’s. I find, on balance of probabilities, that the local Mara would have not begun extorting the claimant soon after he set up shop in 2004. Given their ubiquitous and rapacious [sic] I find no plausible reason for them not to have begun extorting him earlier. I therefore find his statement implausible. His credibility is eroded.
(Decision at para 29)

[14] With respect, this conclusion is unreasonable. The fact that the MS is ubiquitous throughout Guatemala does not imply that they must be targeting every single vendor within the country at the same time nor that they immediately target every vendor as soon as he or she sets up a stall. It is not implausible that the applicant was not targeted until the date he claims the extortion started and there is nothing in the evidence from which the Board could reasonably have concluded otherwise. Accordingly, this implausibility finding is not reasonable.

[15] Second, the Board held that it was implausible that the MS would have come to the market to threaten the applicant without killing him and Mr. Vincente, stating:
The claimant’s own testimony, his exhibits, and the objective documentary evidence all state that the Mara gangs are ruthless, extremely, violent groups who take reprisals when crossed or betrayed. I therefore find it implausible that Mara members would approach the claimant at his stall in the market, after Chubby’s arrest and said that the claimant and his friend were “dead” and warn him that Chubby was “really pissed at him.” First, it is implausible that the gang members would give their intended, victims a warning. Second, as they were armed, and as they are ruthless and violent, why did not they not simply kill the claimant and his friend on the spot. For these reasons, I do not believe such an encounter ever happened. The claimant’s credibility is diminished.
(Decision at para 28)

[16] The applicant, however, alleges that the MS was still seeking to extort money from him when they came to threaten him. Killing him would have eliminated their ability to continue this extortion. In reaching its conclusion, the Board committed a reviewable error by ignoring the applicant’s reasonable explanation of what had occurred (Cao at para 12, cited above at para 11). Moreover, it is not necessarily surprising that the MS would have not killed the applicant and his friend in the middle of a busy marketplace. This plausibility determination was certainly not one of the “clearest of cases” as set out by Justice Muldoon in Valtchev (cited above at para 10) and was an inappropriate basis upon which to conclude that the market encounter never occurred.

[17] Third, the Board pointed to the fact that two affidavits of market vendors supplied by the applicant referred to Chubby as “El Pelon” (which translates as “the Bald One”) rather than “Gordo”. The Board concluded that it was implausible that an MS member would be called by two nicknames and thus viewed the affidavits as undercutting the applicant’s credibility. In my view, this conclusion is flawed as it is not implausible that a person might have, or be referred to by, two nicknames. Moreover, the Board did not explore this apparent inconsistency in its questioning of the applicant, other than noting the two nicknames. In the circumstances, this is a further situation where the implausibility conclusion reached is far from clear and has no foundation in the evidence. It is therefore unreasonable.

[18] In addition to these implausibility findings, the RPD also set out other bases for disbelieving the applicant’s version of events. However, several of these other bases are without foundation.

[19] More specifically, the Board first noted that there were inconsistencies in the applicant’s evidence given at the first and second hearings regarding whether he and Mr. Vincente reported the extortion to a security guard or to the police. While it its true that the applicant (who testified through a translator) used the word “guard” during the first hearing but stated that the report was made to the police during the second hearing, he provided an explanation for this discrepancy, namely that the police sometimes acted as the guards at the market and that on the day in question when the report was made, the police were serving the role of market security (see Certified Tribunal Record [CTR] at p 186). In support of its finding that the applicant could not have reported the extortion to the police, the Board referred to the documentation regarding typical police procedures in Guatemala, which indicated that the police typically took statements when formal complaints were made and reasoned that the complainant’s claim to have gone to the police was not credible as no statement was taken. This, however, does not necessarily follow for two reasons. First, the applicant does not claim to have gone to the police station and filed a formal report: he claims to have reported the incidents to the authorities on duty at the market. Thus, it is not necessarily surprising that “official” procedure would not have been followed, as the applicant did not follow the “official” channels. Second, and more importantly, as counsel for the applicant argued, there was extensive evidence on record to the effect that formal police procedures are often not followed by the police in Guatemala. Therefore, the lack of a formal police report does not undercut the applicant’s claim to have reported the extortion to a member of the police, who was fulfilling the role of security guard on at the market on the day the report was made.

[20] In a similar vein, the Board found it to be of concern that two of the co-worker affidavits stated that the applicant did not complain to the police and this undercut his claim to have reported the extortion to the police. However, one of the affidavits states that the applicant did not report the death threats (as opposed to the extortion) to the police. This is consistent with the applicant’s testimony: he testified that he did not report the death threats to the police due to fear of the MS. Thus, contrary to what the Board found, there is no inconsistency in the evidence on this point. The other affidavit is more general and is not inconsistent with his claim to have not filed a formal police report about the death threats.

[21] The Board further pointed to a press report discussing Mr. Vicente’s murder. This report states that the victim was talking to his brother when he was shot, which the Board held contradicted the applicant’s claim that he and Mr. Vincente ran away in opposite directions when they saw the MS and that Mr. Vincente was shot a few minutes later. The Board additionally highlighted the fact that the article fails to mention the applicant’s presence or the motive for the murder (i.e. retribution for the complaints to the authorities). However, the fact that the applicant would not make himself known to the media in no way undermines his claim – if anything, detailed mention of the applicant in the article might seem to contradict the applicant’s claim of attempts to hide from the MS. The first alleged contradiction noted by the Board appears to be more valid However, this point is insufficient to sustain a negative credibility determination in circumstances like the present where so many other of the bases for the credibility determination are without merit.

[22] Finally, the Board found that the applicant was not credible because his subjective fear was not well-founded. It based this determination on the fact that the applicant had only moved his family 40 miles from the city when he allegedly felt his and their lives were at risk and because his family has not been attacked subsequent to his departure. However, the record reveals that there was good reason for the family to have moved to that area because the applicant’s spouse and children would have the support of her family who lived in the town. In addition, contrary to what the Board held, the fact that the MS did not threaten the applicant’s family following his departure does not undermine the credibility of the applicant’s version of events (although it might well be relevant to whether the applicant might be at risk if returned to El Salvador).

[23] The above-noted observations collectively underpinned the Board’s conclusion that the key events involving the MS had not occurred and were intertwined with each other. In such circumstances, a decision may be set aside as unreasonable, even if peripheral points in the Board’s reasoning might withstand scrutiny, because the central bases for the Board’s credibility determination are unreasonable (see e.g. Calvera v Canada (Minister of Citizenship and Immigration), 2006 FC 1463 at para 27, [2006] FCJ No 1842; Zhuo v Canada (Minister of Citizenship and Immigration), 2005 FC 1271 at paras 7, 21, [2005] FCJ No 154; Tighrine v Canada (Minister of Citizenship and Immigration), [1999] FCJ No 1783, 98 ACWS (3d) 180 at para 7).

[24] I would additionally note that I find the Board to have employed an inappropriate understanding of demeanour in its analysis. The RPD buttressed its negative credibility determination by noting that during the hearing the applicant sat with his arms crossed and appeared “sullen and arrogant” which was “not an attitude one would reasonably expect from someone asking a foreign country to save his life” (Decision at para 35). While this Court has recognized that the Board is well-positioned to assess a claimant’s demeanour in its credibility determinations, demeanour is intended to encompass the way in which the claimant responds to questions, such as whether the claimant appears unc

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 26176:2 · paragraphs 27-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b5780253d8990c457a758ca3e14720e61709c9fd8ed345ecab817207ae277c08`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26176:2:subtheme:1 · paragraphs 27-28

- Raw key terms: `aguilar, allowed, application, cause, certified, citizenship, constituted, costs`
- Display key terms: `aguilar, allowed, certified, constituted, costs`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: aguilar, allowed, certified, constituted, costs Operative outcome context: This application for judicial review is allowed, and the matter is remitted to a differently constituted panel for re-determination; 2. Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5231515` offsets `408-416`; context: No serious question of general importance is certified; and
3.
- Evidence: `disposition` cue `allowed` at chunk `5231515` offsets `301-308`; context: This application for judicial review is allowed, and the matter is remitted to a differently constituted panel for re-determination;
2.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that:
1. This application for judicial review is allowed, and the matter is remitted to a differently constituted panel for re-determination;
2. No serious question of general importance is certified; and
3. There is no order as to costs.
"Mary J.L. Gleason"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-9303-11
STYLE OF CAUSE: Gabino Olegario Aguilar Zacarias v The Minister of Citizenship and Immigration
PLACE OF HEARING: Ottawa, Ontario
DATE OF HEARING: May 28, 2012
REASONS FOR 

## 26176:3 · paragraphs 29-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `84165952c2e86ebc0dd05c5d1f82b0f08229da406f76fe52dbd05d93bea3d451`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26176:3:subtheme:1 · paragraphs 29-29

- Raw key terms: `appearances, applicant, attorney, barrister, canada, dated, deputy, garvin`
- Display key terms: `barrister, dated, deputy, garvin`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, dated, deputy, garvin No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 29-29. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: GLEASON J.
DATED: October 1, 2012
APPEARANCES:
Jamie Liew
FOR THE APPLICANT
Leah Garvin
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Jamie Liew,
Barrister & Solicitor
Ottawa, Ontario
FOR THE APPLICANT
Myles J. Kirvan,
Deputy Attorney General of Canada
Ottawa, Ontario
FOR THE RESPONDENT
