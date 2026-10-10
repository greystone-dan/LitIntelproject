import pandas as pd,re,json,glob,os
exec(open('/tmp/claude-0/w/rr/build.py').read().split("lib=lib0+lib1")[0])
norm=lambda c:re.sub(r'[^A-Za-z0-9]+','_',str(c)).strip('_')
done={norm(x['citation']) for x in lib0}|{os.path.basename(f)[:-19] for f in glob.glob(HERE+'out_claude_pilot/*_issues_claude.json')}

SQ=[
('plausibility RPD',r'implausib\w*|plausibility',['FC','RAD','RPD']),
('bias visa officer interview',r'reasonable apprehension of bias|officer.{0,60}(interview|biased)',['FC']),
('alternatives to detention',r'alternatives? to detention|alternative to detention|bondsperson|release.{0,40}conditions',['FC','RPD']),
('citizenship revoke notice',r'revocation|revoke.{0,60}citizenship|notice of the case|section 10 of the Citizenship Act',['FC','FCA']),
('Express Entry NOC duties',r'Express Entry|National Occupational Classification|NOC (code|duties)|lead statement|main duties',['FC']),
('spousal intention to live together',r'intend(s|ed)? to live (together|with)|genuine relationship|bona fide.{0,60}(spouse|marriage)',['FC']),
('flight risk ID',r'flight risk|unlikely to appear|identity.{0,60}(not established|established)|efforts to establish (his|her|their) identity',['FC']),
('study permit program of study',r'study plan|program of study|career path|makes? sense.{0,80}(program|study)',['FC']),
('employer compliance conditions',r'compliance.{0,80}(conditions|employer)|employer.{0,60}(non-compliance|compliance)|section 203\(1\)\(e\)',['FC']),
('prior travel visitor',r'travel history|previous(ly)? travel|returned.{0,40}(on time|as required)',['FC']),
('gender guidelines',r'Gender Guidelines|Chairperson.s Guideline 4|gender-based|domestic violence',['FC','RAD','RPD']),
('1F(b) political',r'1F\(b\)|serious non-political crime|political offen[cs]e|political context',['FC','RAD','RPD']),
]
cands={}
import datetime
for court in('FC','FCA','RAD','RPD'):
    df=pd.read_parquet(f'hf/{court}.parquet',columns=['citation_en','name_en','unofficial_text_en'])
    df=df[df.citation_en.notna()&df.unofficial_text_en.notna()];df['cid']=df.citation_en.map(norm);df=df[~df.cid.isin(done)]
    df=df[df.unofficial_text_en.str.len().between(5000,60000)]
    yr=df.cid.str.extract(r'^(\d{4})_')[0].astype(float)
    df=df[(yr.isna())|(yr>=2005)]
    if court in('FC','FCA'):df=df[df.unofficial_text_en.str.contains('Immigration and Refugee Protection|Citizenship Act|IRPA',regex=True)]
    for t,rx,cts in SQ:
        if court not in cts:continue
        c=re.compile(rx,re.I);cnt=df.unofficial_text_en.map(lambda x:len(c.findall(x)));d=cnt/df.unofficial_text_en.str.len()*1000
        k=df.assign(dens=d,cnt=cnt);k=k[k.cnt>=3]
        for _,r in k.nlargest(4,'dens').iterrows():cands.setdefault(t,[]).append((r.cid,round(r.dens,2),court))
    del df
out={};used=set()
for t,v in cands.items():
    v.sort(key=lambda x:-x[1]);sel=[]
    for cid,dn,ct in v:
        if cid in used:continue
        sel.append((cid,dn,ct));used.add(cid)
        if len(sel)==4:break
    out[t]=sel
json.dump(out,open('/tmp/claude-0/w/sub2_cands.json','w'))
print(sum(len(v) for v in out.values()))
