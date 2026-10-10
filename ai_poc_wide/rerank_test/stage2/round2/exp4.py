import json,re,math,sys
exec(open('/tmp/claude-0/w/rr/lib2.py').read())
from match_library import toks,Index
from collections import Counter
idx=Index(lib)
docs=[toks(x['text']) for x in lib];N=len(docs);avg=sum(map(len,docs))/N
df=Counter();[df.update(set(d)) for d in docs]
def bm25(q,d,k1=1.4,b=0.75):
    tf=Counter(d);s=0
    for w in set(q):
        if w in tf:
            idf=math.log(1+(N-df[w]+.5)/(df[w]+.5));s+=idf*tf[w]*(k1+1)/(tf[w]+k1*(1-b+b*len(d)/avg))
    return s
src=open('/tmp/claude-0/w/rr/build.py').read()
CUES=eval(src.split('CUES=')[1].split('\ndef cues')[0])
def cues(t):
    t=t.lower();out=set()
    for i,c in enumerate(CUES):
        for m in re.finditer(c,t):out.add((i,m.group(1) if m.groups() and m.group(1) and i==0 else ''))
    return out
cl=[cues(x['text']) for x in lib]
pos={id(x):i for i,x in enumerate(lib)}
def dedupe(ids,k):
    seen=set();out=[]
    for i in ids:
        key=(lib[i]['case_id'],lib[i]['issue'])
        if key in seen:continue
        seen.add(key);out.append(i)
        if len(out)==k:break
    return out
def word(a,k=10):
    q=a['issue']+' '+a['claim']
    return dedupe([pos[id(x)] for s,x in idx.top(q,80)],k)
def bm(a,k=10,cw=0.25,field=1.0):
    qt=a['issue']+' '+a['claim'];q=toks(qt);qc=cues(qt)
    sc=[]
    for i,d in enumerate(docs):
        s=bm25(q,d)*(1+cw*len(qc&cl[i]));sc.append((s,i))
    sc.sort(reverse=True);return dedupe([i for _,i in sc[:80]],k)
def rrf(lists,k=10,c=60):
    s={}
    for l in lists:
        for r,i in enumerate(l):s[i]=s.get(i,0)+1/(c+r+1)
    return dedupe([i for i,_ in sorted(s.items(),key=lambda t:-t[1])],k)
from sentence_transformers import CrossEncoder
ce=CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
def cerank(a,pool,k=10):
    q=a['issue']+' '+a['claim']
    sc=ce.predict([(q,lib[i]['text'][:1200]) for i in pool])
    return dedupe([i for _,i in sorted(zip(sc,pool),key=lambda t:-t[0])],k)
args=json.load(open('/tmp/claude-0/w/fresh/args.json'))
import glob
Qk=json.load(open('/tmp/claude-0/w/dq_by_key.json'))
for f in glob.glob('/tmp/claude-0/w/dq/out_n*.json'):
    for k,v in json.load(open(f)).items():
        x=lib[int(k)];Qk[f"{x['case_id']}||{x['issue']}"]=v
def faithful(q,text):
    t=text.lower()
    for w in re.findall(r'\b\d[\w\-\.\(\)]*|\b[A-Z][a-z]+(?= v\b)',q):
        if w.lower().strip('.') not in t:return False
    return True
qs={i:[q for q in Qk.get(f"{x['case_id']}||{x['issue']}",[]) if faithful(q,x['text'])] for i,x in enumerate(lib)}
print('issues with q',sum(1 for v in qs.values() if v),'of',len(lib))
def mk(docs_text):
    d_=[toks(t) for t in docs_text];N_=len(d_);avg_=sum(map(len,d_))/N_
    df_=Counter();[df_.update(set(d)) for d in d_]
    def sc(qtext):
        q=toks(qtext);out=[]
        for d in d_:
            tf=Counter(d);s=0
            for w in set(q):
                if w in tf:
                    idf=math.log(1+(N_-df_[w]+.5)/(df_[w]+.5));s+=idf*tf[w]*2.4/(tf[w]+1.4*(.25+.75*len(d)/avg_))
            out.append(s)
        return out
    return sc
sq=mk([' '.join(qs[i]) or x['text'] for i,x in enumerate(lib)])
sb=mk([x['text']+' '+' '.join(qs[i]) for i,x in enumerate(lib)])
def rrf2(lists,k=30,cc=60):
    s={}
    for l in lists:
        for r,i in enumerate(l):s[i]=s.get(i,0)+1/(cc+r+1)
    return dedupe([i for i,_ in sorted(s.items(),key=lambda t:-t[1])],k)
out={}
for S in 'ABCD':
    for n,a in enumerate(args[S]):
        q=a['issue']+' '+a['claim']
        W=word(a,30);B=bm(a,30);B0=bm(a,30,cw=0)
        R=rrf2([W,B],30)
        pool=dedupe(W[:20]+B[:20]+B0[:10],40)
        CE=cerank(a,pool,30)
        s1=sq(q);DQ=dedupe(sorted(range(len(lib)),key=lambda i:-s1[i])[:80],30)
        s2=sb(q);DQT=dedupe(sorted(range(len(lib)),key=lambda i:-s2[i])[:80],30)
        out[f'{S}{n}']={'W':W,'B':B,'B0':B0,'RRF':R,'CE':CE,'DQ':DQ,'DQT':DQT,'RRFDQ':rrf2([W,B,DQ]),'RRFALL':rrf2([W,B,DQ,CE]),'RRFDQT':rrf2([W,B,DQT])}
json.dump(out,open('/tmp/claude-0/w/cands4.json','w'))
json.dump([{'i':i,'case_id':x['case_id'],'citation':x['citation'],'issue':x['issue'],'result':x['result']} for i,x in enumerate(lib)],open('/tmp/claude-0/w/lib4.json','w'))
print('ok',len(out))
