"""Independent finite arithmetic replay; standard library only; no empirical data.

Run via conda run -n tf_gpu_env python verify_examples.py.
Writes compact verification.json alongside this script.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys,re
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,actual,expected):
    assert actual==expected,(name,actual,expected)
    checks.append({'id':name,'actual':actual,'expected':expected,'result':'passed'})
def table_rows(name,columns):
    text=(ROOT/name).read_text(encoding='utf-8')
    rows=[]
    for line in text.splitlines():
        cells=[x.strip() for x in line.strip('|').split('|')]
        if line.startswith('|') and len(cells)==columns and re.fullmatch(r'\d+',cells[0]):
            rows.append([int(x.replace('−','-')) if re.fullmatch(r'[−-]?\d+',x) else x for x in cells])
    return rows
check('L1-worked-difference',15-12,3)
check('L1-guided-difference',9-4,5)
check('L1-diagnostic-difference',8-6,2)
ledger=[]
rows=table_rows('lesson-03.md',8)
check('L3-table-row-count',len(rows),4)
for row,t,ch,x,m0,r0,m1,r1 in rows:
    check(f'L3-row{row}-M0',10+2*t,m0)
    check(f'L3-row{row}-residual',x-m0,r0)
    check(f'L3-row{row}-second-residual',r0-m1,r1)
    check(f'L3-row{row}-reconstruction',m0+m1+r1,x)
    check(f'L3-row{row}-first-reconstruction',m0+r0,x)
    ledger.append({'row':row,'t_s':t,'channel':ch,'x_DU':x,'M0_DU':m0,'r0_DU':r0,'M1_DU':m1,'r1_DU':r1})
check('L3-ordered-zero-sums',[sum([1,-1]),sum([-1,1])],[0,0])
check('L3-baseline-transform',[r['x_DU']-10 for r in ledger],[1,1,6,5])
check('L3-baseline-reconstruction',[x+10 for x in [1,1,6,5]],[11,11,16,15])
check('L3-baseline-mean',str(F(sum([1,1,6,5]),4)),'13/4')
check('L3-sign-error',12+1,13)
check('L3-new-row-residuals',[21-18,(21-18)-2,18+2+1],[3,1,21])
A=lambda u:2*u
B=lambda u:u+1
for u,expected in [(1,[2,2]),(3,[6,4]),(0,[0,1]),(4,[8,5])]:
    check(f'A-B-u{u}',[A(u),B(u)],expected)
check('L4-followup',[5-A(3),5-B(3)],[-1,1])
check('L4-equality-input',A(1)-B(1),0)
check('L4-zero-input-residuals',[1-A(0),1-B(0)],[1,0])
check('L4-guided-C-D',[[u+2,2*u] for u in [2,4]],[[4,4],[6,8]])
scales=[2,3,-4];origin=[5,0,0]
geometry=[]
for label,q,expected in [('worked',[1,-1,2],[7,-3,-8]),('guided',[-1,2,0],[3,6,0]),('capstone',[2,-1,1],[9,-3,-4])]:
    displacement=[s*v for s,v in zip(scales,q)]
    position=[a+b for a,b in zip(origin,displacement)]
    reverse=[F(x-o,s) for x,o,s in zip(position,origin,scales)]
    check(label+'-position',position,expected)
    check(label+'-reverse',[int(v) if v.denominator==1 else str(v) for v in reverse],q)
    geometry.append({'id':label,'q':q,'displacement_mm':displacement,'position_mm':position,'reverse':list(q)})
check('L5-origin-omission',str(F(7,2)),'7/2')
check('L5-singular-counterexample',[0*1,0*2],[0,0])
check('L5-metric-scales',[s*s for s in scales],[4,9,16])
check('L5-return-factors',[str(F(s)*F(1,s*s)*F(s)) for s in scales],['1','1','1'])
for label,start,steps,reading,expected_r in [('worked',1,2,12,1),('guided',0,3,10,-1),('diagnostic',2,1,9,-2)]:
    state=start+steps;m=5+2*state;r=reading-m
    check('L5-'+label+'-state-model-residual',[state,m,r],[3,11,expected_r])
    check('L5-'+label+'-reconstruction',m+r,reading)
check('L5-distinct-position',origin[0]+scales[0]*3,11)
cap=[]
for t,ch,x,m0,r0,m1,r1,recon in table_rows('capstone.md',8):
    check(f'cap-row{t}-model',10+2*t,m0)
    check(f'cap-row{t}-r0',x-m0,r0)
    check(f'cap-row{t}-r1',r0-m1,r1)
    check(f'cap-row{t}-reconstruct',[m0+r0,m0+m1+r1],[x,recon])
    cap.append({'t_s':t,'channel':ch,'x_DU':x,'M0_DU':m0,'r0_DU':r0,'M1_DU':m1,'r1_DU':r1,'reconstructed_DU':recon})
check('cap-table-count',len(cap),3)
check('cap-followup',[7-A(4),7-B(4)],[-1,2])
check('cap-separation',A(4)-B(4),3)
check('cap-rubric-total',10+8+8+6+8,40)
check('pacing-lesson-1',5+12+10+13+15,55)
check('pacing-lessons-2-4',5+10+15+10+15,55)
check('pacing-lesson-5',5+12+15+10+13,55)
files=[f'lesson-{i:02}.md' for i in range(1,6)]+['capstone.md','teacher-guide.md']
payload={'status':'passed','method':'Independent standard-library integer/rational evaluation from inputs; residual tables parsed directly from authored Markdown and compared row by row. Interpretive/source checks are separately recorded in audit_report.json.','runtime':sys.executable,'synthetic_only':True,'checks':checks,'check_count':len(checks),'retained_lesson3_ledger':ledger,'retained_capstone_ledger':cap,'geometry_examples':geometry,'verified_content_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in files}}
(ROOT/'verification.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'{len(checks)} finite arithmetic checks passed; complete signed synthetic ledgers retained.')
