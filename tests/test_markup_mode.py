"""Markup mode (third case-reader view): pure-function checks via node plus page wiring checks."""

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

from backend.pages.data_explorer import data_explorer_page_html

PAGES = Path(__file__).resolve().parent.parent / "backend" / "pages"
JS = PAGES / "markup_mode.js"
CSS = PAGES / "markup_mode.css"
NODE = shutil.which("node")
def needs_node(fn):  # node is preinstalled on CI runners; a missing node must fail, not skip
    return fn


PROBE = r"""
const m = require(process.argv[1]);
const p = JSON.parse(process.argv[2]);
const out = {};
out.notes = m.buildNotes(p.payload);
out.layout = m.layoutNotes(p.items, 8);
out.layers = m.sanitizeLayers(p.rawLayers);
out.states = p.stateCases.map(c => m.noteState(c.note, c.layers, c.over));
out.ranges = m.subthemeRanges(p.payload);
out.topics = m.topicIndex(p.payload, 10);
out.topicParas = Array.from(m.topicParas(out.topics, p.selected || [])).sort((a, b) => a - b);
out.runs = m.foldRuns(p.visible || []);
out.peeks = out.notes.filter(n => n.cite).map(n => m.peekFor(n));
console.log(JSON.stringify(out));
"""


def _payload(verified=True):
    chunks = [{"text": "Intro paragraph without number."}] + [
        {"text": f"[{n}] Paragraph {n} text."} for n in range(1, 6)
    ]
    meta = [{"key": "decision_outcome", "value": "allowed"}]
    if verified:
        meta += [
            {"key": "disposition_paragraph", "value": "The application is allowed."},
            {"key": "disposition_paragraph_number", "value": "5"},
        ]
    return {
        "item": {"judge": "<b>Justice X</b>", "court": "FC", "date": "2024-01-02T00:00:00"},
        "readerData": {
            "chunks": chunks,
            "extracted_metadata": meta,
            "citations": [
                {"id": 1, "citation_kind": "neutral", "citation_text": "2019 SCC 65",
                 "target_case_id": 9, "target_title": "Vavilov <x>", "target_paragraph": 7,
                 "target_chunk_text": "Quoted text"},
                {"id": 2, "citation_kind": "statute", "citation_text": "IRPA s 96"},
                {"id": 3, "citation_kind": "case_short", "citation_text": "Baker"},
                {"id": 1, "citation_kind": "neutral", "citation_text": "dup"},
            ],
            "format_blocks": [
                {"type": "para", "num": 2, "start": 10, "end": 20, "cited_by_count": 3},
                {"type": "para", "num": 3, "start": 21, "end": 30, "cited_by_count": 0},
            ],
            "evidence_summary": {"units": [{
                "unit_index": 1, "start_paragraph": 1, "end_paragraph": 4,
                "subthemes": [{"subtheme_id": "s1", "paragraph_indices": [2, 3],
                               "key_terms": ["reasonableness"], "argument_roles": ["governing_rule"]}],
            }]},
        },
    }


def _run(**extra):
    if NODE is None:
        pytest.fail("node is required for markup mode tests")
    data = dict(payload=_payload(), items=[], rawLayers=None, stateCases=[])
    data.update(extra)
    res = subprocess.run([NODE, "-e", PROBE, str(JS), json.dumps(data)],
                         capture_output=True, text=True, check=True)
    return json.loads(res.stdout)


@needs_node
def test_build_notes_counts_and_filters():
    notes = _run()["notes"]
    types = [n["type"] for n in notes]
    assert types.count("cite") == 1  # statute, unresolved short name and duplicate id skipped
    assert types.count("unit") == 1 and types.count("judge") == 1
    assert types.count("citedby") == 1
    cite = next(n for n in notes if n["type"] == "cite")
    assert "7" in cite["quoteLabel"] and cite["quote"] == "Quoted text"


@needs_node
def test_outcome_verified_and_unverified():
    ok = next(n for n in _run()["notes"] if n["type"] == "outcome")
    assert ok["anchor"] == {"kind": "para", "num": 5} and not ok["unverified"]
    bad = next(n for n in _run(payload=_payload(verified=False))["notes"] if n["type"] == "outcome")
    assert bad["unverified"] and bad["anchor"]["kind"] == "top" and "unverified" in bad["pill"]


