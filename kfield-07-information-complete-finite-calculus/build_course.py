"""Authored course production; all persistent outputs stay beside this script."""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent
packet=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(name,text): (ROOT/name).write_text(text.strip()+'\n',encoding='utf-8')
def js(name,data): write(name,json.dumps(data,indent=2,ensure_ascii=False))
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
lessons={}
lessons[1]='''
# Lesson 01 — Changes across a finite edge

Essential question: What must we retain to recover a sequence from its changes?

Goals: calculate a signed finite difference; distinguish change from rate; reconstruct ordered values using an anchor; identify source premises as premises.

Prerequisite bridge: You can subtract signed numbers and solve an equation such as 5=2+u. Check 4−9=−5 and 2+3=5 before continuing. No limiting process or previous calculus is assumed. A function here is simply a table assigning one value to each sample ID. A list in parentheses gives the entries in their recorded order. All numerical samples in this course are synthetic teaching data, not measurements.

## C07.01-E1 — A directed transition

Let s name a starting sample and t an ending sample. An oriented edge s→t tells us which comes first in a subtraction. Write f_s for the value at s and f_t for the value at t. The finite difference on that edge is df=f_t−f_s. The letter d names a change, not division. Thus f_t=f_s+df gives the decoder: add the change back to the start. Reversing an edge reverses its sign, because f_s−f_t=−(f_t−f_s).

If f is recorded in signal-units (abbreviated SU), df is also in SU. When the elapsed time Δτ is nonzero, a rate is df/Δτ, in SU/s if time is in seconds. A difference does not require equal time spacing; a rate does require the actual elapsed time. Sample ID and time are different fields, even when both happen to run 0,1,2,3.

For several edges, keep the first value, called an anchor, and add consecutive differences. Differences alone cannot give an absolute level: adding the same constant to every sample changes no differences. Retaining the anchor supplies the missing coordinate. Keep sample order, time, unit, channel, and edge orientation alongside the numbers.

## C07.01-W1 — Worked reconstruction

Use f=(2,5,4,9) SU at IDs (0,1,2,3), with times (0,1,2,3) s. Forward differences are 5−2=3, 4−5=−1, and 9−4=5 SU. Store anchor f_0=2 SU. Decode successively: 2; 2+3=5; 5−1=4; 4+5=9. Each recovered entry matches its original ID. On the first edge a second channel g changes from 4 to 6 SU, so dg=2 SU. Channels are kept distinct even if their units agree.

## C07.01-W2 — Six source-premise cards

S02#/constitutive_principles/0 through /5 assigns every following card the exact logical_role `premise_not_derived_theorem`. The names and IDs are source names; the explanations below are teaching paraphrases. A constitutive premise specifies how a framework treats a state. Later algebraic equalities follow from stated definitions; a calculation with a geometric basis B does not derive these physical commitments.

| ID and source name | Finite classroom meaning | Where it is used |
|---|---|---|
| EG-A1 complete-state principle | Keep all fields that can change a later result: values, addresses, branches, orientation, scale, residuals and history. Our ledger keeps IDs, times, units and anchors. | This worked sequence |
| EG-A2 decoder principle | A lossless transform has a decoder D with D(T(S))=S: transform a state S with T, then recover it with D. | Lesson 03 pair decoder |
| EG-A3 finite-transition principle | Use endpoint minus start as the primary transition on an edge. | This lesson's df |
| EG-A4 finite-product principle | Retain the interaction df·dg when both factors change. | Lesson 02 |
| EG-A5 residual-information principle | Preserve unresolved components as the next channel for analysis. | Lesson 05 |
| EG-A6 typed-renderer principle | A reduced or displayed view retains its units, scale, projection rule and source state. | Lesson 07 ledger |

Worked reading: a difference list without an anchor is not a complete encoding of f. EG-A1 tells us to retain the later-relevant anchor; EG-A3 declares the chosen transition. The arithmetic above demonstrates recovery for this encoding. It does not establish the source's entire physical ontology. Terms such as lift, gauge transport, infinite resolution and phase are recognition-only here, not additional calculations.

> Claim scope: S02#/backbone_sequence/3 reports mathematical module M04 and its finite difference. The six cards are source-stated premises. Our table is synthetic; its decoder is a freshly checked algebraic consequence. No physical mechanism is inferred from it.

## C07.01-P1 — Practice, then check

For h=(3,7,6,10) SU at the same IDs and times, find forward differences, retain the anchor and reconstruct all samples. Also reverse edge 0→1. Work before reading the answer.

Answer: differences=(4,−1,4) SU and anchor=3 SU. Reconstruction is 3, 3+4=7, 7−1=6, 6+4=10. The reverse edge change is 3−7=−4 SU, a change rather than a sample value. This uses EG-A1 and EG-A3.

## Diagnostics

1. **C07.01-D1:** A signal changes from 5 to 9 SU between 1 and 3 s. Give its difference and rate. Would its difference determine its starting value?
2. **C07.01-D2:** Decode anchor −2 SU with changes (3,0,−1) SU. What does the zero change mean?
3. **C07.01-D3:** Which premise names the decoder requirement? Does a verified basis determinant prove that premise?

Worked answers: D1: df=9−5=4 SU; elapsed time=2 s, so rate=2 SU/s. The difference alone allows starts such as 5 or 15 with corresponding endpoints 9 or 19. D2: (−2,1,1,0) SU; the middle two samples agree but both sample records remain. D3: EG-A2; no, it is source-stated as a premise, not a determinant theorem.

Next dependency: [Lesson 02](lesson-02.md) uses two changes on the same edge to derive the finite product rule.
'''
lessons[2]='''
# Lesson 02 — The finite product rule

Essential question: How does a product change when both factors change by a finite amount?

Goals: derive the full product difference by expansion; calculate its three signed terms; check an equivalent endpoint formula and product units.

Prerequisite bridge: Lesson 01 taught f_t=f_s+df. Recall distributivity: (a+b)c=ac+bc. To multiply two sums, distribute each term of the first across the second. For example (2+3)(4+2)=8+4+12+6. Products here multiply scalar entries at the same edge endpoint; they are not matrix multiplication.

## C07.02-E1 — Derive before shortening

Use starting values f_s,g_s and ending values f_t,g_t on one common edge. Substitute f_t=f_s+df and g_t=g_s+dg:

    d(fg) = f_t g_t − f_s g_s
          = (f_s+df)(g_s+dg) − f_s g_s
          = f_s g_s + f_s dg + g_s df + df dg − f_s g_s
          = f_s dg + g_s df + df dg.

The first term changes g while holding f at its starting value; the second changes f while holding g at its starting value. The third is the joint finite interaction. It can be positive, negative or zero. Nothing in this exact expansion permits us to erase it because a term is inconvenient or small. If either change is zero, the joint term is exactly zero for that edge.

An equivalent grouping is d(fg)=f_s dg+df g_t. This uses the ending g_t, so df g_t already contains g_s df+df dg. Confusing g_t with g_s loses the interaction. If f has unit U and g has unit V, every term has unit UV. In our examples both signals use SU, so products and product changes use SU². A product change is not a time rate.

## C07.02-W1 — Worked two-channel edge

Let f:2→5 SU and g:4→6 SU. Then df=3 SU and dg=2 SU. The direct product change is 5·6−2·4=30−8=22 SU². Separately, f_s dg=2·2=4, g_s df=4·3=12, df dg=3·2=6, all in SU². Their sum is 22. Omitting the interaction gives 16 and fails the endpoint check. The endpoint grouping gives 2·2+3·6=4+18=22 SU².

> Claim scope: S02#/constitutive_principles/3 names EG-A4 as a constitutive premise about retaining finite interaction. S02#/backbone_sequence/3 gives this scalar expansion. Under our definitions, the equality follows from distributivity; the physical commitment is not derived from B alone. The numbers are synthetic.

## C07.02-P1 — Practice with opposing changes

Let f:3→1 SU and g:2→5 SU. Compute the direct product difference, the three-term rule and the endpoint grouping. Label the interaction's sign and connect it to EG-A4.

Answer: df=−2, dg=3 SU. Directly, 1·5−3·2=−1 SU². The terms are 3·3=9, 2·(−2)=−4 and (−2)·3=−6 SU²; total −1. Endpoint form is 3·3+(−2)·5=9−10=−1. The negative interaction is retained under EG-A4; the expansion is exact algebra.

## Diagnostics

1. **C07.02-D1:** For f:1→1 SU and g:2→4 SU, find all three terms. Why is the interaction zero, and what is EG-A4's logical role?
2. **C07.02-D2:** For f:−1→2 SU and g:3→2 SU, check both sides of the rule.
3. **C07.02-D3:** A student writes f_s dg+df g_s and calls it the endpoint formula. Locate and repair the error. State its units.

Worked answers: D1: df=0,dg=2; terms (2,0,0) SU², product change 2. The zero factor df makes the interaction zero. EG-A4 remains a source constitutive premise. D2: df=3,dg=−1; terms 1,9,−3 sum 7 SU², matching 2·2−(−1)·3=7. D3: replace the final g_s by g_t, or add df dg to the written expression; all product terms have SU².

Next dependency: [Lesson 03](lesson-03.md) separates a signal into two retained parts; Lesson 04 will expand their product in the same way.
'''
lessons[3]='''
# Lesson 03 — Coarse and detail coordinates

Essential question: Can averaging be part of a reversible transformation?

Goals: compute a mean and signed half-difference for each fixed pair; reconstruct the original entries; distinguish a compact encoding from an expanded coarse/detail view.

Prerequisite bridge: Lesson 01 recovered a state by adding a retained change. Lesson 02 showed that separating a quantity into parts requires keeping every term. Now use fractions to create two new coordinates for two old ones. Check (2+5)/2=7/2 and (5−2)/2=3/2 before continuing.

## C07.03-E1 — Two coordinates for two entries

For an ordered pair (a,b), define its mean m=(a+b)/2 and signed half-difference d=(b−a)/2. Here d is a pair coordinate; df in Lessons 01–02 is a full edge difference. The decoder is (a,b)=(m−d,m+d), because

    m−d = (a+b−b+a)/2 = a,
    m+d = (a+b+b−a)/2 = b.

Thus retaining both numbers, their order, and the pair membership preserves the original values. A mean alone is many-to-one: (2,4) and (1,5) both have mean 3. Their details are 1 and 2. If (a,b) is reversed, m stays the same and d changes sign. The sign preserves which sample was larger.

For four entries keep fixed blocks {0,1} and {2,3}. Define an operator E, meaning a rule applied to a whole list, which replaces each pair by its repeated mean. Define I to mean the identity rule I(f)=f. Define Q=I−E, so Qf=f−Ef is the detail list. Subtraction is entry by entry. Q here is a detail operator, not any geometric distance or the later integer Q_g. A block's expanded detail is (−d,d). Then f=Ef+Qf at every original sample ID.

The compact encoding stores two means and two half-differences. The expanded view repeats each mean and lists both signed detail entries. They describe the same information, provided the block map is preserved. We retain small expanded examples to make residual accounting visible; real source data need not be duplicated merely to create another view. Exact decoding rules can document the relationship.

## C07.03-W1 — Worked pair transform

Take f=(2,5,4,9) SU. For block {0,1}, m_1=7/2 and d_1=3/2 SU. For {2,3}, m_2=13/2 and d_2=5/2 SU. Thus Ef=(7/2,7/2,13/2,13/2) and Qf=(−3/2,3/2,−5/2,5/2) SU. Decode: 7/2−3/2=2, 7/2+3/2=5, 13/2−5/2=4, 13/2+5/2=9. A zero sum of details within a block does not mean its individual details vanish.

> Claim scope: This is a fully specified synthetic transform. EG-A2 at S02#/constitutive_principles/1 states the decoder premise; our two displayed equalities prove this particular decoder. General operators E in archival formulas need additional properties, taught next. No physical averaging law is inferred.

## C07.03-P1 — Practice

Transform h=(3,7,6,10) SU with the same blocks. Keep compact coordinates and expanded views. Recover the entries, citing EG-A2.

Answer: m=(5,8), d=(2,2) SU; Eh=(5,5,8,8), Qh=(−2,2,−2,2) SU. Decode (5−2,5+2,8−2,8+2)=(3,7,6,10). EG-A2 asks for a decoder; this one is exhibited and checked.

## Diagnostics

1. **C07.03-D1:** Explain why mean 3 cannot distinguish (2,4) from (1,5), and compute both missing coordinates. What changes if the first pair is reversed?
2. **C07.03-D2:** Transform (7,3) SU and decode it. Is a negative d allowed?
3. **C07.03-D3:** A record keeps means (5,8), unsigned detail magnitudes (2,2), and no ordering. Can it determine h uniquely? Give a competing list.

Worked answers: D1: both sums equal 6; d is 1 versus 2. Reversal to (4,2) gives d=−1. D2: m=5,d=−2 SU; (5−(−2),5+(−2))=(7,3); signed details are required. D3: no; (7,3,10,6) has those same means and magnitudes. Keep signs, IDs and block support.

Next dependency: [Lesson 04](lesson-04.md) tests the exact properties of E needed to distribute products across coarse and detail parts.
'''
lessons[4]='''
# Lesson 04 — What a projection must satisfy

Essential question: Which properties justify the detail-product identity?

Goals: verify linearity and idempotence for fixed block averaging; prove the block-factor property; derive and numerically verify the detail-product identity; diagnose a projection that fails it.

Prerequisite bridge: Lesson 03 defined Ef and Qf=f−Ef. Lesson 02 taught expansion of products of sums. We now multiply lists pointwise: (fg)_i=f_i g_i at each original ID i. For this lesson lists are dimensionless real numbers, so every factor and product is dimensionless. Two 55-minute periods are required: first the operator properties and their practice, then the product derivation and counterexample.

## C07.04-E1 — Rules for the coarse view (period 1)

A linear rule respects weighted sums: E(af+bg)=aE(f)+bE(g) for any real numbers a,b. This means averaging a weighted mixture gives the same result as mixing its averages. On a pair, its left side is [a f_0+b g_0+a f_1+b g_1]/2; grouping terms gives a(f_0+f_1)/2+b(g_0+g_1)/2, proving linearity.

Idempotence means E(Ef)=Ef: doing the operation twice has no additional effect. Pair averaging is idempotent because the mean of (m,m) is m. A linear idempotent operator is called a projection here. Its range is the collection of all its possible outputs. Our range B_coarse consists of lists constant within each fixed block, such as (a,a,b,b). It includes the all-ones list 1=(1,1,1,1), and E(1)=1. Adding, scaling or pointwise multiplying block-constant lists gives another block-constant list. Mathematicians call such a collection a subalgebra: for this course that word means exactly this closure under these operations, including 1. B_coarse is not the geometric basis B.

We need a further property. If b_1 and b_2 are block-constant lists, then

    E(b_1 f b_2) = b_1 E(f) b_2.

The subscript on b names a list, not an entry. This is the two-sided block-factor, or bimodule, property. On a block where those lists have constant values c and d, the average of (c f_0 d,c f_1 d) is cd(f_0+f_1)/2. The constants factor outside the average. The same argument holds separately on every block, which proves the property. Fixed-block averaging is a concrete finite conditional expectation: a coarse view with this compatible factor rule. No probability theory is needed here.

For any qf=f−Ef, linearity and idempotence give E(qf)=Ef−E(Ef)=0, the all-zero list. Multiplying a zero-average detail by a block-constant factor still has zero average by the factor rule. That last fact will remove cross terms from the coarse product, while retaining them in the detail product.

Period-1 practice: with f=(0,2,2,4), verify E(Ef)=Ef and the block-factor rule for b=(2,2,−1,−1). Answer: Ef=(1,1,3,3), whose repeated averaging is unchanged. bf=(0,4,−2,−4), so E(bf)=(2,2,−3,−3)=bEf. The equality depends on b being constant inside each block.

## C07.04-E2 — Derive the identity (period 2)

Our sufficient hypotheses are explicit: E is linear and idempotent, fixes 1, has multiplication-closed range B_coarse, and satisfies the two-sided block-factor property for that range. Pair averaging meets each, as just proved. Positivity (averaging nonnegative entries gives nonnegative entries) also holds, but is not needed in the following algebra.

Set qf=Qf=f−Ef and qg=Qg=g−Eg. Expand exactly:

    fg = Ef Eg + Ef qg + qf Eg + qf qg.

Apply E to each term, using linearity. Because Ef Eg is in its range, E(Ef Eg)=Ef Eg. The factor property gives E(Ef qg)=Ef E(qg)=0 and E(qf Eg)=E(qf)Eg=0. Therefore

    E(fg) = Ef Eg + E(qf qg).

Subtract this from the original product expansion. Since Q(fg)=fg−E(fg),

    Q(fg) = Ef qg + qf Eg + qf qg − E(qf qg).

The full detail product qf qg is retained. Its own coarse part is subtracted only in the Q view; that part remains in E(fg), so E(fg)+Q(fg)=fg. This separates information rather than erasing it.

## C07.04-W1 — Worked numerical verification

Take f=(2,4,1,5), g=(1,3,2,4). Then Ef=(3,3,3,3), Eg=(2,2,3,3), qf=(−1,1,−2,2), qg=(−1,1,−1,1). Directly fg=(2,12,2,20), E(fg)=(7,7,11,11), so Q(fg)=(−5,5,−9,9).

Independently compute the right side: Ef qg=(−3,3,−3,3), qf Eg=(−2,2,−6,6), qf qg=(1,1,2,2), and E(qf qg)=(1,1,2,2). Add the first three and subtract the fourth to get (−5,5,−9,9). Here the detail product is block-constant, so its Q view is zero, but its coarse value remains. Indeed Ef Eg=(6,6,9,9); adding (1,1,2,2) recovers E(fg).

> Claim scope: S02#/backbone_sequence/3 states the identity; S03#/findings/5 (AUD-006) flags that Q=I−E alone is insufficient. We have proved a sufficient finite block model, not certified an unspecified general archival E or retrieved its full proof body. EG-A4 and EG-A5 remain source premises; the displayed equalities are derived under our explicit hypotheses.

## C07.04-P1 — Practice

Use f=(0,2,2,4), g=(1,1,0,2). Compute every right-side term and compare with direct Q(fg). Explain why the earlier b-factor calculation is relevant. Before the answer, reproduce the three zero-average steps in the proof.

Answer: Ef=(1,1,3,3), Eg=(1,1,1,1), qf=(−1,1,−1,1), qg=(0,0,−1,1). The terms Ef qg=(0,0,−3,3), qf Eg=(−1,1,−1,1), qf qg=(0,0,1,1), E(qf qg)=(0,0,1,1) yield (−1,1,−4,4). Directly fg=(0,2,0,8), whose means are (1,4), giving that same Q view. The b-factor calculation illustrates the rule that makes E(Ef qg) and E(qf Eg) vanish. E(qf)=Ef−E²f=0 and likewise for qg; then the factor rule pulls Ef or Eg outside E.

## Diagnostics

1. **C07.04-D1:** Define E_star(x,y,z)=(x,x,z+y−x), Q_star=I−E_star. Show it is linear, fixes (1,1,1), is idempotent and has multiplication-closed range (a,a,b). Test its block-factor rule with b=(1,1,0), f=(0,1,0). Then test the proposed detail identity with f=g=(0,1,0).
2. **C07.04-D2:** For pair averaging and u=(2,6), compute E(3u), 3Eu and E(Eu). Which properties do these illustrate? Supply the general pair argument rather than treating one example as a proof.
3. **C07.04-D3:** A student deletes qf qg because its Q view is zero in W1. What coarse product value would be lost? Where is it retained?

Worked answers: D1: every output component is a linear combination of inputs, hence linearity. E_star(1,1,1)=(1,1,1). Applying it twice gives (x,x,(z+y−x)+x−x)=(x,x,z+y−x). Its outputs have form (a,a,b), every such list is fixed, and (a,a,b)(c,c,d)=(ac,ac,bd) has the same form. However E_star(bf)=E_star(0,1,0)=(0,0,1), whereas bE_star(f)=(0,0,0). With f=g, Ef=Eg=(0,0,1), qf=qg=(0,1,−1). The RHS terms are (0,0,−1), (0,0,−1), (0,1,1), and minus E_star(0,1,1)=−(0,0,2). Their sum is (0,1,−3). Direct Q_star(fg)=(0,1,−1). The missing block-factor property is decisive even though the other listed properties hold.

D2: Eu=(4,4); E(3u)=(12,12)=3Eu, and E(Eu)=(4,4). Scaling passes through (u_0+u_1)/2 by distributivity; averaging (m,m) returns m. D3: (1,1,2,2) would be lost; it belongs to E(fg)=Ef Eg+E(qf qg), not to a discard bin.

Next dependency: [Lesson 05](lesson-05.md) applies the coarse/detail split to the residual left by a declared model.
'''
lessons[5]='''
# Lesson 05 — Residuals as new coordinates

Essential question: How can a model leave useful structure while preserving exact recovery?

Goals: compute a full signed residual; model that residual with fixed block means; reconstruct the original state from all retained layers.

Prerequisite bridge: Lesson 03 supplied a reversible pair split and Lesson 04 specified its operator. Subtraction and addition of lists mean matching entries by ID. Check (3,7)−(2,2)=(1,5) before using a second model. This lesson uses SU for every value, model and residual.

## C07.05-E1 — A model is a declared component

A model M_0 is a list proposed to account for part of a state x. The subscript labels a modeling stage; it is not a sample ID. Define r_0=x−M_0. This signed residual is the exact component the model leaves. Then x=M_0+r_0 follows by adding M_0 back. Calling M_0 a model does not establish its physical cause or make it a uniquely chosen fit.

Now use the residual as the input to another declared rule. Choose M_1=E(r_0), using fixed blocks {0,1},{2,3}. Define r_1=r_0−M_1. Substitute r_0=M_1+r_1 into the first equation:

    x = M_0 + M_1 + r_1.

Keep r_0 and r_1 as separately identified layers, even though the equations link them. They answer different questions: what the first model left, and what remains after the next coarse model. A scalar sum or average cannot replace either list. Cancellation in a sum is a relation among entries, not proof of their absence. A zero entry is also a retained coordinate at its original ID.

## C07.05-W1 — Worked residual recursion

Let x=(2,5,4,9) SU and choose M_0=(1,1,1,1) SU. Subtract at each ID to obtain r_0=(1,4,3,8). Pair means of r_0 are 5/2 and 11/2, so M_1=(5/2,5/2,11/2,11/2). Subtract again to get r_1=(−3/2,3/2,−5/2,5/2) SU.

| Sample ID | M_0 | M_1 | r_1 | Reconstructed x |
|---|---:|---:|---:|---:|
| 0 | 1 | 5/2 | −3/2 | 1+5/2−3/2=2 |
| 1 | 1 | 5/2 | 3/2 | 1+5/2+3/2=5 |
| 2 | 1 | 11/2 | −5/2 | 1+11/2−5/2=4 |
| 3 | 1 | 11/2 | 5/2 | 1+11/2+5/2=9 |

Every table value is in SU. The reconstruction error, defined as reconstructed minus original, is (0,0,0,0) SU. This zero error checks the decoder; it does not say that M_0 alone explained every sample.

> Claim scope: EG-A5 at S02#/constitutive_principles/4 treats unresolved components as the next-channel state. Our models are explicitly chosen synthetic components; no measured dataset, causal mechanism or optimal-fit claim is supplied. Recurrent residual structure is retained as a target for further explanation.

## C07.05-P1 — Practice

Use x=(3,7,6,10), fixed M_0=(2,2,2,2) SU and the same pair blocks. Write both residual layers and verify every reconstruction entry.

Answer: r_0=(1,5,4,8), M_1=(3,3,6,6), r_1=(−2,2,−2,2) SU. Reconstruction is (2+3−2,2+3+2,2+6−2,2+6+2)=(3,7,6,10). Retain r_0 and r_1 under different stage labels. EG-A5 supports treating r_0 as input, not erasing it after M_1 is chosen.

## Diagnostics

1. **C07.05-D1:** The sum of r_1 in P1 is zero. Can the four entries be replaced by zero? What if one entry of another residual is exactly zero?
2. **C07.05-D2:** For x=(4,4) and M_0=(1,2) SU, compute r_0, M_1=E(r_0), r_1 and reconstruct x.
3. **C07.05-D3:** If a later model M_2 of r_1 is introduced, define its remaining residual r_2 and give the reconstruction formula. Which earlier residual layers remain in the record?

Worked answers: D1: no, the entries (−2,2,−2,2) are all nonzero. A zero at a particular ID remains a valid entry, not a reason to delete its sample. D2: r_0=(3,2), M_1=(5/2,5/2), r_1=(1/2,−1/2); 1+5/2+1/2=4 and 2+5/2−1/2=4 SU. D3: r_2=r_1−M_2, so x=M_0+M_1+M_2+r_2; retain r_0,r_1,r_2 with their model rules and IDs.

Next dependency: [Lesson 06](lesson-06.md) handles a different kind of missing coordinate: an equation whose output cannot identify its input uniquely.
'''
lessons[6]='''
# Lesson 06 — Singular equations and retained freedom

Essential question: What information must accompany an equation that has many solutions or no exact solution?

Goals: solve a two-equation system by substitution; retain its free coordinate; compute an output compatibility coordinate and declared residual view; distinguish singular and invertible maps.

Prerequisite bridge: You can solve u+v=6 for u=6−v. Lesson 05 retained components a model did not determine. Here missing information can occur on the input side as well as the output side. All quantities in this lesson are dimensionless synthetic numbers.

## C07.06-E1 — Read a matrix as two recipes

Write an input pair as psi=(u,v). The matrix K=[[1,1],[2,2]] is shorthand for the output rule K psi=(u+v,2u+2v). Each row tells you to multiply the input coordinates by its entries and add. To solve K psi=j for an output pair j=(j_1,j_2), ask for an input producing both output numbers.

The second output is always twice the first. Consequently j_2−2j_1=0 is necessary for an exact solution. It is sufficient too: if it holds, set v=t and u=j_1−t; then both equations hold for every real t. A real number here may be positive, negative, zero or fractional. The parameter t is free because the output does not determine it.

This map is singular: different inputs can produce the same output, and some requested outputs are unreachable. Its kernel is the collection of input changes producing zero output. Changing psi by s(−1,1) leaves the sum unchanged; K(−1,1)=(0,0). Every zero-output input has that form, since u+v=0 gives u=−v. Retaining the free coordinate t distinguishes members of a solution family.

On the output side, define the compatibility coordinate c=j_2−2j_1. This is a concrete coordinate for the cokernel information: it records the obstruction left after accounting for reachable outputs. No quotient-space calculation is required. For our chosen view j_fit=(j_1,2j_1), keep output residual rho=j−j_fit=(0,c). Then j=j_fit+rho. This convention matches the first equation exactly; it is not asserted to be uniquely best. The input parameter t and output obstruction c have different roles and both must survive when relevant.

## C07.06-W1 — Worked singular solution

For j=(6,12), the equations are u+v=6 and 2u+2v=12. Divide the second by 2 to see it repeats the first. Set v=t; then psi=(6−t,t). Its output is (6−t+t,12−2t+2t)=(6,12) for all real t. The kernel direction is (−1,1), and c=12−2·6=0. If the actual illustrative input is (2,4), retaining t=4 recovers it. Choosing t=0 would select (6,0), another solution, but would not recover that illustrative state.

Contrast L=[[1,0],[0,2]], whose rule is L(u,v)=(u,2v). It sends (3,4) to (3,8), and its decoder is (j_1,j_2/2) for every real output pair. This invertible map has exactly one input per output. An inverse formula for L cannot be transferred to singular K.

> Claim scope: S02#/backbone_sequence/3/source_relation keeps K psi=j primary on singular strata and restricts inverse formulas to their invertible domain. These small matrices are synthetic analogues. Kernel, cokernel and retained parameters are explicitly distinguished; no physical field equation is being solved.

## C07.06-P1 — Practice with an incompatible request

For j=(6,13), test compatibility. Declare the first-equation-matching view, retain its residual and write the complete fitted input family. Use t=4 to give one input and check its output plus residual.

Answer: c=13−12=1, so no exact input produces j. Keep j_fit=(6,12), rho=(0,1), and psi_fit=(6−t,t) with t retained. With t=4, psi_fit=(2,4); K psi_fit=(6,12), and (6,12)+(0,1)=(6,13). The residual has not made K psi_fit=j true; it makes K psi_fit+rho=j true.

## Diagnostics

1. **C07.06-D1:** Invert L on (3,8). For singular K and output (8,16), recover the input when t=3. What is lost if t is deleted?
2. **C07.06-D2:** For K and j=(8,17), find c, j_fit, rho and the fitted input with t=3. Is it an exact solution of K psi=j?
3. **C07.06-D3:** For K and j=(0,0), list two distinct inputs and describe all of them. Does zero output imply zero input?

Worked answers: D1: L inverse gives (3,8/2)=(3,4). K gives (8−3,3)=(5,3); without t, the whole family (8−t,t) remains and the actual input is undetermined. D2: c=1, j_fit=(8,16), rho=(0,1), psi_fit=(5,3). Its output is (8,16), so it is not an exact solution for (8,17); retain the nonzero residual. D3: (0,0) and (−1,1) both work; all inputs are (−t,t). Zero output alone does not force zero input.

Next dependency: [Lesson 07](lesson-07.md) records anchors, details, model layers, free coordinates and compatibility data in a complete transformation ledger.
'''
lessons[7]='''
# Lesson 07 — A complete transformation ledger

Essential question: Can someone else undo every stage of an analysis using only its records?

Goals: compose three taught transforms; reverse them in the opposite order; document every retained and removed component; link all six constitutive premises to concrete ledger operations.

Prerequisite bridge: Lesson 01 needs an anchor to invert differences; Lesson 03 needs signed detail to invert means; Lesson 05 needs model and residual layers; Lesson 06 needs free input coordinates and output compatibility information for a singular map. No new transform is required. Check that means (3,6) can be encoded by first mean 3 and difference 3, then recovered as (3,3+3).

## C07.07-E1 — Record enough to reverse the chain

A transformation ledger describes the input, output, rule, retained side information and decoder at each stage. A typed view says what its numbers mean: unit, sample or block IDs, ordering, and operation. A shorter display is allowed if its source and omitted components remain recoverable. The last operation must be undone first, because the earlier decoder expects the output of its own stage.

Our three stages are: subtract a fixed model; replace each residual pair by its mean and signed half-difference; replace the mean list by its anchor and difference. Each stage changes representation, not the available information. In a real archive, retain a source reference and a replayable recipe rather than copying raw data into every report. In these tiny synthetic exercises, showing the layers explicitly makes the decoder checkable.

## C07.07-W1 — Worked three-stage ledger

Source record: synthetic channel f, original IDs (0,1,2,3), times (0,1,2,3) s, values x=(2,5,4,9) SU. Blocks are {0,1} and {2,3}, in that order. The model rule is the constant 1 SU at every original ID.

| Stage | Input → output | Retained side information | Decoder |
|---|---|---|---|
| 1: subtract model | x → r_0=(1,4,3,8) SU | M_0=(1,1,1,1) SU; original record and rule | x=M_0+r_0 |
| 2: pair split | r_0 → m=(5/2,11/2), d=(3/2,5/2) SU | Signed d; block support; M_1=(5/2,5/2,11/2,11/2); r_1=(−3/2,3/2,−5/2,5/2) | r_0=(m_1−d_1,m_1+d_1,m_2−d_2,m_2+d_2) |
| 3: mean differences | m → anchor A=5/2, difference δ=3 SU | Anchor, mean order and units | m=(A,A+δ) |

At stage 2, compact m has block indices 1,2, whereas x has sample IDs 0,1,2,3. The support map connects them. At stage 3 δ=11/2−5/2=3. Decode in reverse: m=(5/2,5/2+3)=(5/2,11/2); r_0=(1,4,3,8); add M_0 to recover x=(2,5,4,9). Reconstructed minus original is (0,0,0,0) SU at IDs 0–3. Both r_0 and r_1 remain named layers. There are no unrecorded removed components.

## C07.07-E2 — Premises and ledger fields

EG-A1 governs the complete record, including sample addresses, signs and anchors. EG-A2 asks for the reverse decoder and entrywise equality check. EG-A3 names the endpoint-minus-start operation used on the mean list. EG-A4 governs the product-change side calculation from Lesson 02, in which the signed interaction is retained; the three-stage ledger itself does not multiply signals. EG-A5 names the residual recursion, preserving r_0 and r_1. EG-A6 governs how the compact displayed coordinates remain typed views of the source. A ledger may record an operation as not used in its main chain while retaining the linked side calculation; it must not claim that every premise was numerically exercised by every stage.

> Claim scope: All six EG IDs retain S02's logical_role `premise_not_derived_theorem`. Our decoder equalities are proved for the declared finite definitions. Neither EG-A6 nor the other constitutive commitments follow from a determinant of the geometric basis B. B and its physical geometry are not inputs to this synthetic decoder. The general archival E gap remains scoped in Lesson 04.

## C07.07-P1 — Practice, full reverse replay

Use x=(3,7,6,10) SU with IDs/times as in W1, fixed M_0=(2,2,2,2) SU and the same blocks. Build the three-stage ledger, show both residual layers and reverse every stage. State every reconstruction error entry.

Answer: stage 1 gives r_0=(1,5,4,8). Stage 2 gives means (3,6), signed details (2,2), M_1=(3,3,6,6) and r_1=(−2,2,−2,2). Stage 3 gives A=3, δ=3 SU. Decode m=(3,3+3)=(3,6); r_0=(3−2,3+2,6−2,6+2)=(1,5,4,8); x=M_0+r_0=(3,7,6,10). Error=(0,0,0,0) SU. All fields retain their stage and support labels.

## C07.07-P2 — Practice matching the six cards

Match each EG-A1–EG-A6 ID to a record or side calculation in P1, using the product example in Lesson 02 P1. Correct the sentence “EG-A6 follows from the determinant of B.”

Answer: EG-A1→source order, units and anchors; EG-A2→reverse replay; EG-A3→δ=6−3; EG-A4→Lesson 02's retained interaction (−2)·3=−6 SU²; EG-A5→r_0 and r_1 as distinct layers; EG-A6→typed compact view plus decoder and source record. All six are source-stated constitutive premises. The corrected sentence is: “EG-A6 is a constitutive premise; our specified decoder is an algebraic construction, not a derivation of that premise from B.”

## Diagnostics

1. **C07.07-D1:** Name the minimum ledger fields. Explain what fails if the mean anchor, detail sign or singular free parameter is omitted.
2. **C07.07-D2:** Match all six EG IDs to P1 and its product side calculation. Does any follow from a basis determinant?
3. **C07.07-D3:** Decode A=4, δ=−1, d=(1,−2) SU, model M_0=(2,2,2,2) SU and the standard blocks. Retain r_0 and r_1.

Worked answers: D1: original IDs/order/times/channel/units, source scope, model rule, block support, signed details, anchors, outputs, omitted components and inverse operations; singular views also keep t and c or rho. Missing A leaves an arbitrary common level; missing signs leaves ambiguity within pairs; missing t leaves a family of inputs. D2: use the six explicit mappings in P2; none is derived from B alone. D3: means=(4,3), r_0=(4−1,4+1,3−(−2),3+(−2))=(3,5,5,1); M_1=(4,4,3,3); r_1=(−1,1,2,−2); x=(5,7,7,3) SU.

Next dependency: [Capstone](capstone.md) combines the taught transforms, product checks, operator hypotheses and singular branches into one audited submission.
'''
for i,body in lessons.items(): write(f'lesson-{i:02}.md',body)

