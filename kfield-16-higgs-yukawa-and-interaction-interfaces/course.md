# Higgs, Yukawa, and Interaction Interfaces

Student course. See course-map.md for pacing and capstone.md for synthesis.

<!-- BEGIN: lesson-01 -->
# Lesson 1 — Interactions must match their inputs

Essential question: What must match before an interaction expression can return a scalar?

Goals: identify each input's type; compute its integer charge; track color and weak degrees through all four interfaces.

Bridge from course 15: a sector is a named collection of possible components. We recall every sector needed here, so you need only signed arithmetic and ordered lists. Two 55-minute periods: each uses 5 minutes retrieval, 20 explanation/examples, 15 practice, and 15 diagnostics/repair. Period 1 handles wedge interfaces; period 2 handles dual interfaces.

## C16.01-E1 — A type is part of an input

An ordinary formula such as distance = speed × time requires inputs of the right kind. Our interaction formulas also require kinds, called types. The underlying ordered list is color-first: (c1,c2,c3,w1,w2). The three c labels belong to C₃ and the two w labels belong to W₂. These are abstract basis vectors, not positions or measured colors. A basis is a fixed list used to describe components. The direct sum C₃ ⊕ W₂ places both lists in one five-slot carrier.

The exterior product, written ∧ or “wedge,” records an oriented selection of slots. Exchanging two neighboring slots changes the sign; a repeated slot gives zero. Thus w2∧w1 = −w1∧w2, while w1∧w1 = 0. Products distribute across addition, so the rules for basis selections extend to sums of selections. A bidegree (r,s) counts r color slots and s weak slots. It records type, not amplitude. Joining selections adds their degrees unless a repeated factor makes the result zero.

The integer hypercharge is q = −2r + 3s; the hypercharge convention is Y_h = q/6. Neither is the electric charge introduced in lesson 3. All three charge numbers are dimensionless. The subscript h distinguishes hypercharge from a Yukawa coefficient matrix later. Superscript c in u^c is part of the source's sector label, not an exponent or an instruction to conjugate a number.

| Input | Bidegree | q | Y_h | Role |
|---|---|---:|---:|---|
| u^c | (2,0) | −4 | −2/3 | exterior input |
| Q | (1,1) | 1 | 1/6 | exterior input; Q here is a sector |
| ν^c | (0,0) | 0 | 0 | scalar input |
| L | (3,1) | −3 | −1/2 | exterior input |
| d^c | (2,2) | 2 | 1/3 | exterior input |
| e^c | (0,2) | 6 | 1 | exterior input |
| H | (0,1) | 3 | 1/2 | supplied Higgs vector |
| barH | weak dual | −3 | −1/2 | covector removing a weak slot |

A covector is a linear measuring rule: w1* returns 1 on w1 and 0 on other basis vectors. A vector is an input to that rule. They cannot be substituted for one another. With an orthonormal basis, the Hermitian dual barH of H uses conjugated coefficients; for the real basis vector H=w1, it is w1*. Later we teach the complex phase rule. barH has no ordinary nonnegative exterior bidegree to add: its contraction removes one weak slot.

Set Ω = c1∧c2∧c3∧w1∧w2. It is the reference top form, filling all five slots, with bidegree (3,2). Ω⁻¹ here means “extract the coefficient of Ω”: Ω⁻¹(7Ω)=7. It is not division by a vector. The symbol ι_barH means contract with the covector barH; lesson 2 teaches its sign rule.

Read the supplied M12 interfaces in their stated order:

| Interface | Expression | Type route |
|---|---|---|
| up | I_u = Ω⁻¹(u^c ∧ Q ∧ H) | (2,0)+(1,1)+(0,1)=(3,2) |
| neutrino | I_ν = ν^c Ω⁻¹(L ∧ H) | scalar times (3,1)+(0,1) |
| down | I_d = Ω⁻¹(Q ∧ ι_barH d^c) | (2,2)→(2,1); add Q to get (3,2) |
| electron | I_e = Ω⁻¹(L ∧ ι_barH e^c) | (0,2)→(0,1); add L to get (3,2) |

A zero total q is necessary for these interfaces, but it is not a substitute for the type route. A product of two charge-zero scalars has q=0 yet has degree (0,0), so it is not a top form to which this Ω coefficient extraction applies.

## C16.01-W1 — Worked ledger

For up, insert the rows u^c, Q, H: q_total = −4+1+3=0. Their degrees add to (2+1+0,0+1+1)=(3,2). For neutrino, q_total=0−3+3=0; ν^c has degree zero and L∧H has degree (3,2). Both routes have the correct type. This does not tell us whether any selected component is zero: that requires checking repeated slots.

## C16.01-P1 — Practice before checking the answer

Make the same ledger for down and electron. State the operation on the dual input, not just a charge sum. Then redo the up and neutrino ledgers without looking at W1.

