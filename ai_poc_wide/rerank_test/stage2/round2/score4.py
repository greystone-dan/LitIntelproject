import json,glob
c=json.load(open('cands4.json'));old=json.load(open('g6/cache.json'));L=json.load(open('lib4.json'))
g={}
for f in glob.glob('g6/graded_*.json'):g.update(json.load(open(f)))
def u(S,n,i):
    k=f'{S}{n}_{i}'
    if k in g:return g[k]['useful']=='yes'
    x=L[i];r=old.get(f"{S}|{n}|{x['case_id']}|{x['issue']}")
    return bool(r) and r['useful']=='yes'
meths=['W','B','B0','RRF','CE','DQ','DQT','RRFDQ','RRFDQT','RRFALL']
print('method',*['%s t1/t3'%S for S in 'ABCD'],'ABC t1/t3','D(new) t1/t3')
for m in meths:
    row=[];ab1=ab3=0
    for S in 'ABCD':
        t1=sum(u(S,n,c[f'{S}{n}'][m][0]) for n in range(20));t3=sum(any(u(S,n,i) for i in c[f'{S}{n}'][m][:3]) for n in range(20))
        row.append(f'{t1}/{t3}')
        if S!='D':ab1+=t1;ab3+=t3
    print(m,*row,f'{ab1}/{ab3}')
anyd=lambda S:sum(any(u(S,n,i) for m in meths for i in c[f'{S}{n}'][m][:3]) for n in range(20))
print('any method top3',{S:anyd(S) for S in 'ABCD'})
