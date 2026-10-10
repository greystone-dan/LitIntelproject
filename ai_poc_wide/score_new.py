import json, glob, sys, collections
from pathlib import Path
sys.path.insert(0, '.'); sys.path.insert(0, '/tmp/claude-0/w')
from evalib import *
import position_holder as PH
IN = load_inputs(); A = {n: load_arm(Path('out') / n) for n in ('v4', 'L', 'LF', 'L41')}
R = {}
for f in glob.glob('/tmp/claude-0/w/new/h/out_*.json'):
    for u in json.load(open(f)):
        for p in u['points']: R[(u['unit'], p['n'])] = p
units = {}
for f in glob.glob('/tmp/claude-0/w/new/batch_*.json'):
    for u in json.load(open(f)): units[u['unit']] = u
rule_cache = {}
def rules(cid):
    if cid not in rule_cache:
        d = IN[cid]; rule_cache[cid] = PH.tag_decision([p['text'] for p in d['paragraphs']], d['title'])
    return rule_cache[cid]
def get(arm, cid, para):
    if cid not in A[arm]: return []
    return next((r['propositions'] for r in A[arm][cid]['paragraphs'] if r['para'] == para), [])
rows = []
for (unit, n), rd in R.items():
    cid, para = map(int, unit.split('-'))
    lp = get('L', cid, para)[n - 1]
    row = dict(unit=unit, n=n, court=IN[cid]['court'], fr=IN[cid]['french'], reader=rd, L=lp)
    for arm, key in (('LF', lambda p: p['quote']), ('L41', lambda p: p['quote']), ('v4', lambda p: p['text'])):
        pts = get(arm, cid, para)
        if arm == 'v4':
            sc = [(jaccard(p['text'], lp['quote']), p) for p in pts]
        else:
            sc = [(jaccard(p['quote'], lp['quote']), p) for p in pts]
        thr = 0.25 if arm == 'v4' else 0.5
        best = max(sc, key=lambda x: x[0], default=(0, None))
        row[arm] = dict(best[1], layer=best[1].get('layer') or derive_layer(best[1]['holder'], best[1]['kind'])) if best[1] and best[0] >= thr else None
    idx = [i for i, p in enumerate(IN[cid]['paragraphs']) if p['paragraph_index'] == para][0]
    sents = PH.split_sentences(IN[cid]['paragraphs'][idx]['text']); res = rules(cid)[idx]
    if sents and res.cues:
        b = max(range(len(sents)), key=lambda i: jaccard(sents[i], lp['quote']))
        cue = res.cues[min(b, len(res.cues) - 1)]; row['rules'] = {'holder': cue.holder, 'layer': cue.layer}
    rows.append(row)
json.dump(rows, open('/tmp/claude-0/w/new/scored.json', 'w'), default=str)
def agree(sel, arm, f):
    g = [r for r in sel if (r.get(arm) if arm != 'L' else r['L'])]
    k = sum((r[arm] if arm != 'L' else r['L'])[f] == r['reader'][f if f != 'holder' else 'holder'] for r in g)
    return pct(k, len(g))
print(len(rows), 'reader-labelled L points;', len({r['unit'] for r in rows}), 'paragraphs')
for f in ('holder', 'layer', 'kind'):
    print('\n###', f)
    for arm in ('L', 'LF', 'v4', 'L41', 'rules'):
        if arm == 'rules' and f == 'kind': continue
        print(f'  {arm:6}', agree(rows, arm, f))
common = [r for r in rows if r.get('LF') and r.get('v4')]
print('\n### on the', len(common), 'points matched in L, LF and v4')
for f in ('holder', 'layer', 'kind'):
    print(' ', f, {arm: agree(common, arm, f).split(' (')[0] for arm in ('L', 'LF', 'v4')})
sub = [r for r in rows if r.get('L41')]
print('\n### gpt-4.1 subset', len(sub))
for f in ('holder', 'layer'):
    print(' ', f, {arm: agree(sub, arm, f).split(' (')[0] for arm in ('L', 'L41', 'LF', 'v4')})
print('\n### by court (L / LF layer agreement, holder agreement)')
for c in ('FC', 'FCA', 'SCC', 'RPD', 'RAD'):
    s = [r for r in rows if r['court'] == c]
    print(' ', c, len(s), 'holder L', agree(s, 'L', 'holder').split(' (')[0], 'LF', agree(s, 'LF', 'holder').split(' (')[0], '| layer L', agree(s, 'L', 'layer').split(' (')[0], 'LF', agree(s, 'LF', 'layer').split(' (')[0])
print('\nreader layer 4 count', sum(r['reader']['layer'] == 4 for r in rows), '; L says 4:', sum(r['L']['layer'] == 4 for r in rows), 'and reader agrees', sum(r['L']['layer'] == 4 == r['reader']['layer'] for r in rows), '; LF says 4:', sum(bool(r.get('LF')) and r['LF']['layer'] == 4 for r in rows), 'and reader agrees', sum(bool(r.get('LF')) and r['LF']['layer'] == 4 == r['reader']['layer'] for r in rows))
print('RPD points where L says layer 4:', sum(r['court'] == 'RPD' and r['L']['layer'] == 4 for r in rows), 'LF:', sum(r['court'] == 'RPD' and bool(r.get('LF')) and r['LF']['layer'] == 4 for r in rows))
P = ('applicant', 'respondent')
def harm(a, h):
    if a == h: return 'same'
    s = {a, h}
    if s <= {'applicant', 'witness_or_document'} or s <= {'respondent', 'witness_or_document'} or s <= {'prior_court_or_authority', 'witness_or_document'} or s <= {'court', 'prior_court_or_authority'} or 'other' in s: return 'harmless'
    return 'harmful'
for arm in ('L', 'LF'):
    g = [r for r in rows if (r[arm] if arm != 'L' else r['L'])]
    c = collections.Counter(harm((r[arm] if arm != 'L' else r['L'])['holder'], r['reader']['holder']) for r in g)
    print(arm, 'holder errors', dict(c), 'harmful rate', pct(c['harmful'], len(g)))
print('reader: supported yes', pct(sum(r['reader']['supported'] == 'yes' for r in rows), len(rows)), '; reader confidence high', pct(sum(r['reader']['confidence'] == 'high' for r in rows), len(rows)))