Worked answer: down gives 2+1−3=0. Contract d^c first: (2,2)→(2,1); Q contributes (1,1), giving (3,2). Electron gives 6−3−3=0. Contract e^c: (0,2)→(0,1); L contributes (3,1), giving (3,2). Up gives −4+1+3=0 and (3,2); neutrino gives 0−3+3=0 and (3,2). Each final hypercharge is also zero because Y_h=q/6.

> Claim scope: the sector table is S02 /backbone_sequence/10; the interfaces are S02 /backbone_sequence/11. We freshly check their finite charge/type arithmetic. Basis coefficients in teaching examples are chosen for calculation, not measured interactions. Numerical couplings remain separate inputs.

## Diagnostics and worked answers

1. **C16.01-D1:** Replace barH by H in down. What fails? Answer: 2+1+3=6, and wedging all inputs would give weak degree 4, exceeding two weak slots; it is not the given scalar interface.
2. **C16.01-D2:** Find q for (3,1) and explain the −3. Answer: −2×3+3×1=−6+3=−3; each color contributes −2 and each weak slot contributes +3.
3. **C16.01-D3:** Does q=0 prove a nonzero top form? Answer: no; ν^c alone has q=0 and degree (0,0), and repeated-slot products can be zero.
4. **C16.01-D4:** Is Q an electric-charge operator here? Answer: no, Q names the (1,1) input sector. We will write the operator as Q_electric.

Next dependency: [Lesson 2](lesson-02.md) computes the contractions and their signs.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 2 — Invariant contractions

Essential question: How can a scalar stay unchanged when every input changes coordinates consistently?

Goals: evaluate wedge and contraction signs; compute the four supplied scalars; test vector/dual phase rules; explain the scope of the invariance argument.

Bridge: lesson 1 supplied the types, charges, and color-first order. Now we calculate coefficients. Three 55-minute periods each allocate 5 retrieval, 20 teaching/examples, 15 practice, 15 diagnostics/repair. Use period 1 for wedges and contractions, period 2 for the four interfaces, and period 3 for phase covariance. Complex arithmetic is taught here; no general matrix theory is assumed.

## C16.02-E1 — Remove a slot with its sign

Write c1c2 as shorthand for c1∧c2, never ordinary commuting multiplication. The reference order is c1,c2,c3,w1,w2. To evaluate a full selection, first check repetition, then count neighboring exchanges needed to restore that order. Each exchange multiplies by −1. An even number gives +Ω; an odd number gives −Ω. For example c2c1c3w1w2=−Ω. Repetition gives zero before reordering: c1c2c3w1w1=0.

Contraction removes one selected vector and multiplies by the covector's evaluation on that vector. For a product of k vectors, inspect positions j=1 through k. Delete position j, evaluate ℓ(v_j), and use alternating sign +,−,+,−,…, starting with + at position 1. Add these contributions:

ι_ℓ(v1∧…∧vk) = Σ_j (−1)^(j−1) ℓ(v_j) v1∧…∧v_(j−1)∧v_(j+1)∧…∧vk.

Σ means add the listed terms; a term with evaluation 0 contributes nothing. For ℓ=w1*, only a w1 slot survives. This rule is a concrete algorithm, not an instruction to erase all signs. On the scalar 1 there is no slot to remove, so contraction gives zero.

## C16.02-W1 — Two removals and two scalar interfaces

On w1w2, w1* selects position 1, so ι_w1*(w1w2)=w2. The covector w2* selects position 2, so ι_w2*(w1w2)=−w1. These are different outputs from different measuring rules.

For up choose u^c=c1c2, Q=c3w1, H=w2. The source order gives c1c2c3w1w2=Ω, so I_u=+1. For neutrino choose ν^c=1, L=c1c2c3w1, H=w2. Its wedge is Ω, so I_ν=1×1=+1. The ordered basis components have dimensionless coefficient 1 for this structural exercise; no mass unit is assigned to this finite replay.

## C16.02-P1 — Four-route practice

Compute down for d^c=c1c2w1w2, Q=c3w1, barH=w1*. Compute electron for e^c=w1w2, L=c1c2c3w1, barH=w1*. Also recompute W1's up and neutrino cases independently, and replace neutrino H by w1.

Worked answer: in down the selected w1 is position 3 in d^c. Its sign is (−1)²=+1, giving c1c2w2. The source formula places Q first: c3w1c1c2w2. Moving c1 left takes two swaps, and moving c2 left takes two more. Four swaps give +Ω, so I_d=+1. In electron the contraction yields w2, and L∧w2=Ω, so I_e=+1. Up and neutrino remain +1 as in W1. The changed neutrino case contains w1 twice and equals zero. This is a zero component of an allowed interface; it is not evidence for a new nonzero interaction.

## C16.02-E2 — Change vectors and measuring rules together

Introduce i by i²=−1. Then i(−i)=1, so the inverse of i is −i. Complex conjugation changes i to −i. A phase such as i rotates a component without changing its magnitude; the magnitude of i is 1. A diagonal transformation multiplies each basis vector by its listed factor. The five entries in diag(1,1,1,i,−i) belong, in order, to c1,c2,c3,w1,w2. It changes weak vectors by w1→iw1 and w2→−iw2, leaving colors fixed.