sources=[]
for s in packet['sources']:
    actual=digest(Path(s['path']))
    assert actual==s['sha256'],s['id']
    sources.append(dict(s,actual_sha256=actual,hash_verified=True))
js('sources.json',{'sources':sources,'corpus_generation':'sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','manifest_sha256':'5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','retrieval_note':'Capabilities called; sparse RAG query returned compiler namespace material, not a general M04 E proof. Generation confirmed by RAG response. Exact listed local files read without copying; core pointers read directly.','core_pointers':['S01#/backbone_sequence/3','S02#/backbone_sequence/3','S02#/constitutive_principles/0','S02#/constitutive_principles/1','S02#/constitutive_principles/2','S02#/constitutive_principles/3','S02#/constitutive_principles/4','S02#/constitutive_principles/5','S03#/findings/5','S03#/findings/11'],'source_gap':'A fully specified general archival E proof body is not available in the compressed M04 passage. The course supplies and proves sufficient finite block hypotheses without claiming general proof certification.'})
write('sources.md','''
# Source notes and evidence scope

Exact absolute paths and freshly verified SHA-256 values for S01–S05 are in sources.json. No raw source snapshots were saved. All five supplied hashes matched. Source pointers below are JSON pointers, not page numbers. The synthetic examples were supplied as curriculum anchors or authored for practice; they are not archive measurements.

| Source location | What is used | Evidence class and limit |
|---|---|---|
| S01#/backbone_sequence/3 | Earlier M04 finite rule, Q formula and singular source relation | Archival statement; kept separate from mature S02 |
| S02#/backbone_sequence/3 | Finite differences, finite-product expansion, detail formula and singular branch | Source-reported mathematics; finite scalar algebra freshly checked here |
| S02#/constitutive_principles/0–5 | EG-A1–EG-A6 with exact logical_role premise_not_derived_theorem | Constitutive premises, not conclusions from B |
| S03#/findings/5, AUD-006 | Missing hypotheses behind Q identity | Source audit correction; fulfilled here by a fully defined finite model |
| S03#/findings/11, AUD-012 | EG-A6 omitted from an integrity list | Source audit correction; all six IDs retained in cards and ledger |
| S04 and S05 | Supplied broader corpus context; hashes checked and top-level structure inspected | Not premises of a new numerical or physical claim in this course |

The capabilities endpoint returned interface metadata, not corpus generation. The subsequent read-only sparse RAG search returned the requested generation and manifest digest, both 5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7. Its hits concerned the compiler namespace. Those labels were not substituted for mathematical-backbone M04. Direct local pointers provide the exact grounding used above.

The compressed M04 source has a requires edge to M03. The core here uses the explicitly supplied finite arithmetic bridges, not an unproved import of a physical M03 theorem. Gauge covariance, the infinite-resolution identity and physical mass interpretation in broader material are recognition-only, not assessed prerequisites. The general definition/proof body for archival E remains a retrieval gap; our conditional block theorem is fully stated and proved. A source status such as VERIFIED_FROZEN is reported status, not fresh certification of every archival claim.

The subject's geometry, metric, parity, gauge-order and physical-motion invariants remain in input-contract.json. They are not numerical inputs to this finite-data course. In particular Q here means I−E; it is not a Cell3 distance, Q_g or Q_nu. No geometric constants, compiler authority labels or empirical energy claims are silently imported. There are no empirical observations in these synthetic exercises. Derived equalities, source premises and proposed model choices are explicitly distinguished; no new physical mechanism is asserted.
''')

