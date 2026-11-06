# Lesson 03 — Isometry versus reversible evolution

**Essential question:** Can a map preserve every input length while missing possible outputs?

**Goals:** Compute a squared norm; test injectivity and surjectivity on concrete maps; reconstruct a codomain vector from image and complement.

**Bridge:** Lesson 02 distinguished S from T. It already supplied their adjoints. We now turn the squared-entry calculations into definitions and test precisely what a one-sided inverse guarantees.

**Pacing:** 55 minutes: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

## C18.03-E1 — Length, reach and reversibility

For a real vector v=(x,y,z), its squared norm is ||v||²=x²+y²+z²; its norm is the nonnegative square root. Using the square avoids unnecessary square-root arithmetic. The dot product of two vectors is the sum of matching products. For complex numbers, introduced in Lesson 07, squares in the norm become squared magnitudes. Every present example uses real dimensionless coefficients.

An isometry preserves the norm of every input. Our linear T is an isometry because ||T(a,b)||²=0²+a²+b²=a²+b². This checks all inputs, not just one lucky vector. A linear isometry is injective: two distinct inputs cannot have the same output, since their nonzero difference would then have output norm zero.

Surjective means onto the stated codomain: every vector there is reached. The image is the set actually reached. A two-sided inverse must undo the map on every input **and** every vector in its codomain. A left inverse alone undoes inputs; it does not guarantee that every codomain vector is reachable. Always write the domain and codomain before using “reversible.”

## C18.03-W1 — A missing direction despite preserved length

Let T:R²→R³ be T(a,b)=(0,a,b). R² and R³ mean real two- and three-coordinate spaces. T†(0,2,3)=(2,3), and T†T(a,b)=(a,b). But no a,b satisfy T(a,b)=(1,0,0): the first output coordinate is always zero. Thus T is an isometric injection, not onto R³. It is a bijection, meaning injective and onto, from R² to its image {(0,a,b)}.

For any v=(c,a,b), TT†v=(0,a,b). Subtracting gives (I_3−TT†)v=(c,0,0). Adding the two gives v exactly. The two components are orthogonal because their nonzero entries occupy disjoint slots. Their squared norms add: a²+b²+c². We retain the complement even when c=0.

The square shift S is not an isometry: S(0,0,1)=0 changes squared norm 1 to 0. If we store both Sf and the terminal component, we can reconstruct f, but the augmented record is a different operation from S alone.

## C18.03-P1 — Reconstruction practice

Use v=(5,2,3). Find T†v, TT†v, its complement and the squared norms. Then contrast S(0,0,1).

**Worked answer:** T†v=(2,3), TT†v=(0,2,3), complement (5,0,0). The original squared norm is 25+4+9=38; the two stored pieces contribute 13+25=38. Their sum is (5,2,3). S sends the terminal unit vector to zero, losing squared norm 1 unless its terminal coefficient is separately retained.

> **Claim scope:** These are fresh finite algebra checks. S02 M14 reports W†W=I and WW†≠I, the abstract pattern of an isometry that is not onto. A physical time evolution would require a specified state space, time parameter and dynamical rule; this pattern alone does not supply them. Information in an omitted component remains part of our record.

## Diagnostic checks

1. **C18.03-D1:** Does T†T=I_2 prove reversibility on all of R³? Give a counterexample output.
2. For T(−3,4), calculate input and output squared norm and recover the input.
3. Split (−2,0,6) into image and complement and reconstruct it.
4. A student says S preserves length because it preserves the length of e_0. Correct the quantifier.

**Worked answers:** (1) No; e_0=(1,0,0) is outside the image. The inverse works on the image only. (2) Input norm squared 9+16=25, output (0,−3,4) also 25; T† returns (−3,4). (3) Image (0,0,6), complement (−2,0,0); addition restores (−2,0,6), squared norms 36+4=40. (4) An isometry must preserve every input norm. e_2 is an explicit failure for S.

**Next dependency:** [Lesson 04](lesson-04.md) studies the projectors that separate a record into recoverable pieces.
