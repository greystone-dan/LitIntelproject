# Whose-position rules: scoring and changes (2026-10-10)

Rules: `backend/position_holder.py` (plain regular expressions, no model, no database). Scorer: `scripts/eval_position_rules.py`.
Labels: `data/eval/position_gold_reader.json` (452 paragraphs in 108 decisions, from the QA readers' corrected holders and the wide-run reader labels; a reader, not a lawyer) and `data/eval/position_gold_ai.json` (4,636 paragraphs in 100 decisions; gpt-4.1-mini holders, noisier). Both hold labels only: `scripts/fetch_position_texts.py` re-reads the decision texts from the public pages.

Split: by decision (sha1 of the case id), 30% held out (`split_of`). Rules were developed on `train` only.
Metric: per paragraph, the set of holders the rules found against the labelled set; micro F1 over all holders and over the non-court holders (the part that tells a reader whose argument it is).

## Result

| Set | Decisions | Non-court F1 before | after | Micro F1 before | after |
|---|---|---|---|---|---|
| Reader grades, train | 75 | 0.585 | 0.618 (+0.033, 95% CI +0.012 to +0.060) | 0.698 | 0.713 |
| AI tags, train | 61 | 0.513 | 0.546 (+0.033, CI +0.019 to +0.047) | 0.703 | 0.715 |
| Reader grades, held out | 33 | 0.587 | 0.592 (+0.004, CI -0.022 to +0.029) | 0.736 | 0.737 |
| AI tags, held out | 39 | 0.489 | 0.487 (-0.002, CI -0.017 to +0.014) | 0.696 | 0.694 |

**The gain is shown on the training decisions only. On the held-out decisions it is flat (no measurable gain, no measurable loss).** The held-out set happens to hold only 3 Supreme Court decisions (114 AI-labelled paragraphs against 1,150 in train), and the biggest fix below is for appeal courts, so it could not show there. Where the held-out set has appeal-court decisions it moves the right way: Federal Court of Appeal non-court F1 0.354 to 0.396 (AI tags) and 0.595 to 0.632 (reader grades). Federal Court reader grades dip (0.684 to 0.615 on 6 decisions, within noise; the AI tags show 0.538 to 0.532 on 9). RPD and RAD are unchanged because none of the changes target them. A fresh held-out set with more Supreme Court and Federal Court of Appeal decisions graded by readers is what would settle it.

## What changed

1. **Courts below are earlier decision makers (Supreme Court and Federal Court of Appeal decisions).** "The Federal Court of Appeal found", "Gagnon J.A. concluded", "the trial judge accepted" were read as an authority. Now they are the earlier decision maker unless the sentence is about another case ("In R. v. X, 2020 SCC 34, the Court of Appeal held"). Earlier decision maker F1 on the train AI tags 0.442 to 0.534, on the reader grades 0.521 to 0.582.
2. **A sentence starting "The Officer ...", "The Commission ..." was missed** because the pattern only matched a lowercase "the". Fixed.
3. **Header court name:** a Supreme Court judgment whose header says "On appeal from the Federal Court of Appeal" was read as a Federal Court of Appeal decision. The court named first in the header now wins (`detect_forum`, `case_frame._detect_court`).
4. **"I agree with the Respondent that ..."** keeps the court as the speaker and adds the party whose position it endorses (the QA finding that winning Crown arguments looked like bare submissions).
5. **A citation counts as an authority only in the court's own sentence.** A citation inside a party's or the earlier decision maker's sentence supports that holder's point. Authority F1 up on both label sets (0.565 to 0.590 reader, 0.535 to 0.550 AI, train).
6. **More argument verbs after a named party:** takes issue, challenges, alleges, urges, notes, disagrees, requests, maintains.
7. **Paragraph numbering "1." at the start of a line** is read when a text has no bracketed numbers (memoranda and factums; the QA readers saw such a document go untagged). A numbered list inside a paragraph is skipped because the numbers must climb from 1.
8. **Dissent and concurrence detector** (`backend/opinion_parts.py`, from PR 443's helper, with its tests): reads the headnote and part headings. On the 14 Supreme Court decisions in these sets it found a dissent in all 7 whose headnote says "dissenting" and none in the other 7. `scripts/build_position_layers.py` now writes `"o": "dissenting"` (or "concurring") on those paragraphs so a dissent is never read as the Court's holding. The reader does not show it yet.

## Tried and dropped
- The first-instance body (RPD, Immigration Division) as the subject of any verb in an appeal tribunal's decision: no gain, and it read "The RPD was correct in finding" as the RPD's own finding.
- Treating "reasonably found", "did not err" as the court's evaluation only: the readers' corrected labels keep the earlier decision maker in those sentences, so it lost recall.
- Requiring a law-statement wording before an authority tag: cost as many true authority paragraphs as it removed.

## Known limits
- French decisions are not covered (about 0.7% of the library). Cue words are English.
- Narration about a party ("Ms. Dow filed a complaint") stays the court's voice; the AI tags often call it the party's. The readers' labels are mixed on this, so no rule was written.
- The reader set is small (about 450 paragraphs); changes under about 0.02 are inside the noise. Re-run after any rule change: `python scripts/eval_position_rules.py --gold data/eval/position_gold_reader.json --gold data/eval/position_gold_ai.json --texts position_texts --split test`.
