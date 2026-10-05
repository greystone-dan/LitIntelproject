"""Count the pinpoint forms that really occur in decisions (read-only sampling aid).

Usage: python scripts/sample_pinpoint_forms.py FCA.parquet RPD.parquet [--limit N] [--verify-target FCA.parquet]
Input is any parquet with an ``unofficial_text_en`` column (A2AJ dataset shards).
Classifies each paragraph/page pinpoint into a shape such as ``N``, ``N-N``,
``N,N and N``, ``N ff``, then reports how much of each shape the repo parser
(``backend.citation_refine.pinpoints``) turns into the right set of numbers.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.citation_refine.pinpoints import (  # noqa: E402
	TRAILING_PINPOINT_RE,
	paragraph_pinpoints,
	parse_all_pinpoints,
)

LABEL = r"(?:paragraphs?|paras?\.?|¶¶?|paragraphes?|pars?\.?)"
# Deliberately wider than the parser: numbers, separators and trailing "ff"/"et seq".
CANDIDATE = re.compile(
	rf"(?<![A-Za-z]){LABEL}\s*(?P<body>\d[\d\s,;–—\-and&to(),a-z]{{0,60}})",
	re.IGNORECASE,
)
SEP = re.compile(r"\s*(?:,|;|&|\band\b|\bet\b|\bor\b)\s*", re.IGNORECASE)


def shape(body: str) -> str | None:
	body = re.split(r"\b(?:of|in|the|that|where|which|as|is|was|per|to the)\b", body, maxsplit=0, flags=re.IGNORECASE)[0] if False else body
	ff = re.search(r"\s*\(?\b(ff|et\s+seq|and\s+following|s\.?\s*s?\.?)\b", body, re.IGNORECASE)
	tokens = re.findall(r"\d+(?:\s*(?:[-–—]|\bto\b)\s*\d+)?|,|;|&|\band\b|\bet\b|\bor\b", body, re.IGNORECASE)
	out: list[str] = []
	prev_num = False
	for token in tokens:
		if re.match(r"\d", token):
			if prev_num:
				break
			out.append("N-N" if re.search(r"[-–—]|to", token, re.IGNORECASE) else "N")
			prev_num = True
		else:
			out.append("," if token in {",", ";"} else "and")
			prev_num = False
	while out and out[-1] in {",", "and"}:
		out.pop()
	if not out:
		return None
	text = " ".join(out).replace(" , ", ", ").replace(" ,", ",")
	if ff and ff.group(1).lower() in {"ff", "et seq", "and following"}:
		text += " +ff"
	return text


NEUTRAL = re.compile(r"\b(?:19|20)\d{2} (?:FCA|FC|SCC|FCT|CAF|CF|CSC) \d{1,4}\b")


def classify(raw: str, pins) -> str:
	if pins.open_ended:
		return "ff / et seq"
	if len(pins.paragraphs) == 1:
		return "single"
	has_range = bool(re.search(r"\d\s*(?:[-–—]|to|à)\s*\d", raw))
	has_list = bool(re.search(r",|;|\band\b|\bet\b|&", raw))
	return "range + list" if has_range and has_list else "range" if has_range else "list"


def load_targets(path: str) -> dict[str, set[int]]:
	"""Neutral citation -> paragraph numbers present in that decision ([N] markers at line start)."""
	import pyarrow.parquet as pq

	table = pq.read_table(path, columns=["citation_en", "unofficial_text_en"])
	out: dict[str, set[int]] = {}
	for citation, body in zip(table.column("citation_en").to_pylist(), table.column("unofficial_text_en").to_pylist()):
		if citation and body:
			out[citation] = {int(n) for n in re.findall(r"(?m)^\s*\[(\d{1,4})\]", body)}
	return out


def expected_numbers(body: str) -> set[int]:
	nums: set[int] = set()
	for part in SEP.split(body):
		m = re.match(r"\s*(\d+)(?:\s*(?:[-–—]|to)\s*(\d+))?", part)
		if not m:
			break
		a = int(m.group(1))
		b = int(m.group(2)) if m.group(2) else a
		if b < a or b - a > 200:
			b = a
		nums.update(range(a, b + 1))
	return nums


def main() -> None:
	import pyarrow.parquet as pq

	ap = argparse.ArgumentParser()
	ap.add_argument("files", nargs="+")
	ap.add_argument("--limit", type=int, default=0, help="max decisions per file")
	ap.add_argument("--examples", type=int, default=3)
	ap.add_argument("--verify-target", help="parquet whose decisions are looked up to check cited paragraphs exist")
	args = ap.parse_args()

	forms: Counter[str] = Counter()
	verify = load_targets(args.verify_target) if args.verify_target else {}
	verified: Counter[str] = Counter()
	shapes: Counter[str] = Counter()
	parsed_ok: Counter[str] = Counter()
	examples: dict[str, list[str]] = {}
	decisions = 0
	for name in args.files:
		table = pq.read_table(name, columns=["unofficial_text_en"])
		texts = table.column("unofficial_text_en").to_pylist()
		for text in texts[: args.limit or None]:
			if not text:
				continue
			decisions += 1
			for m in NEUTRAL.finditer(text):
				pin = TRAILING_PINPOINT_RE.match(text[m.end(): m.end() + 80])
				if pin is None:
					continue
				pins = paragraph_pinpoints(pin.group("pinpoint"))
				if pins is None:
					continue
				form = classify(pin.group("pinpoint"), pins)
				forms[form] += 1
				target = verify.get(m.group(0))
				if target is not None:
					for number in pins.paragraphs:
						verified[form + (" found" if number in target else " missing")] += 1
			for m in CANDIDATE.finditer(text):
				s = shape(m.group("body"))
				if s is None:
					continue
				shapes[s] += 1
				got = parse_all_pinpoints(m.group(0))
				got_nums = {v for p in got for v in p.values}
				if got and expected_numbers(m.group("body")) <= got_nums:
					parsed_ok[s] += 1
				else:
					examples.setdefault(s, [])
					if len(examples[s]) < args.examples:
						examples[s].append(" ".join(text[max(0, m.start() - 20): m.end() + 10].split()))
	print(f"decisions={decisions}; paragraph pinpoints that follow a neutral citation: {sum(forms.values())}")
	for form, n in forms.most_common():
		line = f"  {form:22}{n:>7}{n / sum(forms.values()):>8.1%}"
		found, missing = verified[form + " found"], verified[form + " missing"]
		if found + missing:
			line += f"   cited paragraph numbers present in the target decision: {found}/{found + missing}"
		print(line)
	print()
	total = sum(shapes.values())
	print(f"decisions={decisions} pinpoint-like mentions={total}")
	print(f"{'shape':28}{'count':>8}{'share':>8}{'parser ok':>11}")
	for s, n in shapes.most_common(25):
		print(f"{s:28}{n:>8}{n / total:>8.1%}{parsed_ok[s] / n:>11.0%}")
	print("\nparser misses (examples):")
	for s, rows in examples.items():
		if shapes[s] >= 5:
			print(f"[{s}] ({shapes[s] - parsed_ok[s]} misses)")
			for r in rows:
				print("   ", r)


if __name__ == "__main__":
	main()
