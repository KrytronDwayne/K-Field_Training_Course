# Lesson 05 — Determinant-line bookkeeping

**Essential question:** How can a coefficient change while the represented object and its scalar reading stay the same?

**Goals:** Distinguish a line element from its coefficient; apply a one-factor basis change; recover the same scalar using the retained trivialization.

**Prerequisite bridge.** Lesson 04 declared six bases and τ. A familiar number-and-unit expression such as “2 units” separates the amount from the chosen unit. We now use a similar separation for a one-dimensional complex line. This is two periods: first learn one line and the tensor basis, then practice rebasing and scope checks.

## C19.05-E1 — From one line to a tensor product

A complex line is a space in which each element can be written z e, where e is a chosen nonzero basis element and z is a complex coefficient. “One-dimensional” means one such basis element suffices; it does not mean only real coefficients are allowed. Let s=z e. Choose another basis e'=a e, with a≠0. To keep s unchanged, its new coefficient must be z'=z/a, since (z/a)(a e)=z e. This is a change of description, not a change of s.

To combine six lines we use a tensor product, written ⊗. At the level needed here, take the ordered composite basis

E=e_UV⊗e_light⊗e_reg⊗e_heavy⊗e_cap⊗e_induced.

Its rule is that coefficients multiply: (z_1 e_1)⊗...⊗(z_6 e_6)=(z_1...z_6)E. Thus S_total=Z E, where Z is the product of six coefficients. S_total here denotes a combined line element, not the action S from Lessons 01–02. In the source the objects s_label are sections: assignments of line elements over their domain. Our calculation concerns a single specified point/packet, not a whole varying family.

A trivialization τ turns a line element into an ordinary complex number consistently and linearly. Linearity means that τ preserves addition and scalar multiplication: τ(s+t)=τ(s)+τ(t) and τ(zE)=z τ(E). The second rule is the one used in our rebasing calculations. Declare τ(E)=1 initially. The scalar reading is Φ=τ(S_total)=Z τ(E). After rebasing, **the same map τ** may give a different number on the new basis. Forgetting this is the error we will test.

The source calls these determinant lines. Recognition only: for a finite square transformation, its determinant records its signed volume scaling; a determinant line packages the associated top-degree volume coordinate into a one-dimensional space. This motivates line bookkeeping but does not construct the source's determinant lines or their global sections. No determinant computation or exterior-algebra proof is required here.

## C19.05-W1 — Change the UV basis

Start with W1 of Lesson 04: coefficients (i,i,−1,−i,i,1), Z=1, τ(E)=1, Φ=1. Set e'_UV=i e_UV and leave other bases unchanged. The UV coefficient becomes i/i=1, and E'=iE. The new coefficient list is (1,i,−1,−i,i,1), whose product is Z'=−i. Directly, Z'=Z/i=−i. Meanwhile τ(E')=τ(iE)=iτ(E)=i. Therefore Φ'=Z'τ(E')=(−i)i=1. Also S_total=Z'E'=(−i)(iE)=E, so the element itself is unchanged.

This calculation retains three layers: six local coefficients, the combined tensor-basis coefficient, and the scalar reading under τ. Reporting only Z'=−i would falsely suggest that the physical scalar in the toy had changed.

## C19.05-P1 — Guided practice

Use Lesson 04's practice list (−1,i,i,1,−i,i). Rebase e'_cap=−e_cap. Compute the cap coefficient, combined coefficient, τ(E'), scalar and inverse reconstruction.

**Worked answer:** The cap coefficient becomes (−i)/(−1)=i. Thus the new list is (−1,i,i,1,i,i), with product −1. E'=−E and τ(E')=−1. The scalar is (−1)(−1)=1. To reconstruct the old cap coefficient multiply i by −1, obtaining −i; the old basis is −e'_cap. Keep both lists, the multiplier −1 and τ values, so the change is reversible.

> **Claim scope.** S02 `/backbone_sequence/14/determinant_line` supplies the six-factor architecture and the need for τ. Our finite line rules are declared and checked directly. The source's global existence question cannot be settled by choosing a basis in one example. The source's time parameter τ in its action is a different object; here τ is a map, never a duration.

## Diagnostics

1. **C19.05-D1:** Why is multiplying six coefficients alone insufficient after changing bases?
2. If s=2e and e'=−e, what is the new coefficient? Reconstruct s.
3. In W1, what wrong answer results from keeping τ(E')=1?
4. Does a local basis change require changing the represented section value?
5. Which record would permit an auditor to reverse P1?

**Worked answers:** (1) The scalar is Z'τ(E'), so the basis reading must be retained. (2) −2, because (−2)(−e)=2e. (3) −i, whereas the correct invariant scalar is 1. (4) No, coefficients compensate for the basis change; a genuine change in the section would be additional input. (5) Original and new coefficient lists, cap's basis multiplier −1, the ordered tensor basis and τ(E)=1, τ(E')=−1. A final scalar 1 alone loses this information.

**Next dependency:** [Lesson 06](lesson-06.md) applies complete phase ledgers to specified sectors.
