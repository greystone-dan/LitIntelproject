# Discussion Units: case 2517

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **27**
- Continuity pairs: **26**
- Discussion Units: **2**
- Paragraph source hashes: **27**
- Sub-themes: **3**

## 2517:1 · paragraphs 0-25

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `08e09bc5b8201ef1fbb8a692345f257ba285907fdd420dd766d1a6c78678b2d1`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2517:1:subtheme:1 · paragraphs 0-10

- Raw key terms: `canada, albania, applicant, applicants, because, decision, family, female`
- Display key terms: `albania, because, family, female`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: albania, because, family, female Rule/authority context: [1] This is an application for judicial review under section 18. Application context: [2] The male applicant and his wife, the female applicant, are both citizens of Albania, the country that they left in March 2001 to come to Canada because of a well-founded fear of persecution by reason of their politic | That year, they were allowed to return to Tirana where they lived with the female applicant's mother because they had been refused housing. Operative outcome context: That year, they were allowed to return to Tirana where they lived with the female applicant's mother because they had been refused housing. | This event prompted him to send his son to Canada, where he has since been granted refugee status. Evidence spans paragraphs 0-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `4184557` offsets `406-416`; context: The panel also found that the applicants were not persons in need of protection pursuant to paragraphs 97(1)(a) and (b) of the Act.
- Evidence: `governing_rule` cue `under` at chunk `4184557` offsets `47-52`; context: [1] This is an application for judicial review under section 18.
- Evidence: `reasoning_application` cue `because` at chunk `4184558` offsets `148-155`; context: [2] The male applicant and his wife, the female applicant, are both citizens of Albania, the country that they left in March 2001 to come to Canada because of a well-founded fear of persecution by reason of their political opinion and their membership in a social group (the family).
- Evidence: `reasoning_application` cue `because` at chunk `4184561` offsets `175-182`; context: That year, they were allowed to return to Tirana where they lived with the female applicant's mother because they had been refused housing.
- Evidence: `disposition` cue `allowed` at chunk `4184561` offsets `95-102`; context: That year, they were allowed to return to Tirana where they lived with the female applicant's mother because they had been refused housing.
- Evidence: `reasoning_application` cue `Because` at chunk `4184563` offsets `4-11`; context: [7] Because of his political activities with the party, he received numerous telephone calls and anonymous letters threatening his life and the lives of his family if he did not put an end to his political activities.
- Evidence: `disposition` cue `granted` at chunk `4184564` offsets `221-228`; context: This event prompted him to send his son to Canada, where he has since been granted refugee status.
- Evidence: `reasoning_application` cue `therefore` at chunk `4184566` offsets `11-20`; context: [10] It is therefore in this context that, fearing for their lives and the lives of their family, the applicants decided to come to Canada, which they managed to do on March 15, 2001.
- Evidence: `disposition` cue `granted` at chunk `4184566` offsets `252-259`; context: At the same time, they sent their daughter to France, where she was granted refugee status.

#### 2517:1:subtheme:2 · paragraphs 11-25

