"""Code-only paragraph clean-up before any model call: split a paragraph at an embedded "[n]" marker that starts the decision's own next numbered
paragraph, and strip headings glued on the end of a paragraph (carried as 'heading_after' / 'heading_before'). No model, no database.
Test: python split_paras.py --reports-dir <dir> [--show 8]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


MARK = re.compile(r"(?:(?<=\s)|^)\[(\d{1,3})\](?=\s)")
# a heading glued on the end of a sentence: roman numeral / letter / number outline, or a capitalised one-word banner
HEAD = re.compile(r"(?<=[.!?)\"”’])\s+((?:[IVX]{1,4}\.|[A-Z]\.|\d{1,2}\.)\s+[A-Z][^.\[\]]{2,90}?|(?:[A-Z][A-Z’' ,-]{3,40}))\s*$")
HEAD_IN = re.compile(r"(?<=[.!?)\"”’])\s+((?:[IVX]{1,4}\.|[A-Z]\.)\s+[A-Z][^.\[\]]{2,90}?|(?:[A-Z][A-Z’' ,-]{3,40}))\s*$")


def split_heading(text: str) -> tuple[str, str]:
	m = HEAD.search(text)
	if m and len(m.group(1).split()) <= 14:
		return text[:m.start()].rstrip(), m.group(1).strip()
	return text, ""


def resplit(paras: list[dict]) -> list[dict]:
	"""paras: [{paragraph_index, text}] -> same shape, plus heading_before / split_from fields."""
	have = {p["paragraph_index"] for p in paras}
	out: list[dict] = []
	pending_head = ""
	for p in paras:
		idx, text = p["paragraph_index"], p["text"]
		cuts = []
		for m in MARK.finditer(text):
			n = int(m.group(1))
			if m.start() > 0 and idx < n <= idx + 6 and n not in have:
				cuts.append((m.start(), m.end(), n))
		segs, start, cur = [], 0, idx
		for s, e, n in cuts:
			segs.append((cur, text[start:s]))
			start, cur = e, n
		segs.append((cur, text[start:]))
		for i, (num, seg) in enumerate(segs):
			seg, head = split_heading(seg.strip())
			row = {"paragraph_index": num, "text": seg}
			if pending_head:
				row["heading_before"] = pending_head
			if i > 0:
				row["split_from"] = idx
			out.append(row)
			pending_head = head
	return out