To keep w1*(w1)=1 after this change, transform the covector by the inverse factor: w1*→−iw1*. Evaluation now gives (−i)i=1. Transforming both by i would give i²=−1 and fail. In general write U for an invertible change of vectors and U⁻¹ for its undoing. The covector changes as ℓ→ℓU⁻¹. Then (ℓU⁻¹)(Uv)=ℓv because undoing follows doing. This is covariance of evaluation: the parts change consistently.

The exterior action applies U separately to every vector and distributes across products. Contraction respects this action: each term evaluates the transformed covector on the transformed deleted vector, which is the original evaluation; the remaining vectors all carry U. Therefore contracting first and transforming afterward has the same result as transforming all inputs first and then contracting.

The determinant det U is the multiplier of the full oriented top form under U. For a diagonal action it is the product of its five factors. If det U=1, Ω remains Ω, so extracting its coefficient after the covariant operations returns the same scalar. The source group S(U(3)×U(2)) consists here of color/weak block transformations that preserve the Hermitian inner product (lengths and complex angles) and whose combined determinant is 1. This defines the relevant conditions; computing a general determinant or proving a group theorem is not required. The slot argument gives the covariance reason, while the next calculations directly test finite cases. Charge cancellation alone would not give this argument.

## C16.02-W2 — A nontrivial phase test

Apply U=diag(1,1,1,i,−i) to the up case in W1. u^c has factor 1; Q has i from w1; H has −i from w2. The product gains 1×i×(−i)=1, so I_u remains +1. Neutrino L gains i and H gains −i, so I_ν also remains +1. The determinant is 1×1×1×i×(−i)=1. We changed components but preserved the scalar.

## C16.02-P2 — Test the dual and a sign change

Apply the same U to the down and electron examples. Then calculate up using u^c=c1c3, Q=c2w1, H=w2; calculate neutrino with L=c1c2c3w2, H=w1. Finally test the color transformation diag(i,−i,1,1,1) on all four original examples. Explain why transforming a covector by ℓU⁻¹ preserves evaluation and why det U=1 completes the top-form argument.

Worked answer: d^c and e^c each contain w1w2 and gain i(−i)=1. Q or L gains i; barH=w1* gains −i. Down and electron each gain factor 1. In the new up example, c1c3c2w1w2 needs one swap and gives −Ω, hence −1. The new neutrino example ends w2w1, also one swap, giving −1. Invariance means preserving each resulting scalar under an allowed change; it does not say all components have the same sign. For the color transformation, c1c2 gains i(−i)=1, c3 gains 1, and c1c2c3 gains 1. Weak inputs are unchanged; all four original scalars stay +1.

Practice explanation answer: (ℓU⁻¹)(Uv)=ℓ(U⁻¹U)v=ℓv. Each deleted-slot evaluation in the contraction sum is therefore unchanged, while all remaining slots receive U. The final top form gains det U; when det U=1 its coefficient relative to Ω is unchanged. This is the structural reason behind the finite phase checks, under the conditions taught in E2.

> Claim scope: S02 /backbone_sequence/11 supplies the interfaces, and /proof_nodes/84 states representation invariance. Our explicit slot argument explains covariance under the stated determinant-one action. These checks neither execute the source compiler nor determine numerical Yukawa coefficients. All finite component choices are teaching examples.

## Diagnostics and worked answers

1. **C16.02-D1:** Give the full acceptance check for an apparent charge-zero expression. Answer: check vector/dual type, slot removal, repeated slots, sign, final degree (3,2), and consistent transformation of every input; q=0 alone omits these tests.
2. **C16.02-D2:** What happens if barH wrongly gains i instead of −i in the weak-phase down test? Answer: the total factor is i×i=−1. The result flips from +1 to −1, so the mistaken rule fails. Keep that failed result in the audit and correct the dual rule.
3. **C16.02-D3:** Compute ι_w2*(c1c2w1w2). Answer: w2 is fourth, sign (−1)³=−1, result −c1c2w1.
4. **C16.02-D4:** Does det U=1 permit ignoring the covector rule? Answer: no; preserving the final volume does not repair an incorrectly transformed intermediate evaluation.
5. **C16.02-D5:** Why can a nonzero invariant have value −1? Answer: invariance means the value is unchanged under the specified action, not that it is positive. The altered up example has one swap and stays a valid negative component.

Next dependency: [Lesson 3](lesson-03.md) uses the supplied weak doublet to identify a neutral vacuum direction.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 3 — The Higgs doublet interface

Essential question: Which component of the supplied doublet can carry a vacuum without changing electric charge?

Goals: calculate the two component charges; apply a diagonal operator to a vector; test a proposed vacuum and calculate its squared length.

Bridge: H in lessons 1–2 had two available weak basis directions, w1 and w2, and degree (0,1). We now attach coefficients to those directions. One 55-minute period: 5 retrieval, 20 teaching/example, 15 practice, 15 diagnostics/repair.

