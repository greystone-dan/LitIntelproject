"""Run the synthetic Live Analysis documents and score them against expected.json (read-only, nothing stored).

Usage: python scripts/run_live_analysis_mocks.py [folder] [--no-library]
The default folder is tests/live_analysis_mocks; the long speed document (03) lives in
/mnt/project-files/live-analysis/mock-docs and is only scored when it is in the folder given.
"""
import json
import sys
import time
from pathlib import Path

from backend.live_analysis import paragraphs_from_pasted_text
from backend.live_reader import build_live_reader_payload

def score(directory, session):
	d = Path(directory)
	report = []
	expected = json.loads((d / "expected.json").read_text())
	total_pass = total = 0
	for name, exp in expected.items():
		if name.startswith("_") or not (d / name).exists():
			continue
		text, paragraphs = paragraphs_from_pasted_text((d / name).read_text())
		start = time.perf_counter()
		payload = build_live_reader_payload(text, paragraphs, name, session)
		seconds = time.perf_counter() - start
		rows = payload["citations"]
		results = []
		for e in exp.get("cases", []):
			hit = [r for r in rows if r["citation_kind"] != "statute" and e["find"] in text[max(0, r["offset_start"] - 3):r["offset_end"] + 3]]
			ok = bool(hit) and e["identifier"] in " ".join(str(h.get("normalized_citation") or "") + " " + str(h.get("citation_text")) + " " + str(h.get("target_citation") or "") for h in hit)
			if ok and "in_library" in e and session is not None and e["in_library"]:
				ok = any(h.get("target_case_id") for h in hit)
			results.append((f"case: {e['find'][:60]}", ok))
		for e in exp.get("back_references", []):
			hit = [r for r in rows if r["citation_kind"] == "case_short" and e["find"].split(" at ")[0] in r["citation_text"] and r.get("heuristic_note")]
			results.append((f"backref: {e['find'][:50]}", bool(hit) and e["points_to"] in hit[0]["heuristic_note"]))
		for e in exp.get("statutes", []):
			hit = [r for r in rows if r["citation_kind"] == "statute" and e["find"].lower() in text[max(0, r["offset_start"] - 12):r["offset_end"] + 12].lower()]
			ok = bool(hit) and (e.get("instrument") is None or any(h.get("instrument_key") == e["instrument"] for h in hit))
			results.append((f"statute: {e['find'][:55]}", ok))
		for e in exp.get("pinpoints", []):
			hit = [r for r in rows if r["citation_kind"] != "statute" and e["find"].split(" at ")[0] in text[max(0, r["offset_start"] - 3):r["offset_end"] + 60]]
			got = next((h.get("target_paragraphs") or ([h["target_paragraph"]] if h.get("target_paragraph") else None) for h in hit if h.get("target_case_id")), None)
			if session is None or not any(h.get("target_case_id") for h in hit):
				continue
			results.append((f"pinpoint: {e['find'][:50]}", got == e["paragraphs"]))
		if "max_seconds" in exp:
			results.append((f"under {exp['max_seconds']}s", seconds < exp["max_seconds"]))
		if "min_case_citations" in exp:
			results.append((f"at least {exp['min_case_citations']} case citations", payload["summary"]["case_citations"] >= exp["min_case_citations"]))
		passed = sum(ok for _, ok in results)
		total_pass += passed; total += len(results)
		report.append({"name": name, "seconds": seconds, "summary": payload["summary"], "results": results})
	return report


def main(argv):
	folder = next((a for a in argv if not a.startswith("--")), "tests/live_analysis_mocks")
	session = None
	if "--no-library" not in argv:
		from backend.database import SessionLocal

		session = SessionLocal()
	total_pass = total = 0
	for doc in score(folder, session):
		passed = sum(ok for _, ok in doc["results"])
		total_pass += passed
		total += len(doc["results"])
		s = doc["summary"]
		print(f"\n{doc['name']}: {doc['seconds']:.2f}s, {s['case_citations']} case citations ({s['resolved_case_citations']} in library), {s['statute_references']} statutes, {passed}/{len(doc['results'])} checks")
		for label, ok in doc["results"]:
			if not ok:
				print("  FAIL", label)
	print(f"\nTotal {total_pass}/{total}")


if __name__ == "__main__":
	main(sys.argv[1:])
