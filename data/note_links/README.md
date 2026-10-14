# Stored "possibly the same point" links between paragraph notes (14 Oct 2026)
Files only. Nothing loaded. Table paragraph_note_links (migration 0049) and scripts/load_note_links.py are already on main.

links.jsonl.gz: 9,488 links, one JSON object per line {citation_key, para, other_citation_key, other_para, score}. A link points from the note on (decision, paragraph) to a note in a DIFFERENT decision. 6,272 of the 12,578 notes carry a link (at most 2 each); 463 of 464 decisions have at least one.

How they were made (once, at ingest; no model runs at site use): the 8 best word-match candidates per note (BM25, other decisions only) were scored 0-10 by a hosted model (qwen3.5-35b-a3b, US$1.55 for all 12,578 notes) for "makes the same legal point". Kept: score 8 or higher (989 of 9,488 at 8-9, the rest 10), best two per note. Dropped: queries where every candidate got the same score (3,401, no better than word match), identical-text pairs, and pairs where either note is boilerplate by keyword (standard of review, "grants the application", certification, remittal wording): 1,442 queries and 1,254 candidates.

Blind grades (Haiku, 90% intervals, pairs of notes only):
- First sample, 150 links before the boilerplate filter: same point 60% (53-66), same or closely related 98%; 23% judged too generic to help.
- Fresh 60 links after the filter (not used to tune it): same point 60% (49-70), same or close 92% (84-96), clearly unrelated 8% (5 of 60), still 23% generic. The keyword filter removed generic pairs in the first sample but did not carry over to new ones.

So: about 6 in 10 shown links are the same point, about 3 in 10 are a related point, about 1 in 12 is wrong. Show them as "Related paragraphs in other decisions (automatic, may differ)", not as "same point". Rank 1 and rank 2 links grade about the same.

Load (PC thread; additive; dry run first): python scripts/load_note_links.py   then add --apply. Undo: python scripts/load_note_links.py --undo --apply (removes only source links-v1) or DROP TABLE paragraph_note_links. Needs the notes loaded first (all 12,578 are).
