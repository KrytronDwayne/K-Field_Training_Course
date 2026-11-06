"""Exact independent finite checks for the authored teaching examples."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,sys,hashlib
D=Path(__file__).resolve().parent
checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
def add(v,w):return tuple(a+b for a,b in zip(v,w))
def mul(c,v):return tuple(c*a for a in v)
def dot(v,w):return sum(a*b for a,b in zip(v,w))
def T(v):return v[2],v[0],v[1]
def power(v,n):
    for _ in range(n):v=T(v)
    return v
e=((1,0,0),(0,1,0),(0,0,1)); a1=(1,-1,0);a2=(0,1,-1)
roots={add(e[i],mul(-1,e[j])) for i in range(3) for j in range(3) if i!=j}
check('L01 W1 swap norm and sum',sum((2,5))==sum((5,2))==7 and dot((2,5),(2,5))==29)
for v in product(range(-2,3),repeat=3):
    for i,j in product(range(3),repeat=2):
        assert power(power(v,j),i)==power(v,(i+j)%3)
    assert sum(v)==sum(T(v)) and dot(v,v)==dot(T(v),T(v))
checks.append('L01 P1 all 9 table entries and invariants on 125 signed triples plus symbolic argument in text')
check('L01 D2-D4',dot((-2,4),(-2,4))==20 and power((1,2,3),5)==power((1,2,3),2) and dot((3,4),(3,4))==25)
for b,c in product(range(-5,6),repeat=2):
    S,A=b+c,b-c
    assert (S+A)//2==b and (S-A)//2==c and (b+1)-(c-1)==A+2
    r=A%2;k=(A-r)//2
    assert A==r+2*k and S%2==A%2
checks.append('L02 inverse, parity and transfer exhaustive on 121 pairs')
check('L02 W1/P1/D2/D3',[(b+c,b-c) for b,c in [(2,1),(3,0),(-1,3),(0,2),(1,-2),(0,-1)]]==[(3,1),(3,3),(2,-4),(2,-2),(-1,3),(-1,1)] and -5==1+2*(-3))
check('L03 six roots/Cartan',len(roots)==6 and all(sum(r)==0 and dot(r,r)==2 for r in roots) and [[F(2*dot(a,b),dot(b,b)) for b in (a1,a2)] for a in (a1,a2)]==[[2,-1],[-1,2]])
for x,z in product(range(-5,6),repeat=2):assert add(mul(x,a1),mul(-z,a2))==(x,-x-z,z)
checks.append('L03 reconstruction for 121 integer zero-sum triples')
check('L03 W1/P1/D2',add(mul(2,a1),mul(-1,a2))==(2,-3,1) and add(mul(-1,a1),mul(2,a2))==(-1,3,-2) and add(mul(3,a1),mul(2,a2))==(3,-1,-2))
check('L03 D1/D3/D4',sum((F(1,2),F(-1,2),0))==0 and dot(mul(2,a1),mul(2,a1))==8 and dot(a2,add(a1,a2))==1)
# Drawing proof without floating rounding: norms 2 and dot -1 follow directly.
check('L03 drawing coordinates squared norms',F(1,2)+F(3,2)==2)
h=(F(1,3),)*3
u=tuple(add(v,mul(-1,h)) for v in e)
check('L04 centering and sum',add(add(u[0],u[1]),u[2])==(0,0,0) and add(u[0],mul(-1,u[1]))==a1)
for a,b in product(range(-7,8),repeat=2):
    w=add(mul(a,u[0]),mul(b,u[1]))
    assert all(t.denominator==1 for t in w)==((a+b)%3==0)
    r=(a+b)%3;q=add(w,mul(-r,u[0]))
    assert all(t.denominator==1 for t in q) and add(mul(r,u[0]),q)==w
checks.append('L04 class criterion and representative reconstruction for 225 coefficient pairs')
check('L04 P1/D2/D3',add(u[0],u[1])==(F(1,3),F(1,3),F(-2,3)) and add(mul(2,u[0]),u[1])==(1,0,-1) and mul(-1,u[0])==(F(-2,3),F(1,3),F(1,3)) and add(mul(4,u[0]),mul(-1,u[1]))==(3,-2,-1))
rho=(1,0,0)
lifts=[add(rho,mul(3,v)) for v in product((-1,0,1),repeat=3)]
check('L05 all 27 distinct next-level lifts reduce correctly',len({tuple(t%9 for t in l) for l in lifts})==27 and all(tuple(t%3 for t in l)==rho for l in lifts))
check('L05 W1/P1/D2/D3',add(rho,mul(3,(0,1,-1)))==(1,3,-3) and add(rho,mul(3,(-1,0,1)))==(-2,0,3) and add(rho,mul(3,(1,1,1)))==(4,3,3) and mul(F(1,3),add((1,-3,3),mul(-1,rho)))==(0,-1,1))
check('L06 roots, orbit, diagnostic',{T(r) for r in roots}==roots and T(a1)==a2 and T(a2)==(-1,0,1) and [power((2,-3,1),n) for n in range(4)]==[(2,-3,1),(1,2,-3),(-3,1,2),(2,-3,1)] and T((-1,3,-2))==(-2,-1,3))
for v in product(range(-2,3),repeat=3):
    for w in e:assert dot(T(v),T(w))==dot(v,w)
    assert mul(2,T(v))==T(mul(2,v))
checks.append('L06 dot-product on spanning basis and doubling intertwiner; counterexample identity action T(a1)!=a1')
check('L06 false identity intertwiner rejected',T(a1)!=a1)
report={'status':'passed','runtime':sys.executable,'method':'Exact Fraction arithmetic; finite enumerations independently computed from vector rules; symbolic general proofs in lessons','checks':checks,'source_copies_created':False}
(D/'worked-example-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
