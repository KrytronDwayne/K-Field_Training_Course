from author_course import ROOT, write, dump, digest
import json, hashlib
p=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
write('capstone.md',r'''
# Capstone — A reversible shape-and-scale change report

Allow two 55-minute periods. Use the lessons and exact symbolic expressions; calculators are optional. These are separate synthetic records, not one physical acquisition. Submit ordered inputs, transformed values, inverse checks, units, domains, source pointers and retained remainders. L=ln2. Label the dimensionless change parameter t_change and the positive length scale t_length in your final report.

## Student tasks

**C10-CAP-01 (10 points).** Record AREAS has A0=1 LU² and A/A0=(2,4,16) in [ab,ac,bc] order. Find its log triple. Halve all edges at fixed angles, giving a common area factor 1/4. Find the changed logs and dimensional areas, then reconstruct the original areas. Explain the difference between that operation and changing only A0 to 4A0.

**C10-CAP-02 (20 points).** For the original AREAS triple calculate m,z and s,u,v. Use both decompositions to recover every log and area. State what changes and what stays fixed under the edge halving. Explain the limitation of the word shape.

**C10-CAP-03 (15 points).** Record LINEAR uses H with rows (1,1),(1,-1) and input (1,-2)t_change. Apply and invert it. Record SQUARE separately uses f(t_change)=(1+t_change)² with initial value 1. At t_change=1/10 calculate output, change, tangent and signed remainder. Give the exact log change as well. Keep each record's exact versus local status explicit.

**C10-CAP-04 (20 points).** Record JACK uses input (2,-1,1)t_change in [dln l_a,dln l_b,dln l_c] order. Use J from Lesson 4 to find [dln eta,dln alpha,dln Gamma2], then reverse it. Check det J. Check the third output separately using the area tangent changes and coefficients 9,8,-11. State the angle domain, units, meanings of dA and Gamma2, and relevant source pointers.

**C10-CAP-05 (25 points).** Build a typed ledger. Record BOX uses B=diag(2,2,2) LU in a declared synthetic Cartesian frame. Find M_cell, its metric cofactor matrix, R_cell and the inverse product, all with units. Retain B and explain why. Record BRANCH has S=4,A_branch=2; decode and re-encode it, checking integer admissibility. In a separately labeled ANCHOR record, orthogonal face areas are (9,18,18) LU². Find eta, alpha_inverse, k_b,k_c, positive t_length and all edge lengths; reconstruct every area. Include the AREAS scale/shape coordinates from step 2 and JACK scalar tangent from step 4 as separately identified records rather than one unlabeled vector.

**C10-CAP-06 (10 points).** Audit your report. Compare the zero inverse residual of JACK with the finite SQUARE remainder. State the retained reference, angle and branch metadata. Identify what additional information is required for changing angles or a finite physical Gamma2 prediction. Distinguish source formula, fresh finite calculation, synthetic input and unresolved mechanism. Do not delete any signed remainder.

## Full worked answer key

**01.** Original logs y=(1,2,4)L and original areas (2,4,16) LU². Edge halving subtracts 2L from each log, giving (-1,0,2)L and (1/2,1,4) LU². Add 2L to reverse the operation and exponentiate to recover (2,4,16) LU². Changing only the reference to 4A0 produces the same changed log numbers but reconstructs unchanged physical areas with the NEW reference: 4A0 times (1/2,1,4)=(2,4,16)A0. All areas/references are positive.

**02.** m=7L/3; z=(-4,-1,5)L/3, whose sum is zero. s=7L/sqrt3, u=L/sqrt2, v=5L/sqrt6. Mean reconstruction gives coefficients (7-4,7-1,7+5)/3=(1,2,4). Normalized reconstruction gives (7/3-1/2-5/6,7/3+1/2-5/6,7/3+10/6)=(1,2,4). A0 exp(y)=(2,4,16) LU². Edge halving gives m_new=m-2L=L/3 and s_new=s-2sqrt3 L=L/sqrt3; z,u,v stay fixed. Area shape is complete for face-area ratios modulo a common factor, not arbitrary edge-angle shear.

**03.** H(1,-2)t_change=(-1,3)t_change. H/2 returns ((-1+3)/2,(-1-3)/2)t_change=(1,-2)t_change. Its inverse residual is exactly (0,0). SQUARE expands to 1+2t_change+t_change². At 0.1: output 1.21, change 0.21, tangent 0.20, remainder +0.01. The baseline-plus-parts check is 1+0.20+0.01=1.21. Exact log change is 2ln(11/10), approximately 0.19062036. Its difference from log tangent 0.20 is 2ln(11/10)-0.20, approximately -0.00937964. This negative log remainder differs from the positive relative-change remainder; preserve the coordinate label.

**04.** J input gives (-2+1,2+1,34+2-3)t_change=(-1,3,33)t_change. Inverse numerators (33-6-3,33-42-3,33-6-15)=(24,-12,12) give (2,-1,1)t_change after division by 12. Residual is (0,0,0). Determinant=(-1)(3)+(1)(15)=12. Area tangents are (2-1,2+1,-1+1)t_change=(1,3,0)t_change; 9+24-0=33 verifies dG. All entries are dimensionless tangent changes, with fixed included nondegenerate angles and coherent edge scaling. dA=dln alpha, not area or dln alpha_inverse. Gamma2 is a named scalar lift, not a force. Sources: S02#/backbone_sequence/6 for J, /backbone_sequence/4 for eta/alpha, /backbone_sequence/18/branches/gravity_scalar_lift for 9,8,-11.

**05.** BOX: M_cell=4I LU², det(M_cell)=64 LU⁶, cof(M_cell)=16I LU⁴, R_cell=I/4 LU^-2; M_cell R_cell=I. B=diag(2,2,2) LU and its synthetic frame remain in the record because its metric loses orientation. Its face areas are (4,4,4) LU², distinct from the separate AREAS and ANCHOR datasets. BRANCH: both 4 and 2 are even, so C_b=(4+2)/2=3, C_c=(4-2)/2=1 are integers. Re-encoding gives S=3+1=4, A_branch=3-1=2. ANCHOR: eta=1000(18/9)=2000 and alpha_inverse=100(18/18)=100. Orthogonal sine factors=1 imply k_b=1,k_c=2. t_length=sqrt(9/1)=3 LU; lengths (3,3,6) LU reconstruct (9,18,18) LU². The ledger separately retains AREAS (A0,m,z,s,u,v) and JACK dG=33t_change with its source/domain. Metric, shape, scalar tangent and integer branch entries keep distinct types and inverse maps.

**06.** JACK reverses its linear map exactly; SQUARE retains a +0.01 finite approximation remainder, so these results are consistent. The reference is A0=1 LU² for AREAS, with any reference change recorded. JACK angles are fixed; ANCHOR angles are perpendicular. BRANCH has same-parity integer inputs and the M06 side-mode map. All record names, orders and units remain. Varying angles requires their additional dln sin(theta) terms and geometry; J alone is insufficient. A finite physical Gamma2 prediction additionally needs a stated finite relation and physical interpretation/baseline, which the tangent matrix alone does not give. The numeric inputs are synthetic; formula provenance is archival; matrix and reconstruction arithmetic are freshly checkable; a dynamical mechanism is unresolved here. S03 AUD-002's wider DAG gap remains outside these finite checks.

## Rubric

| Step | Points and allocation |
|---|---|
| 01 | 10: positive reference/order 2; original logs 2; scaling 3; reversal/reference distinction 3 |
| 02 | 20: mean/zero-sum 5; projections 5; two reconstructions with areas 6; scale and scope 4 |
| 03 | 15: H and inverse 5; exact square/tangent/remainder 6; exact log and scope 4 |
| 04 | 20: forward 4; inverse 4; determinant 3; independent area-row check 4; domain/units/source meanings 5 |
| 05 | 25: metric/cofactor/reciprocal with units 7; basis retention 2; branch round trip/parity 4; anchor/lengths/area round trip 8; typed separate records 4 |
| 06 | 10: two residual types 3; retained metadata 3; source/synthetic/finite/mechanism distinction and limits 4 |

Total 100. Give method credit for a correctly propagated arithmetic error; identify the earliest defect instead of deducting repeatedly. A high score does not waive a missing scale, omitted residual, changed-angle misuse or force-law conflation: repair those before calling the report reversible. Exact expressions are preferred; rounded decimals must retain their exact parent expression. No novelty or consensus judgment is assessed.
''')
write('terminology.md',r'''
# Terminology and notation

| Symbol or term | Meaning, units and scope | Introduced |
|---|---|---|
| LU, LU² | Declared synthetic length unit and its area unit | 1 |
| A_ab,A_ac,A_bc | Positive face areas, always [ab,ac,bc] in log triples | 1 |
| A0 | ONE common positive reference area, same units as faces | 1 |
| exp, ln, L | Exponential, inverse natural log on positive numbers, L=ln2 | 1 |
| rho | Positive common edge multiplier; areas multiply by rho² | 1 |
| y | Dimensionless ordered log-area triple ln(A_i/A0) | 1 |
| m,z | Mean log and zero-sum shape; y=m1+z | 2 |
| dot product | Multiply corresponding entries and add | 2 |
| orthonormal | Mutually perpendicular, each squared length one | 2 |
| e_s,e_u,e_v | Source unit directions (1,1,1)/sqrt3,(-1,1,0)/sqrt2,(-1,-1,2)/sqrt6 | 2 |
| s,u,v | Dot projections; s=sqrt3 m; u,v area-shape coordinates | 2 |
| A2 shape fiber | Source name for the two-dimensional area-shape component; not arbitrary shear | 2 |
| I, T, P_H | Identity matrix, transpose, mean-removal I-11^T/3 | 2 |
| H | Classroom matrix rows (1,1),(1,-1); inverse H/2 | 3 |
| t_change | Dimensionless small-change parameter; written t in Lessons 3,4,6 | 3 |
| tangent, derivative | Coefficient c in f(t)=f(0)+ct+R(t), R(t)/t approaching zero | 3 |
| Jacobian | Table of local first-order response coefficients at a specified point/domain | 3 |
| remainder | Exact finite change minus tangent prediction, retained with sign | 3 |
| l_a,l_b,l_c | Positive edge lengths; |a| etc. denote these lengths | 4 |
| theta_ij, sin(theta_ij) | Included angle and height/edge factor, supplied in exercises | 4 |
| eta, alpha_inverse, alpha | 1000 A_bc/A_ab, 100 A_bc/A_ac, reciprocal of alpha_inverse | 4 |
| x_a,x_b,x_c | Dimensionless tangent log-length changes | 4 |
| dE,dA,dG | Ordered dln eta,dln alpha,dln Gamma2; dA is not area | 4 |
| Gamma2 | Source scalar-lift coordinate; no force dynamics claimed | 4 |
| J | Fixed-angle Jack matrix with determinant 12 | 4 |
| determinant | Scalar square-matrix invertibility test; formulas taught for required cases | 4 |
| B=[a b c] | Ordered basis columns; retain frame/orientation; synthetic B differs from locked Cell3 | 5 |
| M_cell | B^T B, direct/Gram metric, units LU² in examples | 5 |
| cof(M_cell) | Metric cofactor matrix, LU⁴; not cofactors of B | 5 |
| R_cell | M_cell inverse, LU^-2; not G_phase | 5 |
| G_phase | Distinct source phase metric; recognition only, not computed here | 5 |
| C_b,C_c; S,A_branch | Integer side carries and sum/difference modes; same-parity S,A_branch | 5 |
| t_length,k_b,k_c | Positive scale length and edge ratios, lengths=t_length(1,k_b,k_c) | 5 |
| typed Devon object | Geometry, scale, shape, scalar and branch components with types and return maps | 5 |
| inverse residual | Recovered minus supplied input; distinct from approximation remainder | 6 |

The source uses A for the antisymmetric branch mode; this course writes A_branch to avoid collision. The symbol t in the anchor subsection is a length; t in tangent examples is dimensionless. The capstone spells out t_length and t_change. No nearest-integer rounding, cell ownership, parity fusion or scalar-to-force conversion is performed in this course.
''')
write('teacher-guide.md',r'''
# Teacher guide

Teach seniors who can use signed fractions, powers, ratios and linear equations. Prior courses 03,08,09 are named in the series packet, but the present course supplies operational bridges for every assessed calculation: face areas, logarithms, dot products, matrix rows, elimination, diagonal metrics and supplied branch decoding. No general calculus, abstract algebra or general matrix inverse algorithm is required. Begin with a quick check: 2^-1=1/2, solve h=p+q and k=p-q, and explain why doubling two sides quadruples a rectangle. Re-teach fractions or signed arithmetic if needed before the new operations.

## Pacing and unit checks

| Lesson | Periods / minutes | Teaching focus by period | Cumulative gate |
|---|---|---|---|
| 1 | 1 / 55 | Logs and reference area | Each learner can invert a ratio log |
| 2 | 2 / 110 | Mean then normalized projection | Unit I: m/s distinction; keep scale and A0 |
| 3 | 2 / 110 | H inverse then finite remainder | Identify exact map versus local approximation |
| 4 | 2 / 110 | Derive J then invert | Unit II: independently check 9,8,-11 row and det12 |
| 5 | 3 / 165 | Typed geometry; branch coordinates; area anchor | Preserve units, parity and geometry scope |
| 6 | 1 / 55 | Reversible report synthesis | Unit III: all capstone operations practiced |
| Capstone | 2 / 110 | Compute records; audit and repair | Full reconstruction and scope |

Core total: 11 periods (605 minutes). Complete course: 13 periods (715 minutes). Each core period allocates 5 minutes retrieval, 20 explanation/worked example, 15 guided or independent practice, 15 diagnostic checks and repair. In Lesson 5 period 2 use P1 branch/type questions and D1/D3, leaving anchor work for period 3. The initial blueprint's two periods for Lesson 5 were expanded to three because there are three distinct operational bridges. Stable lesson IDs and concept coverage are preserved. In each capstone period allow 5 minutes setup/retrieval, 35 independent work and 15 checking/repair; withhold the key until work is attempted.

## Teaching and repair moves

Have students say the order and units before every calculation. For logs, accept ln2 as an exact number; approximate decimals are optional. Do not teach dimensional ln(A) without a common A0. For projections, first ask students to verify the zero-sum triple, then use unit directions; s is not the arithmetic mean. Derive each inverse by adding/subtracting equations before using a stored matrix.

If a student says 'a 10% change means log change 0.1', compare ln(1.1) and 0.1 using the exact difference. If they report only an error magnitude, ask for the signed remainder and its coordinate. If they confuse dA and area, have them rewrite dln alpha in full. If a metric is presented as the basis, rotate a drawn box together: its dot products remain the same while its directions change. Keep the basis/frame rather than claiming the metric recovers orientation. For branches ask whether both output sums are even, then reconstruct each integer. For anchoring insist on units under the square root and the positive root.

Separate archived assertions, freshly checked algebra, synthetic inputs, geometric interpretation and unresolved dynamics. The course's source-defined terms remain admissible mathematical objects; assessment asks whether the learner follows their contracts. The scalar Gamma2 label does not itself teach a force law. Source S03's serialization finding is a provenance limit, not a reason to discard the explicit finite matrix computations.

## Assessment and prerequisite closure

Every lesson has worked examples, answered practice and 3–5 diagnostics. Ask students to cover answers, attempt P items, then compare line by line. E05 closure is recorded in course-map.md and coverage.json: each capstone step has a prior explanation, example, independently answered practice and diagnostic. C10.05-E2/W2/P2/D2 specifically teach the area anchor; it is not introduced for the first time in assessment. Lesson 6 rehearses the complete separate-record report.

Use the capstone's 100-point rubric with error propagation credit. Require repair of missing reference, lost scale, omitted residual, unit confusion, inadmissible branch pair, unsupported shear reconstruction or scalar/force conflation regardless of score. Permit algebraic forms and exact logarithms. Recognition-only material includes the source labels A2 and wider Devon object and global proof-DAG context; do not require group theory, full source compiler validation or arbitrary nonorthogonal matrix calculations.

## Reproducibility and recovery

manifest.json is the recovery authority. Verify each hash before trusting a passed checkpoint. Lesson files assemble verbatim into course.md; do not edit only the assembly. If a lesson changes, repair dependent answers, regenerate assembly, recompute verification, update audit and hashes, and rerun the validator. author_course.py and author_support.py are original drafting recipes, not safe resume commands: they overwrite drafts. Use direct targeted edits for passed content. verify_examples.py performs lightweight independent arithmetic checks and writes a compact verification record; it never copies source datasets. finalize_course.py handles final hashes/assembly and validation. Source files are read-only; all persistent output belongs to this directory.
''')
# All source bytes are read-only; retain hashes and pointers, not source snapshots.
sources=[]
for src in p['sources']:
    actual=hashlib.sha256(__import__('pathlib').Path(src['path']).read_bytes()).hexdigest()
    assert actual==src['sha256'],src['id']
    sources.append(dict(src,verified_sha256=actual,hash_match=True))
