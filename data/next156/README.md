# Next 156 FC immigration decisions: frames, issue maps, paragraph notes (13 Oct 2026)
Files only. Nothing loaded. Same row format as data/core150 and data/next158.

- frames.jsonl.gz: 156 rows {citation_key, frame}. Haiku frame v3, checked against the decision text.
- issue_maps.jsonl.gz: 326 issues in 156 decisions, made by hosted qwen3.5-35b-a3b (every row carries review_flags "model_hosted35b"). Clean-up: 7 standard-of-review/costs/remedy issues dropped, 4 result paragraphs moved to the paragraph holding the quote. The old "overall dismissed, so flip allowed to dismissed" rule is NOT applied (it wrongly flipped 2 real issue-level wins). 5 issues carry order_para_only; 25 issues in 15 minister-brought decisions carry minister_applicant.
- paragraph_notes.jsonl.gz: 4,278 notes (4 paragraphs the model marked NONE are left out). Method T03 (qwen3.5-35b-a3b, v12 prompt). Names are not removed.

Blind grades (Haiku grader, 90% intervals): issue maps, 60 decisions / 117 issues: overall result right 59/60, issue result right 96.6% (92.6-98.5), cited paragraph right 98.3% (95.0-99.4), 2 harmful. Notes, 100 random: faithful 87% (80-92), 13% minor, 0 wrong, 0 wrong-speaker. Frames: 60 graded earlier (see thread report).

Load (PC thread, additive, dry run first):
python scripts/load_core150_layers.py --data data/next156 --frame-source next156-haiku-v3 --note-source next156-v12
then add --apply. Undo: same arguments plus --undo. Expect: frames 156 (minus any already present), issue maps 326, notes 4,278.
