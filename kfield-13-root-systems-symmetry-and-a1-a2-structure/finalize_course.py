"""Rebuild assembly, provenance and recovery authorities after reviewed repairs."""
from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
p=json.loads((D/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(n,s):(D/n).write_text(s.strip()+'\n',encoding='utf-8')
def dump(n,o):write(n,json.dumps(o,ensure_ascii=False,indent=2))
def sha(n):return hashlib.sha256((D/n).read_bytes()).hexdigest()
order=[f'lesson-{i:02}' for i in range(1,7)]
titles=[r['title'] for r in p['course_map']]
periods=[1,2,2,2,1,1]
cm=['# Course map — Root Systems, Symmetry, and A1–A2 Structure',
'Audience: high-school seniors. Nine core 55-minute periods plus two capstone periods. Input prerequisites are signed arithmetic, fractions, powers, equations and graphs; courses 09, 11, 12 are series prerequisites. All operations actually assessed here receive a local bridge. The approved six-lesson boundary is retained; lessons 02–04 use two periods each to separate new representations from quotient/metric use.',
'Dependency chain: lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → capstone. Units: I (01–02), II (03–04), III (05–06).',
'| Concept | Introduction and explanation | Worked example | Answered practice | Assessment | Later use | Periods |\n|---|---|---|---|---|---|---|']
for i in range(1,7):
    cid=f'C13.{i:02}';nextid=f'lesson-{i+1:02}' if i<6 else 'capstone'
    cm.append(f'| {cid}: {titles[i-1]} | [lesson-{i:02}](lesson-{i:02}.md), {cid}-E1 | {cid}-W1 | {cid}-P1 | {cid}-D1–D4; C13-CAP-{i:02} | {nextid} | {periods[i-1]} |')
cm+=['Each period: retrieval 5, instruction/worked example 20, practice 15, diagnostics/repair 15 minutes. Teacher guide gives the two-period splits. No hidden prerequisite in Lie theory, calculus, complex vector spaces or quantum mechanics is required.',
'## Concrete capstone inputs and outputs',
'| Step | Input → output | Explanation and prior answered practice |\n|---|---|---|']
ops=['(1,2,3), T → three-operation table, orbit, identity/inverses, sum/norm',
'(-1,3), (+1,-1) → S/A, transferred pair, r/k record, inverse halves',
'α₁,α₂,(-1,3,-2) → six roots and plotted coordinates, Cartan entries, coefficients',
'e_i,u₁+u₂,2u₁+u₂ → centered weights, class labels, coefficient/displacement records',
'ρ=(1,0,0),v=(-1,0,1) and independent tags → decoded lift and typed reconstructible record',
'T,q=(2,-3,1),f(v)=2v on H → matrix, root orbit, norm, commuting map paths and identification boundary']
for i,op in enumerate(ops,1):cm.append(f'| C13-CAP-{i:02} | {op} | C13.{i:02}-E1 and C13.{i:02}-P1 |')
cm.append('Source dependency scope: M09 lists M06 and M08. The carry-coordinate bridge from M06 is taught locally; the finite channel model and M09 definitions are used directly without importing the graph-spectrum results of M08 as unproved assessment premises. Source-local compiler closure and physical assignments remain scoped reports, not prerequisites. See sources.md.')
map_text='\n\n'.join(cm[:3])+'\n\n'+'\n'.join(cm[3:])
map_text=map_text.replace('\nEach period:','\n\nEach period:').replace('\n## Concrete','\n\n## Concrete').replace('## Concrete capstone inputs and outputs\n','## Concrete capstone inputs and outputs\n\n').replace('\nSource dependency scope:','\n\nSource dependency scope:')
write('course-map.md',map_text)
terms=[('carrier','Declared collection on which a rule acts; changing it changes the claim.'),('tuple','Ordered list; its positions retain their identities.'),('composition FG','Apply G first, then F.'),('I,R,T','Identity; pair swap; triple cycle T(x,y,z)=(z,x,y). I here is not a physical tensor.'),('inverse','Rule that restores every input on the stated carrier.'),('closure','Every composition stays inside the specified operation set.'),('invariant','Specified quantity unchanged by an operation.'),('group','Closed operations with identity, inverses and associative composition.'),('Z, congruence, mod n','Integers; equal remainder means the difference is divisible by n. Chosen remainders are 0 through n-1.'),('C_b,C_c','Ordered signed integer carry coordinates; dimensionless.'),('S,A','C_b+C_c and C_b-C_c; inverse halves require equal parity.'),('P₁,Q₁','Integer A weight carrier Z and even transfer displacement lattice 2Z.'),('quotient / class','Grouping by allowed displacement; not a replacement for the full input.'),('r,k in A=r+2k','Remainder 0 or 1 and retained integer displacement coefficient.'),('e₁,e₂,e₃','Formal channel basis of dimensionless triple space.'),('H','Real zero-sum plane x+y+z=0.'),('α₁,α₂','Simple roots (1,-1,0),(0,1,-1).'),('root / root lattice Q₂','One of six unit transfers / all integer zero-sum triples.'),('dot product / squared norm','Sum of matched products / v·v in abstract Euclidean channel space.'),('Cartan C_ij','2(α_i·α_j)/(α_j·α_j); not a carry C_b.'),('h, μ','Common mean vector (1,1,1)/3 for channel centering; general scalar mean retained for reversal.'),('u_i, P₂','Centered weights e_i-h; all integer combinations a u₁+b u₂.'),('weight class','Remainder of a+b mod 3; all three displayed u_i have class 1.'),('ρ,v,ℓ','Address residue, balanced digit, compatible lift ℓ=ρ+3v at n=1; v elsewhere can mean a generic vector explicitly declared locally.'),('family tag','Independent typed identifier, illustrated by synthetic F2.'),('ray and scale','Ratio coordinates with declared positive-scale/oriented convention; retain scale and sign convention.'),('detector parity','Sign of a signal under a declared antipodal map, when that signal has definite parity.'),('matrix / transpose','Row-rule array / rows and columns exchanged.'),('action / intertwiner','Composition-consistent transformations / map f with f(Tv)=U(f(v)).'),('M_cell,R_cell,G_phase,O_K,B','Reserved source symbols: Cell3 Gram metric, its inverse, phase metric, origin and locked ordered basis. They are not used for the abstract dot product.'),('evidence scope','Source report, finite derivation, synthetic illustration, interpretation or unresolved physical mapping; never silently promoted.')]
write('terminology.md','# Terminology and notation\n\nAll core coordinates are dimensionless. Symbol roles are local and explicitly declared. No physical units are inferred from these examples.\n\n| Term | Definition |\n|---|---|\n'+'\n'.join(f'| {a} | {b} |' for a,b in terms))
verified=[]
for s in p['sources']:
    actual=hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()
    assert actual==s['sha256'],s['id']
    verified.append({**s,'fresh_sha256':actual,'hash_matches':True})
source_lines=['# Source notes and evidence boundaries','All five supplied archival byte hashes were freshly checked. Only bounded relevant fields were read for teaching; no raw source files were copied. S02 is the primary mature source. S01 is an earlier corrected branch, S03 an audit-correction instruction, S04 a corpus audit, and S05 a periodic-table branch. Their hashes establish file identity, not automatic authority for every claim. No numerical constants from these branches are merged.',
'| ID | Exact read-only path | SHA-256 |\n|---|---|---|']
source_lines += [f"| {s['id']} | `{s['path']}` | `{s['sha256']}` |" for s in verified]
source_lines+=['''
## Exact pointers used

| Source pointer | Content and evidence class | Course use |
|---|---|---|
| S02 /backbone_sequence/8 | M09 definitions, finite proof statements, type guards; archival source | Lessons 02–06 |
| S02 /backbone_sequence/5/side_modes | S/A transform and integer lattice; archival source | Lesson 02, independently derived halves |
| S02 /backbone_sequence/8/requires | M06 and M08 dependency labels | Local bridges; no graph-spectrum claim needed |
| S02 /proof_nodes/54/formula | KFM-X020 native side transfer and A1 parity guard | Lesson 02 |
| S02 /proof_nodes/58/formula | KFM-X014, lifts u+3ⁿv with v∈{-1,0,1}³, count 27 | Lesson 05 at n=1; ρ used to avoid weight-symbol collision |
| S02 /proof_nodes/63/formula | KFM-X021 weights, Cartan matrix, quotient, primitive/ray guard | Lessons 03–05 |
| S02 /branch_proofs/3 | BR-03 reported address/lift compiler closure | Recognition-only report; no fresh compiler execution |
| S02 /branch_proofs/6 | BR-06 reported gauge-matter closure | Recognition-only report, not physical identification |

The source reports exact/forced root statements under its calibrated compiler contract. This course freshly verifies the finite transfer, integer lattice, divisibility and permutation mathematics. It does not freshly verify the full calibrated compiler, a global physical gauge choice, or an experimental intertwiner. There are no missing source bodies for the finite lesson calculations. The full compiler and physical identification remain outside the verified scope.

## Frozen graph retrieval and namespace guard

Capabilities were read once and expose the read-only interface, but did not expose a corpus generation pair. A hybrid RAG query for KFM-X020, KFM-X021, M09 primitive lifts A1 A2, with rerank=false, returned generation and manifest SHA-256 `5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7`; index SHA-256 `aca56e6b5b2b717459cea9790e6142ea9e8058f74d135710906926e9065ad54a`. Returned material included `kfield_standard_model/formal/KField/StandardModelCompilerAdjudication.agda`, lines 1–199, source SHA-256 `01c849f3d184f367e0c53e1e00f521fa2fad98c1682d0aaa03e7de30667840ad`. Its compiler M09 is not the mathematical-backbone M09. No graph label was promoted to proof. Exact root grounding instead uses the supplied local S02 bytes and pointers above. No archive node was selected for traversal because the returned compiler namespace was not the requested mathematical node.

## Supplied integration provenance card — recognition only

| Record | Exact provenance | Scoped status |
|---|---|---|
| I01 | `applications/kfield_standard_model/collaborator_record/project_record.json`; retrieved alias `kfield_standard_model/project_record.json`; SHA-256 `3800c854da827a64e72507722904bcafab07a31e88f2bc73920a8e7f62f62c1c`; /hazards/3, /open_obligations/1, /open_obligations/2 | Supplied prior RAG provenance, not a fresh local byte hash; admitted family Z1,Z2,Z3,Z6; unique physical member unresolved |
| I02 | `kfield_standard_model/evidence/p12_standard_model_compiler_adjudication_report.json`; SHA-256 `a3dfca0e55e525c6522c3088b95e5bcc048c141fce340bfe980fcfc14123220a`; /direct_authority_modules, /agda/certificate, /known_science_replay | Supplied integration report: direct compiler authority M03,M07,M08 only; no fresh typecheck |

These integration dispositions remain separate from the mature source's branch closure language. Full source-author authentication, proof compilation, and empirical physical uniqueness are not claimed. The admitted global-form family is preserved without choosing a member. Terms in this recognition-only card are not assessed computations.

## Invariant applicability

The approved input-contract.json retains every supplied invariant. This course actively uses evidence separation, carrier ordering and type guards, reversible transforms, abstract-versus-physical metric separation, and provenance distinctions. It performs no Cell3 coordinate conversion, nearest-integer rounding, physical velocity computation, energy/force inference, recursive detail-product operation, or M19/M20 closure argument. Consequently those source contracts are preserved without importing unrelated constants or pretending to verify operations not performed. Centering retains the mean, quotienting retains displacement, and address reduction retains the lift digit. Synthetic family and detector fields are explicitly labeled.
''']
write('sources.md','\n\n'.join(source_lines[:2])+'\n\n'+'\n'.join(source_lines[2:]))
dump('source-verification.json',{'status':'passed','sources':verified,'primary_pointers':['/backbone_sequence/8','/backbone_sequence/5/side_modes','/proof_nodes/54/formula','/proof_nodes/58/formula','/proof_nodes/63/formula','/branch_proofs/3','/branch_proofs/6'],'fresh_compiler_typecheck':False,'raw_copies':False})
write('course.md','# Root Systems, Symmetry, and A1–A2 Structure\n\nStudent course. Use the [course map](course-map.md), [glossary](terminology.md), [capstone](capstone.md), [teacher guide](teacher-guide.md), and [source notes](sources.md) alongside these lessons.\n\n'+'\n\n'.join(f'<!-- BEGIN: {i} -->\n'+(D/f'{i}.md').read_text(encoding='utf-8').rstrip('\n')+f'\n<!-- END: {i} -->' for i in order))
# Explicit item existence is a necessary mechanical complement to content review.
for i in range(1,7):
    body=(D/f'lesson-{i:02}.md').read_text(encoding='utf-8')
    for suffix in ['E1','W1','P1','D1','D2','D3','D4']:assert f'C13.{i:02}-{suffix}' in body
    assert f'C13-CAP-{i:02}' in (D/'capstone.md').read_text(encoding='utf-8')
print('Assembly, course map, glossary, source verification and E05 existence checks written')