- Raw key terms: `evidence, panel, immigration, minister, canada, applicants, court, decision`
- Display key terms: `none`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: no filtered content terms Position/evidence statements: If he had indeed felt that his life was in danger in August 1999, he would certainly not have continued to expose himself to such a risk; - the applicant arrived in Canada on March 15, 2001, but did not claim refugee pro Rule/authority context: Standard of review | [14] The standard of review in matters of questions of fact is the test of patent unreasonableness. Application context: [11] After analysing all of the evidence -testimonial as well as documentary -the panel determined that neither the applicant or his wife were refugees or "persons in need of protection", for the following reasons: - The | The application for judicial review must therefore be dismissed. Operative outcome context: The application for judicial review must therefore be dismissed. | [15] At the hearing, the applicants alleged that the panel should have granted their claim because their son and their daughter were granted refugee status based on their story. Evidence spans paragraphs 11-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUE` at chunk `4184567` offsets `2930-2935`; context: ISSUE
- Evidence: `party_position` cue `claim` at chunk `4184567` offsets `2688-2693`; context: If he had indeed felt that his life was in danger in August 1999, he would certainly not have continued to expose himself to such a risk;
- the applicant arrived in Canada on March 15, 2001, but did not claim refugee protection until March 22.
- Evidence: `evidence_fact` cue `evidence` at chunk `4184567` offsets `32-40`; context: [11] After analysing all of the evidence -testimonial as well as documentary -the panel determined that neither the applicant or his wife were refugees or "persons in need of protection", for the following reasons:
- The claimant's testimony is so full of inconsistencies, hesitations and changes that it is not reliable;
- during the whole time he was testifying, his wife was whispering answers in his ear, despite being warned several times by the panel;
- he wrote that he had been arrested and roughed up, but at the hearing he had to correct himself and say that he had not been arrested but only roughed up by secret service agents;
- the claimant clearly stated that his problems as a member of the Democratic Party began in 1997 because of the fact that he organized meetings at the university and had a very big influence on the students.
- Evidence: `reasoning_application` cue `because` at chunk `4184567` offsets `738-745`; context: [11] After analysing all of the evidence -testimonial as well as documentary -the panel determined that neither the applicant or his wife were refugees or "persons in need of protection", for the following reasons:
- The claimant's testimony is so full of inconsistencies, hesitations and changes that it is not reliable;
- during the whole time he was testifying, his wife was whispering answers in his ear, despite being warned several times by the panel;
- he wrote that he had been arrested and roughed up, but at the hearing he had to correct himself and say that he had not been arrested but only roughed up by secret service agents;
- the claimant clearly stated that his problems as a member of the Democratic Party began in 1997 because of the fact that he organized meetings at the university and had a very big influence on the students.
- Evidence: `evidence_fact` cue `evidence` at chunk `4184568` offsets `95-103`; context: [12] Is the panel's decision patently unreasonable or was it made without regard to all of the evidence before it?
- Evidence: `governing_rule` cue `Standard of review` at chunk `4184569` offsets `121-139`; context: Standard of review
- Evidence: `reasoning_application` cue `therefore` at chunk `4184569` offsets `97-106`; context: The application for judicial review must therefore be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4184569` offsets `110-119`; context: The application for judicial review must therefore be dismissed.
- Evidence: `evidence_fact` cue `evidence` at chunk `4184570` offsets `266-274`; context: 315, the Court said that the findings of fact and credibility must be supported by the evidence.
- Evidence: `governing_rule` cue `standard of review` at chunk `4184570` offsets `9-27`; context: [14] The standard of review in matters of questions of fact is the test of patent unreasonableness.
- Evidence: `evidence_fact` cue `found that` at chunk `4184571` offsets `224-234`; context: However, the panel addressed this element and found that the claim of another family member in another case has little bearing, since the panel makes its decision on the facts in the record.
- Evidence: `reasoning_application` cue `because` at chunk `4184571` offsets `91-98`; context: [15] At the hearing, the applicants alleged that the panel should have granted their claim because their son and their daughter were granted refugee status based on their story.
- Evidence: `counterargument_limitation` cue `However` at chunk `4184571` offsets `178-185`; context: However, the panel addressed this element and found that the claim of another family member in another case has little bearing, since the panel makes its decision on the facts in the record.
- Evidence: `disposition` cue `granted` at chunk `4184571` offsets `71-78`; context: [15] At the hearing, the applicants alleged that the panel should have granted their claim because their son and their daughter were granted refugee status based on their story.
- Evidence: `disposition` cue `dismissed` at chunk `4184572` offsets `73-82`; context: [16] The concept of family unity in matters involving refugee claims was dismissed once again by Nadon J.
- Evidence: `evidence_fact` cue `evidence` at chunk `4184573` offsets `171-179`; context: Assessment of the evidence as a whole
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4184573` offsets `5-16`; context: [17] Accordingly, the applicants' argument, that the panel should have granted their claim because their son had been granted refugee status, must fail.
- Evidence: `disposition` cue `granted` at chunk `4184573` offsets `71-78`; context: [17] Accordingly, the applicants' argument, that the panel should have granted their claim because their son had been granted refugee status, must fail.
- Evidence: `evidence_fact` cue `evidence` at chunk `4184574` offsets `41-49`; context: [18] It is clear that the panel took the evidence, as a whole, into consideration.
- Evidence: `evidence_fact` cue `evidence` at chunk `4184575` offsets `266-274`; context: Preferred evidence
- Evidence: `reasoning_application` cue `therefore` at chunk `4184575` offsets `24-33`; context: [19] The panel did not, therefore, err on this point and it was up to the applicants to fill the evidentiary gap, if need be, because the burden of proof lies on the applicants: Chan v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4184576` offsets `291-299`; context: However, it is worth mentioning that the documentary evidence bearing on the general situation existing in the country of a claimant is not sufficient, in itself, to establish the merits of the claim.
- Evidence: `reasoning_application` cue `conclude` at chunk `4184576` offsets `902-910`; context: In the absence of such evidence, the Board members were entitled to conclude as they did.
- Evidence: `counterargument_limitation` cue `However` at chunk `4184576` offsets `238-245`; context: However, it is worth mentioning that the documentary evidence bearing on the general situation existing in the country of a claimant is not sufficient, in itself, to establish the merits of the claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4184577` offsets `60-68`; context: [21] The panel also has the power to accept the documentary evidence that it prefers when the evidence before it contains discrepancies: Tawfik v.
- Evidence: `evidence_fact` cue `testimony` at chunk `4184578` offsets `443-452`; context: This Court has previously held that the panel may take into account the demeanor of an applicant during his testimony.
- Evidence: `evidence_fact` cue `evidence` at chunk `4184579` offsets `83-91`; context: [23] As this is a decision concerning the assessment of the facts and, without any evidence of the "unreasonableness" of the decision, I do not see how the Court could justify its intervention.
- Evidence: `evidence_fact` cue `evidence` at chunk `4184580` offsets `117-125`; context: The applicants have not presented any evidence that would support a finding that the panel made a patently unreasonable decision.

#### Section text

Gjergo v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2004-03-01
Neutral citation
2004 FC 303
File numbers
IMM-4592-03
Decision Content
Date: 20040301
Docket: IMM-4592-03
Citation: 2004 FC 303
BETWEEN:
GJERGJI GJERGO
DRITA BALLUKU GJERGO
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER
HARRINGTON J.
INTRODUCTION

[1] This is an application for judicial review under section 18.1 of the Federal Court Act, R.S.C. 1985, c. F-7, as amended, of a decision by the Refugee Protection Division of the Immigration and Refugee Board (panel), dated May 23, 2003, that the applicants were not Convention refugees within the meaning of section 96 of the Immigration and Refugee Protection Act (hereinafter the Act). The panel also found that the applicants were not persons in need of protection pursuant to paragraphs 97(1)(a) and (b) of the Act.
FACTUAL BACKGROUND

[2] The male applicant and his wife, the female applicant, are both citizens of Albania, the country that they left in March 2001 to come to Canada because of a well-founded fear of persecution by reason of their political opinion and their membership in a social group (the family). They allege that they are "persons in need of protection" in that they are in danger of being subjected to torture within the meaning of the first section of the Convention against Torture, to a risk to their life or to a risk of cruel and unusual treatment or punishment if they were to return to their country.

[3] In 1974, the female applicant's father, who was, at the time, Minister of Defence and Deputy Prime Minister of Albania, was accused of being an enemy of the people and was assassinated.

[4] The male applicant, who was then a university professor, was pressured by the academic council to divorce his wife, which he refused to do. His career as a professor was then put to an end, he and his wife lost the benefit of their diplomas, and the Minister of the Interior transferred them to Mirdite, in northern Albania, at the end of 1974, where they became ordinary workers.

[5] They were then transferred to Kurbnesh, where they stayed until 1990. That year, they were allowed to return to Tirana where they lived with the female applicant's mother because they had been refused housing.

[6] After the fall of the Communist regime, the male applicant became a member of the Democratic Party, as of August 15, 1991. He participated in the party's meetings and rallies. When the party came into power, he obtained a position at the faculty of medicine of the University of Tirana.

[7] Because of his political activities with the party, he received numerous telephone calls and anonymous letters threatening his life and the lives of his family if he did not put an end to his political activities.

[8] In 1997, the Communists came back into power and, in April 1999, he was mistreated by secret service agents and plainclothes police officers. This event prompted him to send his son to Canada, where he has since been granted refugee status.

[9] In November 2000, his daughter was raped by individuals who identified themselves as being from the Socialist Party. On March 8, 2001, while he was leaving a Party meeting in the company of a colleague, shots were fired in his direction, but he was not hit.

[10] It is therefore in this context that, fearing for their lives and the lives of their family, the applicants decided to come to Canada, which they managed to do on March 15, 2001. At the same time, they sent their daughter to France, where she was granted refugee status.
IMPUGNED DECISION

[11] After analysing all of the evidence -testimonial as well as documentary -the panel determined that neither the applicant or his wife were refugees or "persons in need of protection", for the following reasons:
- The claimant's testimony is so full of inconsistencies, hesitations and changes that it is not reliable;
- during the whole time he was testifying, his wife was whispering answers in his ear, despite being warned several times by the panel;
- he wrote that he had been arrested and roughed up, but at the hearing he had to correct himself and say that he had not been arrested but only roughed up by secret service agents;
- the claimant clearly stated that his problems as a member of the Democratic Party began in 1997 because of the fact that he organized meetings at the university and had a very big influence on the students. However, he had neglected to say that he had retired from the university in 1993. When he was confronted with that fact, he said that officially he had retired, but he was still at the university. The panel rejected that explanation, since it is obvious that the claimant made it up to get out of a tight spot;
- the applicant also stated that at demonstrations that he had organized for the Party, he was the first to speak against the government of the Socialist Party. This is an important fact that is not in his PIF. When that was pointed out to him, he said he had not wanted to write a long text and then said, [TRANSLATION] "It is for lack of experience." The panel rejected that explanation, because he could have easily said so in his PIF, where he had written a six-and-a-half-page narrative;
- after the attack in 1999, he and his wife decided to send their son and daughter away to the town of Korca in Albania. He said that he had understood that the attackers had put the names of his son and daughter on a blacklist. But this detail is not in his PIF. When the panel pointed this out to him, he could not give an explanation and simply said it was because of a lack of experience, an explanation which, according to the panel, did not bear examination and which the panel rejected;
- on the matter of subjective fear, according to his testimony, he was the main person targeted in the family, but he said he sent his son and daughter away and stayed in Albania, with his wife, until March 2001. He had trouble justifying this position and he gave a vague explanation that he had thought democracy would finally win out. If he had indeed felt that his life was in danger in August 1999, he would certainly not have continued to expose himself to such a risk;
- the applicant arrived in Canada on March 15, 2001, but did not claim refugee protection until March 22. When asked why, he simply said he had not known how to go about it, even though, on arriving in Canada, they went to stay with his wife's brother and with their own son, who is in Canada as a refugee.
ISSUE

[12] Is the panel's decision patently unreasonable or was it made without regard to all of the evidence before it?
ANALYSIS

[13] The panel's decision is not patently unreasonable. The application for judicial review must therefore be dismissed.
Standard of review

[14] The standard of review in matters of questions of fact is the test of patent unreasonableness. In Aguebor v. Canada (Minister of Employment and Immigration) (1993), 160 N.R. 315, the Court said that the findings of fact and credibility must be supported by the evidence. Russell J. in Ramachanthran v. Canada (Minister of Citizenship and Immigration), 2003 FCT 673, at paragraph 51, wrote:
The Court must show significant deference to findings of fact made by a panel of the Refugee Division. The standard of review of decisions of the Refugee Division is generally patent unreasonableness except for questions involving the interpretation of a statute, in which case, the standard becomes one of correctness.

[15] At the hearing, the applicants alleged that the panel should have granted their claim because their son and their daughter were granted refugee status based on their story. However, the panel addressed this element and found that the claim of another family member in another case has little bearing, since the panel makes its decision on the facts in the record. I agree with this reasoning, because the facts of these other cases are not before the Court. The judicial review is concerned with the applicants' refugee status, not that of their children. Nadon J.A. in Rahmatizadeh v. Canada (Minister of Employment and Immigration), [1994] F.C.J. No. 578 (QL) wrote at paragraph 8:
Before concluding, however, I would like to make the following comments. In paragraph 31 of his memorandum, the applicant asserts that the Refugee Division accepted his sister's refugee claim on April 9, 1992. The mere fact of proving that his sister had been found to be a refugee does not carry a lot of weight, since the members of the Division who made that decision made it on the basis of the facts in the record. Why did the applicant not call his sister and brother-in-law to testify to establish that he is of Kurdish nationality? The Division was not bound by a decision made by another panel since it may be that the other panel made an incorrect decision. [Emphasis added]

[16] The concept of family unity in matters involving refugee claims was dismissed once again by Nadon J.A., writing in Bromberg v. Minister of Citizenship and Immigration (2002), 224 F.T.R. 176, at paragraph 35:
. . . He concluded that the principle of family unity does not relieve a claimant of the onus of demonstrating that he falls within the definition of "Convention refugee" set out in subsection 2(1) of the Act.

[17] Accordingly, the applicants' argument, that the panel should have granted their claim because their son had been granted refugee status, must fail.
Assessment of the evidence as a whole

[18] It is clear that the panel took the evidence, as a whole, into consideration. The fact that the panel did not give their evidence as much weight as the applicants would have liked is not sufficient to warrant the intervention of the Court. It is clear, according to Canada (Minister of Employment and Immigration) v. Hundal (1994), 167 N.R. 75, that the panel need not mention, in its decision, every piece of evidence that it has before it.

[19] The panel did not, therefore, err on this point and it was up to the applicants to fill the evidentiary gap, if need be, because the burden of proof lies on the applicants: Chan v. Canada (Minister of Employment and Immigration), [1995] 3 S.C.R. 593.
Preferred evidence

[20] The applicants allege that the panel did not consider exhibit A-3.15, "Albania: Opinions of three specialists on a series of questions related to the current situation in Albania", which describes the political situation in Albania. However, it is worth mentioning that the documentary evidence bearing on the general situation existing in the country of a claimant is not sufficient, in itself, to establish the merits of the claim. In Sinora v. Canada (Minister of Employment and Immigration), (1993) 66 F.T.R. 113, Noël J. wrote the following:
It is settled law that an applicant must demonstrate an objective and subjective fear of persecution. In this case, it was not sufficient simply to file documentary evidence. It was necessary at the very least to establish that the applicant himself had a real fear of persecution. In the absence of such evidence, the Board members were entitled to conclude as they did.

[21] The panel also has the power to accept the documentary evidence that it prefers when the evidence before it contains discrepancies: Tawfik v. Canada (Minister of Employment and Immigration) (1993), 137 F.T.R. 43.
Behaviour of the applicants

[22] The applicants contest the fact that the panel pointed out that the female applicant "was whispering" the answers to the male applicant when he was having difficulty testifying. Upon review of the hearing transcript, it is clear that the female applicant intervened several times to help the male applicant in relating the facts. This Court has previously held that the panel may take into account the demeanor of an applicant during his testimony. When the witness has difficulty giving adequate and direct answers, the panel may make a negative credibility finding. In Grinevich v. Canada (Minister of Citizenship and Immigration), [1997] F.C.J. No. 444 (QL), Pinard J. wrote:
In addition to noting the unsatisfactorily explained contradiction between the PIF and the applicants' oral testimony, the Tribunal noted the demeanour, lack of spontaneity and uncooperative behaviour of the applicants as factors contributing to its assessment that their account of the events they suffered in Israel lack credibility. It is well established that the Board is entitled to draw negative credibility inferences from such factors, and that unless the credibility finding is unreasonable, this Court ought not to interfere.

[23] As this is a decision concerning the assessment of the facts and, without any evidence of the "unreasonableness" of the decision, I do not see how the Court could justify its intervention.
CONCLUSION

[24] For all of these reasons, I dismiss this application for judicial review. The applicants have not presented any evidence that would support a finding that the panel made a patently unreasonable decision.
"Sean Harrington"
Judge
Ottawa, Ontario
March 1, 2004
Certified true translation
Kelley A. Harvey, BA, BCL, LLB
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-4592-03
STYLE OF CAUSE: GJERGJI GJERGO
DRITA BALLUKU GJERGO
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: MONTRÉAL, QUEBEC
DATE OF HEARING: FEBRUARY 24, 2004
REASONS FOR 

## 2517:2 · paragraphs 26-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e8ba27b6f8744f378926cc28a30ae804eb3b3f737dd5ba5aefe3bb7b18c16212`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2517:2:subtheme:1 · paragraphs 26-26

- Raw key terms: `appearances, applicant, arpin, attorney, canada, danielle, date, deputy`
- Display key terms: `arpin, danielle, date, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: arpin, danielle, date, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 26-26. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER BY: HARRINGTON J.
DATE OF REASONS: MARCH 1, 2004
APPEARANCES:
Danielle Arpin FOR THE APPLICANT
Michel Joubert FOR THE RESPONDENT
SOLICITORS OF RECORD:
Danielle Arpin FOR THE APPLICANT
Montréal, Quebec
Morris Rosenberg FOR THE RESPONDENT
Deputy Attorney General
of Canada
