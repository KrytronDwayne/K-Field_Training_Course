"""Independent finite checks using exact Fraction arithmetic and explicit DFT matrix."""
from pathlib import Path
from fractions import Fraction as F
import json, hashlib
R=Path(__file__).resolve().parent
checks=[]
def check(name,actual,expected):
 assert actual==expected,(name,actual,expected)
 checks.append({'check':name,'actual':str(actual),'expected':str(expected),'status':'passed'})
raw=list(map(F,[2,5,8,1,3])); clear=list(map(F,[10,0,20,10,10]))
ratios=[a/c if c else None for a,c in zip(raw,clear)]
check('Clear ratios',ratios,[F(1,5),None,F(2,5),F(1,10),F(3,10)])
check('Raw reconstruction including undefined branch',[r*c if r is not None else a for a,c,r in zip(raw,clear,ratios)],raw)
check('Ten significant digits closure',F(1,3)-F('0.3333333333'),F(1,30000000000))
check('Exposure row2',[F(2)-F(1,10),F(2)+F(1,10)],[F(19,10),F(21,10)])
def split(x,other): return ([F(a+b,2) for a,b in zip(x,other)],[F(a-b,2) for a,b in zip(x,other)])
for x,s,a in [([1,2,4,3],[2,3,3,2],[-1,-1,1,1]),([3,1,-1,1],[2,0,0,2],[1,1,-1,-1]),([-2,0,2],[0,0,0],[-2,0,2])]:
 actual=split(x,x[::-1]); check('Reflection '+str(x),actual,(list(map(F,s)),list(map(F,a))))
 check('Reflection reconstruction '+str(x),[u+v for u,v in zip(*actual)],x)
 check('Same parity '+str(x),actual[0][::-1],actual[0]); check('Inverted parity '+str(x),actual[1][::-1],[-v for v in actual[1]])
M=[[1,1,1,1],[1,-1j,-1,1j],[1,-1,1,-1],[1,1j,-1,-1j]]
def dft(x): return [sum(c*v for c,v in zip(row,x)) for row in M]
def inv(y): return [sum(complex(M[j][k]).conjugate()*y[j] for j in range(4))/4 for k in range(4)]
for x,e,o,ff in [([1,2,3,4],[2,3,2,3],[-1,-1,1,1],[0,-2+2j,0,-2-2j]),([3,1,-1,1],[1,1,1,1],[2,0,-2,0],[0,4,0,4])]:
 h=x[2:]+x[:2]; actual=split(x,h)
 check('Half turn '+str(x),actual,(list(map(F,e)),list(map(F,o))))
 check('Half turn reconstruction '+str(x),[u+v for u,v in zip(*actual)],x)
 check('Odd DFT '+str(x),dft(o),ff); check('Odd inverse '+str(x),inv(ff),o)
 for shift in range(4):
  shifted=e[shift:]+e[:shift]
  check('Comparator dot shift '+str(shift)+' for '+str(x),sum(u*v for u,v in zip(shifted,o)),0)
check('Pulse magnitudes',[abs(v) for v in dft([1,0,0,0])],[abs(v) for v in dft([0,1,0,0])])
check('Pulse inverse',inv(dft([0,1,0,0])),[0,1,0,0])
for indices,expected_mean,expected_detail in [(list(range(5)),F(19,5),[F(-9,5),F(6,5),F(21,5),F(-14,5),F(-4,5)]),([1,2,3],F(14,3),[F(1,3),F(10,3),F(-11,3)])]:
 x=[raw[i] for i in indices]; m=sum(x)/len(x); d=[v-m for v in x]
 check('Mean '+str(indices),m,expected_mean); check('Detail '+str(indices),d,expected_detail)
 check('Mean/detail reconstruction '+str(indices),[m+v for v in d],x); check('Detail closure '+str(indices),sum(d),0)
events=[t for t in range(5) if F(t,2).denominator==1]
check('Frozen events',events,[0,2,4])
raw_windows=[]; ratio_masks=[]
for t in events:
 ids=[t-1,t,t+1]
 raw_windows.append([raw[i] if 0<=i<5 else None for i in ids])
 ratio_masks.append([int(0<=i<5 and ratios[i] is not None) for i in ids])
check('Raw windows',raw_windows,[[None,2,5],[5,8,1],[1,3,None]])
check('Ratio support masks',ratio_masks,[[0,1,0],[0,1,1],[1,1,0]])
check('Side difference',raw[1]-raw[3],4); check('Side sum',raw[1]+raw[3],6)
products=[k*x for k in [F('1.9'),F('2.1')] for x in [F('.9'),F('1.1')]]
check('Box bounds',[min(products),max(products)],[F('1.71'),F('2.31')])
check('Timing support',[F(2)-F('.1')-F('.1'),F(2)+F('.1')+F('.1')],[F('1.8'),F('2.2')])
check('Forward midpoint schedule',list(range(10)),[0,1,2,3,4,5,6,7,8,9])
check('Rubric total',9*4,36)
for n in range(1,9):
 text=(R/f'lesson-{n:02}.md').read_text(encoding='utf-8')
 for anchor in [f'C28.{n:02}-E1',f'C28.{n:02}-W1',f'C28.{n:02}-P1',f'C28.{n:02}-D1','Essential question:','## Prerequisite bridge','**Student task.**','### Worked answer','Next dependency:']:
  assert anchor in text,(n,anchor)
 checks.append({'check':f'lesson-{n:02} contract and exact exercise anchors','status':'passed'})
out={'schema_version':'1.0','status':'passed','scope':'Finite synthetic arithmetic, exact Fraction ratios/means/bounds; independent DFT matrix and conjugate inverse; structural anchor checks. Does not certify source experiments or replace human teaching audit.','check_count':len(checks),'checks':checks}
(R/'worked-example-verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks)}))
