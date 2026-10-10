import json,sys
S=sys.argv[1];gdir=sys.argv[2]
c=json.load(open('cands3.json'))
g={}
import glob
for f in glob.glob(gdir+'/graded_*.json'):g.update(json.load(open(f)))
def u(n,i):
    r=g.get(f'{n}_{i}');return bool(r) and r['useful']=='yes'
meths=list(c[S+'0'].keys())
rows=[]
for m in meths:
    t1=sum(u(n,c[f'{S}{n}'][m][0]) for n in range(20))
    t3=sum(any(u(n,i) for i in c[f'{S}{n}'][m][:3]) for n in range(20))
    rows.append((m,t1,t3))
for m in ['W','B','RRF','CE','DQ','RRFDQ','RRFALL']:
    try:p=json.load(open(f'pk/out_{S}_{m}.json'))
    except: continue
    k=0
    for r in p:
        if r['pick']:k+=u(r['id'],c[f'{S}{r["id"]}'][m][:10][r['pick']-1])
    rows.append(('Haiku pick over '+m,k,''))
for r in rows:print(r)
miss=sum(1 for n in range(20) if not any(u(n,i) for m in meths for i in c[f'{S}{n}'][m][:3]))
print('no useful in any top3:',miss)
