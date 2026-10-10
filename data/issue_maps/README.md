# Issue maps for Live Analysis

`issue_maps.jsonl.gz` holds 2,670 decided issues from 849 public decisions (2005 and later, immigration), one JSON object per line:
source key, live case id (when known), citation, court, the issue, the applicant's position, who won, the result paragraph number and text, and the plain-language questions written for it.

The issues were mapped by a language model once, at ingest, from public decisions, and every quoted result sentence was checked by code against the decision text. They are stored as ordinary data: no model runs when someone uses the site.

Load with `python scripts/load_issue_maps.py` (dry run) then `--apply`. Undo: `DROP TABLE issue_map_questions; DROP TABLE issue_maps;`.
Method and test results: `ai_poc_wide/rerank_test/stage2/` and the wide-run report.