## C16.03-E1 — A doublet has two components

A doublet is an ordered pair of components. Write H=(H_plus,H_zero) in the basis (w1,w2). The subscripts anticipate the charges we will calculate, not assumed measurements. A diagonal operator diag(a,b) multiplies the first component by a and the second by b: diag(a,b)(x,y)=(ax,by). The identity I=diag(1,1) leaves the pair unchanged. Adding two diagonal operators adds their corresponding entries.

For this supplied Higgs carrier, define T3=diag(1/2,−1/2), and Y_h=I/2=diag(1/2,1/2). The electric-charge operator is Q_electric=T3+Y_h=diag(1,0). Thus the upper component has electric charge +1 and the lower component charge 0. Both have the same hypercharge +1/2. T3 distinguishes the two weak positions; hypercharge alone does not.

The source vacuum is H_vac=(0,v/√2), with v a supplied nonnegative magnitude. √2 is the positive number whose square is 2; v/√2=v√2/2. In the compiler mass convention used here, v and H_vac carry a mass unit μ. μ denotes an arbitrary teaching unit, not a measured energy scale. The squared length of a real pair is x²+y², with unit μ² if x,y have unit μ. Our real vacuum examples need no complex-length formula.

An unbroken charge generator annihilates the vacuum: Q_electric H_vac=(0,0). “Annihilates” means returns the zero vector, not that the vacuum itself vanishes. The lower component has multiplier zero, so every value of v in this supplied direction meets this test. At a nonzero upper component, the multiplier is 1 and the test fails. The source's continuous symmetry statement uses this generator test; we do not need calculus to evaluate it. This checks the displayed electric generator, not a count of every symmetry at v=0.

## C16.03-W1 — Evaluate a neutral direction

Take synthetic v=2 μ. Then v/√2=√2 μ, so H_vac=(0,√2) μ. Its squared length is 0²+(√2)²=2 μ². Applying Q_electric gives (1×0,0×√2) μ=(0,0). Notice the vacuum is nonzero while the operator output is zero. The charge test selects a direction, but it has not selected the magnitude 2.

## C16.03-P1 — Practice

For synthetic v=4 μ, find the vacuum, its squared length, and its Q_electric output. Compare the test vector (1,0) μ.

Worked answer: 4/√2=2√2, so H_vac=(0,2√2) μ. Squaring gives 4×2=8 μ². The charge output is (0,0). For (1,0) μ the output is (1,0) μ, nonzero, so a vacuum placed solely there with nonzero magnitude would not preserve this generator.

> Claim scope: S02 /backbone_sequence/11 and /proof_nodes/80 supply the doublet, neutral direction, and parameter v. Numerical choices above are synthetic. The potential is a function used to specify which field configurations are energetically favored; its coefficients and vacuum stability are not determined by this charge test. No potential minimization is assessed.

## Diagnostics and worked answers

1. **C16.03-D1:** Does neutrality determine v, potential coefficients, stability, or rate? Answer: none of them; Q_electric(0,v/√2)=0 for every v, so the equation cannot choose a particular magnitude or evolution.
2. **C16.03-D2:** Why is the upper charge 1 rather than 1/2? Answer: add its T3 and Y_h contributions: 1/2+1/2=1.
3. **C16.03-D3:** At v=0, what is the tested vacuum? Answer: (0,0), squared length 0; Q_electric annihilates it too. This does not establish that only one generator is unbroken there.
4. **C16.03-D4:** What is the squared length for v=6 μ? Answer: v²/2=36/2=18 μ²; the general formula comes from squaring the lower component.

Next dependency: [Lesson 4](lesson-04.md) uses the same supplied v in mass formulas.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# Lesson 4 — Unbroken charge and mass formulas

Essential question: What can algebra determine from supplied couplings and a vacuum magnitude?

Goals: substitute values with correct units; derive the rho identity on its domain; distinguish a formula input from its output.

Bridge: lesson 3 selected the neutral direction without selecting v. Here v enters two supplied formulas. Two 55-minute periods each use 5 retrieval, 20 teaching/examples, 15 practice, 15 diagnostics/repair. Period 1 focuses on squares and units; period 2 on cancellation, boundaries, and rescaling.

## C16.04-E1 — An identity with a domain

The source compiler formulas are

m_W² = g2² v²/4, and m_Z² = (g2²+gY²)v²/4.

Here g2 and gY are real dimensionless coupling inputs; v≥0 has mass unit μ. A coupling records a strength in the supplied convention. W and Z label two gauge-boson mass outputs; detailed particle dynamics are outside this calculation. Squared masses have unit μ², and the masses themselves are the nonnegative square roots. Square each input before adding: g2²+gY² is generally different from (g2+gY)².

Define c²_theta = g2²/(g2²+gY²). The source notation for this number is cos²θ. In this course the ratio is its operational definition; no trigonometry or angle extraction is required. It is defined when g2²+gY²>0. Define rho, written ρ, by ρ=m_W²/(m_Z² c²_theta) only if that denominator is nonzero.