write('terminology.md','''
# Terminology and notation

| Term/symbol | Meaning and first use |
|---|---|
| Sample ID; time | Original address versus recorded time; lesson 01. They are preserved separately. |
| SU | Synthetic signal-unit, a declared teaching unit; lesson 01. SU² denotes the product of two such units. |
| f_s, f_t; s→t | Start and end values on an oriented edge; lesson 01. |
| df | Full finite difference f_t−f_s, with the same units as f; lesson 01. |
| Rate | Finite difference divided by nonzero elapsed time; lesson 01. |
| Anchor | Retained starting value needed to decode differences; lesson 01. |
| Premise | A stated starting commitment, distinguished from a derived conclusion; lesson 01. |
| T, D, S | Transform, decoder, state in D(T(S))=S; lesson 01 premise card. |
| df dg | Signed joint finite interaction; product units; lesson 02. |
| m, d | Pair mean and signed half-difference, same units as the pair; lesson 03. Pair d is half the corresponding full edge difference. |
| E, I, Q | Fixed pair averaging, identity, and detail I−E; lesson 03. Q is not a geometric quadratic form. |
| Block support | Original sample IDs belonging to each pair; lesson 03. |
| Linear | Preserves addition and multiplication by scalar weights; lesson 04. |
| Idempotent; projection | E²=E; a linear rule with that property is a projection here; lesson 04. E² means composition E(Ef), not squaring entries. |
| Range B_coarse | Outputs of E, the block-constant arrays; lesson 04. Distinct from geometric basis B. |
| Pointwise product | Multiply entries at the same sample ID; lessons 02 and 04. |
| Subalgebra | Here, lists closed under sums, scalar multiples, pointwise products and containing 1; lesson 04. |
| Bimodule/block-factor rule | E(b_1 f b_2)=b_1 E(f)b_2 for block-constant factors; lesson 04. |
| Conditional expectation | Here, fixed finite block averaging with the stated factor property; lesson 04. No probability theory assumed. |
| qf, qg | Short names for Qf,Qg; lesson 04. |
| E_star, Q_star | Three-entry counterexample rule and I−E_star; lesson 04 only. |
| M_0,M_1; r_0,r_1 | Stage-labeled models and residual fields, not sample subscripts; lesson 05. |
| Reconstruction error | Reconstructed minus original at every ID; lesson 05. |
| K, L; psi=(u,v); j | Explicit matrix rules, input pair and output pair; lesson 06. Matrices are taught as row recipes. |
| Singular; invertible | Respectively the lesson's nonunique/unreachable-output map K; and uniquely reversible map L; lesson 06. |
| Kernel | Input changes mapped to zero; lesson 06. |
| t | Free input coordinate in lesson 06; distinct from the endpoint label t of lesson 01. |
| c; cokernel information | Compatibility coordinate j_2−2j_1 for K, recording an output obstruction; lesson 06. |
| j_fit; rho | Declared first-equation-matching output and residual (0,c); lesson 06. |
| Ledger; typed view | Replayable operation record; display with units/support/rules/source retained; lesson 07. |
| A, δ | Mean anchor and full difference of the two means; lesson 07. |

The source's geometry symbols M_cell, R_cell, G_phase, O_K and B are reserved by input-contract.json and are not used as computational variables here. Mathematical M04 and compiler M04 are not interchangeable labels. EG-A1–EG-A6 keep the exact source logical role given in lesson 01.
''')

