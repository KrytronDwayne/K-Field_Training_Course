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
