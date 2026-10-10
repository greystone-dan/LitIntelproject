import json,re,math,sys
exec(open('/tmp/claude-0/w/retest.py').read().split("idx0=Index")[0])  # builds lib0,lib1,paras0,paras1,args
lib=lib0+lib1;P={**paras0,**paras1}
idx=Index(lib)
def cand(a,k=10):
    q=a['issue']+' '+a['claim']
    seen=[];out=[]
    for s,x in idx.top(q,60):
        key=(x['case_id'],x['issue'])
        if key in seen: continue
        seen.append(key);out.append((s,x))
        if len(out)==k:break
    return out
# BM25 + cues
from match_library import toks
from collections import Counter
docs=[toks(x['text']) for x in lib];N=len(docs);avg=sum(map(len,docs))/N
df=Counter();[df.update(set(d)) for d in docs]
def bm25(q,d,k1=1.4,b=0.75):
    tf=Counter(d);s=0
    for w in set(q):
        if w in tf:
            idf=math.log(1+(N-df[w]+.5)/(df[w]+.5));s+=idf*tf[w]*(k1+1)/(tf[w]+k1*(1-b+b*len(d)/avg))
    return s
CUES=[r"\bs(?:ection|ec)?\.?\s*(\d+(?:\([0-9a-z]+\))*)",r"\b(h&c|humanitarian|compassionate)\b",r"\bvavilov\b",r"\bprocedural fairness|natural justice\b",r"\bbias\b",r"\bcredib\w+",r"\bstate protection\b",r"\binternal (flight|refuge)|ifa\b",r"\bbest interests\b",r"\bpre-removal|prra\b",r"\bgenuine\b|\bbona fide\b",r"\bresidency|residence\b",r"\binadmissib\w+",r"\bcertif\w+ question\b",r"\bjurisdiction\b",r"\breasons? (were )?(inadequate|insufficient)|adequacy of reasons\b",r"\bdelay\b",r"\bmisrepresentation\b"]
def cues(t):
    t=t.lower();out=set()
    for i,c in enumerate(CUES):
        for m in re.finditer(c,t):out.add((i,m.group(1) if m.groups() and m.group(1) and i==0 else ''))
    return out
cl=[cues(x['text']) for x in lib]
def bm25plus(a):
    qt=a['issue']+' '+a['claim'];q=toks(qt);qc=cues(qt+' '+a.get('quote',''))
    sc=[]
    for i,d in enumerate(docs):
        s=bm25(q,d);inter=len(qc&cl[i]);s*=1+0.25*inter
        sc.append((s,i))
    sc.sort(reverse=True);return [lib[i] for _,i in sc[:10]]
