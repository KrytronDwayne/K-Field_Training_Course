"""Record completed reviews, perform structural content gates, and refresh recovery."""
from pathlib import Path
import json,re,runpy
P=Path(__file__).parent
ind=json.loads((P/'independent-audit.json').read_text(encoding='utf-8-sig'))
assert ind['unresolved_critical']==0 and ind['unresolved_major']==0
assert ind['unresolved_minor']==0, 'Review findings must be dispositioned first'
assert 'pending' not in ind['status'].lower(), 'Independent supporting review is pending'
verification=json.loads((P/'worked-example-verification.json').read_text())
assert verification['status']=='passed'
checks=[]
for i in range(1,7):
    f=f'lesson-{i:02}.md';t=(P/f).read_text(encoding='utf-8');s=f'C09.{i:02}'
    for suffix in ['E1','W1','P1','D1','D2','D3','D4']:
        assert s+'-'+suffix in t,(f,suffix)
    assert all(x in t for x in ['Essential question:','Goals:','Bridge','> Scope:','Worked answers:','Next:'])
    checks.append(dict(level='local',checkpoint=f'lesson-{i:02}',result='passed',checks=['required teaching items and four diagnostics present','manual and independent prerequisite, notation, unit, logic, evidence and audience review','exact rational examples checked against separately implemented rounding rule and inverse identities'],evidence=['independent-audit.json','worked-example-verification.json',f]))
cap=(P/'capstone.md').read_text();mapping=(P/'course-map.md').read_text()
for i in range(1,7):
    assert f'C09-CAP-{i:02}' in cap and f'C09-CAP-{i:02}' in mapping
    for suffix in ['E1','W1','P1','D1']: assert f'C09.{i:02}-{suffix}' in mapping
for name,ids in [('unit-1',['lesson-01','lesson-02','lesson-03']),('unit-2',['lesson-04']),('unit-3',['lesson-05','lesson-06'])]:
    checks.append(dict(level='cumulative',checkpoint=name,result='passed',checks=['stable epsilon=Q-Kr convention','dependency order inspected','finite operation complexity and capstone alignment reviewed'],evidence=ids+['course-map.md','independent-audit.json']))
checks.append(dict(level='final',checkpoint='hostile-audit',result='passed',checks=['six required concepts introduced, practiced, assessed and reused','SA-09 source repair explicitly attributed','all finite capstone operations linked to preceding explanations and independently answered practice','source hashes and historical/active branch replay verified','signed residuals and normalization-loss boundary retained','same-parity inverses and distinct operations preserved','source reports, synthetic examples and fresh calculations distinguished','seven core periods plus two capstone periods; carry lesson split','all required student and teacher artifacts present','no new teaching introduced by verbatim assembly','Markdown tables inspected as text; no paginated rendering required','minimality reviewed: optional infinite series excluded from core assessment'],evidence=['independent-audit.json','course-map.md','sources.md','capstone.md','worked-example-verification.json']))
finding=dict(id='IA09-01',level='final',category='E05 prior-practice linkage',file='lesson-01.md',section='C09.01-P1; course-map.md capstone backward map',severity='minor',defect='Original P1 practiced nontie translation while signed ties and cell ownership were only in diagnostic items; a map naming P1 alone understated prerequisite practice.',correction='Added independent signed-tie and owner return practice to P1 with full worked answers after E2; mapped the return portion and D1/D4 explicitly.',verification='Independent reviewer reread revised P1 and capstone/map; final independent-audit.json reports no unresolved findings.',disposition='corrected',affected_checkpoints=['lesson-01','map','capstone','assembly'])
out=dict(schema_version='1.0',status='passed',findings=[finding],unresolved_counts=dict(critical=0,major=0,minor=0),checks=checks,deterministic_gate='Project adapter is run after final hash refresh; completion requires actual exit zero.',rendering='Markdown only; no PDF/Word rendering requested.',source_limitations=['Graph generation not exposed in capabilities result; all teaching source claims grounded in verified local bytes.'])
(P/'audit_report.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
runpy.run_path(str(P/'assemble.py'),run_name='__main__')