Substitute before cancelling:

m_Z² c²_theta = [(g2²+gY²)v²/4] × [g2²/(g2²+gY²)] = g2²v²/4 = m_W².

The cancelled factor g2²+gY² must be nonzero. To divide by the resulting m_W² also requires g2≠0 and v≠0. On that domain, ρ=(g2²v²/4)/(g2²v²/4)=1. The result is dimensionless because μ² cancels. This is a derived algebraic identity conditional on the supplied formulas, not a derivation of those formulas from a kinetic field theory.

## C16.04-W1 — Worked substitution

Choose synthetic g2=3, gY=4, v=2 μ. Then g2²=9, gY²=16, v²=4 μ². We obtain m_W²=9×4/4=9 μ² and m_Z²=(9+16)×4/4=25 μ². Thus m_W=3 μ and m_Z=5 μ. Also c²_theta=9/25. The rho denominator is 25×9/25=9 μ², nonzero; ρ=9/9=1.

## C16.04-P1 — Practice and scaling

Choose synthetic g2=4, gY=3, v=2 μ. Calculate squared masses, masses, c²_theta, and ρ. Then double only v. Finally set v=0 and test whether ρ can be evaluated.

Worked answer: m_W²=16×4/4=16 μ²; m_Z²=(16+9)×4/4=25 μ². Nonnegative roots give 4 μ and 5 μ. c²_theta=16/25, and the denominator 25×16/25=16 μ² gives ρ=1. At v=4 μ, squared masses are 64 and 100 μ²; masses are 8 and 10 μ. Doubling v multiplies v² by four, so it quadruples squared masses and doubles positive masses while leaving the couplings and ratio fixed. At v=0 both squared masses vanish, and the displayed ratio is 0/0, which is undefined.

> Claim scope: S02 /proof_nodes/80 supplies the mass-squared relations and reports the compiler rho identity. Our fresh verification is substitution and cancellation on the explicit nonzero domain. Values are synthetic; matching scale and numerical couplings are retained inputs. No measured mass or compiler execution is asserted.

## Diagnostics and worked answers

1. **C16.04-D1:** Is rho numerically 1 at v=0? Answer: the displayed expression is undefined there. A limiting value is a different statement and is not used to fill 0/0.
2. **C16.04-D2:** If g2=0, gY=3, v=2 μ, what fails? Answer: m_W²=0, m_Z²=9 μ², c²_theta=0; the rho denominator is zero. If both couplings vanish, even c²_theta is undefined.
3. **C16.04-D3:** Does changing gY from 3 to −3 change P1? Answer: no; gY enters through gY²=9 in these formulas. This degeneracy means the squared-mass outputs alone do not recover every sign.
4. **C16.04-D4:** Is 25 μ² a mass? Answer: it is a squared mass; its nonnegative square root is 5 μ. Confusing them would break units and scaling.

Next dependency: [Lesson 5](lesson-05.md) treats coefficient matrices as additional inputs, independent of charge cancellation.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 5 — Yukawa maps and mixing inputs

Essential question: Why does knowing an allowed interaction leave its numerical coefficients undetermined?

Goals: apply a two-by-two coefficient map; distinguish matrix shape from entries; perform a reversible basis swap; track mass normalization and units.

Bridge: lessons 1–2 establish the interaction's type and invariant scalar structure; lesson 4 shows how supplied numbers affect outputs. Two 55-minute periods, each with 5 retrieval, 20 teaching/examples, 15 practice, 15 diagnostics/repair. Period 1 introduces matrix action, period 2 basis changes and reversibility.

## C16.05-E1 — A table of coefficients is a rule

A matrix is a rectangular array of numbers. For a two-component column f=(f1,f2), the matrix A=[[a,b],[c,d]] sends it to (a f1+b f2,c f1+d f2). Each row gives one output; each column records how one input contributes. The notation [[a,b],[c,d]] lists rows. This is a finite linear map: scaling and adding inputs scales and adds outputs. Matrix multiplication means composition: AB acts by B first, then A. You can compute each output directly without memorizing a general multiplication algorithm.

We write Y_Yuk for the supplied Yukawa coefficient matrix, reserving Y_h for hypercharge. A family label distinguishes copies of the matter structure. It is not a weak slot, color slot, handedness, or detector parity. A two-family teaching model illustrates the map; it is not a claim that the source has only two physical families. Compatibility determines which sectors can connect. It does not supply the numerical entries of Y_Yuk or the state f.

Use dimensionless entries and dimensionless f in the exercises. Y_Yuk f is dimensionless. For a declared classroom mass convention, M=(v/√2)Y_Yuk has entries in μ, so Mf has mass units. A matrix's entries and a map output are not automatically particle mass eigenvalues; we do not ask you to diagonalize a physical mass operator.

