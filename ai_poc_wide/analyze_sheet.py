"""Compare blind helper labels with the stored AI labels on the 160 paragraphs of the human review sheet (all 534 points in them)."""
import json, glob, sys, collections
sys.path.insert(0, '.')
from evalib import derive_layer, pct
W = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/w/sheet/'
helper_dir = sys.argv[2] if len(sys.argv) > 2 else 'h1'
C = {int(k): v for k, v in json.load(open(W + 'sheet_cases.json')).items()}
R = json.load(open(W + 'sheet_rows.json'))
sheet_ids = {r['Point ID'] for r in R}
H = {}
for f in sorted(glob.glob(f'{W}{helper_dir}/out_*.json')):
    for u in json.load(open(f)):
        H[u['unit']] = u
rows = []
for unit, u in H.items():
    c, p = map(int, unit.split('-'))
    pr = next(x for x in C[c]['props'] if x['para'] == p)
    for hp in u['points']:
        ai = pr['propositions'][hp['n'] - 1]
        rows.append(dict(unit=unit, n=hp['n'], court=C[c]['court'], ai_holder=ai['holder'], ai_kind=ai['kind'], ai_layer=derive_layer(ai['holder'], ai['kind']), ai_text=ai['text'],
			h_holder=hp['holder'], h_kind=hp['kind'], h_layer=hp['layer'], sup=hp['supported'], conf=hp['confidence'], in_sheet=f"{c}-{p}.{hp['n']}" in sheet_ids))
json.dump(rows, open(W + f'compare_{helper_dir}.json', 'w'), indent=0)
def rep(name, sel):
    n = len(sel)
    print(f'--- {name}: {n} points')
    print(' holder agrees   ', pct(sum(r['ai_holder'] == r['h_holder'] for r in sel), n))
    print(' kind agrees     ', pct(sum(r['ai_kind'] == r['h_kind'] for r in sel), n))
    print(' layer agrees (AI layer derived from holder/kind)', pct(sum(r['ai_layer'] == r['h_layer'] for r in sel), n))
    print(' all three agree ', pct(sum(r['ai_holder'] == r['h_holder'] and r['ai_kind'] == r['h_kind'] and r['ai_layer'] == r['h_layer'] for r in sel), n))
    print(' point supported (yes) ', pct(sum(r['sup'] == 'yes' for r in sel), n), ' partial', sum(r['sup'] == 'partial' for r in sel), ' no', sum(r['sup'] == 'no' for r in sel))
rep('all labelled points', rows)
rep('the 160 sheet points', [r for r in rows if r['in_sheet']])
rep('high-confidence helper labels', [r for r in rows if r['conf'] == 'high'])
for c in ['FC', 'FCA', 'SCC', 'RPD', 'RAD']:
    rep(c, [r for r in rows if r['court'] == c])
print('--- confusion holder (AI -> helper), top')
cm = collections.Counter((r['ai_holder'], r['h_holder']) for r in rows if r['ai_holder'] != r['h_holder'])
for k, v in cm.most_common(10): print(' ', k, v)
print('--- layer confusion (AI derived -> helper)')
cl = collections.Counter((r['ai_layer'], r['h_layer']) for r in rows if r['ai_layer'] != r['h_layer'])
for k, v in cl.most_common(10): print(' ', k, v)
print('helper layer distribution', sorted(collections.Counter(r['h_layer'] for r in rows).items()), ' AI derived', sorted(collections.Counter(r['ai_layer'] for r in rows).items()))
miss = [(u['unit'], m) for u in H.values() for m in u.get('missing', [])]
print('units with missing points:', sum(1 for u in H.values() if u.get('missing')), 'of', len(H), ' missing points:', len(miss), ' merged flagged', sum(bool(u.get('merged')) for u in H.values()), ' split flagged', sum(bool(u.get('split')) for u in H.values()))
