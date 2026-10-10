import json,re,math,sys
exec(open('/tmp/claude-0/w/retest.py').read().split("idx0=Index")[0])
lib_all=lib0+lib1;P={**paras0,**paras1}
def year(x):
    m=re.search(r'(19|20)\d\d',x.get('citation') or '') or re.match(r'((?:19|20)\d\d)_',str(x['case_id']))
    if m: return int(m.group(0)[:4])
    return 2010 # RAD/RPD ids modern
IMM=re.compile(r'Immigration and Refugee|IRPA|refugee|Citizenship Act|permanent resident|visa|removal order|inadmissib|work permit|study permit',re.I)
def isimm(x):
    if x['court'] in('FC','FCA','RAD','RPD'):return True
    t=' '.join(P.get(x['case_id'],{}).get(k,'') for k in list(P.get(x['case_id'],{}))[:15])
    return bool(IMM.search(t))
lib=[x for x in lib_all if year(x)>=2005 and isimm(x)]