write('teacher-guide.md','''
# Teacher guide — Information-Complete Finite Calculus

Audience: high-school seniors comfortable with signed arithmetic, fractions, ratios, simple equations and coordinate tables. Course 06 is listed as a series prerequisite, but all finite operations needed here are bridged explicitly. Begin with −3+5, 4−9, (2+5)/2, and solving u+v=6 for u. Expected answers are 2, −5, 7/2, u=6−v. If a learner cannot explain these, use paired counters for signed addition and two-share diagrams for halves before progressing. This repair is additional time, not skipped content.

The course has seven lessons over eight 55-minute core periods plus two 55-minute capstone periods. Lesson 04 deliberately spans two periods; no core requirement was removed. For each core period allocate 5 minutes retrieval, 20 explanation/worked example, 15 independently attempted practice followed by comparison, and 15 diagnostics/repair. Thus teaching totals 160 minutes, practice 120, diagnostics/repair 120 and retrieval 40. Students should cover worked answers while attempting practice.

| Period | Teaching and practice focus | Gate before proceeding |
|---|---|---|
| 1 | Lesson 01 differences, anchor, source cards | Decode four values and distinguish difference/rate |
| 2 | Lesson 02 product expansion, signed interaction | Obtain −1 by both calculations in P1 |
| 3 | Lesson 03 means/details and block support | Decode a negative signed detail correctly |
| 4 | Lesson 04 E1 properties and factor practice | Explain why fixed factors leave a block average |
| 5 | Lesson 04 E2 product proof, W1/P1 and E_star | Show precisely which hypothesis fails, not just a mismatch |
| 6 | Lesson 05 residual recursion | Reconstruct each ID and retain both residual layers |
| 7 | Lesson 06 singular/compatible/incompatible cases | Distinguish t from c and retain rho |
| 8 | Lesson 07 complete ledger and premise mapping | Another learner can reverse the record unaided |

At the end of periods 3, 5 and 8, review cumulative vocabulary and ask learners to reconstruct an earlier state from a new representation. Keep the same fixed supports; changing supports without notice changes the transform. Ask why zero average is not zero detail. For lesson 04, use one pair on paper to prove the properties before four-entry calculations. The general algebra may be copied into a proof scaffold, but learners must justify each zero cross term. The counterexample's three entries do not use the two-pair block map: it is a different rule designed to test whether idempotence alone suffices.

For residuals, ask what the first model left and then what the second model left. Do not call either remainder disposable. For singular equations, compare (6,0),(2,4),(0,6) to reveal the same output; contrast this input freedom with the impossible output (6,13). A residual view does not create an exact solution to the original incompatible equation.

Use the three diagnostics per lesson (with worked answers in the lesson) as observable gates, not as a requirement to erase incorrect attempts. Preserve the attempt, mark the exact error and have the learner replay the corrected operation. A sign error gets a reversed-pair exercise; an anchor error gets two shifted lists with identical differences; a source-scope error gets the EG cards. Reassess with changed small numbers before dependent work. Extra periods are allowed if a gate fails.

Capstone period 1: 5 minutes instructions, 40 independent work on steps 1–4, 10 checking definitions. Period 2: 5 retrieval, 35 steps 5–7, 15 partner decoder replay and submission. Do not let partner checking replace each learner's initial answers. The 100-point rubric is in capstone.md. A missing retained coordinate requires repair regardless of total score, because the core outcome is exact reconstruction. Give arithmetic partial credit but require corrected final entries and provenance before mastery signoff.

Source cards are teaching paraphrases of exact identified premises, not newly discovered physical evidence. Refer to sources.md for the scoped general-E retrieval gap. Recognition-only source extensions are not surprise examination content. Markdown tables and code-form equations are the delivery format; no paginated artifact or render-dependent assertion is made.
''')

