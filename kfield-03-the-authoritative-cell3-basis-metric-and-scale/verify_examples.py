"""Read original sources; retain only compact authored verification coordinates."""
from pathlib import Path
from decimal import Decimal as D, getcontext, ROUND_HALF_EVEN
from fractions import Fraction as F
import json, hashlib, sys

p=Path(__file__).parent
c=json.loads((p/'input-contract.json').read_text(encoding='utf-8-sig'))
getcontext().prec=60
getcontext().rounding=ROUND_HALF_EVEN
def tr(a): return [list(x) for x in zip(*a)]
def mul(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in tr(b)] for row in a]
def sub(a,b): return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def cross(a,b): return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def strings(a): return [[str(x) for x in row] for row in a]
I=[[F(int(i==j)) for j in range(3)] for i in range(3)]
B=[[F(x) for x in row] for row in [[1,1,0],[0,2,0],[0,0,-3]]]
M=mul(tr(B),B)
R=[[F(5,4),F(-1,4),F(0)],[F(-1,4),F(1,4),F(0)],[F(0),F(0),F(1,9)]]
assert M==[[1,1,0],[1,5,0],[0,0,9]]
assert mul(M,R)==I and mul(R,M)==I and mul(mul(B,R),tr(B))==I
a,b,d=tr(B)
faces=[cross(a,b),cross(a,d),cross(b,d)]
assert faces==[[0,0,2],[0,3,0],[-6,3,0]]
assert [dot(v,v) for v in faces]==[4,9,45]
assert dot(a,cross(b,d))==-6
cases=[]
for q,expected in [([1,-1,2],[0,-2,-6]),([-1,2,0],[1,4,0]),([1,1,0],[2,2,0]),([1,-1,0],[0,-2,0]),([2,1,1],[3,2,-3]),([-1,2,2],[1,4,-6])]:
 out=[r[0] for r in mul(B,[[F(v)] for v in q])]
 assert out==expected
 recovered=[r[0] for r in mul(tr(mul(B,R)),[[v] for v in out])]
 assert recovered==q
 cases.append(dict(q=q,displacement=[str(v) for v in out],reconstruction_residual=['0','0','0'],squared_length=str(dot(out,out))))
scale_checks=[]
for scale,expected_squares,expected_det in [(2,[64,144,720],-48),(3,[324,729,3645],-162)]:
 scaled=[[scale*x for x in row] for row in B]
 sa,sb,sc=tr(scaled)
 squares=[dot(v,v) for v in [cross(sa,sb),cross(sa,sc),cross(sb,sc)]]
 determinant=dot(sa,cross(sb,sc))
 assert squares==expected_squares and determinant==expected_det
 assert mul(tr(scaled),scaled)==[[scale**2*x for x in row] for row in M]
 scaled_R=[[x/F(scale**2) for x in row] for row in R]
 assert mul(mul(scaled,scaled_R),tr(scaled))==I
 scale_checks.append(dict(s=scale,areas_squared=[str(x) for x in squares],determinant=str(determinant),inverse_metric_factor=str(F(1,scale**2))))
rounding_checks=[]
for stored,expected in [('0.333','-0.001'),('0.3333','-0.0001')]:
 residual=3*D(stored)-1
 assert residual==D(expected) and 1+residual==3*D(stored)
 rounding_checks.append(dict(stored=stored,residual=str(residual),reconstructed_product=str(1+residual)))
assert D('1.25').quantize(D('0.1'))==D('1.2')
assert D('1.35').quantize(D('0.1'))==D('1.4')
sources=[]; parsed={}
for src in c['sources']:
 raw=Path(src['path']).read_bytes()
 actual=hashlib.sha256(raw).hexdigest()
 assert actual==src['sha256'],src['id']
 sources.append(dict(id=src['id'],path=src['path'],sha256=actual,status='matched'))
 parsed[src['id']]=json.loads(raw.decode('utf-8-sig'),parse_float=D,parse_int=D)