@needs_node
def test_unit_paragraph_mapping_via_chunks():
    res = _run()
    unit = next(n for n in res["notes"] if n["type"] == "unit")
    assert unit["anchor"] == {"kind": "para", "num": 1}
    assert [(r["first"], r["last"]) for r in res["ranges"]] == [(2, 3)]


@needs_node
def test_layout_never_overlaps():
    items = [{"y": 10, "h": 50}, {"y": 12, "h": 30}, {"y": 400, "h": 20}, {"y": 5, "h": 10}]
    laid = _run(items=items)["layout"]
    for a, b in zip(laid, laid[1:]):
        assert b["top"] >= a["top"] + items[a["index"]]["h"] + 8
    assert len(laid) == 4


@needs_node
def test_layers_sanitised_and_note_state():
    layers = _run(rawLayers={"cite": "open", "tags": "bogus", "zzz": "open"})["layers"]
    assert layers["cite"] == "open" and layers["tags"] == "underline"
    assert _run(rawLayers={"tags": "soft"})["layers"]["tags"] == "underline"  # saved before tag modes existed
    for mode in ("off", "underline", "tint", "bubbles"):
        assert _run(rawLayers={"tags": mode})["layers"]["tags"] == mode
    cases = [
        dict(note={"type": "cite", "id": "a"}, layers={"cite": "off"}, over={"a": True}),
        dict(note={"type": "cite", "id": "a"}, layers={"cite": "markers"}, over={"a": True}),
        dict(note={"type": "cite", "id": "a"}, layers={"cite": "open"}, over={"a": False}),
        dict(note={"type": "citedby", "id": "c"}, layers={"citedby": "gutter"}, over={}),
    ]
    assert _run(stateCases=cases)["states"] == ["off", "open", "markers", "off"]


@needs_node
def test_notes_escape_nothing_in_data_html_is_escaped_by_E():
    out = subprocess.run(
        [NODE, "-e", "const m=require(process.argv[1]);console.log(m.E('<img onerror=\"x\">&\\''))", str(JS)],
        capture_output=True, text=True, check=True).stdout.strip()
    assert "<" not in out and "&lt;img" in out and "&quot;" in out and "&#39;" in out


@needs_node
def test_script_is_valid_javascript():
    subprocess.run([NODE, "--check", str(JS)], check=True)


def test_script_has_no_network_or_ai_calls():
    src = JS.read_text(encoding="utf-8")
    for banned in ("XMLHttpRequest", "openai", "WebSocket", "sendBeacon"):
        assert banned.lower() not in src.lower(), banned
    # The only request is the user-clicked Word export to this site's own route; it sends no query text.
    assert src.count("fetch(") == 1
    assert "fetch(`/cases/${encodeURIComponent(cid)}/markup-export`" in src


def test_page_wires_markup_mode():
    html = data_explorer_page_html()
    assert 'id="readerMarkupToggle"' in html
    assert "data-cite-id" in html
    assert "window.__markupMode" in html
    assert "#markupStage" in html
    assert html.count("markup-on") > 3
    assert re.search(r"<style>[^<]*markup-on", html)
    assert CSS.read_text(encoding="utf-8")[:20] in html


@needs_node
def test_topics_ranked_by_paragraph_coverage_and_select_paragraphs():
    payload = _payload()
    payload["readerData"]["evidence_summary"]["units"][0]["subthemes"].append(
        {"subtheme_id": "s2", "paragraph_indices": [4], "key_terms": ["Reasonableness", "credibility"],
         "argument_roles": []})
    res = _run(payload=payload, selected=["credibility"])
    topics = res["topics"]
    by_key = {t["key"]: t for t in topics}
    assert by_key["reasonableness"]["paras"] == 3  # ¶2-3 plus ¶4; "Reasonableness" and "reasonableness" are one topic
    assert by_key["reasonableness"]["label"] == "reasonableness"  # first spelling seen
    assert topics[0]["key"] == "reasonableness"
    assert res["topicParas"] == [4]
    assert all(t["color"] for t in topics)


@needs_node
def test_fold_runs_groups_consecutive_hidden_entries():
    runs = _run(visible=[True, False, False, True, False, True, False, False])["runs"]
    assert runs == [{"start": 1, "end": 2}, {"start": 4, "end": 4}, {"start": 6, "end": 7}]
    assert _run(visible=[True, True])["runs"] == []
    assert _run(visible=[False, False])["runs"] == [{"start": 0, "end": 1}]