write('capstone.md','''
# Capstone — A reversible three-stage finite-data analysis

Work independently before reading the answer key. Use only operations taught in lessons 01–07. All data are synthetic. Preserve original channel h, IDs (0,1,2,3), times (0,1,2,3) s and signal h=(3,7,6,10) SU. Pair blocks are {0,1},{2,3}. In step 4 and step 6, arrays are explicitly dimensionless and separate from h.

## Tasks

1. **C07-CAP-01 (10 points):** Record the ordered source fields, calculate forward differences, retain the anchor and recover all four samples. Name the inverse operation.
2. **C07-CAP-02 (10 points):** For separate signals f:3→1 SU and g:2→5 SU on one edge, compute product change directly and by the full finite product rule. Preserve the signed joint term and product units.
3. **C07-CAP-03 (10 points):** Compute h's compact means/details and expanded E and Q views. Decode h with signs and block support.
4. **C07-CAP-04 (25 points):** State the fixed pair-average hypotheses (linearity, idempotence, unit preservation, multiplication-closed range, two-sided factor property), prove them on a generic pair and derive the detail-product identity. For dimensionless f=(0,2,2,4),g=(1,1,0,2), compute both sides. Diagnose why E_star(x,y,z)=(x,x,z+y−x) fails that identity with f=g=(0,1,0), even though it is an idempotent linear map with the stated closed range. Keep its signed mismatch.
5. **C07-CAP-05 (10 points):** Subtract fixed model (2,2,2,2) SU from h. Model its residual by pair means. Record both residual layers and reconstruct every sample.
6. **C07-CAP-06 (15 points):** For K=[[1,1],[2,2]], solve K psi=(8,16) as a family, then retain t=3 to identify an input. Separately handle (8,17): retain its compatibility coordinate and a declared first-equation-matching residual view. Contrast with the unique inverse for L=[[1,0],[0,2]].
7. **C07-CAP-07 (20 points):** Build the complete three-stage ledger: subtract the model, split residual pairs, encode their means by an anchor and difference. Reverse it and show the full reconstruction-error list. Match all EG-A1–EG-A6 premises to ledger fields or the product side calculation. Correct any assertion that these premises follow from B alone. State whether any removed component is unrecorded.

## Full answer key

1. Differences=(7−3,6−7,10−6)=(4,−1,4) SU; anchor=3 SU. Addition decodes 3,7,6,10 at IDs 0–3, retaining given times, channel and units.
2. df=−2,dg=3 SU. Direct change=1·5−3·2=−1 SU². Three terms are 9,−4,−6 SU² and sum to −1. Endpoint form is 3·3+(−2)·5=−1. The −6 interaction is retained.
3. Means=(5,8), d=(2,2) SU; Eh=(5,5,8,8), Qh=(−2,2,−2,2). Decoder yields (5−2,5+2,8−2,8+2)=h on the declared support.
4. Linearity follows by distributing weighted sums through (u+v)/2. Repeated mean of (m,m) is m, giving E²=E; averaging ones gives ones. Outputs (a,a,b,b) remain of that form under multiplication and are fixed by E. For constants c,d on a block, average(cu d,cv d)=cd(u+v)/2, which proves the two-sided factor rule. Set qf=f−Ef,qg=g−Eg. Then E(qf)=Ef−E²f=0 and E(qg)=0. Expand fg=Ef Eg+Ef qg+qf Eg+qf qg. Applying E fixes the first term, makes the middle two zero by the factor rule and retains E(qf qg). Subtract to get Q(fg)=Ef qg+qf Eg+qf qg−E(qf qg).

   For the supplied arrays, Ef=(1,1,3,3),Eg=(1,1,1,1),qf=(−1,1,−1,1),qg=(0,0,−1,1). Four RHS terms are (0,0,−3,3), (−1,1,−1,1), (0,0,1,1), and minus (0,0,1,1), giving (−1,1,−4,4). Direct fg=(0,2,0,8), E(fg)=(1,1,4,4), so Q(fg) agrees.

   E_star is linear because every component is linear in x,y,z; applying it twice returns (x,x,z+y−x). It fixes (1,1,1) and its range (a,a,b) is multiplication-closed. But with b=(1,1,0), f=(0,1,0), E_star(bf)=(0,0,1) differs from bE_star(f)=0. For f=g=(0,1,0), Ef=(0,0,1),qf=(0,1,−1); RHS=(0,0,−1)+(0,0,−1)+(0,1,1)−(0,0,2)=(0,1,−3). Direct Q_star(fg)=(0,1,−1). RHS minus direct=(0,0,−2), retained as a counterexample mismatch. Idempotence alone is insufficient.
5. M_0=(2,2,2,2),r_0=(1,5,4,8),M_1=(3,3,6,6),r_1=(−2,2,−2,2) SU. Reconstruct (2+3−2,2+3+2,2+6−2,2+6+2)=(3,7,6,10). r_0 and r_1 are distinct preserved layers.
6. psi=(8−t,t), all real t; kernel direction (−1,1), compatibility 16−2·8=0. With t=3, psi=(5,3). For j=(8,17), c=17−16=1, so no exact solution. Choose j_fit=(8,16),rho=(0,1),psi_fit=(8−t,t); with t=3 its output plus rho is (8,17). This view matches the first equation and is not a unique optimum. L sends (u,v) to (u,2v) and has unique inverse (j_1,j_2/2); K does not have that full inverse.
7. The stage-1 record contains h, M_0, r_0 and decoder M_0+r_0. Stage 2 contains block means m=(3,6),signed d=(2,2),support, M_1,r_1 and pair decoder. Stage 3 contains A=3,δ=6−3=3 SU and decoder (A,A+δ). Reverse: (3,6)→(1,5,4,8)→(3,7,6,10). Error=(0,0,0,0) SU with IDs/times intact. No removed component is unrecorded. EG-A1→source fields, supports, signs and anchors; EG-A2→the reverse check; EG-A3→δ and forward sample differences; EG-A4→the retained −6 SU² product side calculation; EG-A5→both residual layers; EG-A6→the compact typed view with source and decoder. All six have logical_role premise_not_derived_theorem. Finite decoder/product equalities follow under the supplied definitions, without deriving the constitutive physical premises from B.

## Rubric and repair

| Step | Points awarded for observable work |
|---|---|
| 1 | 3 metadata/order; 3 differences; 4 anchor and correct addition decoder |
| 2 | 2 endpoint products; 4 signed three terms; 2 agreement; 2 SU² |
| 3 | 4 means/details; 2 expanded views; 4 signed inverse/support |
| 4 | 7 hypotheses with pair proofs; 7 justified line-by-line derivation; 5 finite numerical check; 6 counterexample and missing factor property |
| 5 | 4 both residual layers; 2 M_1; 4 entrywise reconstruction |
| 6 | 4 solution family/kernel; 2 t=3; 5 incompatibility and residual view; 4 invertible contrast/scope |
| 7 | 6 complete three-stage ledger; 4 reverse replay/errors; 6 all six premise links; 4 source scope and removed-component accounting |

Total: 100 points. Award arithmetic partial credit when the method and retained coordinates are explicit. Exact reconstruction, all six premise IDs and the E hypotheses must be repaired if missing, regardless of score. Recognition-only gauge/infinite-resolution extensions are not assessed. The source gap about a general archival E is not filled by this capstone; the theorem proved here is the explicit finite block theorem.
''')

