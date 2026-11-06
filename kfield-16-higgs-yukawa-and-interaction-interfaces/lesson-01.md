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
