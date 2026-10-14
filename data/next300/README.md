# Next 300: FCA and SCC immigration decisions, 2005 onward (14 Oct 2026)
Files only. Nothing loaded. Same row format as data/next156 and data/note_links. SCC maps and SCC notes are HELD (not in these files).

- frames.jsonl.gz: 299 rows {citation_key, frame} (276 FCA, 23 SCC). Haiku frame v3 (4 SCC frames re-made with extra SCC rules), checked against the decision text.
- issue_maps.jsonl.gz: 623 issues in 276 FCA decisions, hosted qwen3.5-35b-a3b, second run with the party names given to the model. Every row carries review_flags "model_hosted35b"; 92 decisions also carry minister_applicant; 6 issues carry order_para_only. Clean-up: 26 standard-of-review / certify / costs issues dropped, 8 result paragraphs moved to the paragraph holding the quote. No direction flip.
- paragraph_notes.jsonl.gz: 13,309 FCA notes (prompt v12a: appeal-court wording). Names are not removed.
- links.jsonl.gz: 10,065 "possibly the same point" links from 6,888 new FCA notes to notes in other decisions (old library notes included), score 8 or higher, best two per note. Same method as data/note_links (BM25 candidates, hosted scoring; uniform-score, identical and boilerplate pairs dropped).

Blind grades (Sonnet strict for frames/maps/notes, Haiku for links; 90% intervals):
- Frames, FCA 80: parties, levels, subject 100%; issues right 91%; challenged part 98%; arguments precision 97%, recall 92%. SCC 23: parties/levels/subject 100%, issues 100%, challenged 91%, precision 99%, recall 92%.
- Maps, FCA 60 decisions: overall result right 59/60; issue result right 90% (85-94%); cited paragraph supports 100%. 18 extra hard cases: overall right 15 of 18.
- Notes, FCA 150: faithful 82% ok, 17% minor, 1.3% wrong (0.4-3.9%); speaker right 94.7%.
- Links, FCA 60: same point 63% (53-73), same or closely related 100%, unrelated 0% (0-4), generic 17% (10-26).

Held and why: SCC notes (158 graded: 7.6% wrong, and 13 of 28 minority-opinion paragraphs shown as "The Court"); SCC maps (issue result right 85.5%, overall result right only 19 of 23, 1 in 10 issues harmful).
Limits: SCC reasons rarely recite party submissions, so respondent and intervener arguments in SCC frames are thin; some frame "arguments" are the court's own framing; the map and note layers are model output and may be wrong. Show links as "Related paragraphs in other decisions (automatic, may differ)".

Load (PC thread; additive; dry run first; each step has its own label and undo):
1. python scripts/load_core150_layers.py --data data/next300 --frame-source next300-haiku-v3 --note-source next300-v12a   (add --apply). Undo: same plus --undo --apply. Expect frames 299, issue maps 623, notes 13,309 (minus any decision already present).
2. python scripts/load_note_links.py --data data/next300/links.jsonl.gz --source links-v2   (add --apply). Needs step 1 first. Undo: same plus --undo --apply.