A basis change relabels the component coordinates. The swap matrix P=[[0,1],[1,0]] sends (x,y) to (y,x); doing it twice restores the original vector, so P⁻¹=P. Transpose, marked T, interchanges rows and columns. Here P^T=P=P⁻¹. If we swap both input and output coordinates, use Y′=P Y_Yuk P^T and f′=Pf. Then Y′f′=P Y_Yuk P^T P f=P Y_Yuk f because P^T P=I. This changes coordinates while preserving the map's meaning. It is a reversible relabeling, not deletion of a component.

## C16.05-W1 — Worked row-by-row action

Choose synthetic Y_Yuk=[[1,2],[0,3]] and f=(2,−1). The first row gives 1×2+2×(−1)=0; the second gives 0×2+3×(−1)=−3. The output is (0,−3). A zero output component is a retained result, not a reason to erase an input. In the separate normalization example v=√2 μ, v/√2=1 μ, so M has the same numerical entries as Y_Yuk, each multiplied by μ. Mf=(0,−3) μ. Preserve Y_Yuk, f, v, units, and output to replay the computation.

## C16.05-P1 — Practice a map and its swap

Use synthetic Y_Yuk=[[2,0],[1,1]] and f=(1,2). Compute the output, swap both coordinate lists, find Y′ and f′, then compute the new output. Show how to recover the original records.

Worked answer: the original output is (2×1+0×2,1×1+1×2)=(2,3). Swapping rows gives P Y_Yuk=[[1,1],[2,0]]. Swapping columns then gives Y′=[[1,1],[0,2]]. The new input is f′=(2,1); the new output is (1×2+1×1,0×2+2×1)=(3,2), exactly P(2,3). Undo with f=Pf′ and Y_Yuk=P Y′ P, recovering all coefficients. This coordinate change introduces no residual. If v=2 μ, M=√2 μ times Y_Yuk and Mf=(2√2,3√2) μ; this optional normalization uses the same rule, not a new physical inference.

> Claim scope: S02 /backbone_sequence/11 lists Yukawa coefficient matrices and mixing coordinates as occupied-state inputs; /proof_nodes/84 preserves that boundary. All matrix numbers, states, and the classroom normalization above are explicitly supplied examples. A simple simultaneous swap teaches consistency; general mixing can involve different basis changes on input and output, and physical mixing parameters require additional specification.

## Diagnostics and worked answers

1. **C16.05-D1:** Can charge cancellation pick a Yukawa matrix or mixing angle? Answer: no. It checks compatibility, not numerical coefficients or relative basis choices.
2. **C16.05-D2:** Keep Y′ from P1 but forget to swap f. What output results? Answer: [[1,1],[0,2]](1,2)=(3,4), not the required (3,2). Mixing coordinate conventions changes the calculation.
3. **C16.05-D3:** Replace W1's matrix by the identity with the same shape. What happens? Answer: the output becomes (2,−1), demonstrating that shape alone does not select the result.
4. **C16.05-D4:** Is replacing (2,3) by its sum 5 reversible? Answer: not from 5 alone; many pairs have that sum. Retain both components or enough additional coordinates to reconstruct them. The swap, by contrast, has an explicit inverse.

Next dependency: [Lesson 6](lesson-06.md) uses the same preservation discipline for signed energy changes.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 6 — Energy and transition accounting

Essential question: What information does an energy difference contain, and what must still be supplied to describe a transition?

Goals: reconstruct signed component changes; retain a prediction and its residual; distinguish energy, action architecture, and transition rate.

Bridge: lesson 5 preserved every component and the coordinate map. An energy ledger needs the same care. One 55-minute period: 5 retrieval, 20 teaching/example, 15 practice, 15 diagnostics/repair.

## C16.06-E1 — Subtract endpoints without losing their labels

An energy ledger records values for specified components at specified states. For each component define ΔE=E_after−E_before. A positive sign means an increase in that component; a negative sign means a decrease. Add components only if they use the same unit and the accounting assigns them without double counting. A total loses information about distribution, so retain the labeled component rows even when reporting their sum.

In the teaching examples A, B, C are three synthetic, nonoverlapping bookkeeping components, all in an arbitrary energy unit ε. These rows are not the source's action sectors. The labels “before” and “after” specify order but supply no elapsed time. Define a model-predicted net change p and residual r=ΔE_total−p. Then ΔE_total=p+r exactly. The residual is retained primary information: it records what this prediction did not encode. It is not removed because it is small or negative.

For an energy balance, distinguish this model residual from a transfer residual. If a supplied external transfer into the system is T, the unclosed balance is b=ΔE_total−T. Conservation for a fully closed accounting would require b=0. If T is absent, record “not supplied”; do not invent it. A synthetic open ledger may have a nonzero total change without asserting that an isolated system creates or destroys energy. If later evidence identifies a missing transfer channel, retain the earlier residual and its explanation rather than replacing the original record.

