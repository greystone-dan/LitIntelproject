# Discussion Units: case 23750

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **24**
- Continuity pairs: **23**
- Discussion Units: **3**
- Paragraph source hashes: **24**
- Sub-themes: **9**

## 23750:1 · paragraphs 0-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6956d13d80a8dbfa748449e86615f74825e8855ba82fd8ce2ac584c6982781e0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23750:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, canada, alleged, china, chinese, claim, decision, falun`
- Display key terms: `alleged, china, chinese, falun`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: alleged, china, chinese, falun Position/evidence statements: [1] The applicant is a citizen of the People’s Republic of China and claims to be a practitioner of Falun Gong. Rule/authority context: The RPD therefore found the applicant was neither a refugee nor a protected person under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the IRPA]. Application context: The Board reasoned that the applicant had not been a Falun Gong practitioner in China, that as his claimed adherence to Falun Gong in Canada was tied to his claim to have been a practitioner in China, he was not a genuin Operative outcome context: [2] In a decision dated June 28, 2012, the Refugee Protection Division of the Immigration and Refugee Board [the RPD or the Board] dismissed the applicant’s claim, finding that he lacked credibility and that the claimed  Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `5115969` offsets `69-75`; context: [1] The applicant is a citizen of the People’s Republic of China and claims to be a practitioner of Falun Gong.
- Evidence: `evidence_fact` cue `evidence` at chunk `5115969` offsets `564-572`; context: In support of his claim, he provided evidence regarding his alleged practice of Falun Gong in Canada, which included photographs of him engaged in the practice and letters from other Falun Gong adherents.
- Evidence: `evidence_fact` cue `testimony` at chunk `5115970` offsets `341-350`; context: The Board premised its credibility finding on six different weaknesses in the applicant’s testimony, including his demeanour and lack of ability to recount any real detail regarding what he alleged happened in China.
- Evidence: `governing_rule` cue `under` at chunk `5115970` offsets `1037-1042`; context: The RPD therefore found the applicant was neither a refugee nor a protected person under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the IRPA].
- Evidence: `reasoning_application` cue `therefore` at chunk `5115970` offsets `729-738`; context: The Board reasoned that the applicant had not been a Falun Gong practitioner in China, that as his claimed adherence to Falun Gong in Canada was tied to his claim to have been a practitioner in China, he was not a genuine practitioner in Canada and that he was therefore not a true adherent of Falun Gong.
- Evidence: `disposition` cue `dismissed` at chunk `5115970` offsets `131-140`; context: [2] In a decision dated June 28, 2012, the Refugee Protection Division of the Immigration and Refugee Board [the RPD or the Board] dismissed the applicant’s claim, finding that he lacked credibility and that the claimed events in China did not occur.

#### 23750:1:subtheme:2 · paragraphs 3-6