dump('sources.json',{'sources':sources,'primary_pointers':['S02#/backbone_sequence/6','S02#/backbone_sequence/4','S02#/backbone_sequence/5/side_modes','S02#/scale_uniqueness_theorem','S02#/backbone_sequence/18/branches/gravity_scalar_lift','S03#/findings/1'], 'corpus_generation_observed_in_rag':'sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','manifest_sha256_observed_in_rag':'5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','capabilities_note':'Read-only capabilities checked; generation was supplied by RAG response, not capabilities.','rag_query':'Devon Jack Jacobian M07','rerank':False,'rag_context_only':{'path':'kfield_standard_model/formal/KField/SourceAuthorityBindings.agda','sha256':'46ef9c143cc2f80d4352906cd386e79c862409594d12ee00a6648b30d182bb21','lines':'1-413','class':'source','use':'Discovery context only; no compiler or formal certification claimed.'},'evidence_class':'archival formulas plus fresh finite arithmetic; no empirical data','source_gaps':['S03 AUD-002 global serialization/DAG repair not certified; local explicit M07 formulas retrieved and checked.','No physical dynamics or finite Gamma2 response derived from J alone.']})
notes=['# Compact source notes','', 'All five hashes were checked against the contract. S02 supplies the operative formulas; the other supplied branches are not mixed into its constants. No source snapshots were copied.','', '| ID | Exact read-only path | SHA-256 |','|---|---|---|']
for s in sources: notes.append(f"| {s['id']} | `{s['path']}` | `{s['sha256']}` |")
notes += ['', '## Exact pointers and evidence', '', '- S02#/backbone_sequence/6: definitions 0–5 give logs/projections; proof 0–5 supplies scale and fixed-angle Jack claims; jack_inverse gives the inverse; devon_dimension supplies the typed object. SA-10 makes every dimensional-log shorthand ln(A/A0).', '- S02#/backbone_sequence/4/definitions: eta=1000 A_bc/A_ab, alpha_inverse=100 A_bc/A_ac. The source ray uses [bc,ac,ab]; this course explicitly uses [ab,ac,bc] for LOG AREAS and never treats the orders as interchangeable.', '- S02#/backbone_sequence/5/side_modes: sum/difference maps and the same-parity integer domain. Supplied synthetic pairs do not constitute replay of the mature carry history.', '- S02#/scale_uniqueness_theorem: area equations, fixed-angle length ratios, positive scale and anchor. Only coherent, nondegenerate supplied geometry is used; orthogonal boxes are synthetic.', '- S02#/backbone_sequence/18/branches/gravity_scalar_lift/formulas/0: scalar tangent row 9,8,-11. This named branch is not authority for other M19 extensions or M20 closure.', '- S03#/findings/1 (AUD-002): source-reported semantic-DAG incompleteness includes M07 expansions. No global repair is certified by this course.', '', 'Krytronx discovery returned the packet generation and manifest digest (see sources.json). Its source-binding labels are context, not freshly rerun Lean/Agda certificates. Mathematical backbone M07 is not automatically compiler M07. Direct local reads of the hashed archival formulas ground the lessons. No real experimental data, quotations attributed to people, measured forces or historical numerical branch mixtures are introduced.', '', 'Fresh checks are limited to displayed identities, finite examples, units/domain reasoning and reconstruction. Every numerical teaching input is explicitly synthetic; source-exact J and projection directions retain their archival identity. Geometry/orientation, scalar lift and branch coordinates remain separately typed. Wider physical mechanisms remain unresolved within this course.']
write('sources.md','\n'.join(notes))
coverage=[]
for n in range(1,7):
    tag=f'C10.{n:02d}'
    coverage.append({'concept_id':tag,'lesson':f'lesson-{n:02d}','explanation':tag+'-E1','worked_example':tag+'-W1','practice':tag+'-P1','diagnostic':tag+'-D1','capstone':f'C10-CAP-{n:02d}','later_use':f'lesson-{n+1:02d}' if n<6 else 'capstone'})
