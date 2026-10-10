import json,re,math,glob
exec(open('/tmp/claude-0/w/rr/lib2.py').read())
from match_library import toks
from collections import Counter
Q={}
for f in glob.glob('/tmp/claude-0/w/dq/out_*.json'):
    Q.update({int(k):v for k,v in json.load(open(f)).items()})
def faithful(q,text):
    t=text.lower()
    for w in re.findall(r'\b\d[\w\-\.\(\)]*|\b[A-Z][a-z]+(?= v\b)',q):
        if w.lower().strip('.') not in t:return False
    return True
kept=0;tot=0;qs={}
for i,x in enumerate(lib):
    l=[q for q in Q.get(i,[]) if (faithful(q,x['text']))]
    tot+=len(Q.get(i,[]));kept+=len(l);qs[i]=l
print('questions',tot,'kept',kept,'issues with q',sum(1 for v in qs.values() if v))
def mk(docs_text):
    docs=[toks(t) for t in docs_text];N=len(docs);avg=sum(map(len,docs))/N
    df=Counter();[df.update(set(d)) for d in docs]
    def sc(qtext):
        q=toks(qtext);out=[]
        for i,d in enumerate(docs):
            tf=Counter(d);s=0
            for w in set(q):
                if w in tf:
                    idf=math.log(1+(N-df[w]+.5)/(df[w]+.5));s+=idf*tf[w]*2.4/(tf[w]+1.4*(.25+.75*len(d)/avg))
            out.append(s)
        return out
    return sc
sq=mk([' '.join(qs[i]) or x['text'] for i,x in enumerate(lib)])
sb=mk([x['text']+' '+' '.join(qs[i]) for i,x in enumerate(lib)])
def dedupe(ids,k):
    seen=set();out=[]
    for i in ids:
        key=(lib[i]['case_id'],lib[i]['issue'])
        if key in seen:continue
        seen.add(key);out.append(i)
        if len(out)==k:break
    return out
args=json.load(open('/tmp/claude-0/w/fresh/args.json'));c=json.load(open('/tmp/claude-0/w/cands2.json'))
def rrf(lists,k=30,cc=60):
    s={}
    for l in lists:
        for r,i in enumerate(l):s[i]=s.get(i,0)+1/(cc+r+1)
    return dedupe([i for i,_ in sorted(s.items(),key=lambda t:-t[1])],k)
for S in 'ABC':
    for n,a in enumerate(args[S]):
        q=a['issue']+' '+a['claim']
        for name,f in (('DQ',sq),('DQT',sb)):
            s=f(q);c[f'{S}{n}'][name]=dedupe(sorted(range(len(lib)),key=lambda i:-s[i])[:80],30)
        d=c[f'{S}{n}'];d['RRFDQ']=rrf([d['W'],d['B'],d['DQ']]);d['RRFALL']=rrf([d['W'],d['B'],d['DQ'],d['CE']])
json.dump(c,open('/tmp/claude-0/w/cands3.json','w'))
json.dump(qs,open('/tmp/claude-0/w/dq_kept.json','w'))
