"""Exact rational checks of authored examples; no source copies or packages."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,sys,re
R=Path(__file__).resolve().parent
checks=[]
def check(label,test,evidence):
    assert test,label
    checks.append({'check':label,'result':'passed','evidence':evidence})
def rows(ds):
    signed=[sum(ds[j]*3**j for j in range(d)) for d in range(1,len(ds)+1)]
    return signed,[s%3**d for d,s in enumerate(signed,1)]
for ds,ss,aa in [([1,-1,0,1,-1],[1,-2,-2,25,-56],[1,7,25,25,187]),([0,1,-1,0,1],[0,3,-6,-6,75],[0,3,21,75,75]),([-1]*4,[-1,-4,-13,-40],[2,5,14,41]),([1]*4,[1,4,13,40],[1,4,13,40])]:
    check('prefix '+str(ds),rows(ds)==(ss,aa) and all(aa[d]%(3**d)==aa[d-1] for d in range(1,len(aa))),{'signed':ss,'residues':aa})
check('incompatible proposal',8%3==2 and 8%3!=1,'Preserved (1,8), failed reduction.')
def delta(a,b):
    n=abs(a-b); k=0
    if n==0:return F(0)
    while n%3==0:n//=3;k+=1
    return F(1,3**k)
check('distances',delta(1,28)==F(1,27) and delta(4,13)==F(1,9) and delta(1,2)==1 and delta(0,81)==F(1,81) and max(delta(1,28),delta(4,13),delta(0,0))==F(1,9),'Difference factoring and coordinate maximum recomputed.')
check('depth thresholds',F(1,128)<=F(1,100)<F(1,64) and F(1,2916)<=F(1,1000)<F(1,972) and F(1,2187)<=F(1,1000)<F(1,729) and F(1,32)<F(1,16),'Binary N7, normalized ternary N6, physical N7; binary practice N5.')
render=lambda ds:sum(F(u,2*3**j) for j,u in enumerate(ds,1))
check('signed rendering',render([1,1])==F(2,9) and render([-1,-1])==-F(2,9) and -F(1,2)-2*render([-1,-1])==-F(1,18),'All-positive and capstone all-negative depth2 images and signed displacement tail.')
check('endpoint histories',F(1,2)*(F(1,3)-F(1,6))==F(1,12)==F(1,2)*F(1,6) and render([1,-1])==F(1,9) and render([0,1])==F(1,18),'Both infinite images1/12; signed depth2 tails −1/36,+1/36.')
check('depth3 image',render([1,1,1])==F(13,54) and F(1,4)-F(13,54)==F(1,108),'Normalized all-positive partial and exact tail.')
# Exhaustive small-tail check of bound without using the lesson examples as expected output.
for N in range(1,5):
    for ds in product([-1,0,1],repeat=4):
        tail=sum(F(u,2*3**(N+j)) for j,u in enumerate(ds,1))
        assert abs(tail)<=F(1,4*3**N)
check('finite tail exhaustive check',True,'324 signed four-digit tails at N1..4 satisfy the symbolic absolute bound; infinite statement is proved in lesson04.')
check('cylinder digits',[rows(d)[1][-1] for d in ([1,-1,1],[1,-1,-1],[1,-1,0])]==[7,16,25] and all(a%9==7 for a in [7,16,25]),'Third balanced digits1,−1,0 retained; all outputs7.')
P0=[[F(1,4)]*4 for i in range(4)]
P1=[[F(int(i//2==j//2),2) for j in range(4)] for i in range(4)]
I=[[F(int(i==j)) for j in range(4)] for i in range(4)]
sub=lambda A,B:[[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]
Q0=sub(P1,P0);Q1=sub(I,P1)
mm=lambda A,B:[[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
mv=lambda A,v:[sum(a*b for a,b in zip(row,v)) for row in A]
Z=[[F(0)]*4 for i in range(4)]
sectors=[P0,Q0,Q1]
check('projectors',all(mm(A,A)==A and A==[list(x) for x in zip(*A)] for A in [P0,P1,Q0,Q1]) and all(mm(A,B)==Z for i,A in enumerate(sectors) for j,B in enumerate(sectors) if i!=j) and mm(P0,P1)==P0 and mm(P1,P0)==P0,'Exact 4x4 rational products; nested P1 correctly excluded from disjoint-sector zero-product claim.')
for v,expected in [([1,3,5,7],[[4]*4,[-2,-2,2,2],[-1,1,-1,1]]),([2,0,6,4],[[3]*4,[-2,-2,2,2],[1,-1,1,-1]])]:
    got=[mv(A,v) for A in sectors]
    check('reconstruction '+str(v),got==expected and [sum(col) for col in zip(*got)]==v,str(expected))
check('zero detail',mv(Q1,[2]*4)==[0]*4,'All four zero coordinates retained.')
check('finite product',1*(5-2)+2*(3-1)+(3-1)*(5-2)==3*5-1*2==13,'Terms3,4,6, total13.')
for k in range(8):
    block=sum(F(1,n*n) for n in range(2**k,2**(k+1)))
    assert block<=F(1,2**k)
check('sequence blocks',True,'First8 rational blocks satisfy2^-k; general proof uses2^k terms each≤2^-2k.')
for n in range(1,100):
    assert n*n*F(1,n*n)**2==F(1,n*n)
    assert F(1,n**6)<=F(1,n**4)<=F(1,n**2)
check('domain identities',True,'Weighted-square identities checked at99 n; general cancellation and comparison proved in lesson07, no finite replay promoted to infinite proof.')
for i in range(1,8):
    lesson=(R/f'lesson-{i:02}.md').read_text(encoding='utf-8')
    for k in 'EWPD':assert f'C22.{i:02}-{k}1' in lesson
    for phrase in ['Essential question:','Goals:','Bridge and pacing:','Claim scope:','Next dependency:','Worked answers:']:assert phrase in lesson
    assert len(re.findall(r'^\d\. ',lesson,re.M))==4
cap=(R/'capstone.md').read_text(encoding='utf-8')
assert all(f'C22-CAP-{i:02}' in cap and f'C22.{i:02}-P1' in cap and f'C22.{i:02}-E1' in cap for i in range(1,8))
check('content contract and E05 links',True,'28 actual E/W/P/D anchors, four answered diagnostics each, seven capstone trails; substantive alignment separately audited.')
report={'status':'passed','runtime':sys.executable,'checks':checks,'scope':'Independent rational recomputation and finite exhaustive checks, plus actual content-anchor checks. Infinite claims use the explicit proofs; no empirical data are generated.'}
(R/'worked-example-verification.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','check_groups':len(checks),'runtime':sys.executable}))
