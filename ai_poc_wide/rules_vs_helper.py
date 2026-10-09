"""Compare PR 439 rules (position_holder.py, copied beside this script) with blind helper labels and the AI's labels, point by point, on the sheet paragraphs."""
import json, sys, collections, re
sys.path.insert(0, '.'); sys.path.insert(0, '/tmp/claude-0/w')
import position_holder as PH
from evalib import jaccard, pct, derive_layer
W = '/tmp/claude-0/w/sheet/'
C = {int(k): v for k, v in json.load(open(W + 'sheet_cases.json')).items()}
cmp_rows = json.load(open(W + 'compare_h1.json'))
by_case = collections.defaultdict(list)
for r in cmp_rows:
    c, p = map(int, r['unit'].split('-')); by_case[c].append((p, r))
out = []
for c, items in by_case.items():
    paras = C[c]['paras']
    res = PH.tag_decision([p['text'] for p in paras], C[c]['title'])
    pos = {p['paragraph_index']: i for i, p in enumerate(paras)}
    for p, r in items:
        text = paras[pos[p]]['text']; rr = res[pos[p]]
        sents = PH.split_sentences(text)
        if not sents or not rr.cues:
            continue
        best = max(range(len(sents)), key=lambda i: jaccard(sents[i], r['ai_text']))
        sc = jaccard(sents[best], r['ai_text'])
        cue = rr.cues[min(best, len(rr.cues) - 1)]
        out.append(dict(r, rule_holder=cue.holder, rule_layer=cue.layer, match=sc))
print(len(out), 'points with a rule reading;', sum(o['match'] >= 0.2 for o in out), 'with a decent sentence match')
good = [o for o in out if o['match'] >= 0.2]
def row(name, sel, a, b):
    print(f'{name}: ', pct(sum(o[a] == o[b] for o in sel), len(sel)))
for nm, sel in (('all matched', good),):
    row('rules holder = helper holder', sel, 'rule_holder', 'h_holder')
    row('AI holder = helper holder (same points)', sel, 'ai_holder', 'h_holder')
    row('rules layer = helper layer', sel, 'rule_layer', 'h_layer')
    row('AI derived layer = helper layer (same points)', sel, 'ai_layer', 'h_layer')
    print('court-for-everything baseline holder', pct(sum(o['h_holder'] == 'court' for o in sel), len(sel)))
# where rules and AI differ, who does the helper side with?
dis = [o for o in good if o['rule_holder'] != o['ai_holder']]
print('rules and AI disagree on holder:', len(dis), '| helper sides with AI', sum(o['h_holder'] == o['ai_holder'] for o in dis), '| with rules', sum(o['h_holder'] == o['rule_holder'] for o in dis), '| neither', sum(o['h_holder'] not in (o['ai_holder'], o['rule_holder']) for o in dis))
agree = [o for o in good if o['rule_holder'] == o['ai_holder']]
print('rules and AI agree on holder:', len(agree), '| helper agrees with them', pct(sum(o['h_holder'] == o['ai_holder'] for o in agree), len(agree)))
json.dump(out, open(W + 'rules_compare.json', 'w'))
