import json,glob,sys,os
sys.path.insert(0,'/home/user/LitIntelproject/ai_poc_wide')
import match_draft as md
from match_library import Index
HERE='/home/user/LitIntelproject/ai_poc_wide/'
lib0,paras0=md.load_library()
# pilot maps
links={x['case_id']:x for x in json.load(open(HERE+'out_claude_pilot/_link_to_live_cases.json'))}
pp={}
for f in glob.glob('/tmp/claude-0/w/pil*/dec_*.json'):
    d=json.load(open(f));pp.setdefault(d['case_id'],{}).update({}) 
    pp[d['case_id']]={}
    for q in d['paragraphs']:(pp[d['case_id']].__setitem__(q['paragraph_index'],q['text']) if len(q['text'])>len(pp[d['case_id']].get(q['paragraph_index'],'')) else None)
    pp[d['case_id']]['_court']=d['court']
S='_issues_claude.json'
lib1=[];paras1={}
for f in sorted(glob.glob(HERE+'out_claude_pilot/*'+S)):
    cid=os.path.basename(f)[:-len(S)]
    if cid not in pp: continue
    x=json.load(open(f))
    paras1[cid]={k:v for k,v in pp[cid].items() if k!='_court'}
    cit=links.get(cid,{}).get('citation') or cid
    for i in x['result']['issues']:
        lib1.append({'case_id':cid,'citation':cit,'court':pp[cid]['_court'],'issue':i['issue'],'result':i['result'],'result_para':i['result_para'],'soften':'' if i['result_para'] and i['result']!='not_decided' else 'No paragraph states a result for this issue.','text':i['issue']+' '+i['applicant_position']})
print('pilot decisions',len(paras1),'issues',len(lib1),'base issues',len(lib0))
# 32 draft args
args=[]
for f in sorted(glob.glob(HERE+'out_chain/out/*_chain.json')):
    d=json.load(open(f))
    for i,r in enumerate(d['results']):args.append({'key':os.path.basename(f)[:-11]+f'#{i}','arg':r['argument']})
print('args',len(args))
idx0=Index(lib0);idx1=Index(lib0+lib1);P0=dict(paras0);P1={**paras0,**paras1}
out=[]
for a in args:
    A=a['arg'];ex=None
    m0=md.match_argument(idx0,P0,A,ex);m1=md.match_argument(idx1,P1,A,ex)
    b0=m0['best'] if m0 else None;b1=m1['best'] if m1 else None
    out.append({'key':a['key'],'issue':A['issue'],'claim':A['claim'],'quote':A.get('quote',''),'old':b0,'new':b1,'changed':(b0 or {}).get('citation')!=(b1 or {}).get('citation') or (b0 or {}).get('issue')!=(b1 or {}).get('issue')})
json.dump(out,open('/tmp/claude-0/w/retest_out.json','w'))
print('changed',sum(o['changed'] for o in out),'of',len(out),'library issues',len(lib0)+len(lib1))