coverage.append({'concept_id':'C10.05-anchor','lesson':'lesson-05','explanation':'C10.05-E2','worked_example':'C10.05-W2','practice':'C10.05-P2','diagnostic':'C10.05-D2','capstone':'C10-CAP-05','later_use':'lesson-06'})
dump('coverage.json',{'rows':coverage,'capstone_backward_map':p['capstone_specification']['backward_map'],'pacing':{'core_periods':11,'capstone_periods':2,'period_minutes':55},'revision':'Lesson 5 increased from two to three periods to teach geometry, branch and anchor bridges separately.'})
lines=['# Course map — Shape and Scale: Devon Reduction and the Jack Jacobian','', 'Audience: high-school seniors. Entry capabilities: signed arithmetic, fractions, ratios, powers, linear equations and coordinate graphs; courses 03,08,09 provide series context. This course reteaches every additional operation used in its assessments.','', 'Dependency chain: lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → capstone. Unit boundaries follow lessons 2,4,6.','', '| Lesson | Concept / operational outcome | Periods |','|---|---|---|']
for i,row in enumerate(p['course_map']): lines.append(f"| [{row['id']}]({row['id']}.md) | {row['title']}: {row['assessment_target']} | {[1,2,2,2,3,1][i]} |")
lines+=['','11 core periods plus 2 capstone periods, each 55 minutes. Lesson 5 gained one period for prerequisite closure; IDs remain stable. All core periods allocate 5 retrieval, 20 teaching, 15 practice and 15 checks/repair minutes.','', '## Actual content and E05 backward map','', '| Concept | Explanation / example | Independently answered practice / diagnostic | Later assessment |','|---|---|---|']
for r in coverage: lines.append(f"| {r['concept_id']} | {r['lesson']}.md: {r['explanation']}, {r['worked_example']} | {r['practice']}, {r['diagnostic']} | capstone.md: {r['capstone']} |")
lines+=['','Each identifier above appears in actual student-facing content. The capstone uses named separate records, not an implicit single dataset. The concrete operations and supplied inputs/outputs are as follows:','']
for r in p['capstone_specification']['backward_map']: lines.append(f"- **{r['step_id']}**: {r['operation']} Prior explanation {r['explanation_id']} and answered practice {r['prior_practice_id']}." + (' Anchor additionally uses C10.05-E2 and C10.05-P2.' if r['step_id']=='C10-CAP-05' else ''))
lines+=['','Preserved invariants: positive dimensionless log ratios; retained scale and signed remainders; fixed-angle Jack domain; separate geometry/scalar/branch types; source formulas versus fresh finite checks; no scalar-to-force or arbitrary-shear promotion. Markdown delivery adds no new teaching in assembly. See sources.md for exact provenance and limitations.']
write('course-map.md','\n'.join(lines))
spec=[('course-map','course-map','course-map.md',[])]
for n in range(1,7): spec.append((f'lesson-{n:02d}','lesson',f'lesson-{n:02d}.md',['course-map'] if n==1 else [f'lesson-{n-1:02d}']))
spec += [('terminology','terminology','terminology.md',['lesson-06']),('teacher-guide','teacher-guide','teacher-guide.md',['lesson-06']),('capstone','capstone','capstone.md',['lesson-06']),('sources','supplement','sources.md',[]),('source-record','supplement','sources.json',[]),('coverage','supplement','coverage.json',['capstone'])]
checkpoints=[{'id':i,'kind':k,'path':f,'dependencies':deps,'status':'drafted','sha256':digest(f),'summary':'Complete authored content; final independent audit pending.'} for i,k,f,deps in spec]
dump('manifest.json',{'schema_version':'1.0','topic':p['topic'],'audience':p['audience'],'assumptions':p['assumptions']+['Lesson 5 uses three periods; total 11 core and 2 capstone periods.','Synthetic records are separate examples; no empirical measurements are supplied.'],'ordered_deliverables':[c['path'] for c in checkpoints]+['completion_report.json'],'checkpoints':checkpoints,'dependencies':{c['id']:c['dependencies'] for c in checkpoints},'course_order':[f'lesson-{n:02d}' for n in range(1,7)],'assembly':{'path':'course.md','section_ids':[f'lesson-{n:02d}' for n in range(1,7)]},'audit_counts':{'critical':0,'major':0,'minor':0},'blockers':[],'next_action':'Independent audit, example verification, final assembly and deterministic validator.'})