rows=[]
for i in range(1,8):
    q=f'C07.{i:02}'
    rows.append(f'| {q} | lesson-{i:02}: {q}-E1'+(' and E2' if i in (4,7) else '')+f' | {q}-W1 | {q}-P1 | {q}-D1 | C07-CAP-{i:02} | '+(f'lesson-{i+1:02}' if i<7 else 'capstone')+' |')
write('course-map.md','''
# Course map — Information-Complete Finite Calculus

Seven lessons, eight core periods, two capstone periods. The approved lesson boundaries are retained; lesson 04 spans two periods to teach hypotheses before their use. The chain is lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → lesson-07 → capstone. No calculus, university linear algebra or probability is assumed; arithmetic and substitution bridges appear locally. Course 06 is the series prerequisite; the assessed finite operations are self-contained here.

| Concept | Explanation | Worked | Independently attempted practice with answer | Diagnostic | Capstone | Later use |
|---|---|---|---|---|---|---|
'''+ '\n'.join(rows)+'''

Additional required content: C07.01-W2 contains all six source-premise cards. C07.07-P2 and C07.07-D2 assess their complete ledger mapping. Lesson 04 E1 and period-1 practice teach the hypotheses; E2 and P1 teach the derivation and numerical check; D1 teaches the E_star counterexample before capstone 04. Lesson 06 E1, P1 and D1–D3 teach compatible, incompatible and invertible branches before capstone 06. Source amendment SA-07 is satisfied in these named sections and the all-six-ID ledger.

## Capstone backward map: concrete inputs and outputs

| Step | Input → required output | Earlier explanation and answered practice |
|---|---|---|
| C07-CAP-01 | h=(3,7,6,10), IDs/times → (4,−1,4), anchor 3, decoded h | C07.01-E1, C07.01-P1 |
| C07-CAP-02 | f:3→1,g:2→5 → signed terms 9,−4,−6 and change −1 SU² | C07.02-E1, C07.02-P1 |
| C07-CAP-03 | h and pair support → means (5,8), d=(2,2), inverse | C07.03-E1, C07.03-P1 |
| C07-CAP-04 | fixed block E and f,g → justified identity, (−1,1,−4,4); E_star → mismatch | C07.04-E1/E2, C07.04-P1, C07.04-D1 with full worked answer |
| C07-CAP-05 | h,M_0 → r_0,M_1,r_1 and entrywise h | C07.05-E1, C07.05-P1 |
| C07-CAP-06 | K,j,t → solution family/input; incompatible j → c,rho | C07.06-E1, C07.06-P1, C07.06-D1/D2 |
| C07-CAP-07 | residual means → A,δ, reverse ledger and all six premise links | C07.07-E1/E2, C07.07-P1/P2 |

Each 55-minute core period allocates retrieval 5, teaching/worked example 20, practice 15, diagnostic/repair 15 minutes. Lesson 04 receives two such periods, with properties first and product/counterexample second. Teacher guide gives the exact progression and remediation gates. Units 1 (lessons 01–03), 2 (lesson 04), and 3 (lessons 05–07) close at cumulative checks.
''')