The source's action architecture is S=S_native+S_gauge+S_fermion+S_Higgs+S_Yukawa+S_TG. An action is a quantity used to specify dynamics when its full functional rules and conditions are supplied; its physical dimension is energy × time in ordinary units. The six names label native, gauge, fermion, Higgs, Yukawa, and tetrad-gravity contributions. For this course those names are recognition-only architecture. They are not automatically six independently measured energies, and their symbols inside the full source expression have their own local meanings. We do not use source action-variable q as our integer charge q.

A transition rate requires a temporal and dynamical specification, such as events per unit time for a defined preparation and observation procedure. An energy difference alone has no time unit. Even ΔE/Δt, if time were supplied, would be an average power, not automatically an event probability or count rate. A rule linking states, interactions, time, and counted events is additional information.

## C16.06-W1 — Worked signed record

| Component | Before (ε) | After (ε) | After − before (ε) |
|---|---:|---:|---:|
| A | 5 | 4 | −1 |
| B | 2 | 4 | +2 |
| C | 1 | 1 | 0 |
| Total | 8 | 9 | +1 |

The total change computed by rows is −1+2+0=1 ε. Computed by endpoints it is 9−8=1 ε, a useful independent check. If p=0.8 ε, r=1−0.8=+0.2 ε; reconstruction gives 0.8+0.2=1 ε. External transfer is not supplied, so no closed-system claim follows. A hypothetical T=1 ε would close the balance, but it remains a hypothetical value, not an observation.

## C16.06-P1 — Practice

Record A,B,C endpoints before=(3,1,2) ε and after=(2,1,1) ε. Compute every signed change and both totals. With p=−1.5 ε find and retain the residual. State what is missing for a transition rate.

Worked answer: changes are (2−3,1−1,1−2)=(−1,0,−1) ε. Totals are 6 and 4 ε, and their difference is −2 ε, matching −1+0−1. The residual is −2−(−1.5)=−0.5 ε. Reconstruct −1.5+(−0.5)=−2 ε. Retain endpoint labels and all three changes; the total alone cannot reconstruct them. No elapsed time, event definition, preparation, or dynamical rate rule is supplied. External transfer is also unspecified, so the balance remains open rather than silently assigning a transfer of −2 ε.

> Claim scope: S02 /proof_nodes/86 supplies the six-sector action architecture and explicitly leaves weights and boundary values as inputs. Our energy ledgers are synthetic additive exercises, not observations or a derivation of energy from that action. A photon-equivalent model energy would also need separate labeling; it is not automatically measured transferred energy. Phase is not a force in this ledger.

## Diagnostics and worked answers

1. **C16.06-D1:** Can the six action names be inserted as six measured energy rows? Answer: not without a defined energy mapping, units, and measurement evidence. The source list specifies architecture.
2. **C16.06-D2:** Someone retains only p=−1.5 ε in P1. What is lost? Answer: r=−0.5 ε and the true synthetic change −2 ε; the separate endpoint/component information is also needed for full replay.
3. **C16.06-D3:** If a separate supplied transfer T=−1.8 ε were added to P1, find b. Answer: b=−2−(−1.8)=−0.2 ε. Keep it distinct from model residual −0.5 ε because the reference quantities differ.
4. **C16.06-D4:** Does −2 ε specify a decay rate? Answer: no; its unit is energy and its sign describes an energy change. A transition rate needs time-based and dynamical information.

Next dependency: [Lesson 7](lesson-07.md) gathers structure, numerical inputs, units, and unresolved coordinates into one contract.
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# Lesson 7 — What a complete interaction specification needs

Essential question: How can a precise interaction contract show both what is determined and what remains open?

Goals: assemble a typed interaction record; distinguish source-defined inputs from outputs; identify possible constraining observations and their limits.

Bridge: lessons 1–6 supplied type checks, contractions, vacuum and mass calculations, coefficient maps, and reversible ledgers. One 55-minute period: 5 retrieval, 20 teaching/example, 15 practice, 15 diagnostics/repair.

## C16.07-E1 — Structure and occupied-state coordinates

A contract states enough about inputs and operations that another person can reproduce the same result. It also names blanks. “Unspecified” is more informative than a guessed value: it tells us which future input could change an output. A structural contract can be fully described even when the numerical physical state remains undetermined.

S02 M12 lists five occupied-state inputs: vacuum magnitude, Higgs-potential coefficients, Yukawa coefficient matrices, mixing coordinates, and matching scale. “Occupied-state” means values specifying the chosen state within the supplied architecture. The matching scale records the scale at which model parameter conventions are compared or matched; a value and unit must be declared when making a numerical physical comparison. We do not evolve coefficients between scales in this course.

Our computational ledger also needs g2 and gY, ordered bases, units and normalization, initial/boundary states, dual/conjugation rules, Ω, and any dynamical rule used for rates. A boundary state specifies conditions at the edge of the modeled region or process; an initial state specifies where evolution starts. These are needed even if the list of allowed interactions is already known.

