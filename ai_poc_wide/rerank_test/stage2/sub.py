import pandas as pd,re,json,glob,os
exec(open('/tmp/claude-0/w/rr/build.py').read().split("lib=lib0+lib1")[0])
norm=lambda c:re.sub(r'[^A-Za-z0-9]+','_',str(c)).strip('_')
done={norm(x['citation']) for x in lib0}|{os.path.basename(f)[:-19] for f in glob.glob(HERE+'out_claude_pilot/*_issues_claude.json')}
SQ=[
('H&C best interests of the child',r'best interests of the child|Kanthasamy',['FC']),
('PRRA new evidence 113(a)',r'paragraph 113\(a\)|Raza|new evidence.{0,60}PRRA|PRRA.{0,60}new evidence',['FC']),
('PRRA oral hearing',r'section 167|oral hearing.{0,80}PRRA|PRRA.{0,80}oral hearing',['FC']),
('Study permit dual intent',r'dual intent|intention to leave Canada.{0,80}study|study permit.{0,120}ties to',['FC']),
('Study permit funds',r'sufficient (financial )?(funds|resources).{0,100}study|study permit.{0,100}funds',['FC']),
('Work permit employer genuine',r'genuineness of the (job )?offer|section 200\(5\)|offer of employment.{0,60}genuine|employer.{0,40}genuine',['FC']),
('Visitor visa ties',r'temporary resident visa.{0,200}ties|ties to (his|her|their) (home )?country.{0,100}visitor|visitor visa',['FC']),
('Marriage bad faith',r'primary purpose|not genuine.{0,80}marriage|marriage.{0,80}bad faith|section 4 of the (Immigration and Refugee Protection )?Regulations',['FC']),
('Dependent child definition',r'dependent child|age of dependency|lock-in',['FC']),
('Criminality equivalency',r'equivalen(t|cy).{0,120}(Criminal Code|offence)|section 36\(1\)\(b\)|paragraph 36\(1\)\(b\)',['FC','FCA']),
('Innocent misrepresentation',r'innocent mistake|honest and reasonable belief|innocently|subsection 40\(1\)',['FC','FCA']),
('Security inadmissibility 34',r'section 34 of the|paragraph 34\(1\)|danger to the security of Canada',['FC','FCA']),
('IFA',r'internal flight alternative|IFA',['FC','RAD']),
('State protection presumption',r'clear and convincing|presumption of state protection',['FC','RAD','RPD']),
('Sur place',r'sur place',['FC','RAD']),
('Plausibility findings',r'implausib|plausibility finding|Valtchev',['FC','RAD']),
('RAD new evidence 110(4)',r'subsection 110\(4\)|110\(4\)',['FC','RAD']),
('RAD hearing 110(6)',r'subsection 110\(6\)|110\(6\)',['FC','RAD']),
('RAD standard Huruglica',r'Huruglica',['FC','FCA']),
('Fairness letter',r'procedural fairness letter|opportunity to respond to.{0,80}concerns',['FC']),
('Officer bias',r'reasonable apprehension of bias',['FC']),
('Alternatives to detention',r'alternatives? to detention|bond|release.{0,40}conditions',['FC']),
('Flight risk danger',r'flight risk|danger to the public|paragraph 58\(1\)',['FC','FCA']),
('Citizenship revocation',r'revocation.{0,100}Citizenship Act|section 10 of the Citizenship Act|obtained.{0,40}fraud.{0,60}citizenship',['FC','FCA']),
('Express Entry',r'Express Entry|Comprehensive Ranking System|express entry',['FC']),
('Stay irreparable harm',r'RJR-?MacDonald|irreparable harm.{0,80}removal|Toth',['FC']),
('Deferral of removal',r'defer(ral)? .{0,30}removal|Baron v|enforcement officer',['FC']),
('Certified question',r'serious question of general importance|Lunyk|certif\w+ question',['FC','FCA']),
('Mootness',r'moot|Borowski',['FC']),
('Charter s 7',r'section 7 of the Charter|security of the person',['FC','FCA']),
('Exclusion 1F(b)',r'1F\(b\)|serious non-political',['FC','RAD','RPD']),
('Vacation 109',r'section 109|vacat\w+ .{0,30}refugee|application to vacate',['FC','RAD','RPD']),
('IAD humanitarian Ribic',r'Ribic|Immigration Appeal Division.{0,100}humanitarian',['FC']),
('Mandamus delay',r'mandamus|Conille|unreasonable delay',['FC']),
('Residency obligation',r'residency obligation|section 28 of the|subsection 28\(2\)',['FC']),
]
cands={}
for court in('FC','FCA','RAD','RPD'):
    df=pd.read_parquet(f'hf/{court}.parquet',columns=['citation_en','name_en','unofficial_text_en'])
    df=df[df.citation_en.notna()&df.unofficial_text_en.notna()];df['cid']=df.citation_en.map(norm);df=df[~df.cid.isin(done)]
    df=df[df.unofficial_text_en.str.len().between(5000,70000)]
    if court in('FC','FCA'):df=df[df.unofficial_text_en.str.contains('Immigration and Refugee Protection|Citizenship Act|IRPA',regex=True)]
    for t,rx,cts in SQ:
        if court not in cts:continue
        c=re.compile(rx,re.I);cnt=df.unofficial_text_en.map(lambda x:len(c.findall(x)));d=cnt/df.unofficial_text_en.str.len()*1000
        k=df.assign(dens=d,cnt=cnt);k=k[k.cnt>=3]
        for _,r in k.nlargest(3,'dens').iterrows():cands.setdefault(t,[]).append((r.cid,round(r.dens,2),court))
    del df
out={};used=set()
for t,v in cands.items():
    v.sort(key=lambda x:-x[1]);sel=[]
    for cid,dn,ct in v:
        if cid in used:continue
        sel.append((cid,dn,ct));used.add(cid)
        if len(sel)==2:break
    out[t]=sel
print(sum(len(v) for v in out.values()),[ (t,len(v)) for t,v in out.items() if len(v)<2])
json.dump(out,open('sub_cands.json','w'))
