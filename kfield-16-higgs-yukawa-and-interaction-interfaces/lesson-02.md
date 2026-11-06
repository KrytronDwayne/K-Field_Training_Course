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
