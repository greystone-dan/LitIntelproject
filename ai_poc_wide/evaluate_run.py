"""Offline checks on the arm outputs of the wide run. Usage: python evaluate_run.py --root <folder holding v4/ L/ LF/ L41/> [--inputs inputs]"""
import argparse, collections, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from evalib import *

ap = argparse.ArgumentParser()
ap.add_argument('--root', type=Path, required=True)
ap.add_argument('--inputs', type=Path, default=HERE / 'inputs')
ap.add_argument('--json-out', type=Path, default=None)
a = ap.parse_args()
IN = load_inputs(a.inputs)
ARMS = {n: load_arm(a.root / n) for n in ('v4', 'L', 'LF', 'L41') if (a.root / n).exists()}
res = {}
for n, arm in ARMS.items():
    rows = list(points(arm))
    paras = sum(len(d['paragraphs']) for d in arm.values())
    r = {'decisions': len(arm), 'paragraphs': paras, 'points': len(rows), 'points_per_paragraph': round(len(rows) / max(paras, 1), 2),
		'usd': round(sum(d.get('usd', 0) for d in arm.values()), 3), 'paragraphs_missing': sum(len(d['paragraphs_missing']) for d in arm.values()), 'dropped_rows': sum(d['dropped_rows'] for d in arm.values())}
    lay = collections.Counter()
    bad = 0
    qs = collections.Counter()
    qs_court = collections.defaultdict(collections.Counter)
    for cid, para, i, pr in rows:
        court = IN[cid]['court'] + ('-fr' if IN[cid]['french'] else '')
        L = pr.get('layer') or derive_layer(pr['holder'], pr['kind'])
        lay[L] += 1
        if L not in range(1, 7) or pr['holder'] not in OK_PAIRS[L]:
            bad += 1
        if 'quote' in pr:
            text = next(p['text'] for p in IN[cid]['paragraphs'] if p['paragraph_index'] == para)
            others = {p['paragraph_index']: p['text'] for p in IN[cid]['paragraphs']}
            s = quote_status(pr['quote'], text, others, para)
            qs[s] += 1
            qs_court[court][s] += 1
    r['layers'] = dict(sorted(lay.items()))
    r['layer_source'] = 'model' if 'quote' in rows[0][3] else 'derived from holder/kind (as in the review sheet)'
    r['impossible_holder_layer_pairs'] = bad
    if qs:
        r['quote_status'] = dict(qs)
        r['quote_verbatim_or_near_pct'] = pct(sum(qs[k] for k in ('exact', 'parts', 'near')), sum(qs.values()))
        r['quote_by_court'] = {c: dict(v) for c, v in qs_court.items()}
    r['layer4_by_court'] = dict(collections.Counter(IN[cid]['court'] for cid, para, i, pr in rows if (pr.get('layer') == 4)))
    res[n] = r

def pair(x, y, key, thr):
    n = m = h = l = k = 0
    for cid in set(ARMS[x]) & set(ARMS[y]):
        px = {r['para']: r['propositions'] for r in ARMS[x][cid]['paragraphs']}
        py = {r['para']: r['propositions'] for r in ARMS[y][cid]['paragraphs']}
        for para in px:
            A, B = px[para], py.get(para, [])
            n += len(A)
            for i, j, s in match_points(A, B, key=key, thr=thr):
                m += 1
                h += A[i]['holder'] == B[j]['holder']
                lx = A[i].get('layer') or derive_layer(A[i]['holder'], A[i]['kind'])
                ly = B[j].get('layer') or derive_layer(B[j]['holder'], B[j]['kind'])
                l += lx == ly
                k += A[i]['kind'] == B[j]['kind']
    return {'points_in_first': n, 'matched': pct(m, n), 'holder_agree': pct(h, m), 'layer_agree': pct(l, m), 'kind_agree': pct(k, m)}

if 'L' in ARMS and 'LF' in ARMS:
    res['L_vs_LF'] = pair('L', 'LF', lambda p: p['quote'], 0.5)
if 'L' in ARMS and 'v4' in ARMS:
    res['v4_vs_L'] = pair('v4', 'L', lambda p: p['text'], 0.25)
if 'L' in ARMS and 'L41' in ARMS:
    res['miniL_vs_gpt41L'] = pair('L', 'L41', lambda p: p['quote'], 0.5)
print(json.dumps(res, indent=1))
if a.json_out:
    a.json_out.write_text(json.dumps(res, indent=1))
