# Lesson 06 — Retained-detail filtrations

Essential question: How can coarse summaries and signed detail together reconstruct every entry?

Goals: Calculate nested averages and both detail sectors; verify projector and orthogonality identities in a finite model; state the missing assumptions in an infinite or product extension.

Bridge and pacing: Lesson 05 grouped inputs without identifying them. Now average four explicit entries while retaining what the averages omit. Two 55-minute periods, each retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15. Period 1 covers matrices and reconstruction; period 2 covers projector tests and the scope of extension.

## C22.06-E1 — Split, retain, reconstruct

A vector v=(v₁,v₂,v₃,v₄) is an ordered list; here entries are dimensionless synthetic cell values with equal cell weights. P₀ replaces all four entries by their mean. P₁ replaces entries 1–2 by their pair mean and entries 3–4 by their pair mean. I is the identity operation, which leaves all entries unchanged. Define Q₀=P₁−P₀ and Q₁=I−P₁. Apply the operations before subtracting entry by entry. Then P₀v+Q₀v+Q₁v=P₀v+(P₁v−P₀v)+(v−P₁v)=v by cancellation. Zero-valued detail entries remain entries in the stored vectors.

Here are the matrices; multiply a row by v by summing the four row-entry times vector-entry products. A product AB means apply B first, then A.

```
P0 = (1/4) [1 1 1 1; 1 1 1 1; 1 1 1 1; 1 1 1 1]
P1 = (1/2) [1 1 0 0; 1 1 0 0; 0 0 1 1; 0 0 1 1]
Q0 = (1/4) [1 1 -1 -1; 1 1 -1 -1; -1 -1 1 1; -1 -1 1 1]
Q1 = (1/2) [1 -1 0 0; -1 1 0 0; 0 0 1 -1; 0 0 -1 1]
I  =       [1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1]
```

Semicolons separate rows. For instance, Q₀'s first row gives (v₁+v₂−v₃−v₄)/4. A projector P satisfies P²=P: applying it twice adds nothing. A transpose swaps rows and columns; Pᵀ=P means the matrix is symmetric. A symmetric projector is an orthogonal projector for the dot product v·w=Σv_iw_i. “Orthogonal” means dot product zero, not absence of either piece.

Verify the operations before using the terminology. Averaging constants again changes nothing, so P₀²=P₀; repeating pair averages also changes nothing, so P₁²=P₁. Averaging pair averages globally gives the original global mean, hence P₀P₁=P₀. Pair-averaging a global constant leaves it unchanged, so P₁P₀=P₀. It follows that Q₀²=P₁²−P₁P₀−P₀P₁+P₀²=P₁−P₀=Q₀ and Q₁²=I−2P₁+P₁²=Q₁. All displayed matrices are symmetric. Mixed products of P₀,Q₀,Q₁ vanish: for example P₀Q₀=P₀P₁−P₀²=0 and Q₀Q₁=(P₁−P₀)(I−P₁)=0; reversing the order gives zero too. These verifications prove all three sectors are orthogonal projectors. P₁ itself overlaps P₀, so **not every pair among P₀,P₁,Q₀,Q₁ has zero product**.

## C22.06-W1 — Worked reconstruction

For v=(1,3,5,7), global mean is 16/4=4 and pair means are 2 and 6. Therefore P₀v=(4,4,4,4), P₁v=(2,2,6,6), Q₀v=(−2,−2,2,2), Q₁v=(−1,1,−1,1). Adding each column gives (1,3,5,7). For an independent orthogonality check, Q₀v·Q₁v=2−2−2+2=0. Dot products with the constant mean vanish because each detail vector sums to zero. Neither signed detail vector may be erased by that zero sum.

> Claim scope: This four-cell equal-weight, pairwise example is a synthetic finite bridge to S02 M18 /proof/4. Its two-way grouping is not a redefinition of ternary address depth. An infinite filtration is a sequence of nested coarse spaces. To assert I=P₀+ΣQ_n there, one must specify an ambient space and convergence of P_Nv to v in the chosen mode. If P_Nv converges only to a coarser projection, its sum reconstructs only that projection; retain the complementary component.

## A product boundary from S03 AUD-006

An averaging E on these finite cells is linear, preserves constants, satisfies E²=E, and has the following property: if c is constant on each averaging block, E(cf)=cE(f). Products here mean entrywise multiplication. Let Q=I−E. Then E(Qf)=0, and expanding f=Ef+Qf and g=Eg+Qg gives four terms. Applying E kills Ef·Qg and Qf·Eg by the block-constant property; it retains Ef·Eg and E(Qf·Qg). Subtracting this average from fg gives

Q(fg)=Ef·Qg+Qf·Eg+Qf·Qg−E(Qf·Qg).

This derivation uses the stated properties, not Q=I−E alone. The finite difference product also retains its last term: if Δf=f_t−f_s and Δg=g_t−g_s, expanding (f_s+Δf)(g_s+Δg)−f_sg_s gives f_sΔg+g_sΔf+ΔfΔg. For f_s=1,f_t=3,g_s=2,g_t=5 the three terms are 3,4,6, totaling 13=15−2. Dropping 6 gives a false answer. These source-reading bridges explain what a claimed general product identity would need; no unprovided infinite product domain is assumed.

## C22.06-P1 — Practice, then check

Decompose v=(2,0,6,4), reconstruct P₁v, then reconstruct v. Also apply Q₁ to a constant vector (2,2,2,2).

Answer: P₀v=(3,3,3,3), Q₀v=(−2,−2,2,2), Q₁v=(1,−1,1,−1). Adding the first two gives P₁v=(1,1,5,5); adding the third gives the input. Q₁(2,2,2,2)=(0,0,0,0); retain all four zeros and the operation label.

## Diagnostics — C22.06-D1

1. Can P₀v alone reconstruct the worked input?
2. Is P₀P₁ zero?
3. Does a finite identity automatically prove infinite norm convergence?
4. In the product formula, can E(Qf·Qg) always be omitted because E(Qf)=E(Qg)=0?

Worked answers: (1) No; both detail vectors are needed, and many inputs share mean 4. (2) No, it equals P₀; only the disjoint sectors P₀,Q₀,Q₁ have zero mixed products. (3) No; an ambient space, limiting subspace and convergence mode must be supplied. (4) No: on one pair take Qf=Qg=(1,−1). Each mean is zero but the product is (1,1) with mean 1. The product detail must be centered explicitly.

Next dependency: [Lesson 07](lesson-07.md) turns these infinite-scope obligations into a precise operator-domain checklist.