lock=parsed['S02']['mature_locked_cell3']
canonical=parsed['S03']['canonical_locked_values']
assert lock['B_nm']==canonical['B_nm']
assert lock['face_areas_nm2']==canonical['face_areas_nm2']
DB=lock['B_nm']; DM=lock['direct_metric_nm2']; DR=lock['reciprocal_metric_nm_minus2']
DI=[[D(int(i==j)) for j in range(3)] for i in range(3)]
gram_res=sub(mul(tr(DB),DB),DM)
inverse_res=sub(mul(DM,DR),DI)
external_res=sub(mul(mul(DB,DR),tr(DB)),DI)
reciprocal_res=sub(mul(tr(DB),lock['reciprocal_basis_nm_minus1']),DI)
da,db,dc=tr(DB)
det=dot(da,cross(db,dc))
af=[cross(da,db),cross(da,dc),cross(db,dc)]
areas=[dot(x,x).sqrt() for x in af]
area_res=[areas[i]-lock['face_areas_nm2'][key] for i,key in enumerate(['ab','ac','bc'])]
def matrix_record(value,unit):
 return dict(values=strings(value),units=unit,max_abs=str(max(abs(x) for row in value for x in row)))
out=dict(schema_version='1.0',status='passed',runtime=sys.executable,source_hash_checks=sources,
 arithmetic=dict(synthetic='exact fractions.Fraction; no tolerance',locked='decimal.Decimal',precision=60,rounding='ROUND_HALF_EVEN',input='original source decimal lexemes',comparison_rule='No tolerance gate; preserve every component; equality asserted only for source lock agreement and exact synthetic expectations'),
 synthetic=dict(label='Classroom analogue, not Cell3',gram=strings(M),inverse=strings(R),reciprocal_basis=strings(mul(B,R)),face_order=['ab','ac','bc'],face_vectors=strings(faces),face_area_squared=['4','9','45'],face_areas=['2','3','3*sqrt(5)'],signed_volume='-6',MR_minus_I=strings(sub(mul(M,R),I)),BRBT_minus_I=strings(sub(mul(mul(B,R),tr(B)),I)),cases=cases,scale_checks=[dict(s=2,areas=['8','12','12*sqrt(5)'],determinant=-48),dict(s=3,areas=['18','27','27*sqrt(5)'],determinant=-162)]),
 locked=dict(BTB_minus_M=matrix_record(gram_res,'nm^2'),MR_minus_I=matrix_record(inverse_res,'dimensionless'),BRBT_minus_I=matrix_record(external_res,'dimensionless'),BTD_minus_I=matrix_record(reciprocal_res,'dimensionless'),R_minus_RT=matrix_record(sub(DR,tr(DR)),'nm^-2'),determinant_recomputed=str(det),determinant_minus_source=str(det-lock['det_B_nm3']),determinant_units='nm^3',areas_recomputed=[str(x) for x in areas],areas_minus_source=[str(x) for x in area_res],area_order=['ab','ac','bc'],area_units='nm^2',source_reported_closure_scalar=str(lock['direct_reciprocal_closure_max_abs']),source_reported_closure_status='Reported scalar; source arithmetic not freshly reproduced; not substituted for any new residual matrix'),
 reconstruction_rules=['B^T B = M_stored + BTB_minus_M','M_stored R_stored = I + MR_minus_I','B R_stored B^T = I + BRBT_minus_I','B^T D_stored = I + BTD_minus_I','det_recomputed = det_source + determinant_minus_source','areas_recomputed = areas_source + areas_minus_source'],
 limitations=['Numerical closure checks are declared witnesses, not replacement canonical decimals.','No external experimental dataset or physical mechanism is inferred.'])
out['synthetic']['scale_checks']=scale_checks
out['synthetic']['rounding_checks']=rounding_checks
(p/'verification.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('PASS: exact synthetic checks, five source hashes, lock agreement; full Decimal residuals preserved')
print('Runtime:',sys.executable)
print('max |BTB-M|:',out['locked']['BTB_minus_M']['max_abs'])
print('max |MR-I|:',out['locked']['MR_minus_I']['max_abs'])
