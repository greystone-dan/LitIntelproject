import json, glob, sys, collections
sys.path.insert(0, '.')
from evalib import pct
W = '/tmp/claude-0/w/sheet/'
def lab(d):
    out = {}
    for f in sorted(glob.glob(f'{W}{d}/out_*.json')):
        for u in json.load(open(f)):
            for p in u['points']: out[(u['unit'], p['n'])] = p
    return out
a, b = lab('h1'), lab('h2')
k = sorted(set(a) & set(b))
print(len(k), 'points read by both')
for f in ('holder', 'kind', 'layer'):
    print(f, 'reader1 = reader2:', pct(sum(a[x][f] == b[x][f] for x in k), len(k)))
print('all three', pct(sum(all(a[x][f] == b[x][f] for f in ('holder','kind','layer')) for x in k), len(k)))
cmp = {(r['unit'], r['n']): r for r in json.load(open(W + 'compare_h1.json'))}
for nm, src in (('reader1', a), ('reader2', b)):
    print(nm, 'vs AI: holder', pct(sum(src[x]['holder'] == cmp[x]['ai_holder'] for x in k), len(k)), '| layer(derived)', pct(sum(src[x]['layer'] == cmp[x]['ai_layer'] for x in k), len(k)), '| kind', pct(sum(src[x]['kind'] == cmp[x]['ai_kind'] for x in k), len(k)))
both = [x for x in k if a[x]['holder'] == b[x]['holder']]
print('where the two readers agree on holder:', len(both), '-> AI agrees', pct(sum(a[x]['holder'] == cmp[x]['ai_holder'] for x in both), len(both)))
bl = [x for x in k if a[x]['layer'] == b[x]['layer']]
print('where the two readers agree on layer:', len(bl), '-> AI derived layer agrees', pct(sum(a[x]['layer'] == cmp[x]['ai_layer'] for x in bl), len(bl)))
print('layer-by-layer reader agreement', {l: pct(sum(a[x]['layer'] == b[x]['layer'] for x in k if a[x]['layer'] == l), sum(1 for x in k if a[x]['layer'] == l)) for l in (1,2,3,4,5,6)})
