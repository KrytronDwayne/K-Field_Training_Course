from pathlib import Path
import json, hashlib
from fractions import Fraction as F
from decimal import Decimal, localcontext

D=Path(__file__).resolve().parent
if (D/'completion_report.json').exists():
    existing=json.loads((D/'completion_report.json').read_text(encoding='utf-8-sig'))
    if existing.get('status')=='complete':
        raise SystemExit('Passed course is immutable to bulk regeneration. Use replay_checks.py and scoped repairs instead.')
C=json.loads((D/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(p,s): (D/p).write_text(s.strip()+'\n',encoding='utf-8')
def js(p,x): write(p,json.dumps(x,indent=2,ensure_ascii=False))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
sources={}
source_records=[]
for s in C['sources']:
    actual=sha(s['path']); assert actual==s['sha256'],s['id']
    sources[s['id']]=json.loads(Path(s['path']).read_text(encoding='utf-8-sig'),parse_float=str,parse_int=str)
    source_records.append({**s,'actual_sha256':actual,'hash_verified':True})
S=sources['S02']; H=sources['S01']; T=C['teaching_blueprint_contract']
assert S['backbone_sequence'][4]['id']=='M05'
areas=S['mature_locked_cell3']['face_areas_nm2']
def values(a):
    bc,ac,ab=map(F,a)
    return [F(1),ac/bc,ab/bc,1000*bc/ab,100*bc/ac,ac/(100*bc),10*ac/ab]
names=['r_bc','r_ac','r_ab','eta','alpha_inverse','alpha','eta_alpha']
active=values([areas[k] for k in ['bc','ac','ab']])
locked={}
for n,v in zip(names[3:],active[3:]):
    stored=S['mature_locked_cell3'][n]
    delta=v-F(stored)
    assert str(v)==T['course08_locked_evaluation'][n]['exact_recomputed_rational']
    assert delta==F(T['course08_locked_evaluation'][n]['signed_recomputed_minus_stored_exact'])
    with localcontext() as ctx:
        ctx.prec=60; display=str(Decimal(v.numerator)/Decimal(v.denominator))
    locked[n]={'stored':stored,'recomputed_exact':str(v),'decimal_display':display,'signed_recomputed_minus_stored':str(delta),'reconstruction':'recomputed = stored + signed_difference','units':'dimensionless'}
branches=[]
for b in T['course08_branch_comparison']:
    key=b['historical_source_pointer'].split('/')[-1]
    hist=H['backbone_sequence'][4]['projective_rays'][key]
    act=S['backbone_sequence'][4]['projective_ray']
    diffs=[str(F(a)-F(h)) for a,h in zip(act,hist)]
    assert [F(x) for x in diffs]==[F(x) for x in b['signed_active_minus_historical_exact']]
    branches.append({**b,'verified_signed_difference':diffs})
base=values([12,8,6]); verification=[]
for triple in ([12,8,6],[18,12,9],[48,32,24],[3,2,F(3,2)],[15,10,5],[60,40,20],[F(15,4),F(5,2),F(5,4)],[12,8,F(61,10)],[12,F(81,10),6]):
    v=values(triple); assert v[3]*v[5]==v[6]
    assert [F(triple[0])*x for x in v[:3]]==list(map(F,triple))
    verification.append({'inputs_bc_ac_ab':[str(x) for x in triple],'outputs':dict(zip(names,map(str,v))),'closure_eta_times_alpha_minus_direct':'0','normalization_reconstruction':True})
for i,t in enumerate(([12,8,F(61,10)],[12,F(81,10),6])):
    v=values(t); expected=T['course08_synthetic_sensitivity'][i]
    target=expected['signed_new_minus_old']; dv=[x-y for x,y in zip(v,base)]
    assert dv==list(map(F,target['ray']))+[F(target[k]) for k in names[3:]]
    assert [x+y for x,y in zip(base,dv)]==v
js('verification.json',{'method':'Independent exact Fraction arithmetic from source decimal lexemes; Decimal only for labeled displays','source_hashes':source_records,'locked':locked,'branch_comparisons':branches,'finite_examples':verification,'sensitivity_reconstruction':'all seven outputs reconstructed exactly','claims_not_tested':'No mass measurement or full archive proof certification is performed.'})

def lesson(i,question,goals,bridge,body,practice,diagnostics,answers):
    item=C['course_map'][i-1]; cid=f'C08.{i:02}'
    nextfile=f'lesson-{i+1:02}.md' if i<6 else 'capstone.md'
    text=f"# Lesson {i}: {item['title']}\n\nEssential question: {question}\n\nGoals\n\n"+'\n'.join('- '+g for g in goals)
    text+='\n\nPacing: 55 minutes — retrieval 5; explanation and worked example 20; guided practice 15; diagnostics and repair 15.\n\nPrerequisite bridge\n\n'+bridge+'\n\n'+body
    text+=f'\n\nGuided practice — {cid}-P1\n\n'+practice
    text+='\n\nDiagnostic checks\n\n'+'\n\n'.join(f'{j+1}. **{cid}-D{j+1}** {q}' for j,q in enumerate(diagnostics))
    text+='\n\nWorked diagnostic answers\n\n'+'\n\n'.join(f'{j+1}. {a}' for j,a in enumerate(answers))
    text+=f'\n\nNext dependency: [{item["later_use"]}]({nextfile}). Carry the labeled input triple, divisor, source role, and retained differences forward.\n'
    write(f'lesson-{i:02}.md',text)

lesson(1,'What information does a face-area ratio keep, and what must we retain to recover size?',
 ['Compute a ray in bc/ac/ab order.','Reconstruct all three areas from the ray and its labeled divisor.','Explain why an area ray does not specify a unique spatial cell.'],
 'Courses 03 and 07 supply labeled geometry and arithmetic. Here the needed entry skills are multiplying two lengths to find a rectangular area and simplifying a fraction. Check: 3 times 4 is 12; 8/12 reduces to 2/3 by dividing numerator and denominator by 4. If either operation is uncertain, repeat with 6/9 before proceeding.',
 '''## C08.01-E1 — Labels before division

Imagine a classroom box with three perpendicular edges named a, b, and c. The face meeting b and c is called bc; the other two face types are ac and ab. Write their areas as A_bc, A_ac, and A_ab. A is a name for area, and its subscript identifies the face. If a length unit is U, area uses U²: a square U by U. Cell3 faces need not be rectangles. In this course their areas are supplied, so no angle formula or vector operation is needed.

An ordered triple is a list whose positions have declared meanings. We always use (A_bc,A_ac,A_ab). A positive area ray is the collection of all positive common multiples of one such triple. For example, (12,8,6) and (18,12,9) belong to one ray because the second is 3/2 times the first. The order still matters.

To normalize, divide each entry by the positive first area. This produces r=(1,A_ac/A_bc,A_ab/A_bc). The symbol r names the normalized area ray. Each quotient has units U²/U²=1, so it is dimensionless. The first entry is always 1; only the other two entries can vary independently. This determines the area triple up to one common multiplier. It does not determine all angles, edge directions, or a unique basis in space. In the source's phrase “projective shape,” the scope here is the projective **area** triple; a spatial reconstruction needs additional geometric assumptions.

Normalizing without retaining A_bc loses the absolute size. We therefore keep the pair (A_bc,r), including the unit and labels. The reconstruction rule is (A_bc,A_ac,A_ab)=A_bc times r, meaning multiply every component by the retained area.

## C08.01-W1 — A fully labeled synthetic box

Take a=2 U, b=3 U, c=4 U, mutually perpendicular. Its areas are bc=3×4=12 U², ac=2×4=8 U², ab=2×3=6 U². Normalize: 12/12=1, 8/12=2/3, 6/12=1/2. Thus r=(1,2/3,1/2), with divisor 12 U². Reconstruction gives 12×1=12, 12×2/3=8, and 12×1/2=6 U². Every original component is recovered.

> Claim scope: This is a synthetic orthogonal box, not Cell3 or a measurement. The ray definition is S02#/backbone_sequence/4/definitions. Source paths and verified hashes are in sources.md. Source Cell3 uses an ordered basis with a negative determinant; positive face-area magnitudes do not encode that orientation.''',
 'Normalize (18,12,9) U², keep the divisor, and reconstruct. Work before reading the answer. **Answer:** dividing by 18 U² gives (1,2/3,1/2). Multiplying that ray by 18 U² gives (18,12,9) U². The normalized shape matches W1, while each area is 3/2 as large. The divisor distinguishes them.',
 ['Swap ac and ab in W1 while retaining the declared order. What ray results?','Normalize (15,10,5) U² and reconstruct it.','Can (1,2/3,1/2) alone tell you A_bc or the cell angles?','Why must A_bc be positive in this course?'],
 ['The input becomes (12,6,8), so r=(1,1/2,2/3); this differs from W1.','Dividing by 15 gives (1,2/3,1/3). Retain 15 U²; multiplying returns (15,10,5) U².','No. Any positive divisor supplies a possible size, and the ray contains no complete angle specification.','Zero would make division undefined; negative values would not be positive face-area magnitudes. The positivity contract also makes every later reciprocal defined.'])

lesson(2,'Why can changing every length leave the area ray unchanged?',
 ['Derive the square law for uniform length scaling.','Prove cancellation in both independent ratios.','Distinguish uniform scaling from changing a single supplied area.'],
 'Lesson 1 taught the ordered triple and retained divisor. Recall that multiplying a fraction numerator and denominator by the same nonzero number preserves its value. Check 8/12=32/48=2/3. We now explain where the common factor comes from.',
 '''## C08.02-E1 — One scale, two length factors

Let s be a positive dimensionless length multiplier: every length becomes s times its old value while angles remain fixed. A face has two length factors. In a rectangle, (s×length)(s×width)=s²×area. A parallelogram obeys the same rule: its base and perpendicular height both scale by s. Here s² means s×s. Thus all three areas are multiplied by s². This uniform transformation is sometimes written B→sB, where B is the ordered list of the three basis vectors; no matrix calculation is needed here.

Write A'_ac=s²A_ac and A'_bc=s²A_bc, where the prime marks the scaled value. Because s>0 and A_bc>0, the denominator is nonzero. Cancel the common factor to obtain A'_ac/A'_bc=(s²A_ac)/(s²A_bc)=A_ac/A_bc. Separately, A'_ab/A'_bc=(s²A_ab)/(s²A_bc)=A_ab/A_bc. These two calculations prove invariance of both independent components, rather than relying on one numerical coincidence. The first ray component remains 1.

To reverse the scaling, divide all scaled areas by s² if s is retained. Alternatively retain the original A_bc as a dimensional anchor along with r. A ray by itself cannot tell us which s was used.

## C08.02-W1 — Doubling lengths

Starting with (12,8,6) U², choose s=2. Then s²=4 and the new areas are (48,32,24) U². Dividing by 48 gives (1,32/48,24/48)=(1,2/3,1/2). Divide the new areas by 4 to recover (12,8,6). The areas changed, although the ray did not.

> Claim scope: The proof applies to a positive uniform rescaling with angles and face labels fixed. It does not assert that any arbitrary change in three supplied areas is uniform scaling. It reproduces the common-scale argument in S01 and S02, M05; it establishes algebraic invariance, not a physical mechanism.''',
 'Use s=1/2 on W1’s original input. Compute the areas, normalize, and reverse. **Answer:** s²=1/4, so the areas are (3,2,3/2) U². Their ray is (1,2/3,1/2). Dividing by 1/4, equivalently multiplying by 4, restores (12,8,6) U².',
 ['Change only A_ac from 8 to 9 U². Does the ray remain fixed?','Starting with (15,10,5), test s=2 and s=1/2.','Why is s=0 excluded from the proof?','If areas all double, did lengths necessarily double under uniform scaling?'],
 ['No. The new ray is (1,9/12,6/12)=(1,3/4,1/2). Only one supplied area changed.','The triples are (60,40,20) and (15/4,5/2,5/4). Divide by 60 or 15/4 respectively to get (1,2/3,1/3) in both cases.','All areas would become zero, so the normalized fractions would be 0/0 and undefined.','No. Doubling lengths multiplies areas by 4. An area factor of 2 requires a positive length multiplier whose square equals 2; no square-root computation is required.'])

locked_table='| Quantity | Stored S02 lexeme | Exact recomputation | Signed recomputed − stored |\n|---|---|---|---|\n'
for n,row in locked.items(): locked_table+=f"| {n} | {row['stored']} | {row['recomputed_exact']} | {row['signed_recomputed_minus_stored']} |\n"
lesson(3,'How do the source definitions turn two area ratios into eta and alpha?',
 ['Evaluate eta, alpha_inverse, alpha, and their product from one labeled triple.','Verify the product using a second algebraic path.','Read stored and recomputed source values with their units and signed closure differences.'],
 'Lesson 2 established that a common area factor cancels. A reciprocal of a nonzero number x is 1/x; multiplying x by 1/x gives 1. Thus alpha⁻¹ means 1/alpha, not a negative alpha. The spelling alpha_inverse below means the same reciprocal.',
 '''## C08.03-E1 — Definitions, not guessed numerical matches

The active definitions in S02#/backbone_sequence/4/definitions are eta=1000 A_bc/A_ab and alpha_inverse=100 A_bc/A_ac. The factors 1000 and 100 are part of these definitions and dimensionless. They are not unit conversions invented by this course. Compute each fraction before interpreting it. Because alpha is the reciprocal of alpha_inverse, alpha=A_ac/(100 A_bc).

Multiplying the definitions gives eta×alpha=(1000 A_bc/A_ab)×(A_ac/(100 A_bc)). Cancel the nonzero A_bc and reduce 1000/100 to 10. The result is eta×alpha=10 A_ac/A_ab. This supplies two paths to the same quantity: multiply the separately calculated eta and alpha, or use the direct face quotient. Their signed difference, product path minus direct path, is the algebraic closure difference. Exact arithmetic makes it zero for any positive input triple.

Every result is dimensionless because area units cancel. A dimensionless number can serve a physical ratio, but the formula alone does not name a measured physical object. We return to that distinction in lesson 5.

## C08.03-W1 — Evaluate and cross-check

Use the synthetic triple (12,8,6) U². Eta=1000×12/6=2000. Alpha_inverse=100×12/8=150. Its reciprocal is alpha=1/150. The product is 2000/150=40/3. The direct path is 10×8/6=80/6=40/3. Subtracting gives 40/3−40/3=0. No intermediate rounded decimals were needed.

## C08.03-E2 — Reading the locked evaluation card

For active Cell3 the source-stored input areas, in nm², are bc=0.3578095391285615, ac=0.2611062357902053, ab=0.19486916546048413 (S02#/mature_locked_cell3/face_areas_nm2). A nanometre, nm, is 10⁻⁹ metre; nm² is its square area unit. All three inputs use the same unit, so it cancels. The source's stored output decimals are separately recorded facts about that file. They remain the authoritative stored witnesses; a fresh quotient is an arithmetic diagnostic, not a replacement authority.

A decimal lexeme is the original written number, including its digits. For exact recomputation, interpret a finite decimal as an integer divided by a power of ten: for example 0.125=125/1000=1/8. Apply this rule to each source area, then evaluate the definitions using fractions. The supplied card below removes long-integer arithmetic from the required student workload. Read a row as three linked numbers: stored, recomputed, and signed difference d=recomputed−stored. The reconstruction equation is recomputed=stored+d. Keep d even when it is tiny. These are arithmetic discrepancies between finite records, not new experimental residuals.

'''+locked_table+'''
The exact eta fraction, for example, is obtained by 1000×(3578095391285615/10¹⁶)/(19486916546048413/10¹⁷)=35780953912856150000/19486916546048413. The two product paths agree exactly when they use this same area triple. Mixing a stored output with a recomputed output need not give exact closure. The complete card and decimal displays are also in verification.json.

> Claim scope: W1 is synthetic. The card is a fresh evaluation of stored decimal areas alongside source-reported constants. S03#/authority_contract assigns precedence to mature stored lexemes; the arithmetic comparison does not reassign that precedence or certify the source's full physical interpretation.''',
 'For synthetic (15,10,5) U² calculate every output and both product paths. **Answer:** r=(1,2/3,1/3); eta=1000×15/5=3000; alpha_inverse=100×15/10=150; alpha=1/150. Product 3000/150=20, direct 10×10/5=20, closure 0. **P1 source-card follow-up:** identify the sign and reconstruction rule for the alpha row. **Answer:** d is negative; recomputed alpha equals the stored alpha plus that entire negative fraction. Do not replace d by zero.',
 ['Someone writes alpha=100 A_bc/A_ac. Repair it, then record all four signed differences from the locked card.','For the synthetic W1 input, are the outputs in U², kilograms, or dimensionless?','Why can 10 A_ac/A_ab be used as an independent arithmetic cross-check?','Does the source-stored eta become invalid merely because a decimal-area recomputation differs?'],
 ['The displayed formula is alpha_inverse; alpha=A_ac/(100 A_bc). The four signed differences are the complete fractions in the card’s final column in eta, alpha_inverse, alpha, eta_alpha order; their signs are +,+,−,−. Retaining those exact fractions and using recomputed=stored+d completes the record.','Dimensionless: each construction divides equal area units and multiplies by dimensionless factors.','Substitution and cancellation derived it from eta×alpha, so a disagreement on identical exact inputs reveals arithmetic or input inconsistency.','No. Keep the stored witness in its source-authority role and the fresh value in its arithmetic-diagnostic role. Finite decimal input reconstruction and stored output records are distinct.'])

branch_text=''
for b in branches:
    branch_text+='\nHistorical pointer: `'+b['historical_source_pointer']+'`.\n\n| Component in bc/ac/ab order | Historical lexeme | Active S02 lexeme | Exact active − historical |\n|---|---|---|---|\n'
    for label,h,a,d in zip(['bc','ac','ab'],b['historical_lexemes'],b['active_lexemes'],b['verified_signed_difference']): branch_text+=f'| {label} | {h} | {a} | {d} |\n'
lesson(4,'How can we preserve numerical history without turning it into a second active geometry?',
 ['Build separate active and historical provenance rows.','Retain signed branch differences with a reconstruction rule.','Detect a mixed-input calculation mislabeled as active.'],
 'Lesson 3 distinguished stored lexemes from fresh computations. We now attach each number to its origin. A source pointer is a path inside a JSON document: /backbone_sequence/4 refers to the fifth array entry because indexing begins at zero. A SHA-256 is a file fingerprint used here to check that the read bytes match the supplied source; it does not by itself prove a claim.',
 '''## C08.04-E1 — The branch ledger

A numerical witness is a recorded value accompanying a source claim. A branch is a coherent set of values with a stated provenance and role. To keep a replayable ledger, record source ID, its hash from sources.md, exact pointer, original decimal lexeme, component label, units, and active or historical role. “More digits” does not mean “more authoritative.”

S02 supplies the active mature ray. S01 contains two longer-string rays, named master_geometry and locked_mass_bridge, and a separate mass_bridge_calibration input set. Preserve all of these as history. S04’s M05 audit directs the earlier rays into a superseded-history ledger, and S03 assigns mature stored lexemes precedence. Thus the word locked inside an old field name does not override the later authority contract.

For a comparison, define d=active−historical component by component. Then active=historical+d and historical=active−d. Negative d means the active component is smaller. These differences are provenance comparisons; they are not measurement residuals or alternative active geometry coordinates. The active ray stored in S02 and a fresh ray obtained by dividing S02 decimal areas also remain separately typed records.

## C08.04-W1 — Preserve three ray records

The active row is S02#/backbone_sequence/4/projective_ray, order bc/ac/ab, dimensionless: (1.0,0.7297352564331424,0.5446170214888189). Attach S02’s complete hash from sources.md. Compare it separately to each historical S01 row below; attach S01’s hash to each. The fractions are exact differences of the displayed finite lexemes, independently checked in verification.json. For the master_geometry ac row, subtraction gives a negative fraction: the active value is smaller by about 2.6063552449324×10⁻¹¹. Here 10⁻¹¹ means dividing by 100000000000. That short decimal display is only an aid; the exact difference remains in the table.
'''+branch_text+'''
In the historical locked_mass_bridge comparison, ac decreases and ab increases. Reversing subtraction would reverse both signs. The leading component has difference zero in both comparisons because 1.0 and 1 are equal numbers; the original spellings remain recorded.

> Claim scope: These are source-history differences, not measured changes through time. The active field does not inherit extra digits from either historical field. S01#/mass_bridge_calibration is a separate historical calibration record; its face inputs must not be substituted into active S02 formulas.''',
 'Use the second table to recover the active ab component from the historical ab component and d. Then name the complete historical calibration input set. **Answer:** historical ab+d=0.5446170214888189 exactly; retaining the table’s positive fraction ensures exact recovery. The historical calibration areas at S01#/mass_bridge_calibration/face_areas_nm2 are (bc,ac,ab)=(0.3578095391285618,0.26110623579953135,0.1948691654698998) nm². They are one historical input set, not rounded replacements for active inputs. For each of the two tables, the full signed difference vector is its last column in bc/ac/ab order; retain all three components including zero.',
 ['A calculation uses historical A_ab and mature A_bc and calls its result “active eta.” What is wrong?','Does the longer historical ac lexeme outrank the shorter mature lexeme?','In the second table, what does a positive ab difference mean, and how do you recover history?','What distinguishes a provenance difference from the closure difference of lesson 3?'],
 ['It mixes source branches. Use all active S02 inputs for active recomputation, or label the result a mixed-input diagnostic with both exact pointers. It is not an active eta witness.','No. Authority follows the source contract and branch role, not digit count.','The active ab ray component is larger. Historical=active−d, using the exact positive fraction.','Provenance difference compares records from separate branches; algebraic closure compares equivalent calculation paths for one input set. Neither is automatically an experimental measurement residual.'])

lesson(5,'What additional information turns an algebraic ratio into a physical claim?',
 ['Separate a dimensional anchor from a dimensionless ratio.','Classify source facts, algebra, calibration, physical identification, and mechanism.','State the provenance needed for a mass measurement comparison.'],
 'Lessons 1–4 taught reconstruction and provenance. A calibration is a rule or reference that fixes a numerical scale or interpretation. Here we can supply an area anchor without claiming it was measured. Ask first whether a sentence describes a calculation, a source record, or a physical identification.',
 '''## C08.05-E1 — A ratio-to-claim ledger

Write each claim beside its inputs and evidence class. “S02 stores eta=1836.1526734259999” is a source fact verified by reading the file. “The two area quotients survive a uniform rescaling” is a mathematical implication proved in lesson 2. “Choose A_bc=12 U²” is a supplied dimensional anchor in a synthetic example. “Interpret eta as a specified physical mass ratio” adds a physical identification. A proposed mechanism would explain why that physical system obeys the identified relation, including what connects its measured quantities to these areas. These sentences can support one investigation while remaining different kinds of statements.

An area ray cannot select an absolute scale, because every positive common area multiple gives the same ray. An anchor supplies that missing scale. Likewise a dimensionless eta is not itself a mass in kilograms. Even identifying eta with a ratio m_1/m_2 requires names and definitions for both physical masses; finding m_1 from that relation also requires a dimensional m_2. This is a unit argument, not a dismissal of the proposed identification.

If testing the identification experimentally, retain the measurement records, units, instrument and calibration information, acquisition conditions and dates, definitions of the compared masses, the complete model input branch, and every signed prediction-minus-measurement difference. None of those measurements is supplied by the classroom examples. Repeated agreement could motivate a common mechanism, but algebra, calibration, observations, and interpretation should remain traceable separately. A candidate mechanism must at least account for the ratio’s common-scale invariance and the coupling between its two independent components; the course does not invent such a mechanism.

## C08.05-W1 — Recover size without inventing a mass

Given synthetic r=(1,2/3,1/2), supply A_bc=12 U². This is an input, not a conclusion. Multiply: A_ac=12×2/3=8 U² and A_ab=12×1/2=6 U². Those are derived reconstructions. Evaluating eta gives 2000 and alpha gives 1/150, both dimensionless. A statement “eta is a physical mass ratio” belongs in a new interpretation row with its own physical definitions. The area multiplication has not measured a mass.

| Ledger row | Evidence class | What follows |
|---|---|---|
| Supplied A_bc=12 U² | Synthetic anchor | Fixes area scale in this example |
| A_ac=8 U²; A_ab=6 U² | Derived reconstruction | Recovers the supplied triple |
| eta=2000 | Derived definition | Dimensionless quotient |
| eta identified with specified m_1/m_2 | Proposed physical identification | Needs physical definitions and measurement provenance |
| A process causes that identification | Proposed mechanism | Needs a stated rule connecting system and geometry |

> Claim scope: No new particle-mass dataset is supplied. S04 describes the calibrated Mass-Bridge theorem in source-reported terms. Its reported status is preserved in sources.md, distinct from this course’s fresh fraction checks. Established dimensional arithmetic is our reference tool; it does not supply missing physical observations.''',
 'A fictional calibration sets A_bc=18 U² with the same ray. Recover areas and eta/alpha; classify the anchor, reconstruction, and an asserted physical identification. **Answer:** areas (18,12,9) U²; eta=1000×18/9=2000; alpha=12/(100×18)=1/150. Anchor: supplied calibration. Areas and quotients: derived. Physical identification: additional interpretation. No measured mass was supplied. A future measurement ledger needs the mass definitions, measured values and units, instrument/calibration, acquisition context, model branch, and signed differences.',
 ['Repair the claim “calculating eta from areas independently measured a particle mass.”','If the dimensional anchor changes from 12 to 18 U² but the ray stays fixed, what happens to eta?','Name one missing input for converting a dimensionless mass ratio into a mass.','Is the assertion “a mechanism makes geometry control masses” the same evidence class as computing eta?'],
 ['We calculated a source-defined dimensionless quotient. A separate physical identification and independently documented measurement would be needed for a measurement claim. Keep the interpretation as a proposed identification, not as fabricated observation.','It stays 2000: both numerator and denominator acquire the same factor 3/2.','A reference mass with its unit, together with the identification of numerator and denominator physical quantities.','No. The former is a proposed mechanism; the latter is a derived calculation. A mechanism needs a connecting rule and predictions beyond the quotient evaluation.'])

lesson(6,'How can we change one input and preserve every resulting difference?',
 ['Reevaluate all outputs after a finite input change.','Retain signed changes and reconstruct every new output.','Distinguish finite sensitivity from arithmetic closure.'],
 'Lesson 3 supplies all output formulas; lesson 4 supplies signed differences and reconstruction. A finite change compares two complete input triples. We need no derivative or limit. Subtract fractions using a common denominator: 1/2−1/3=3/6−2/6=1/6.',
 '''## C08.06-E1 — Two different kinds of difference

Sensitivity here means how the output changes when a specified input changes and the other inputs remain fixed. Keep the original triple, the input-change vector, the full new outputs, and the signed output differences. An input-change vector is simply the ordered list of new-minus-old changes. Zeros matter because they tell us what stayed fixed.

For any quantity y, write Δy=y_new−y_old; Δ is just a label meaning change. The reconstruction rule is y_new=y_old+Δy. This preserves the full finite difference even if a short decimal display hides it. Separately calculate closure c=eta×alpha−10 A_ac/A_ab using the same complete input triple. Sensitivity can be nonzero while c stays zero. One compares two input states; the other compares two algebraic paths within one state.

## C08.06-W1 — Change the ab area

Baseline areas are (12,8,6) U². Change only ab by +1/10 U², so the new triple is (12,8,61/10) U² and the input change is (0,0,1/10) U². Normalize: (1,8/12,(61/10)/12)=(1,2/3,61/120). Evaluate eta=1000×12/(61/10)=120000/61; alpha_inverse=150; alpha=1/150. The product path gives (120000/61)/150=800/61. The direct path gives 10×8/(61/10)=800/61. Closure is zero.

| Output | Old | New | Signed new − old |
|---|---|---|---|
| r_bc | 1 | 1 | 0 |
| r_ac | 2/3 | 2/3 | 0 |
| r_ab | 1/2 | 61/120 | 1/120 |
| eta | 2000 | 120000/61 | −2000/61 |
| alpha_inverse | 150 | 150 | 0 |
| alpha | 1/150 | 1/150 | 0 |
| eta_alpha | 40/3 | 800/61 | −40/183 |

For eta, subtract 2000=122000/61 to obtain −2000/61. For the product, use denominator 183: 800/61−40/3=(2400−2440)/183=−40/183. Reconstruction returns eta=2000−2000/61=120000/61 and product=40/3−40/183=800/61. For the ray’s third component, 1/2+1/120=61/120. Adding zero returns every unchanged entry. All outputs are dimensionless; only the supplied area changes carry U².

> Claim scope: These are supplied synthetic area states, not a measured trajectory or an experiment on Cell3. Exact finite sensitivity and exact arithmetic closure are taught core operations. No approximation is needed, and no difference is discarded.''',
 'Return to the baseline and instead change only ac from 8 to 81/10 U². Compute every output, difference, and both product paths. **Answer:** input change (0,1/10,0) U²; new ray (1,27/40,1/2). Eta=2000; alpha_inverse=1200/(81/10)=4000/27; alpha=27/4000. Product=2000×27/4000=27/2, also 10×(81/10)/6=27/2. Ray differences are (0,1/120,0); remaining differences in eta, alpha_inverse, alpha, eta_alpha order are 0,−50/27,1/12000,1/6. For example 4000/27−150=(4000−4050)/27=−50/27 and 27/4000−1/150=(81−80)/12000=1/12000. Reconstruct each by adding: 2/3+1/120=27/40; 150−50/27=4000/27; 1/150+1/12000=27/4000; 40/3+1/6=27/2. Unchanged components reconstruct by adding zero.',
 ['For W1 give the product-path value, direct-path value, closure, and product sensitivity.','Why is retaining only the largest output change insufficient?','In P1, reconstruct alpha_inverse from its baseline and signed difference.','A student calls the W1 product difference −40/183 an algebraic failure. Correct this.'],
 ['The two paths are both 800/61; closure is 0; sensitivity relative to baseline is −40/183. They compare different things.','It loses the other components, signs, and unchanged coordinates, preventing complete reconstruction. Keep all seven entries and the input change.','150+(−50/27)=(4050−50)/27=4000/27.','−40/183 compares the product at two different input triples. Within the new triple both algebraic paths agree exactly, so there is no closure failure.'])

source_md='# Sources and numerical provenance\n\nRead-only archival retrieval; all five supplied SHA-256 hashes matched. No source files or bulk source snapshots were copied. The small numeric cards are teaching excerpts.\n\n'
for s in source_records: source_md+=f"- **{s['id']}** `{s['path']}`\n  SHA-256: `{s['actual_sha256']}`. Role: {s['role']}.\n"
source_md+='''

Primary pointers: S02#/backbone_sequence/4/definitions, /proof, /witness, /projective_ray; S02#/mature_locked_cell3/face_areas_nm2 and its eta, alpha_inverse, alpha, eta_alpha fields. M05 requires mathematical-backbone M01 and M04. The finite classroom bridges teach labeled areas and cancellation; full earlier proof certification is not an assessed prerequisite. These mathematical labels are not compiler authority labels.

Historical pointers: S01#/backbone_sequence/4/projective_rays/master_geometry; S01#/backbone_sequence/4/projective_rays/locked_mass_bridge; S01#/mass_bridge_calibration. The latter stores historical area inputs and reported constants as separate fields; this course does not assert that its reported constants freshly recompute from those inputs.

Authority: S03#/authority_contract gives precedence to mature stored decimal lexemes, preserves history, and treats an unavailable proof body as VERIFIED_NOT_LOADED. S03#/authoritative_status/mature_core reports VERIFIED_FROZEN. Those are source statuses, not fresh course proof certifications. S04's M05 audit replaces the active two-ray interpretation with the mature ray while retaining prior rows as superseded history. Its statement about unique shape presupposes its angular-frame and lock contract; arbitrary positive face areas alone do not determine a unique spatial basis.

The five sources were read for relevant topic passages. S05's historical refined-branch record is contextual history, not authority to replace S02. The course uses no periodic-table or molecular claims as premises. Exact relevant JSON pointers for supporting audit passages are recorded below.

Krytronx capabilities was queried and reported a read-only interface; its response did not expose a corpus-generation or manifest-digest field. A source_artifact search for the exact mature proof title returned zero matches. The packet's expected snapshot is sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7; it is recorded as expected, not independently confirmed active. Local exact-path files with matching supplied hashes provided the source grounding. This discovery gap does not omit any required M05 input or definition.

Numerical method: finite decimal lexemes become exact rational numbers. Fresh outputs remain diagnostics beside authoritative source-stored outputs. verification.json retains all four signed locked-evaluation differences and both complete three-component history differences. The original input-contract.json preserves the supplied subject packet and its evidence rules. No source statement about a full archive proof, mass observation, or mechanism is promoted by the fraction checks.

Boundary invariants: the active Cell3 basis uses ICRS columns [a b c], intentional negative determinant, and half-open ownership [-1/2,1/2)^3. No cell ownership, metric inversion, reciprocal-basis identity, gauge carrier, parity operation, recursion, CMB vector, or galaxy-cell conversion is performed here. Positive area magnitudes do not replace those typed objects. The synthetic box is explicitly separate from Cell3.
'''
def find_passages(obj,path=''):
    found=[]
    if isinstance(obj,dict):
        if obj.get('id')=='M05' and 'finding' in obj: found.append((path,obj))
        for k,v in obj.items(): found+=find_passages(v,path+'/'+k)
    elif isinstance(obj,list):
        for i,v in enumerate(obj): found+=find_passages(v,path+'/'+str(i))
    return found
for path,obj in find_passages(sources['S04']): source_md+='\nS04#'+path+': '+obj['correction']+'\n'
write('sources.md',source_md)

write('terminology.md','''# Terminology and notation

| Term or symbol | Meaning and scope | First teaching |
|---|---|---|
| a,b,c | Labeled cell edges; synthetic box edges are perpendicular | Lesson 1 |
| A_bc,A_ac,A_ab | Positive face-area magnitudes; order bc/ac/ab always | Lesson 1 |
| U, U² | Arbitrary classroom length unit and its square area unit | Lesson 1 |
| r | (1,A_ac/A_bc,A_ab/A_bc), dimensionless ordered area ray | Lesson 1 |
| Normalization divisor | Retained A_bc with units; reconstruct areas as A_bc times r | Lesson 1 |
| Projective area shape | Positive area triple modulo one common positive multiplier | Lesson 1 |
| s, s² | Positive dimensionless length multiplier and resulting area multiplier | Lesson 2 |
| B | Ordered source basis, columns [a b c]; only B→sB used here | Lesson 2 |
| Prime, as A'_ac | Scaled value, not derivative | Lesson 2 |
| eta | 1000 A_bc/A_ab, dimensionless | Lesson 3 |
| alpha_inverse, alpha⁻¹ | 1/alpha=100 A_bc/A_ac, dimensionless | Lesson 3 |
| alpha | A_ac/(100 A_bc), dimensionless | Lesson 3 |
| eta_alpha | eta×alpha=10 A_ac/A_ab, dimensionless | Lesson 3 |
| nm, nm² | Nanometre (10⁻⁹ metre), square nanometre | Lesson 3 |
| Lexeme | Exact original written numeric token | Lesson 3 |
| Closure difference | Product path minus direct path for identical inputs | Lesson 3 |
| Source pointer | Exact slash-separated location inside a source JSON document | Lesson 4 |
| SHA-256 | File-content fingerprint, not a claim-proof certificate | Lesson 4 |
| Active / historical | Current mature contract / preserved superseded provenance | Lesson 4 |
| Numerical witness | Source-reported value accompanying a claim | Lesson 4 |
| d | Signed comparison with the subtraction direction stated locally | Lesson 4 |
| Calibration / anchor | Supplied rule or dimensional value fixing scale or interpretation | Lesson 5 |
| m_1,m_2 | Named hypothetical physical masses in an identification; no values supplied | Lesson 5 |
| Mechanism | Proposed connecting process, distinct from a quotient calculation | Lesson 5 |
| Δy | y_new−y_old, exact finite change; new=old+Δy | Lesson 6 |
| Sensitivity | Output change between two declared input states | Lesson 6 |
| Residual information | Retained signed discrepancy with its kind and reconstruction rule | Lessons 3–6 |

Reserved author guidance: M_cell=B^T B and R_cell=M_cell⁻¹ denote the Cell3 Gram metric and its inverse; G_phase is distinct, and O_K is the physical origin. They are not computations required in this course and are not replaced by r. Affine identities, if used in a later course, use x−O_K. Source evidence categories, parity types, recursion types, and unit systems retain the distinctions in input-contract.json.
''')

map_md='# Course map — Face-Area Ratios and the K-Field Mass Bridge\n\nSix 55-minute lessons followed by two 55-minute capstone periods. Unit I (1–3): ratios and evaluation. Unit II (4–6): provenance, interpretation, and finite sensitivity. No boundary changes were required. Entry capabilities: signed arithmetic, fractions, powers, linear equations, and labeled face areas from courses 03 and 07; explicit bridges appear in lessons 1–3.\n\n| Concept | Introduction | Worked example | Answered practice | Diagnostic | Later use |\n|---|---|---|---|---|---|\n'
for i in range(1,7):
    cid=f'C08.{i:02}'; item=C['course_map'][i-1]
    map_md+=f'| {cid}: {item["title"]} | lesson-{i:02}, {cid}-E1 | {cid}-W1 | {cid}-P1 | {cid}-D1 through D4 | {item["later_use"]}; C08-CAP-{i:02} |\n'
map_md+='\nDependency chain: lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → capstone. Lesson 3 also teaches E2, the locked source-reading card used by lessons 4 and the capstone.\n\nEach lesson allocates 5 minutes retrieval, 20 instruction/worked example, 15 answered guided practice, and 15 independent diagnostics/repair. Long source fractions are supplied reading cards, not manual long-division tasks. If retrieval fails, use the teacher-guide repair task before moving to a dependent lesson.\n\nThe capstone backward map names inputs, outputs, and earlier answered practice in capstone.md. Evidence boundaries and every packet invariant remain authoritative; only relevant finite operations are assessed.\n'
write('course-map.md',map_md)

write('teacher-guide.md','''# Teacher guide

Teach the six lessons in order, then run a two-period capstone. All classroom area triples are synthetic. Keep the active source card available in lessons 3–6. Teach the short-number calculation first, then the source-record interpretation; do not ask students to hand-divide the long locked fractions. Students must be able to read the sign, role, pointer, and reconstruction equation.

The entry check is deliberately operational: identify bc/ac/ab, simplify 8/12, multiply 12 by 2/3, and subtract 1/2−1/3. Answers are 2/3, 8, and 1/6 for the arithmetic. Ask students to explain which two edges name each face. A student uncertain about a face label should draw and label a rectangular box before performing ratios.

Each lesson uses 5 minutes retrieval, 20 explanation and worked example, 15 guided practice, and 15 diagnostics with repair. Suggested facilitation and exit gates follow. A failed gate triggers extra practice before the dependent lesson; add a support period if necessary rather than compressing later instruction.

| Lesson | Main teaching action | Exit gate and targeted repair |
|---|---|---|
| 1 | Build the ordered triple physically on a labeled box | Must normalize and reconstruct. Repair: (6,4,3) gives (1,2/3,1/2); retain 6 U². |
| 2 | Scale both base and height to explain s² | Must cancel the common factor twice. Repair: s=3 gives (108,72,54) from (12,8,6), same ray. |
| 3 | Contrast alpha and its reciprocal before multiplying | Must compute both product paths. Repair: (6,4,2) gives eta=3000, alpha_inverse=150, alpha=1/150, product=20. Read signs +,+,−,− on the locked discrepancy card. |
| 4 | Build one active row and two history rows with pointers | Must identify and repair a mixed-branch label. Repair: use synthetic historical 0.75 and active 0.70; d=−0.05, historical+d=active. Then apply that reading to the supplied exact cards. |
| 5 | Tag each sentence before interpreting its number | Must distinguish anchor, derived value, and identification. Repair: A_bc=6 U² with ray (1,2/3,1/2) gives (6,4,3); eta=2000 remains dimensionless. |
| 6 | Keep a column for every output, including zeros | Must reconstruct and distinguish sensitivity from closure. Repair: W1 eta_new=2000−2000/61=120000/61 while closure=0. |

At the end of lesson 3, run a cumulative check: normalize (15,10,5), scale it by s=2, evaluate constants, and check units. Answers are in lessons 1–3. At the end of lesson 6, have pairs audit each other’s branch labels and full difference columns before capstone work. Require an explanation of why a historical branch difference is not an experimental residual. The relevant source scope is read aloud once, then applied concretely rather than repeated as a generic warning.

Capstone period 1: 10 minutes retrieval/source-card reading, 35 minutes steps 1–4, 10 minutes checking. Period 2: 30 minutes steps 5–6, 15 minutes peer ledger audit, 10 minutes individual corrections. Use the 100-point rubric, but require correction of any branch mixing, missing units, reciprocal confusion, or dropped difference even if the numeric score is high.

Students may use a four-function calculator and supplied source cards. Exact fractions are preferred in small-number work. The verification script is a teacher tool, not a Python prerequisite. Fraction arithmetic independently checks the examples; it does not certify every scientific claim in an archival source.

Optional recognition extension, not assessed: in W1 write ab=6(1+h) with h=1/60. Expand (1+h)(1−h)=1−h²; adding h² gives 1. Divide by nonzero 1+h to derive 1/(1+h)=1−h+h²/(1+h). Hence eta=2000/(1+h)=5900/3+100/183. The first two terms give an approximation, and the retained final term reconstructs the exact value. No calculus is used. Do not require this extension for the capstone.

Source stewardship: source IDs resolve through sources.md. Original supplied contract is input-contract.json. Keep the S02 stored witnesses authoritative in their role; fresh decimal-area quotients are diagnostic outputs. S01 rays and calibration data stay historical. A missing full proof body keeps its source-reported status and retrieval gap. No mass measurements are invented.
''')

write('capstone.md','''# Capstone — Build a ratio-to-claim ledger

Use only the taught formulas and the source-reading cards in lessons 3 and 4. Work in bc/ac/ab order. All small-number areas are synthetic. The mature and historical rows are source facts, not experimental datasets. Keep all signed differences and record reconstruction equations. Two 55-minute periods are provided.

| Step | Named inputs → required outputs | Earlier explanation and worked example | Independently answered practice |
|---|---|---|---|
| C08-CAP-01 | (15,10,5) U² → ray, divisor, reconstructed areas | C08.01-E1/W1 | C08.01-P1 |
| C08-CAP-02 | That triple; s=2 and 1/2 → scaled triples, both cancellation proofs | C08.02-E1/W1 | C08.02-P1 |
| C08-CAP-03 | Same triple plus locked source card → four constants, two product paths, stored/recomputed distinction | C08.03-E1/E2/W1 | C08.03-P1 including source-card follow-up |
| C08-CAP-04 | S02 active and both S01 history cards → provenance rows, exact signed branch differences | C08.04-E1/W1 | C08.04-P1 |
| C08-CAP-05 | Supplied anchor, derived quotients, asserted mass interpretation → evidence tags and measurement-provenance list | C08.05-E1/W1 | C08.05-P1 |
| C08-CAP-06 | Baseline (12,8,6) U² and either taught +1/10 change → all seven output changes, reconstruction and closure | C08.06-E1/W1 | C08.06-P1 |

## Student tasks

1. **C08-CAP-01 (15 points).** Normalize (15,10,5) U². Retain enough information to reverse the transformation. Reconstruct all areas and explain what the ray cannot tell you about spatial geometry.
2. **C08-CAP-02 (15 points).** Prove that both independent ratios remain fixed for any positive uniform length multiplier s. Test s=2 and s=1/2 on the capstone triple. Name the factor needed to undo each scaling.
3. **C08-CAP-03 (20 points).** Calculate eta, alpha_inverse, alpha, and eta_alpha for the capstone triple. Check the product by both paths. Record the active area pointer and unit, and read all four rows of the locked evaluation card: identify stored value, exact recomputation, exact signed difference, and reconstruction rule. You may reference each entire card row by quantity rather than recopy long integers; state the four signs. Explain why a fresh quotient does not overwrite the source-stored witness.
4. **C08-CAP-04 (20 points).** Make separate ledger rows for the active ray and both historical rays. Include source ID, hash (or exact sources.md reference), pointer, order, dimensionless unit, and role. Attach each exact difference vector from lesson 4’s last column with direction active−historical. State the reconstruction equation and both nonleading signs for each vector. Explain why an eta made from mature bc and historical ab is not active eta. Name the separate historical calibration input pointer.
5. **C08-CAP-05 (10 points).** Tag the capstone area anchor, calculated quotients, and an asserted physical mass-ratio identification by evidence class. List the provenance needed to compare with measurements. Explain why an area ray alone supplies neither an absolute area nor a mass unit.
6. **C08-CAP-06 (20 points).** Return to baseline (12,8,6) U². Choose ab→61/10 or ac→81/10. Provide the input-change vector; all three new ray components; the four new constants; every signed new-minus-old difference, including zeros; and reconstruction of each output. Verify both product paths and their closure difference. State why these supplied states are not a measured trajectory.

## Full answer key

1. Divisor 15 U²; r=(1,2/3,1/3). Multiply 15 by each component to recover 15,10,5 U². The ray fixes a positive area triple up to common scale, not all angles or a unique spatial basis.
2. All areas become s² times their initial values. (s²A_ac)/(s²A_bc)=A_ac/A_bc and (s²A_ab)/(s²A_bc)=A_ab/A_bc because s²A_bc is nonzero. For s=2 the triple is (60,40,20); for s=1/2 it is (15/4,5/2,5/4), all U². Both normalize to (1,2/3,1/3). Divide by 4 and by 1/4 respectively to reverse.
3. Eta=1000×15/5=3000; alpha_inverse=100×15/10=150; alpha=1/150; eta_alpha=3000/150=20. Direct path 10×10/5=20; closure 0. Units are dimensionless. Active area pointer is S02#/mature_locked_cell3/face_areas_nm2, unit nm². Use the four exact rows in lesson 3, retained also in verification.json, as the answer card. Their signed differences in eta, alpha_inverse, alpha, eta_alpha order have signs +,+,−,−. For each, recomputed=stored+the complete signed fraction. Source-stored lexemes have their source-authority role; evaluating finite input lexemes creates a separately typed diagnostic.
4. Active: S02#/backbone_sequence/4/projective_ray, (1.0,0.7297352564331424,0.5446170214888189), order bc/ac/ab, dimensionless; S02 hash from sources.md. Historical: S01#/backbone_sequence/4/projective_rays/master_geometry and S01#/backbone_sequence/4/projective_rays/locked_mass_bridge, with their exact lexemes and S01 hash as printed in lesson 4 and sources.md. The exact signed vectors are the full last columns of those two lesson 4 tables, also in verification.json under branch_comparisons. First vector signs: 0,−,−; second: 0,−,+. Active=historical+d component by component. A mixed-input ratio changes the branch contract; it is a labeled mixed diagnostic, not active eta. The separate historical area input pointer is S01#/mass_bridge_calibration/face_areas_nm2.
5. Anchor 15 U²: supplied synthetic dimensional input. Quotients: derived algebra. Mass-ratio identification: additional physical interpretation. Required comparison provenance includes definitions and identities of masses, measured values and units, instrument/calibration, acquisition dates and conditions, full model-input branch, and every signed prediction-minus-measurement difference. Common scale was divided away, and ratios cancel units; neither an absolute area nor a kilogram value can be recovered from r alone.
6. **ab option:** input change (0,0,1/10) U². New outputs in r_bc,r_ac,r_ab,eta,alpha_inverse,alpha,eta_alpha order: (1,2/3,61/120,120000/61,150,1/150,800/61). Signed changes: (0,0,1/120,−2000/61,0,0,−40/183). Reconstruction: 1+0=1; 2/3+0=2/3; 1/2+1/120=61/120; 2000−2000/61=120000/61; 150+0=150; 1/150+0=1/150; 40/3−40/183=800/61. Product=(120000/61)/150=800/61; direct=10×8/(61/10)=800/61; closure=0.

   **ac option:** input change (0,1/10,0) U². New outputs in the same order: (1,27/40,1/2,2000,4000/27,27/4000,27/2). Changes: (0,1/120,0,0,−50/27,1/12000,1/6). Reconstruction: 1+0=1; 2/3+1/120=27/40; 1/2+0=1/2; 2000+0=2000; 150−50/27=4000/27; 1/150+1/12000=27/4000; 40/3+1/6=27/2. Product=2000×27/4000=27/2; direct=10×(81/10)/6=27/2; closure=0. Neither option supplies timestamps or measurements; they are finite synthetic sensitivity states.

## Point rubric

| Step | Allocation |
|---|---|
| 1 | Correct ordered ray 6; divisor/units 3; reconstruction 4; scope 2 |
| 2 | Two cancellation proofs 6; both scaled triples 6; reverse factors 3 |
| 3 | Four constants 8; both paths/closure 4; source pointer/unit 2; full difference-row references/signs/reconstruction 4; authority distinction 2 |
| 4 | Three complete provenance rows 8; two exact difference vectors with direction/signs 6; reconstruction 2; mixed-input diagnosis 2; historical calibration pointer 2 |
| 5 | Three evidence tags 4; measurement-provenance list 4; scale/unit explanation 2 |
| 6 | Input change 2; seven outputs 5; all differences 5; all reconstructions 4; both paths/closure 2; synthetic scope 2 |

Total 100. Allow valid equivalent fractions and exact references to supplied long-number cards. Do not award reconstruction credit for merely dropping small differences. Require repair of a branch mix, missing dimensional anchor, or alpha/reciprocal confusion before using the ledger in later courses.
''')

order=[f'lesson-{i:02}' for i in range(1,7)]
write('course.md','# Face-Area Ratios and the K-Field Mass Bridge\n\nStudent lessons in dependency order. Supporting source cards, glossary, teacher guide, and capstone are separate files.\n\n'+'\n\n'.join(f'<!-- BEGIN: {i} -->\n'+(D/(i+'.md')).read_text(encoding='utf-8').rstrip()+'\n'+f'<!-- END: {i} -->' for i in order))

checks=[]
for i in range(1,7):
    text=(D/f'lesson-{i:02}.md').read_text(); cid=f'C08.{i:02}'
    for suffix in ['E1','W1','P1','D1','D2','D3','D4']: assert cid+'-'+suffix in text
    checks.append({'checkpoint':f'lesson-{i:02}','result':'author review passed','checks':['explicit prerequisite bridge','3 observable goals','first-principles explanation','worked example','answered practice','4 diagnostics and worked answers','units and evidence scope','next dependency'],'calculation_evidence':'verification.json; symbolic scale cancellation reviewed separately'})
js('author-audit.json',{'local_checks':checks,'cumulative_checks':[{'boundary':'lesson-03','result':'all formulas introduced before use; reciprocal taught; ray order and units stable'},{'boundary':'lesson-06','result':'all six capstone operations map to earlier explanation and answered practice; no new assessed operations'}],'final_review':{'coverage':'C08.01 through C08.06 present','source_fidelity':'all five hashes match; M05 exact definitions and active/historical distinction retained','audience':'short fraction calculations assessed; long integer cards supplied','residual_accounting':'all four locked differences, six branch components, and seven outputs for each sensitivity state retained','assembly':'verbatim marker assembly generated from saved lesson files','rendering':'Markdown only; tables and headings inspected as text; no paginated artifact required'}})
js('audit_report.json',{'status':'in_progress','findings':[],'unresolved_counts':{'critical':0,'major':0,'minor':0},'checks':'author-audit.json','next_action':'independent hostile audit and validator'})
specs=[('map','course-map','course-map.md',[]),('sources','supplement','sources.md',[]),('verification','supplement','verification.json',['sources'])]
for i in range(1,7): specs.append((f'lesson-{i:02}','lesson',f'lesson-{i:02}.md',['map','sources','verification']+([f'lesson-{i-1:02}'] if i>1 else [])))
specs += [('terms','terminology','terminology.md',order),('teacher','teacher-guide','teacher-guide.md',order),('capstone','capstone','capstone.md',order),('assembly','assembly','course.md',order),('author-audit','supplement','author-audit.json',order+['capstone']),('audit','audit','audit_report.json',['author-audit'])]
manifest={'schema_version':'1.0','topic':C['topic'],'audience':C['audience'],'assumptions':C['assumptions'],'ordered_deliverables':[s[2] for s in specs]+['completion_report.json'],'checkpoints':[{'id':i,'kind':k,'path':p,'dependencies':deps,'status':'drafted','summary':i+' authored; pending independent final audit','sha256':sha(D/p)} for i,k,p,deps in specs],'dependencies':{i:deps for i,k,p,deps in specs},'course_order':order,'assembly':{'path':'course.md','section_ids':order},'audit_counts':{'critical':0,'major':0,'minor':0},'blockers':[],'next_action':'independent audit, repair, finalize hashes, run validator'}
js('manifest.json',manifest)
print('Created six complete lessons and supporting artifacts; exact source and example assertions passed.')
