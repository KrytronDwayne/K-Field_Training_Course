"""Read-only replay of compact course calculations. No source copies or writes."""
from pathlib import Path
from fractions import Fraction as F
import json, hashlib
D=Path(__file__).resolve().parent
v=json.loads((D/'verification.json').read_text(encoding='utf-8'))
for s in v['source_hashes']:
    assert hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()==s['sha256']
for case in v['finite_examples']:
    b,c,a=map(F,case['inputs_bc_ac_ab'])
    o={k:F(x) for k,x in case['outputs'].items()}
    assert [o['r_bc']*b,o['r_ac']*b,o['r_ab']*b]==[b,c,a]
    assert o['eta']*a==1000*b
    assert o['alpha_inverse']*c==100*b
    assert o['alpha']*o['alpha_inverse']==1
    assert o['eta_alpha']*a==10*c
    assert o['eta']*o['alpha']==o['eta_alpha']
for row in v['locked'].values():
    assert F(row['stored'])+F(row['signed_recomputed_minus_stored'])==F(row['recomputed_exact'])
for row in v['branch_comparisons']:
    for a,h,d in zip(row['active_lexemes'],row['historical_lexemes'],row['verified_signed_difference']):
        assert F(h)+F(d)==F(a)
# Teacher repair items and optional finite remainder.
assert [F(108)/9,F(72)/9,F(54)/9]==[12,8,6]
assert 1000*F(6,2)==3000 and 100*F(6,4)==150 and 10*F(4,2)==20
assert F('0.70')-F('0.75')==F('-0.05')
assert F(5900,3)+F(100,183)==F(120000,61)
assert F(2000)*F(1,60)**2/(1+F(1,60))==F(100,183)
for i in range(1,7):
    t=(D/f'lesson-{i:02}.md').read_text(encoding='utf-8')
    for kind in ['E1','W1','P1','D1','D2','D3','D4']:
        assert f'C08.{i:02}-{kind}' in t
print('PASS: five source hashes, nine finite triples, four locked reconstructions, six branch differences, teacher repairs, optional remainder, and lesson IDs.')