# Save substantive drafts and recovery hashes before audit; this is not a completion declaration.
order=[f'lesson-{i:02}' for i in range(1,8)]
write('course.md','# Information-Complete Finite Calculus\n\nStudent lessons in approved order. See teacher-guide.md, capstone.md and sources.md for supporting materials.\n\n'+'\n\n'.join(f'<!-- BEGIN: {lid} -->\n'+(ROOT/f'{lid}.md').read_text().rstrip()+'\n'+f'<!-- END: {lid} -->' for lid in order))
spec=[('course-map','course-map','course-map.md',[])]+[(lid,'lesson',lid+'.md',['course-map'] if i==0 else [order[i-1]]) for i,lid in enumerate(order)]+[('terminology','terminology','terminology.md',order),('teacher-guide','teacher-guide','teacher-guide.md',order),('capstone','capstone','capstone.md',order),('sources','supplement','sources.md',[]),('source-record','supplement','sources.json',[]),('assembly','assembly','course.md',order),('audit','audit','audit_report.json',order)]
manifest={'schema_version':'1.0','topic':packet['topic'],'audience':packet['audience'],'assumptions':packet['assumptions']+['Synthetic SU examples only; general archival E proof remains scoped; seven lessons occupy eight core periods.'],'ordered_deliverables':[p for _,_,p,_ in spec]+['completion_report.json'],'checkpoints':[{'id':cid,'kind':kind,'path':path,'status':'drafted','dependencies':deps,'sha256':digest(ROOT/path),'summary':f'Complete draft of {cid}; pending independent audit.'} for cid,kind,path,deps in spec],'course_order':order,'assembly':{'path':'course.md','section_ids':order},'audit_counts':{'critical':0,'major':0,'minor':0},'blockers':[],'next_action':'Independently recompute examples, inspect actual teaching coverage, and audit before passing checkpoints.'}
manifest['dependencies']={c['id']:c['dependencies'] for c in manifest['checkpoints']}
js('manifest.json',manifest)
js('completion_report.json',{'status':'in_progress','topic':packet['topic'],'next_action':manifest['next_action']})
print('Complete drafts saved; checkpoints remain drafted pending audit.')