@needs_node
def test_peek_uses_stored_data_and_says_when_not_in_library():
    payload = _payload()
    payload["readerData"]["citations"].append(
        {"id": 8, "citation_kind": "neutral", "citation_text": "2015 FC 1", "normalized_citation": "2015 FC 1"})
    peeks = {p["id"]: p for p in _run(payload=payload)["peeks"]}
    lib = peeks["cite-1"]
    assert lib["inLibrary"] and lib["caseId"] == 9 and lib["paragraph"] == 7
    assert lib["text"] == "Quoted text" and "[7]" in lib["label"] and lib["missing"] == ""
    gone = peeks["cite-8"]
    assert not gone["inLibrary"] and gone["text"] == ""
    assert "Not in the library" in gone["missing"]


def test_follow_up_features_are_wired_into_the_page():
    html = data_explorer_page_html()
    for needle in ("mkPanel", "mkHover", "markup-mode-on", "data-mk-topic", "mk-foldbar", "mk-tags-bubbles"):
        assert needle in html, needle
    css = CSS.read_text(encoding="utf-8")
    assert "reader-hover-tooltip" in css  # the page's own tooltip is replaced in markup mode


@needs_node
def test_cited_by_gutter_uses_stored_rows_and_falls_back_without_them():
    plain = next(n for n in _run()["notes"] if n["type"] == "citedby")
    assert plain["meta"].startswith("Distinct cases") and plain["foot"] == []
    payload = _payload()
    payload["readerData"]["paragraph_cited_by"] = {
        "coverage": {"sources_total": 4, "sources_processed": 2, "complete": False},
        "paragraphs": [{"paragraph": 2, "citer_count": 3, "mention_count": 4,
                        "purposes": {"followed": 2, "see": 1},
                        "citers": [{"case_id": 11, "citation": "2020 FC 1", "mentions": 2, "purpose": "followed", "signal": "applied in"},
                                   {"case_id": 12, "citation": "2021 FC 5", "mentions": 1, "purpose": "see", "signal": "see"}]}],
    }
    payload["readerData"]["citations"][0]["target_cited_by"] = {"citer_count": 2, "purposes": {"quoted": 1}}
    out = _run(payload=payload)
    note = next(n for n in out["notes"] if n["type"] == "citedby")
    assert "Partial: 2 of 4" in note["meta"] and "Cited by 3 cases · Followed 2, See 1" in note["meta"]
    assert "2020 FC 1 ×2 · Followed (\"applied in\")" in note["body"] and "+ 1 more" in note["body"]
    assert [f["arg"] for f in note["foot"]] == [11, 12]
    assert out["peeks"][0]["citedBy"] == "Cited by 2 cases · Quoted 1"


def _node(script, arg=None):
    if NODE is None:
        pytest.fail("node is required for markup mode tests")
    res = subprocess.run([NODE, "-e", "const m = require(process.argv[1]); const a = JSON.parse(process.argv[2] || 'null');\n" + script,
                          str(JS), json.dumps(arg)], capture_output=True, text=True, check=True)
    return json.loads(res.stdout)


@needs_node
def test_private_notes_add_replace_delete_and_caps():
    out = _node("""
let l = [];
l = m.mineUpsert(l, 5, 'first', false);
l = m.mineUpsert(l, 2, 'second', true);
l = m.mineUpsert(l, 5, 'first edited', false);
const afterEdit = JSON.parse(JSON.stringify(l));
const highlightOnly = m.mineUpsert([], 9, '   ', true);
const removed = m.mineUpsert(l, 5, '', false);
let many = [];
for (let i = 1; i <= 250; i++) many = m.mineUpsert(many, i, 'n' + i, false);
const long = m.mineUpsert([], 1, 'x'.repeat(5000), false)[0].text.length;
console.log(JSON.stringify({afterEdit, highlightOnly, removed, many: many.length, long,
  notes: m.mineToNotes(afterEdit.concat(highlightOnly))}));
""")
    assert [n["para"] for n in out["afterEdit"]] == [2, 5] and out["afterEdit"][1]["text"] == "first edited"
    assert out["highlightOnly"][0]["hl"] is True  # a highlight with no text is kept
    assert [n["para"] for n in out["removed"]] == [2]
    assert out["many"] == 200 and out["long"] == 2000
    ids = [n["id"] for n in out["notes"]]
    assert ids == ["mine-2", "mine-5"]  # the highlight-only paragraph gets no margin card
    assert out["notes"][0]["anchor"] == {"kind": "para", "num": 2} and out["notes"][0]["foot"][0]["action"] == "mine-edit"


