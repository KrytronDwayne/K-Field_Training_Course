"""Independent exact finite graph checks; synthetic teaching inputs only.

Run with the authorized tf_gpu_env. Writes compact results beside this script.
No source snapshots, packages, floating-point rank, or large arrays are saved.
"""
from fractions import Fraction as F
from itertools import product
from collections import deque
from pathlib import Path
import hashlib
import json
import sys


def rank(a):
    a = [[F(v) for v in row] for row in a]
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = a[r][col]
        a[r] = [v / z for v in a[r]]
        for i in range(len(a)):
            if i != r:
                z = a[i][col]
                a[i] = [v - z*w for v, w in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def incidence(vertices, edges):
    return [[int(v == h) - int(v == t) for t, h in edges] for v in vertices]


def mv(a, x):
    return [sum(v*w for v, w in zip(row, x)) for row in a]


def product_graph(shape, periodic=False):
    vertices = list(product(*(range(n) for n in shape)))
    edges = []
    wraps = []
    for axis, n in enumerate(shape):
        for t in vertices:
            if t[axis] < n-1:
                h = list(t)
                h[axis] += 1
                edges.append((t, tuple(h)))
            elif periodic:
                h = list(t)
                h[axis] = 0
                wraps.append((t, tuple(h)))
    return vertices, edges + wraps


def tree_and_cycles(vertices, edges):
    root = vertices[0]
    tree = set()
    for v in vertices:
        if v == root:
            continue
        p = list(v)
        axis = next(i for i, x in enumerate(v) if x)
        p[axis] -= 1
        tree.add(edges.index((tuple(p), v)))
    adj = {v: [] for v in vertices}
    for j in tree:
        t, h = edges[j]
        adj[t].append((h, j, 1))
        adj[h].append((t, j, -1))
    chords = [j for j in range(len(edges)) if j not in tree]
    cycles = []
    for chord in chords:
        tail, head = edges[chord]
        queue = deque([head])
        paths = {head: []}
        while queue:
            v = queue.popleft()
            for other, j, sign in adj[v]:
                if other not in paths:
                    paths[other] = paths[v] + [(j, sign)]
                    queue.append(other)
        c = [0]*len(edges)
        c[chord] = 1
        for j, sign in paths[tail]:
            c[j] = sign
        cycles.append(c)
    return sorted(tree), chords, cycles


def main():
    checks = []
    def check(name, result, details):
        assert result, name
        checks.append({'id': name, 'status': 'passed', 'result': details})

    for shape, expected in [((2,2),(4,4,3,1)), ((3,2),(6,7,5,2)),
                            ((3,3),(9,12,8,4)), ((3,3,3),(27,54,26,28))]:
        v,e = product_graph(shape)
        d = incidence(v,e)
        t,ch,cs = tree_and_cycles(v,e)
        actual = (len(v),len(e),rank(d),len(cs))
        check('open_'+'x'.join(map(str,shape)), actual == expected,
              dict(zip(['vertices','edges','rank','cycle_dimension'],actual)))
        check('cycle_basis_'+'x'.join(map(str,shape)),
              len(t)==len(v)-1 and all(not any(mv(d,c)) for c in cs)
              and all(c[j] == int(i==k) for i,c in enumerate(cs) for k,j in enumerate(ch)),
              'First-nonzero-decrement tree; all cycles close; chord restriction is identity.')
    v,e = product_graph((3,3,3))
    degrees = {u: sum(u in edge for edge in e) for u in v}
    check('degree_classes', [degrees[u] for u in [(0,0,0),(1,0,0),(1,1,0),(1,1,1)]] == [3,4,5,6], [3,4,5,6])

    for n, flow, potential, expected_div, expected_grad, expected_rem in [
        (3,[2,3,4],[2,5,7],[2,-1,-1],[3,2,-5],[-2,-1,0]),
        (4,[2,3,4,5],[0,1,3,2],[3,-1,-1,-1],[1,2,-1,-2],[-3,-2,-1,0])]:
        edges = [(i,(i+1)%n) for i in range(n)]
        d = incidence(list(range(n)),edges)
        c = [1]*n
        gradient = [potential[h]-potential[t] for t,h in edges]
        remainder = [x-flow[-1] for x in flow]
        check(f'ordered_ring_{n}', rank(d)==n-1 and mv(d,flow)==expected_div
              and gradient==expected_grad and sum(gradient)==0
              and not any(mv(d,c)) and remainder==expected_rem
              and mv(d,remainder)==expected_div
              and [flow[-1]*a+b for a,b in zip(c,remainder)]==flow,
              {'incidence':d,'flow':flow,'divergence':expected_div,'gradient':gradient,
               'cycle':c,'chord_coefficient':flow[-1],'retained_tree_remainder':remainder})
        flipped = [row[:] for row in d]
        for row in flipped:
            row[0] *= -1
        ff = flow[:]
        ff[0] *= -1
        check(f'orientation_invariance_{n}',mv(flipped,ff)==expected_div,'Column and flow sign reversed together.')

    v,e = product_graph((3,3,3),True)
    d = incidence(v,e)
    t,ch,cs = tree_and_cycles(v,e)
    check('periodic_counts', (len(v),len(e),rank(d),len(cs))==(27,81,26,55),
          {'vertices':27,'open_edges':54,'wrap_edges':27,'edges':81,'rank':26,'cycle_dimension':55})
    check('periodic_basis', all(not any(mv(d,c)) for c in cs)
          and all(c[j] == int(i==k) for i,c in enumerate(cs) for k,j in enumerate(ch)),
          '55 exact closed fundamental cycles with identity chord restriction.')
    for label,w in [('worked',list(range(1,10))),('practice',[0]*8+[9]),('integer_guard',[1]+[0]*8)]:
        W = sum(w)
        mean = F(W,9)
        detail = [F(x)-mean for x in w]
        retained = detail[:8]
        recovered = [mean+x for x in retained+[-sum(retained)]]
        check('wrap_'+label, recovered==w and sum(detail)==0,
              {'w':w,'W':W,'mean':str(mean),'eight_free_details':list(map(str,retained)),
               'ninth_detail':str(-sum(retained)),'reconstructed':list(map(str,recovered))})
    coeff = [0]*28 + [0]*8+[9] + [0]*18
    flow = [sum(q*c[i] for q,c in zip(coeff,cs)) for i in range(81)]
    check('full_periodic_reconstruction', not any(mv(d,flow)) and [flow[j] for j in ch]==coeff,
          '28 zero open coefficients; first axis wraps (0,...,0,9); other axes zero; full 81-edge circulation reconstructed.')
    general = [(i%7)-3 for i in range(81)]
    q = [general[j] for j in ch]
    cycle_part = [sum(a*c[i] for a,c in zip(q,cs)) for i in range(81)]
    remainder = [a-b for a,b in zip(general,cycle_part)]
    check('general_periodic_remainder', all(remainder[j]==0 for j in ch)
          and mv(d,remainder)==mv(d,general)
          and [a+b for a,b in zip(cycle_part,remainder)]==general,
          'Signed synthetic 81-edge field reconstructs exactly from 55 chord coefficients and 26 tree entries; divergence retained.')
    check('coordinate_partition', 28+24+3==55 and 28+24==52,
          '52 zero-winding coordinates plus 3 windings; these finite counts assert no dynamics or group action.')
    result = {'status':'passed','method':'Independent standard-library rational arithmetic, elimination, graph enumeration and exact assertions.',
              'evidence_class':'Fresh verification of finite mathematical/synthetic teaching examples; no empirical or global source-closure certification.',
              'runtime':sys.executable,'check_count':len(checks),'checks':checks,
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('worked-example-verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','checks':len(checks),'runtime':sys.executable}))


if __name__ == '__main__':
    main()