- Raw key terms: `decision, applicant, board, credibility, application, arguing, assessment, based`
- Display key terms: `credibility, arguing, assessment, based`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: credibility, arguing, assessment, based Position/evidence statements: [3] In this application for judicial review, the applicant seeks to set aside the RPD’s decision, arguing that its credibility determination was unreasonable and that it erred in failing to properly assess his sur place  Rule/authority context: The Board found it implausible that the smuggler would have kept the applicant’s Resident Identity Card [RIC] card when accompanying the applicant on his travel to Canada under a false passport due to the risk of being d Application context: This application for judicial review will therefore be dismissed. Operative outcome context: This application for judicial review will therefore be dismissed. Evidence spans paragraphs 3-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claim` at chunk `5115971` offsets `220-225`; context: [3] In this application for judicial review, the applicant seeks to set aside the RPD’s decision, arguing that its credibility determination was unreasonable and that it erred in failing to properly assess his sur place claim (or claim to protection based on his activities in Canada).
- Evidence: `evidence_fact` cue `determined that` at chunk `5115972` offsets `42-57`; context: [4] For the reasons set out below, I have determined that the Board did not commit any such reviewable error and that its decision is reasonable.
- Evidence: `reasoning_application` cue `therefore` at chunk `5115972` offsets `188-197`; context: This application for judicial review will therefore be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `5115972` offsets `201-210`; context: This application for judicial review will therefore be dismissed.
- Evidence: `evidence_fact` cue `testimony` at chunk `5115973` offsets `170-179`; context: The applicant’s testimony regarding what he claimed happened in China lacked authenticity and, in the Board’s words, “had the hallmarks of a rehearsed story rather than a recollection of events arising from having lived through the experience himself” (Decision at para 9).
- Evidence: `governing_rule` cue `under` at chunk `5115973` offsets `1200-1205`; context: The Board found it implausible that the smuggler would have kept the applicant’s Resident Identity Card [RIC] card when accompanying the applicant on his travel to Canada under a false passport due to the risk of being discovered;
4.

#### 23750:1:subtheme:3 · paragraphs 7-13

- Raw key terms: `board, applicant, finding, basis, canada, citizenship, credibility, determination`
- Display key terms: `finding, basis, credibility, determination`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: finding, basis, credibility, determination Position/evidence statements: The applicant asserts that there is no contradiction between the two as he noted his PIF that the PSB went to his close relatives’ homes in their search for him. | [13] As concerns the Board’s treatment of the documents from China filed by the applicant, contrary to what the applicant asserts, the RPD did not discard them solely because of the prevalence of fraudulent documents in  Rule/authority context: [7] Prior to discussing each of the errors that applicant alleges the RPD made, it is useful to review the general principles applicable to the assessment of the Board’s credibility determinations. Application context: As I noted in Rahal v Canada (Minster of Citizenship and Immigration), 2012 FC 319 at para 42 [Rahal]: [T]he starting point in reviewing a credibility finding is the recognition that the role of this Court is a very limi | Accordingly, the RPD’s determination that lack of persecution of the applicant’s family rendered his version of events unbelievable is reasonable. Operative outcome context: Similar determinations were upheld in Hou v Canada (Minister of Citizenship and Immigration), 2012 FC 993 at para 36 [Hou] and Li v Canada (Minister of Citizenship and Immigration), 2005 FC 28 at para 4. Evidence spans paragraphs 7-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5115975` offsets `999-1004`; context: Moreover, in many cases, the tribunal has expertise in the subject matter at issue that the reviewing court lacks.
- Evidence: `evidence_fact` cue `evidence` at chunk `5115975` offsets `912-920`; context: As I noted in Rahal v Canada (Minster of Citizenship and Immigration), 2012 FC 319 at para 42 [Rahal]:
[T]he starting point in reviewing a credibility finding is the recognition that the role of this Court is a very limited one because the tribunal had the advantage of hearing the witnesses testify, observed their demeanor and is alive to all the factual nuances and contradictions in the evidence.
- Evidence: `governing_rule` cue `principles` at chunk `5115975` offsets `115-125`; context: [7] Prior to discussing each of the errors that applicant alleges the RPD made, it is useful to review the general principles applicable to the assessment of the Board’s credibility determinations.
- Evidence: `reasoning_application` cue `because` at chunk `5115975` offsets `749-756`; context: As I noted in Rahal v Canada (Minster of Citizenship and Immigration), 2012 FC 319 at para 42 [Rahal]:
[T]he starting point in reviewing a credibility finding is the recognition that the role of this Court is a very limited one because the tribunal had the advantage of hearing the witnesses testify, observed their demeanor and is alive to all the factual nuances and contradictions in the evidence.
- Evidence: `evidence_fact` cue `testimony` at chunk `5115976` offsets `808-817`; context: Likewise, lack of ability to recall detail – especially in circumstances where it ought to be remembered – provides a tribunal a reasonable basis for rejecting testimony (see e.
- Evidence: `evidence_fact` cue `testimony` at chunk `5115977` offsets `199-208`; context: [9] Thus, the types of matters relied on by the Board in this case in support of its adverse credibility determination fall well within the sort of matters that can be relied on to reject a witness’ testimony.
- Evidence: `party_position` cue `asserts` at chunk `5115979` offsets `141-148`; context: The applicant asserts that there is no contradiction between the two as he noted his PIF that the PSB went to his close relatives’ homes in their search for him.
- Evidence: `evidence_fact` cue `testimony` at chunk `5115979` offsets `116-125`; context: [11] Likewise, the Board did not err in its reliance on the contradictions between the applicant’s PIF and his oral testimony.
- Evidence: `evidence_fact` cue `evidence` at chunk `5115980` offsets `471-479`; context: Likewise, there was support in the objective evidence before the Board for the finding that the Chinese authorities often persecute families of suspected Falun Gong practitioners.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5115980` offsets `606-617`; context: Accordingly, the RPD’s determination that lack of persecution of the applicant’s family rendered his version of events unbelievable is reasonable.
- Evidence: `disposition` cue `upheld` at chunk `5115980` offsets `781-787`; context: Similar determinations were upheld in Hou v Canada (Minister of Citizenship and Immigration), 2012 FC 993 at para 36 [Hou] and Li v Canada (Minister of Citizenship and Immigration), 2005 FC 28 at para 4.
- Evidence: `party_position` cue `asserts` at chunk `5115981` offsets `122-129`; context: [13] As concerns the Board’s treatment of the documents from China filed by the applicant, contrary to what the applicant asserts, the RPD did not discard them solely because of the prevalence of fraudulent documents in China and, thus, this case is distinguishable from Lin v Canada (Minister of Citizenship and Immigration), 2012 FC 157, relied on by the applicant.
- Evidence: `evidence_fact` cue `evidence` at chunk `5115981` offsets `590-598`; context: In Cao, Justice Mactavish noted that:
There was, however, no evidence before the Board to indicate that Mr.
- Evidence: `reasoning_application` cue `because` at chunk `5115981` offsets `167-174`; context: [13] As concerns the Board’s treatment of the documents from China filed by the applicant, contrary to what the applicant asserts, the RPD did not discard them solely because of the prevalence of fraudulent documents in China and, thus, this case is distinguishable from Lin v Canada (Minister of Citizenship and Immigration), 2012 FC 157, relied on by the applicant.
- Evidence: `counterargument_limitation` cue `however` at chunk `5115981` offsets `578-585`; context: In Cao, Justice Mactavish noted that:
There was, however, no evidence before the Board to indicate that Mr.

#### 23750:1:subtheme:4 · paragraphs 14-15

- Raw key terms: `applicant, assessment, basis, board, claim, comments, credibility, deference`
- Display key terms: `assessment, basis, comments, credibility, deference`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: assessment, basis, comments, credibility, deference Position/evidence statements: Did the Board err in its assessment of the applicant’s sur place claim? Rule/authority context: [14] Finally, insofar as concerns the Board’s treatment of the summons issue, as the applicant correctly notes, a finding that the credibility of a claim for protection from China is undermined by the lack of a PSB summo Application context: ), at paragraph 10: The Board drew a negative inference from the lack of a summons in part because the applicant claimed that the PSB had visited his home nine times. | [15] I believe these comments apply equally here. Evidence spans paragraphs 14-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5115982` offsets `71-76`; context: [14] Finally, insofar as concerns the Board’s treatment of the summons issue, as the applicant correctly notes, a finding that the credibility of a claim for protection from China is undermined by the lack of a PSB summons has been rejected as unreasonable in some recent jurisprudence of this Court (see e.
- Evidence: `evidence_fact` cue `evidence` at chunk `5115982` offsets `1518-1526`; context: In my view, every case must be assessed based on the evidence before the Board and its assessment of that evidence.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5115982` offsets `272-285`; context: [14] Finally, insofar as concerns the Board’s treatment of the summons issue, as the applicant correctly notes, a finding that the credibility of a claim for protection from China is undermined by the lack of a PSB summons has been rejected as unreasonable in some recent jurisprudence of this Court (see e.
- Evidence: `reasoning_application` cue `because` at chunk `5115982` offsets `1845-1852`; context: ), at paragraph 10:
The Board drew a negative inference from the lack of a summons in part because the applicant claimed that the PSB had visited his home nine times.
- Evidence: `counterargument_limitation` cue `However` at chunk `5115982` offsets `455-462`; context: However, as noted by Justice Zinn in Jiang v Canada (Minister of Citizenship and Immigration), 2012 FC 1067 at paras 20-22, an unreasonable finding with respect to a summons need not be determinative of the entire application for judicial review:
The applicant cites recent decisions of this Court which have held that “a finding by the Board that on a balance of probabilities it would be reasonable to assume that a summons would have been left is a reviewable error[”]: Liang v.
- Evidence: `party_position` cue `claim` at chunk `5115983` offsets `450-455`; context: Did the Board err in its assessment of the applicant’s sur place claim?
- Evidence: `reasoning_application` cue `apply` at chunk `5115983` offsets `30-35`; context: [15] I believe these comments apply equally here.

#### 23750:1:subtheme:5 · paragraphs 16-17

- Raw key terms: `applicant, assertion, assess, canada, claim, falun, gong, place`
- Display key terms: `assertion, assess, falun, gong, place`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: assertion, assess, falun, gong, place Position/evidence statements: [16] Turning, then, to the second issue, as noted, the applicant argues that the RPD erred in failing to properly assess his sur place claim and in relying on the lack of a legitimate motive for his practice of Falun Gon | [17] Contrary to what the applicant asserts, the Board did assess the sur place claim and the evidence the applicant tendered in support of his assertion that he was a genuine Falun Gong practitioner in Canada. Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5115984` offsets `34-39`; context: [16] Turning, then, to the second issue, as noted, the applicant argues that the RPD erred in failing to properly assess his sur place claim and in relying on the lack of a legitimate motive for his practice of Falun Gong in Canada.
- Evidence: `party_position` cue `argues` at chunk `5115984` offsets `65-71`; context: [16] Turning, then, to the second issue, as noted, the applicant argues that the RPD erred in failing to properly assess his sur place claim and in relying on the lack of a legitimate motive for his practice of Falun Gong in Canada.
- Evidence: `party_position` cue `asserts` at chunk `5115985` offsets `36-43`; context: [17] Contrary to what the applicant asserts, the Board did assess the sur place claim and the evidence the applicant tendered in support of his assertion that he was a genuine Falun Gong practitioner in Canada.
- Evidence: `evidence_fact` cue `evidence` at chunk `5115985` offsets `94-102`; context: [17] Contrary to what the applicant asserts, the Board did assess the sur place claim and the evidence the applicant tendered in support of his assertion that he was a genuine Falun Gong practitioner in Canada.

#### 23750:1:subtheme:6 · paragraphs 18-19

- Raw key terms: `applicant, canada, claim, falun, gong, motive, place, practicing`
- Display key terms: `falun, gong, motive, place, practicing`
- Argument roles: `counterargument_limitation, disposition, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, issue, party_position, reasoning_application Display terms: falun, gong, motive, place, practicing Position/evidence statements: [18] To similar effect, it was not unreasonable for the Board to have assessed and considered the applicant’s motive for practicing Falun Gong as a reason for rejecting his sur place claim. | [19] It follows that the RPD did not err in considering the applicant’s motive for practicing Falun Gong in Canada nor in its assessment of his sur place claim. Application context: Because my reasons in that case apply equally here, I have reproduced a portion of them below: [C]ontrary to what the applicant claims, Canadian case law does recognise that motive for engaging in a religious practice in Operative outcome context: And this Court upheld the Board’s findings in those cases. Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5115986` offsets `1353-1358`; context: The sincerity of those beliefs will be an issue in cases, like the present, where continuing the religious practice in the country of origin might place the claimant at risk.
- Evidence: `party_position` cue `claim` at chunk `5115986` offsets `183-188`; context: [18] To similar effect, it was not unreasonable for the Board to have assessed and considered the applicant’s motive for practicing Falun Gong as a reason for rejecting his sur place claim.
- Evidence: `reasoning_application` cue `Because` at chunk `5115986` offsets `627-634`; context: Because my reasons in that case apply equally here, I have reproduced a portion of them below:
[C]ontrary to what the applicant claims, Canadian case law does recognise that motive for engaging in a religious practice in Canada may be considered by the RPD in an appropriate case.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5115986` offsets `264-270`; context: While beginning to practice a religion solely to buttress a refugee claim cannot, in and of itself, be the basis for rejecting a sur place claim, the Board may legitimately have regard to such motive in assessing the genuineness of a claimant’s claimed religious beliefs.
- Evidence: `disposition` cue `upheld` at chunk `5115986` offsets `3092-3098`; context: And this Court upheld the Board’s findings in those cases.
- Evidence: `party_position` cue `claim` at chunk `5115987` offsets `154-159`; context: [19] It follows that the RPD did not err in considering the applicant’s motive for practicing Falun Gong in Canada nor in its assessment of his sur place claim.

#### 23750:1:subtheme:7 · paragraphs 20-20

- Raw key terms: `accordingly, application, arises, case, certification, dismissed, irpa, none`
- Display key terms: `accordingly, arises, case, certification, dismissed, irpa, none`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: accordingly, arises, case, certification, dismissed, irpa, none Rule/authority context: No question for certification was submitted under section 74 of the IRPA and none arises in this case. Application context: [20] This application will accordingly be dismissed. Operative outcome context: [20] This application will accordingly be dismissed. Evidence spans paragraphs 20-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5115988` offsets `56-64`; context: No question for certification was submitted under section 74 of the IRPA and none arises in this case.
- Evidence: `governing_rule` cue `under` at chunk `5115988` offsets `97-102`; context: No question for certification was submitted under section 74 of the IRPA and none arises in this case.
- Evidence: `reasoning_application` cue `accordingly` at chunk `5115988` offsets `27-38`; context: [20] This application will accordingly be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `5115988` offsets `42-51`; context: [20] This application will accordingly be dismissed.

#### Section text

Su v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2013-05-17
Neutral citation
2013 FC 518
File numbers
IMM-7356-12
Decision Content
Date: 20130517
Docket: IMM-7356-12
Citation: 2013 FC 518
Ottawa, Ontario, May 17, 2013
PRESENT: The Honourable Madam Justice Gleason
BETWEEN:
HAO WEN SU
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] The applicant is a citizen of the People’s Republic of China and claims to be a practitioner of Falun Gong. He alleges that the Chinese Public Security Bureau [PSB] conducted a raid on his Falun Gong group in 2010, that he and others were alerted to the raid by a look-out who called a warning and that he and the others fled through the back door of the premises. He claims he then went into hiding at a relative’s home, sought the assistance of a smuggler, came to Canada and made a refugee claim shortly after arriving. In support of his claim, he provided evidence regarding his alleged practice of Falun Gong in Canada, which included photographs of him engaged in the practice and letters from other Falun Gong adherents.

[2] In a decision dated June 28, 2012, the Refugee Protection Division of the Immigration and Refugee Board [the RPD or the Board] dismissed the applicant’s claim, finding that he lacked credibility and that the claimed events in China did not occur. The Board premised its credibility finding on six different weaknesses in the applicant’s testimony, including his demeanour and lack of ability to recount any real detail regarding what he alleged happened in China. The Board reasoned that the applicant had not been a Falun Gong practitioner in China, that as his claimed adherence to Falun Gong in Canada was tied to his claim to have been a practitioner in China, he was not a genuine practitioner in Canada and that he was therefore not a true adherent of Falun Gong. It thus concluded he was unlikely to face risk if returned to China as he would not practice Falun Gong and was unlikely to be perceived by the Chinese authorities as an adherent. The RPD therefore found the applicant was neither a refugee nor a protected person under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [the IRPA].

[3] In this application for judicial review, the applicant seeks to set aside the RPD’s decision, arguing that its credibility determination was unreasonable and that it erred in failing to properly assess his sur place claim (or claim to protection based on his activities in Canada). In this regard, the applicant argues that the Board committed a reviewable error in considering and relying on the lack of a legitimate motive for his practice of Falun Gong in Canada.

[4] For the reasons set out below, I have determined that the Board did not commit any such reviewable error and that its decision is reasonable. This application for judicial review will therefore be dismissed.
Is the Board’s credibility assessment reasonable?

[5] As noted, the Board offered six different reasons for disbelieving the applicant’s claims regarding what he alleged happened in China. These were:
1. The applicant’s testimony regarding what he claimed happened in China lacked authenticity and, in the Board’s words, “had the hallmarks of a rehearsed story rather than a recollection of events arising from having lived through the experience himself” (Decision at para 9). The Board made this finding based on the applicant’s demeanor and fact he recalled very little detail regarding what he alleged happened, which the RPD felt he ought to have remembered, given the nature of the events he claimed had occurred;
2. The Board questioned the authenticity of certain of the documents the applicant tendered, given the prevalence of fraudulent documents in China the fact that the applicant’s parents mailed them to him (despite the risk of their mail being screened and alleged threats to them by the PSB if they were to help the applicant in his pursuit of Falun Gong);
3. The Board found it implausible that the smuggler would have kept the applicant’s Resident Identity Card [RIC] card when accompanying the applicant on his travel to Canada under a false passport due to the risk of being discovered;
4. The applicant claimed the PSB had searched his uncle’s house, but failed to mention this important detail in the narrative to his Personal Identification Form [PIF] he was required to complete by virtue of section 5(1) of the Refugee Protection Division Rules, SOR/2002-228, even though he was represented by experienced immigration counsel when he completed the PIF;
5. The implausibility of the applicant’s claim that the PSB visited his parents’ home six times over the two year period following the applicant’s departure from China, but did not leave a summons or other documents with the applicant’s parents; and
6. The implausibility of the applicant’s version of events when no punishment was visited on his family.

[6] The applicant challenges each of these findings, arguing that especially when viewed cumulatively, the errors made by the RPD in its credibility assessment render the decision unreasonable.

[7] Prior to discussing each of the errors that applicant alleges the RPD made, it is useful to review the general principles applicable to the assessment of the Board’s credibility determinations. Such determinations are reviewable on the reasonableness standard and must be afforded significant deference (see e.g. Aguebor v (Canada) Minister of Employment and Immigration (1993), [1993] FCJ No 732 at para 4, 160 NR 315 [Aguebor]; Frederick v Canada (Minister of Citizenship and Immigration), 2012 FC 649 at para 14). As I noted in Rahal v Canada (Minster of Citizenship and Immigration), 2012 FC 319 at para 42 [Rahal]:
[T]he starting point in reviewing a credibility finding is the recognition that the role of this Court is a very limited one because the tribunal had the advantage of hearing the witnesses testify, observed their demeanor and is alive to all the factual nuances and contradictions in the evidence. Moreover, in many cases, the tribunal has expertise in the subject matter at issue that the reviewing court lacks. It is therefore much better placed to make credibility findings, including those related to implausibility. Also, the efficient administration of justice, which is at the heart of the notion of deference, requires that review of these sorts of issues be the exception as opposed to the general rule.

[8] In terms of the bases upon which the Board may reasonably rely for an adverse credibility finding, it is well-established that discrepancies between the version of events offered by a claimant at various times provide a solid basis for adverse credibility determinations (see e.g. He v Canada (Minister of Employment and Immigration), [1994] FCJ No 1107, 49 ACWS (3d) 562 (CA); Rajaratnam v Canada (Minister of Employment and Immigration), [1991] FCJ No 1271, 135 NR 300 (CA); Jin v Canada (Minister of Citizenship and Immigration), 2012 FC 595 at para 11 [Jin]; Wei v Canada (Minister of Citizenship and Immigration), 2012 FC 911 at para 59). Likewise, lack of ability to recall detail – especially in circumstances where it ought to be remembered – provides a tribunal a reasonable basis for rejecting testimony (see e.g. Ma v Canada (Minister of Citizenship and Immigration), 2011 FC 417 at paras 31-33; Li v Canada (Minister of Citizenship and Immigration), 2012 FC 998 at para 18; Pjetri v Canada (Minister of Citizenship and Immigration), 2013 FC 376 at para 43). The RPD may additionally rely on implausibility in a claimant’s version of events to found an adverse credibility determination, provided the implausibility is actual as opposed to illusory (see e.g. Aguebor; Alizadeh v Canada (Minister of Employment and Immigration), [1993] FCJ No 11, 38 ACWS (3d) 361 (CA); Shahamati v Canada (Minister of Employment and Immigration), [1994] FCJ No 415 (CA)). Finally, a witness’ demeanor or manner of testifying may be relied on to ground an adverse credibility finding, but it is preferable it not be the sole basis for such a finding (see e.g. Rahal at paras 42, 45).

[9] Thus, the types of matters relied on by the Board in this case in support of its adverse credibility determination fall well within the sort of matters that can be relied on to reject a witness’ testimony.

[10] The Board placed the greatest weight on its first reason, and, in particular, the lack of detail offered by the applicant and the fact that his story seemed to be rehearsed. The applicant offers no real challenge to this finding other than arguing that it was incorrect, which is no basis to disregard it. Moreover, the transcript does reveal that the applicant’s version of events was extraordinarily sparse, and the Board was in a privileged position to assess the lack of authenticity in the applicant’s demeanor. Thus, the first reason the RPD offered in support of its credibility determination, in my view, is unassailable.

[11] Likewise, the Board did not err in its reliance on the contradictions between the applicant’s PIF and his oral testimony. The applicant asserts that there is no contradiction between the two as he noted his PIF that the PSB went to his close relatives’ homes in their search for him. In my view, this is a different assertion from the claim he made during his testimony, to the effect that the PSB twice conducted a searches of his uncle’s home. Thus, there was a basis for the Board to find a contradiction between the applicant’s testimony and his PIF and the Board’s reliance on the difference between the two is not unreasonable.

[12] The implausibility findings surrounding the allegation that the smuggler kept the applicant’s RIC and the lack of punishment visited on the applicant’s family are similarly reasonable. There is a solid basis for the implausibility of the applicant’s claim that the smuggler kept his RIC as this finding is based on the common sense determination that one would be at risk carrying two different pieces of identification. Likewise, there was support in the objective evidence before the Board for the finding that the Chinese authorities often persecute families of suspected Falun Gong practitioners. Accordingly, the RPD’s determination that lack of persecution of the applicant’s family rendered his version of events unbelievable is reasonable. Similar determinations were upheld in Hou v Canada (Minister of Citizenship and Immigration), 2012 FC 993 at para 36 [Hou] and Li v Canada (Minister of Citizenship and Immigration), 2005 FC 28 at para 4.

[13] As concerns the Board’s treatment of the documents from China filed by the applicant, contrary to what the applicant asserts, the RPD did not discard them solely because of the prevalence of fraudulent documents in China and, thus, this case is distinguishable from Lin v Canada (Minister of Citizenship and Immigration), 2012 FC 157, relied on by the applicant. That said, the finding made by Justice Mactavish in Cao v Canada (Minister of Citizenship and Immigration), 2012 FC 694 [Cao] does appear to apply to this case. In Cao, Justice Mactavish noted that:
There was, however, no evidence before the Board to indicate that Mr. Cao’s immigration consultant had ever told him that Chinese authorities monitor the postal system and track fugitives through a computer network. Nor was there any evidence that either Mr. Cao, a farmer from rural China, or his family would have been aware of this practice. The Board’s finding was based on nothing more than speculation and was thus unreasonable.
These comments are equally applicable here. Therefore, this point in the Board’s reasoning is likely unreasonable.

[14] Finally, insofar as concerns the Board’s treatment of the summons issue, as the applicant correctly notes, a finding that the credibility of a claim for protection from China is undermined by the lack of a PSB summons has been rejected as unreasonable in some recent jurisprudence of this Court (see e.g. Liang v Canada (Minister of Citizenship and Immigration), 2011 FC 65; and Chen v Canada (Minister of Citizenship and Immigration), 2012 FC 545). However, as noted by Justice Zinn in Jiang v Canada (Minister of Citizenship and Immigration), 2012 FC 1067 at paras 20-22, an unreasonable finding with respect to a summons need not be determinative of the entire application for judicial review:
The applicant cites recent decisions of this Court which have held that “a finding by the Board that on a balance of probabilities it would be reasonable to assume that a summons would have been left is a reviewable error[”]: Liang v. Canada (Minister of Citizenship & Immigration), 2011 FC 65 (F.C.) and Chen v. Canada (Minister of Citizenship & Immigration), 2012 FC 545 (F.C.). The respondent submits that the jurisprudence subsequent to Liang indicates that the issue is not as clear cut as suggested and that “each case must be determined on its facts and on how those facts were assessed by the Board[”]: Li v. Canada (Minister of Citizenship & Immigration), 2011 FC 941 (F.C.) and He v. Canada (Minister of Citizenship & Immigration), 2011 FC 1199 (F.C.).
In my view, every case must be assessed based on the evidence before the Board and its assessment of that evidence. With respect to this particular submission, I adopt and agree with the comments of Justice Mosley in Lin v. Canada (Minister of Citizenship & Immigration), 2012 FC 671 (F.C.), at paragraph 10:
The Board drew a negative inference from the lack of a summons in part because the applicant claimed that the PSB had visited his home nine times. Considering the evidence on the uneven enforcement practice of the PSB, this may have been unreasonable (see Weng v Canada (Minister of Citizenship and Immigration), 2011 FC 422 at paras 16-18). However, this one inference was not determinative and is not sufficient to render the entire decision unreasonable.
I find that even if the Board’s finding relating to the lack of a summon is disregarded, there remains a sufficient basis to support the Board’s finding that her story was not to be believed when one applies the test of reasonableness in New Brunswick (Board of Management) v. Dunsmuir, 2008 SCC 9 (S.C.C.), and the deference which the Court must give to the Board’s decision.

[15] I believe these comments apply equally here. Even if one or possibly two of the reasons offered by the Board in support of its credibility determination bear no weight, the bulk of its reasons are solid. Thus, there is no basis to interfere with the RPD’s assessment of the applicant’s lack of credibility, particularly in light of the deference to be afforded to its assessment.
Did the Board err in its assessment of the applicant’s sur place claim?

[16] Turning, then, to the second issue, as noted, the applicant argues that the RPD erred in failing to properly assess his sur place claim and in relying on the lack of a legitimate motive for his practice of Falun Gong in Canada. Neither assertion has merit.

[17] Contrary to what the applicant asserts, the Board did assess the sur place claim and the evidence the applicant tendered in support of his assertion that he was a genuine Falun Gong practitioner in Canada. It simply found this evidence insufficient to establish the genuineness of the claimed practice. There is nothing unreasonable in this conclusion, especially when viewed in light of the determination that the applicant fabricated what had occurred in China. In short, there is nothing unreasonable in finding that a few letters and pictures do not establish that a claimant is a genuine adherent to a religion, especially where, as here, he has lied about being a practitioner in order to make a fraudulent refugee claim. In this regard, I endorse the comment of Justice Pinard in Jin at para 20, that:
[I]t would be absurd to grant a sur place claim every time a pastor provides a letter attesting to an applicant’s membership in his church.

[18] To similar effect, it was not unreasonable for the Board to have assessed and considered the applicant’s motive for practicing Falun Gong as a reason for rejecting his sur place claim. While beginning to practice a religion solely to buttress a refugee claim cannot, in and of itself, be the basis for rejecting a sur place claim, the Board may legitimately have regard to such motive in assessing the genuineness of a claimant’s claimed religious beliefs. In many respects, this case is on all fours with my decision in Hou, where I reviewed and rejected an argument identical to that made by the applicant in this case. Because my reasons in that case apply equally here, I have reproduced a portion of them below:
[C]ontrary to what the applicant claims, Canadian case law does recognise that motive for engaging in a religious practice in Canada may be considered by the RPD in an appropriate case. However, a finding that a claimant was motivated to practice a religion in Canada to buttress a fraudulent refugee claim cannot be used, in and of itself, as a basis to reject the claim. Rather, the finding that the claimant has been motivated by a desire to buttress his or her refugee claim is one factor that may be considered by the RPD in assessing the sincerity of a claimant’s religious beliefs.
The sincerity of those beliefs will be an issue in cases, like the present, where continuing the religious practice in the country of origin might place the claimant at risk. If the beliefs are not genuine, then there is no risk, as a claimant would not practice his or her newly-acquired religion in the country of origin if adherence to the religion is motivated solely by a desire to support a refugee claim. On the other hand, there may well be situations where a claimant might initially have been motivated to join a religion due to these types of motivations, but along the route, may have developed faith and become a true adherent of the religion.
[…]
In a series of recent cases involving claimants from China, this Court has applied the holding in Ejtehadian [v Canada (Minister of Citizenship and Immigration), 2007 FC 158] and held that the Board cannot reject a sur place claim due solely to lack of credibility or improper motive but, rather, must assess the genuineness of the applicant’s religious practice to determine if he or she will be at risk if returned to the country of origin […] In Jin and Wang [v Canada (Minister of Citizenship and Immigration), 2011 FC 614] […] the Board noted the questionable motive for conversion but then went on to assess the genuineness of the applicant’s conversion and found it to be lacking. The Board based its findings on the claimants’ lack of credibility, the fact that they had fabricated stories about being Christians in China and their lack of knowledge of the details of the religion they claimed to practice. Because the claimants were found to not be genuine practitioners, the RPD held they would not practice their claimed religions if returned to China and thus were determined to face no risk. And this Court upheld the Board’s findings in those cases. In short, in circumstances very much like the present, the RPD’s decisions were upheld.
(Hou at paras 61-65.)

[19] It follows that the RPD did not err in considering the applicant’s motive for practicing Falun Gong in Canada nor in its assessment of his sur place claim.

[20] This application will accordingly be dismissed. No question for certification was submitted under section 74 of the IRPA and none arises in this case.


## 23750:2 · paragraphs 21-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d441391983136f03fddb0a88271393e22e9475ce82d3136bc0dcc922cdcac376`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23750:2:subtheme:1 · paragraphs 21-22

- Raw key terms: `application, april, cause, certified, citizenship, costs, court, date`
- Display key terms: `april, certified, costs, date`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: april, certified, costs, date Operative outcome context: This application for judicial review is dismissed; 2. Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5115988` offsets `256-264`; context: No question of general importance is certified; and
3.
- Evidence: `disposition` cue `dismissed` at chunk `5115988` offsets `239-248`; context: This application for judicial review is dismissed;
2.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that:
1. This application for judicial review is dismissed;
2. No question of general importance is certified; and
3. There is no order as to costs.
"Mary J.L. Gleason"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-7356-12
STYLE OF CAUSE: Hao Wen Su v The Minister of Citizenship and Immigration
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: April 24, 2013
REASONS FOR 

## 23750:3 · paragraphs 23-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `85caa2066aa138b9e6fdd0f6877cdf65a4b9e784b2b6c711cce3bc05e716056b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23750:3:subtheme:1 · paragraphs 23-23

- Raw key terms: `appearances, applicant, attorney, barristers, blanshay, canada, dated, deputy`
- Display key terms: `barristers, blanshay, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barristers, blanshay, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 23-23. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: GLEASON J.
DATED: May 17, 2013
APPEARANCES:
Jennifer Luu
FOR THE APPLICANT
Negar Hashemi
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Blanshay & Lewis
Barristers & Solicitors
Toronto, Ontario
FOR THE APPLICANT
William F. Pentney,
Deputy Attorney General of Canada
Toronto, Ontario
FOR THE RESPONDENT