@needs_node
def test_my_notes_layer_defaults_and_old_saved_layers_still_load():
    out = _node("console.log(JSON.stringify({d: m.defaultLayers(), s: m.sanitizeLayers({cite: 'off', tags: 'soft'}), st: m.noteState({id: 'mine-1', type: 'mine'}, m.defaultLayers(), {})}))")
    assert out["d"]["mine"] == "open" and out["s"]["mine"] == "open" and out["s"]["cite"] == "off"
    assert out["st"] == "open"


@needs_node
def test_export_plan_uses_visible_layers_and_keeps_anchor_text():
    payload = _payload()
    payload["readerData"]["citations"][0]["citation_text"] = "2019 SCC 65 at para 7"
    out = _node("""
const notes = m.buildNotes(a).concat(m.mineToNotes([{para: 2, text: 'check this', hl: false}]));
const layers = m.defaultLayers();
const blockOf = n => n.anchor.kind === 'top' ? null : (n.anchor.num || 0) * 10;
const on = m.exportPlan(notes, layers, blockOf);
layers.unit = 'off'; layers.cite = 'off'; layers.citedby = 'off';
const off = m.exportPlan(notes, layers, blockOf);
console.log(JSON.stringify({on, off, mine: m.commentFor(notes.find(n => n.type === 'mine'))}));
""", payload)
    kinds = {c["label"].split(":")[0] for c in out["on"]}
    assert {"Citation", "Discussion unit", "Outcome", "Judge", "Cited by others", "My note", "Act / statute"} <= kinds
    cite = next(c for c in out["on"] if c["label"].startswith("Citation"))
    assert cite["quote"] == "2019 SCC 65 at para 7" and "Quoted text" in cite["text"]
    judge = next(c for c in out["on"] if c["label"].startswith("Judge"))
    assert judge["block"] is None  # case-level notes go on the header
    assert next(c for c in out["on"] if c["author"] == "My note")["block"] == 20
    assert {c["label"].split(":")[0] for c in out["off"]} == {"Outcome", "Judge", "My note", "Act / statute"}  # hidden layers are not exported
    assert out["mine"]["text"] == "check this"  # no "private, saved in this browser" boilerplate in Word


def test_notes_and_export_are_wired_into_the_page():
    html = data_explorer_page_html()
    js = JS.read_text(encoding="utf-8")
    assert 'data-mk-act="export"' in js and "/markup-export" in js and "mkEditor" in js
    assert "ilit.markup.notes.v1" in js and "ResizeObserver" in js
    assert "#mkEditor" in CSS.read_text(encoding="utf-8")
    assert "markup-export" in html


@needs_node
def test_statute_notes_group_by_act_with_stored_text_only():
    payload = _payload()
    payload["readerData"]["citations"] += [
        {"id": -1, "citation_kind": "statute", "citation_text": "section 110(4) of the Act", "instrument_key": "canada.irpa",
         "pinpoint": "110(4)", "legislation_url": "https://laws-lois.justice.gc.ca/eng/acts/I-2.5/",
         "provision_text": "Subsection (1) does not apply to a person referred to in 112(3)...", "unresolved": False,
         "statute_version_label": "Version unknown"},
        {"id": -2, "citation_kind": "statute", "citation_text": "s 96", "instrument_key": "canada.irpa", "pinpoint": "96",
         "legislation_url": "javascript:alert(1)", "unresolved": False},
        {"id": -3, "citation_kind": "statute", "citation_text": "In the Order", "instrument_key": None, "unresolved": True},
    ]
    notes = [n for n in _run(payload=payload)["notes"] if n["type"] == "statute"]
    by_id = {n["id"]: n for n in notes}
    assert "statute--3" not in by_id  # an unmatched "instrument" is not shown as an Act
    full, bare = by_id["statute--1"], by_id["statute--2"]
    assert full["pill"] == "IRPA s 110(4)" and full["quote"].startswith("Subsection (1)")
    assert full["foot"] == [{"label": "Open the Act", "action": "open-url", "arg": "https://laws-lois.justice.gc.ca/eng/acts/I-2.5/"}]
    assert bare["quote"] == "" and "not stored" in bare["body"] and bare["foot"] == []  # no invented text, no unsafe link
    assert full["anchor"] == {"kind": "cite", "id": -1}
