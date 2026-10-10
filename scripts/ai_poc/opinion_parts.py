"""Majority, concurring and dissenting parts of a decision, found by code from the text's own markers.

Supreme Court texts carry a headnote ("Held (Côté J. dissenting): The appeal should be dismissed.") and part
headings ("Reasons for Judgment: (paras. 1 to 73)", "Joint Dissenting Reasons: (paras. 74 to 143)"), or, without
ranges, the same headings in order followed by "The judgment of ... was delivered by" / "The reasons of ... were
delivered by" lines. Without this, the blocks call reads the dissent (which comes last) as the Court's conclusion:
in the batch-4 run all five split SCC decisions reported the dissent's result as the holding.

No model, no database. ``opinion_parts(text)`` returns {"held": str | None, "parts": [{"kind", "label", "start", "end"}]}
with paragraph numbers inclusive; ``part_of(parts, n)`` gives the kind for a paragraph, "majority" when no parts are known.
"""
from __future__ import annotations

import re

_HELD = re.compile(r"^\s*Held\b[^\n]{0,400}", re.M)
_RANGED = re.compile(r"^\s*((?:Joint\s+)?(?:Dissenting|Concurring|Partially Dissenting|Partly Dissenting)\s+Reasons|Reasons for Judgment)\s*:?\s*\(paras?\.?\s*(\d+)\s*(?:to|-|–)\s*(\d+)\)", re.M | re.I)
_PLAIN = re.compile(r"^\s*((?:Joint\s+)?(?:Dissenting|Concurring|Partially Dissenting|Partly Dissenting)\s+Reasons|Reasons for Judgment)\s*:?\s*$", re.M | re.I)
_DELIVERED = re.compile(r"^(?:English version of )?(?:the (?:judgment|reasons) of .{3,200}? (?:was|were) delivered by|the following are the reasons delivered by|the judgment of the Court was delivered by)\s*$", re.M | re.I)
_PARA = re.compile(r"\[(\d{1,4})\]\s")


def _kind(label: str) -> str:
	l = label.lower()
	if "dissent" in l:
		return "dissenting"
	if "concur" in l:
		return "concurring"
	return "majority"


def opinion_parts(text: str) -> dict:
	text = text or ""
	held = _HELD.search(text)
	out = {"held": " ".join(held.group(0).split()) if held else None, "parts": []}
	ranged = list(_RANGED.finditer(text))
	if ranged:
		for m in ranged:
			out["parts"].append({"kind": _kind(m.group(1)), "label": m.group(1).strip(), "start": int(m.group(2)), "end": int(m.group(3))})
		return out
	labels = [m.group(1).strip() for m in _PLAIN.finditer(text)]
	starts = []
	for m in _DELIVERED.finditer(text):
		nxt = _PARA.search(text, m.end())
		if nxt:
			starts.append(int(nxt.group(1)))
	if len(starts) >= 2 and len(labels) == len(starts):
		last = max((int(m.group(1)) for m in _PARA.finditer(text)), default=starts[-1])
		for i, (label, start) in enumerate(zip(labels, starts)):
			end = starts[i + 1] - 1 if i + 1 < len(starts) else last
			out["parts"].append({"kind": _kind(label), "label": label, "start": start, "end": end})
	return out


def part_of(parts: list[dict], n: int) -> str:
	for p in parts:
		if p["start"] <= n <= p["end"]:
			return p["kind"]
	return "majority"


def describe(info: dict) -> str:
	"""One line for a prompt: which paragraphs are the majority and which a dissent or concurrence, plus the headnote."""
	parts = info.get("parts") or []
	if not parts and not info.get("held"):
		return ""
	bits = [f"{p['kind']} paras {p['start']}-{p['end']}" for p in parts]
	line = "Opinion parts: " + "; ".join(bits) + ". " if bits else ""
	if info.get("held"):
		line += f"Headnote: {info['held']} "
	if any(p["kind"] != "majority" for p in parts):
		line += ("The Court's holding and conclusions are the MAJORITY's only. Points from concurring or dissenting paragraphs "
			"describe those judges' view, not the Court's: give them holder 'other' and start their text with 'Dissent:' or 'Concurrence:'.")
	return line.strip()