| Contract layer | What to record | What it supports |
|---|---|---|
| Structure | C₃ ⊕ W₂ order; sector table; four source interface orders; dual rule; Ω | type, charge, and contraction tests |
| Numerical state | v, potential coefficients, Y_Yuk, mixing coordinates, couplings | declared numerical outputs where formulas are supplied |
| Conventions | mass/energy units, normalization, bases, matching scale | reproducible comparison |
| Evolution/accounting | initial/boundary conditions, time rule, transfers, component labels | evolution or balance only to supplied scope |
| Evidence | source pointers, synthetic labels, actual observations if supplied, residuals | separation of source statements and fresh checks |

Possible observations are proposals, not data. With an applicable model and conventions, masses may constrain combinations of v and couplings; the formulas alone leave tradeoffs (rescale v and inversely rescale both couplings, and the two masses stay fixed). Relative transition observations may constrain mixing and coefficient combinations when the interaction-to-observation rule is supplied. Potential-sensitive measurements may constrain potential coefficients under a specified potential model. Time-resolved event counts with preparation/exposure information can constrain rates when an evolution model is available. Matching scale and basis choices are recorded comparison metadata; an isolated mass value does not determine every input. Keep every observation and its residual against the chosen prediction.

## C16.07-W1 — A worked contract with honest blanks

Take the worked mass example g2=3, gY=4, v=2 μ, and the worked coefficient matrix [[1,2],[0,3]] with f=(2,−1). Record the color-first basis and Ω from lesson 1 and the four basis contraction tests from lesson 2. Derived mass outputs are (3,5) μ and rho=1. The dimensionless matrix output is (0,−3). At this contract's v=2 μ, M=√2 μ Y_Yuk and Mf=(0,−3√2) μ; the separate lesson-5 normalization example used v=√2 μ and must not silently replace this value.

Attach the energy endpoints (5,2,1)→(4,4,1) ε, p=0.8 ε, r=0.2 ε. Potential coefficients, physical matching scale, empirical mixing values, external transfer, elapsed time, and a dynamical rate rule are unspecified. The chosen basis is specified, but no physical mixing inference has been made. The source reports a typed architecture; our recomputation verifies this finite synthetic record. No empirical observation has been acquired.

## C16.07-P1 — Build the practice contract

Use g2=4, gY=3, v=2 μ; Y_Yuk=[[2,0],[1,1]], f=(1,2); swap P from lesson 5; and the practice energy ledger from lesson 6. Identify all recorded outputs and open inputs. Propose two measurement categories without pretending that either was performed. Read the source-scope card below, then write one sentence distinguishing its compiler authority and global-form status from our M12 finite replay.

Worked answer: retain the ordered basis, four interfaces, covector action, Ω, and charges. Record masses 4 and 5 μ, c²_theta=16/25 and rho=1; Y_Yuk f=(2,3); P=[[0,1],[1,0]], Y′=[[1,1],[0,2]], f′=(2,1), output′=(3,2). With v=2 μ, M=√2 μ Y_Yuk. Energy endpoints are (3,1,2)→(2,1,1) ε, changes (−1,0,−1) ε, totals 6→4 ε, prediction −1.5 ε, residual −0.5 ε. Potential coefficients, physical mixing coordinates, matching scale, physical preparation/boundary states and rate model remain unfilled. Possible mass and time-resolved transition measurements could constrain parameter combinations and rates under an explicit model; neither is present as data here.

> Claim scope: S02 /backbone_sequence/11 and /branch_proofs/7 report the architecture and its state-coordinate boundary. The integration's compiler labels M03/M07/M08 have direct-authority status in that separate namespace; that status does not attach automatically to mathematical-backbone M12. The integration admits global-form alternatives Z1,Z2,Z3,Z6 rather than a uniquely selected physical member. These are source-reading boundaries, not extra capstone calculations. We have not freshly typechecked a compiler certificate.

Source-scope practice answer: integration direct authority covers compiler M03/M07/M08 in a separate namespace, not automatically backbone M12, and its admitted global-form family Z1,Z2,Z3,Z6 does not select a unique physical member; our calculations freshly replay finite examples without executing that compiler.

## Diagnostics and worked answers

1. **C16.07-D1:** Is a precise structural contract a table of unique physical masses and rates? Answer: no; it names operations and open numerical inputs. Unfilled entries must remain visible.
2. **C16.07-D2:** Which five input categories come directly from M12? Answer: vacuum magnitude, Higgs-potential coefficients, Yukawa coefficient matrices, mixing coordinates, and matching scale.
3. **C16.07-D3:** Distinguish “rho=1 was recomputed” from “a rate was measured.” Answer: the former is a finite algebraic result from supplied formulas and nonzero inputs; the latter would require actual time-based observations, which this course does not supply.
4. **C16.07-D4:** Can two measured masses alone choose all five M12 inputs? Answer: no; even v and two couplings can trade off while maintaining these masses, and potential, Yukawa, and mixing information remains additional.

Next dependency: [Capstone](capstone.md) assembles and defends a complete synthetic interaction ledger using only these taught operations.
<!-- END: lesson-07 -->
