# Matter States, Hypercharge, and Anomaly Accounting

Seven lessons, fourteen core periods. See teacher-guide.md, terminology.md, sources.md and capstone.md for supporting materials.

<!-- BEGIN: lesson-01 -->
# Lesson 1 — Choosing states with combinations

Essential question: How can order change a sign without creating another basis state?

Goals: sort a product and retain its sign; identify repeated-label zero products; count subsets of a specified size.

Prerequisite bridge: You can multiply signed numbers and divide whole-number counts. Course 14 supplies the color-first carrier, but we restate everything needed: H has five independent labels in the order (c1,c2,c3,w1,w2). The c labels form a three-dimensional color block C3; the w labels form a two-dimensional weak block W2. Here dimension counts independent labels, not spatial directions.

Pacing: two 55-minute periods. Each uses 5 minutes retrieval, 20 explanation/example, 15 practice, 15 diagnostic/repair. First period: signs and subsets of three. Second: combinations and the five-label count.

## C15.01-E1 — A signed subset language

A subset records which labels are selected, each at most once. Its size is its degree. The empty subset has degree zero and one basis symbol, written 1. It is not the zero vector: 1 records selecting nothing, whereas 0 records a vanishing expression.

An exterior product, written ∧ and read “wedge,” is our rule for combining labels. Exchanging neighboring labels reverses the coefficient sign; any repeated label makes the product zero. Products distribute over addition and scalar coefficients multiply as usual. Thus c1∧c2 and −c2∧c1 describe the same expression. Our standard basis writes every selected subset in the fixed order above. A negative coefficient does not create a second basis direction, just as −x is not a second coordinate axis.

To sort a product, first check for repetition. Otherwise move out-of-order neighbors past each other and count the swaps. An even number gives sign +1; an odd number gives −1. Multiply this by any sign already present. Keep this information; deleting it changes the expression.

How many degree-two subsets of five labels exist? There are five choices for the first label and four for a different second label: 20 ordered choices. Each unordered pair appears twice, so there are 20/2=10 basis pairs. More generally, “n choose k,” written binom(n,k), counts k-element subsets of n labels. Count ordered selections n(n−1)…(n−k+1), then divide by k!, the number of ways to order k different labels. Here k! means k(k−1)…1, with 0!=1. We only need small cases. Choosing four of five is equivalent to choosing the one label to leave out, giving five possibilities.

## C15.01-W1 — Worked example

c2∧c1 needs one swap, so it is −c1∧c2. c1∧c1=0. On three labels x,y,z, the subsets are 1; x,y,z; x∧y,x∧z,y∧z; x∧y∧z. Counts by degree are 1,3,3,1. On five labels, even degrees are 0,2,4. Their counts are 1,10,5, totaling 16. All degrees together contain 2×2×2×2×2=32 subsets because each label is independently included or excluded.

## C15.01-P1 — Practice, then reveal the worked answers

Sort w1∧c1 and c3∧c1∧c2. List all pairs of (c1,c2,w1,w2). Evaluate c1∧w1∧c1.

Answers: w1∧c1=−c1∧w1. Move c3 past c1 and c2: two swaps give +c1∧c2∧c3. The six pairs are c1∧c2, c1∧w1, c1∧w2, c2∧w1, c2∧w2, w1∧w2. The repeated c1 makes the last expression zero regardless of the intervening w1.

## Diagnostic checks

1. **C15.01-D1:** Why does counting 20 ordered pairs overcount the degree-two basis?
2. Sort −w2∧c2. Does its final coefficient remain negative?
3. How many degree-four subsets exist? Explain without a factorial.
4. Does even exterior degree specify physical left-handed chirality?

Worked answers: (1) Each pair occurs in two orders; the order change is a coefficient sign, not a new basis. (2) One swap adds another minus sign, giving +c2∧w2. (3) Five: choose the omitted label. (4) No. It labels an internal subset degree; physical Lorentz chirality concerns a separate spacetime transformation property.

> Claim scope: These are algebraic definitions and finite consequences. The source selects the even exterior sector as a matter carrier; counting alone does not select a physical chirality. Source: S02 /backbone_sequence/10 and /proof_nodes/74/formula (KFM-F033); provenance in sources.md.

Next dependency: [Lesson 2](lesson-02.md) separates the sixteen subsets into color and weak counts.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 2 — The sixteen even exterior states

Essential question: How can a census prove that no state was missed or counted twice?

Goals: enumerate the six allowed bidegrees; calculate their multiplicities; list every degree-four state and track a block exchange sign.

Prerequisite bridge: Lesson 1 gave sorted signed subsets and binom(n,k). We now group those subsets without losing labels or signs.

Pacing: two 55-minute periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks/repair. Use period 1 for bidegrees and period 2 for explicit lists and block signs.

## C15.02-E1 — Two counts instead of one

The bidegree (r,s) records r selected color labels and s selected weak labels. Thus 0≤r≤3 and 0≤s≤2. The total exterior degree is r+s. Even requires r+s to be 0,2,or 4. To enumerate systematically, run through r=0,1,2,3 and retain s values with the same parity. No other allowed pair can have an even sum.

A multiplicity is the number of independent basis states in a group. For each choice of r colors, there are binom(2,s) choices of s weak labels. Choices are independent, so multiply: m=binom(3,r)binom(2,s). This multiplication counts pairs of choices.

The source calls a group with common transformation behavior a sector or multiplet. We attach its labels after counting. A superscript c in nu^c, e^c, u^c, d^c is part of the supplied left-Weyl naming convention; it is not a color basis label or an instruction to take a complement. Q and L are sector names. We teach transformation labels in Lesson 6.

## C15.02-W1 — Worked census

|Bidegree (r,s)|Choice calculation|Multiplicity m|Source sector|
|---|---|---:|---|
|(0,0)|1×1|1|nu^c|
|(0,2)|1×1|1|e^c|
|(1,1)|3×2|6|Q|
|(2,0)|3×1|3|u^c|
|(2,2)|3×1|3|d^c|
|(3,1)|1×2|2|L|

Sum: 1+1+6+3+3+2=16. Q has c1∧w1,c1∧w2,c2∧w1,c2∧w2,c3∧w1,c3∧w2. The degree-two groups contain 1+6+3=10, agreeing with Lesson 1. This second route independently checks the count.

Suppose someone writes the weak block before the color block. Passing s weak labels across r colors requires rs neighbor swaps, because each weak label passes every color. Therefore the sign is (−1)^(rs). For (1,1) it is −1; for (2,2) it is +1. Merely renaming a block order does not justify discarding this sign.

## C15.02-P1 — Practice and answers

List all degree-four states by the omitted label. Separate them into bidegrees. Reverse their color/weak blocks and record the signs. Also split the degree-two count into its three groups.

Omitting c1 gives c2∧c3∧w1∧w2; omitting c2 gives c1∧c3∧w1∧w2; omitting c3 gives c1∧c2∧w1∧w2. These are the three (2,2) states, whose block sign is (−1)^4=+1. Omitting w1 gives c1∧c2∧c3∧w2; omitting w2 gives c1∧c2∧c3∧w1. These are the two (3,1) states, whose block sign is (−1)^3=−1. Degree two has three color pairs, six mixed pairs and one weak pair. Together with the empty state, the totals are 1+10+5=16.

These lists use positive coefficients in canonical order. They are not oriented complement formulas; Lesson 6 adds those orientation signs.

## Diagnostic checks

1. **C15.02-D1:** Convert w2∧c3 into color-first order. Is the sign optional?
2. Why is (3,2) excluded even though both counts lie within their bounds?
3. Why does (2,0) have three states rather than six?
4. Does the full exterior algebra contain sixteen or thirty-two basis states?

Worked answers: (1) −c3∧w2, with a required minus sign. (2) Degree 5 is odd. (3) Each pair of colors is an unordered subset: 3×2/2=3. (4) Thirty-two; the source selects sixteen even states. The sixteen odd states remain a separately recorded complementary sector.

> Claim scope: This is finite mathematics for H=C3⊕W2, color first. Sector names follow S02 /backbone_sequence/10/sector_census. Exterior block factorization is KFM-X022 at /proof_nodes/67/formula. Names and dimension alone do not establish a physical realization.

Next dependency: [Lesson 3](lesson-03.md) assigns additive charges to the census.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 3 — Charge as an additive rule

Essential question: How can five basis weights determine every charge in a sixteen-state census?

Goals: compute q and Y from a bidegree; distinguish individual charge from weighted contribution; evaluate the supplied descent remainder test.

Prerequisite bridge: Lesson 2 supplies six bidegrees and their multiplicities. Signed multiplication and fractions now attach numbers to those states.

Pacing: two 55-minute periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks/repair. Period 1 assigns charges; period 2 teaches remainders and descent.

## C15.03-E1 — Add labels' weights

Assign the same weight a to each color label and b to each weak label. A central phase is a common rotation applied to all labels of a block. We need only its exponent rule: multiplying two phase factors adds their exponents. Consequently a wedge with r colors and s weak labels has total weight q=ar+bs. The empty product has q=0. These weights and all charges here are dimensionless; they are not measured electric charges in coulombs.

For the source's primitive convention set a=−2 and b=3. Lesson 5 will derive the allowed ratio and explain “primitive.” Define hypercharge Y=q/6. Y is the source hypercharge label, not electric charge. Each basis state in one bidegree has the same q, but a row with multiplicity m contains m distinct components. Its linear contribution is mq; its cubic contribution is m(q³). Cube each component's charge before adding. Cubing mq would introduce terms between components and answer another question.

The source also supplies a descent test: q+2t+3p must leave remainder zero on division by 6. Here triality t is the remainder of r upon division by 3 (0,1,2); weak parity p is the remainder of s upon division by 2 (0,1). “x=0 mod 6” means x is an integer multiple of 6, including zero and negative multiples. Descent means the representation can respect the source's stated identification of symmetry transformations. Evaluating this finite test does not require deriving that global symmetry construction.

## C15.03-W1 — Worked examples

Q has (r,s)=(1,1), so q=−2+3=1, Y=1/6, and m=3×2=6. With t=1,p=1, its descent integer is 1+2+3=6, remainder 0. The u^c row has (2,0), q=−4, Y=−4/6=−2/3,m=3. Its t=2,p=0 give −4+4=0. Its linear contribution is 3(−4)=−12; its cubic contribution is 3(−4)³=3(−64)=−192, not (−12)³.

## C15.03-P1 — Complete the other rows

Calculate m,q,Y,t,p and the descent integer for nu^c,e^c,d^c,L. Then use Lesson 2's explicit basis lists to assign those values to every component, keeping the row multiplicities visible.

|Sector|(r,s)|m|q|Y|t|p|q+2t+3p|remainder mod 6|
|---|---|---:|---:|---|---:|---:|---:|---:|
|nu^c|(0,0)|1|0|0|0|0|0|0|
|e^c|(0,2)|1|6|1|0|0|6|0|
|Q|(1,1)|6|1|1/6|1|1|6|0|
|u^c|(2,0)|3|−4|−2/3|2|0|0|0|
|d^c|(2,2)|3|2|1/3|2|0|6|0|
|L|(3,1)|2|−3|−1/2|0|1|0|0|

Worked route: d^c uses q=−2(2)+3(2)=2 and m=3×1=3; L uses q=−2(3)+3(1)=−3 and m=1×2=2. For e^c, s=2 has remainder zero, not two. For L, r=3 has triality zero. All three d^c components have q=2 individually; both L components have q=−3 individually.

## Diagnostic checks

1. **C15.03-D1:** For m=3,q=−4, give linear and cubic contributions and explain the order of operations.
2. For (3,1), why is t=0 rather than 3?
3. Change the synthetic weights to (a,b)=(1,0). What is Q's q and what is d^c's q?
4. Does reversing the coefficient sign of a wedge reverse its charge?

Worked answers: (1) −12 and −192; compute each component's power first, then multiply by m. (2) Dividing 3 by 3 leaves zero. (3) q=r, giving 1 and 2. (4) No. A coefficient sign changes the state expression's coefficient, not which basis labels determine the charge. Reversing all basis weights would reverse charges.

> Claim scope: The additive rule, primitive convention and congruence are source inputs replayed as arithmetic. Sources: S02 /backbone_sequence/10, KFM-F033 /proof_nodes/74/formula and KFM-X026 /proof_nodes/75/formula. Nonzero remainders in alternative trials must be retained, not silently repaired.

Next dependency: [Lesson 4](lesson-04.md) adds the components with several distinct test weights.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# Lesson 4 — Why anomaly sums are bookkeeping constraints

Essential question: What precisely has been checked when a weighted sum vanishes?

Goals: calculate five named sums with declared normalization; preserve sector contributions including failed trials; derive their general dependence on a,b.

Prerequisite bridge: Lesson 3 taught q=ar+bs and mq versus mq³. We now supply the weights for the source's local anomaly tests. An anomaly here names a potential symmetry-consistency obstruction in the reference field-theory interpretation. The core task is to evaluate its supplied finite coefficient, not derive quantum field theory.

Pacing: three 55-minute periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks/repair. Period 1: linear and cubic sums. Period 2: mixed and pure-color sums. Period 3: general polynomials and retained failing trials.

## C15.04-E1 — Five different ledgers

The source uses a left-Weyl inventory: all six rows are counted in one declared chirality convention, including the c-labelled sectors. SU3 names the color symmetry; SU2 names the weak symmetry; U1 names the phase/charge symmetry. The superscripts in test names identify which factors participate, not powers to apply to a group name.

For the gravity²–U1 test, sum mq. For U1³, sum mq³. These use all components. For SU3²–U1, the supplied quadratic index T is 1/2 for a color triplet 3 and its dual bar3, zero for a color singlet. Multiply T by q and the number of weak copies. Thus Q contributes 2q/2, u^c and d^c each q/2. Do not multiply by three again: T already describes the color representation. A spectator multiplicity counts copies from the other symmetry factor.

For SU2²–U1, each weak doublet has T=1/2. Q has three color copies and L one: contributions 3q/2 and q/2. The remaining rows are weak singlets and contribute zero. For pure SU3³, a 3 has coefficient +1 and a bar3 has −1, with weak spectator copies. Hence Q,u^c,d^c contribute +2,−1,−1. Notice that bar3 has the SAME quadratic index but the OPPOSITE cubic color coefficient. This distinction is essential.

## C15.04-W1 — Worked primitive ledger

The following uses q, not Y:

|Sector|mq|mq³|SU3²–U1|SU2²–U1|SU3³|
|---|---:|---:|---:|---:|---:|
|nu^c|0|0|0|0|0|
|e^c|6|216|0|0|0|
|Q|6|6|1|3/2|2|
|u^c|−12|−192|−2|0|−1|
|d^c|6|24|1|0|−1|
|L|−6|−54|0|−3/2|0|
|Sum|0|0|0|0|0|

For example, the cubic sum is 216+6−192+24−54=0. The mixed sums are (2×1−4+2)/2=0 and (3×1−3)/2=0. Switching consistently to Y=q/6 divides the linear and mixed sums by 6 and the U1 cubic sum by 216; the pure-color sum is unchanged. Zero remains zero, but nonzero trial coefficients must report their normalization.

## General calculation, with multiplication taught explicitly

In census order the six charges are 0,2b,a+b,2a,2a+2b,3a+b. Adding their multiplicity-weighted values gives 24a+16b=8(3a+2b). The first mixed sum is [2(a+b)+2a+(2a+2b)]/2=3a+2b; the second is [3(a+b)+(3a+b)]/2=3a+2b.

To expand a cube, distribute each factor in (x+y)(x+y)(x+y): the terms are x³, three x²y, three xy², and y³. Therefore (x+y)³=x³+3x²y+3xy²+y³. The cubic ledger is

8b³+6(a+b)³+24a³+24(a+b)³+2(3a+b)³.

The two (a+b) groups combine to 30(a+b)³. Their coefficients are (30,90,90,30), in the order (a³,a²b,ab²,b³). The final group contributes (54,54,18,2); the other two contribute (24,0,0,8). Adding columns gives 108a³+144a²b+108ab²+40b³. Lesson 5 factors this expression.

## C15.04-P1 — Two trials that must remain in the record

Recompute all five sums for synthetic choices (1,0) and (0,1). These are tests of the formula, not measured data or alternatives to be erased.

For (1,0), q=(0,0,1,2,2,3). Linear contributions are (0,0,6,6,6,6), totaling 24. Cubic contributions (0,0,6,24,24,54) total 108. SU3 mixed contributions (Q,u^c,d^c)=(1,1,1) total 3; SU2 contributions (Q,L)=(3/2,3/2) total 3. SU3³ remains 2−1−1=0.

For (0,1), q=(0,2,1,0,2,1). Linear contributions (0,2,6,0,6,2) total 16; cubic (0,8,6,0,24,2) total 40. SU3 mixed contributions (1,0,1) total 2; SU2 (3/2,1/2) total 2; SU3³ stays zero. Neither trial passes all five tests. Keeping the individual contributions lets us locate the obstruction rather than hiding it in a pass/fail label.

## Diagnostic checks

1. **C15.04-D1:** Derive the two general mixed sums and linear sum.
2. Why is Q's color mixed weight 2/2 rather than 6/2?
3. At (a,b)=(1,1), compute the cubic coefficient using the expanded polynomial.
4. Does SU3³=0 certify the remaining four tests? What happens to the (1,0) linear sum in Y units?

Worked answers: (1) Both mixed sums simplify to 3a+2b; the linear sum is 8 times that, as the expanded terms above show. (2) T=1/2 already incorporates the color representation; only its two weak copies multiply it. (3) 108+144+108+40=400. (4) No: (1,0) gives the counterexample retained in P1. Its linear Y sum is 24/6=4.

> Claim scope: These five source perturbative local coefficients are exactly checked for the declared inventory and normalization. They do not substitute for the separate Witten count or a proof for every non-liftable quotient-group bundle. Sources: S02 KFM-X023 /proof_nodes/68/formula and KFM-F035 /proof_nodes/82/formula. The reference-theory weights are supplied; the finite arithmetic is derived here.

Next dependency: [Lesson 5](lesson-05.md) solves the common cancellation condition.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 5 — The primitive hypercharge line

Essential question: Which part of the charge choice is forced by the equations, and which part is a convention?

Goals: factor the cubic and verify a completed square; solve 3a+2b=0 over integers; select a primitive generator and declare its sign.

Prerequisite bridge: Lesson 4 derived the cubic polynomial and two mixed sums. We use ordinary distribution, the fact that a real square is nonnegative, and divisibility of integers. No matrix positivity theorem is assumed.

Pacing: two 55-minute periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks/repair. First: factorization and positivity. Second: determinant connection, integer solutions and normalization.

## C15.05-E1 — A line of solutions

Factoring means writing an expression as a product that expands to the original. Verify by distribution that the cubic from Lesson 4 equals

(3a+2b)(36a²+24ab+20b²).

The products with 3a are 108a³+72a²b+60ab². The products with 2b are 72a²b+48ab²+40b³. Combining like powers gives exactly (108,144,108,40). No terms disappear.

Now “complete the square”: turn part of a quadratic into a squared expression plus a remainder. Since (a+b/3)²=a²+2ab/3+b²/9, multiplying by 36 gives 36a²+24ab+4b². Our quadratic has 20b², so the remainder is 16b²:

36a²+24ab+20b² = 36(a+b/3)²+16b².

For real a,b, both squares are nonnegative. If their sum is zero, the second term forces b=0 and the first then forces a=0. Thus for any nonzero pair the quadratic is positive. A product can vanish only if one factor is zero; the cubic therefore vanishes precisely on 3a+2b=0 for nonzero real pairs. The zero pair also satisfies the equation but supplies no nonzero charge generator. Mixed and linear tests already impose the same line. Pure SU3³ is zero independently of a,b for this inventory.

Why call this a determinant lock? The top exterior state Ω=c1∧c2∧c3∧w1∧w2 uses all five basis labels. Under a diagonal transformation its multiplier is the product of the five individual multipliers; this product is the diagonal determinant. If the color phase exponent is aθ and the weak exponent is bθ, the top product has exponent (3a+2b)θ. Requiring that top product to stay unchanged for every continuously varying θ requires 3a+2b=0. In this course that volume-preservation contract is declared, then its arithmetic is checked. It agrees with the anomaly line for this particular carrier; we have not classified arbitrary matter assignments.

## C15.05-W1 — Worked primitive solution

Solve 3a=−2b with integers a,b. Because 3 does not supply a factor of 2, a must be even. Write a=−2k; substitution yields b=3k. Conversely every integer k produces a solution. A nonzero pair is primitive when the greatest common divisor gcd(|a|,|b|) is 1: no common positive factor larger than one remains. Here gcd(2|k|,3|k|)=|k|, so k=+1 or −1. We declare color negative and weak positive, choosing (−2,3). This fixes the global sign and gives the basis weights (−2,−2,−2,3,3); Y=q/6 is the normalization already used.

## C15.05-P1 — Practice with worked answers

Classify (−4,6), (2,−3) and (1,1). Independently expand both the completed square and the factored cubic before checking the preceding derivation.

Answers: (−4,6) has 3a+2b=−12+12=0 but gcd=2, so divide both entries by 2 to get (−2,3). (2,−3) is primitive and lies on the line, but reverses the declared sign convention and all charges. At (1,1), the quadratic is 36+24+20=80, the linear factor 5, and the cubic 400, agreeing with Lesson 4. Expanding the square gives 36a²+24ab+4b²+16b². Expanding the product gives a³ coefficient 108, a²b coefficient 72+72=144, ab² coefficient 60+48=108 and b³ coefficient 40. These are the required independent multiplication checks.

## Diagnostic checks

1. **C15.05-D1:** Why is (0,0) excluded from primitive nonzero generators although it cancels every charge sum?
2. Give two further integer solutions and reduce them to a primitive pair.
3. Could the quadratic vanish at a nonzero real pair with b≠0?
4. Does the equation alone choose which block has positive charge? State the determinant-lock hypothesis.

Worked answers: (1) It generates no nonzero weights; primitive here requires a nonzero pair with gcd 1. (2) (−6,9) and (−8,12), dividing by 3 and 4 respectively, give (−2,3). (3) No: 16b² is then strictly positive. (4) No; the chosen sign is declared. The determinant argument preserves the five-label top product for every phase parameter θ, on this color-first carrier.

> Claim scope: Algebra and divisibility establish the line conditional on the stated inventory and weights. S02 KFM-X024 /proof_nodes/69/formula reports primitive central selection. No new physical sign selection or different matter-carrier classification is inferred here.

Next dependency: [Lesson 6](lesson-06.md) checks complement, dual action and the separate parity count.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 6 — Parity and representation checks

Essential question: Which different questions can be hidden by the word parity?

Goals: compute an oriented complement and its charge; verify a diagonal dual-color action; distinguish exterior degree, weak-doublet count and physical chirality.

Prerequisite bridge: Lessons 1–2 taught wedge signs and bidegrees; Lesson 5 fixed the top product Ω and zero total basis charge. We now use those exact operations to check what representation labels mean.

Pacing: two 55-minute periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks/repair. Period 1: complements and orientation. Period 2: diagonal action, representations and Witten count.

## C15.06-E1 — Complements retain orientation

The complement of a subset consists of the omitted labels. A bidegree (r,s) therefore maps to (3−r,2−s). Since the total number of labels is five, an even subset complements to an odd subset. Total charge is zero at (a,b)=(−2,3), so the omitted labels' charge is −q. This does not say that odd states have been added to the chosen sixteen-state inventory.

For signs, define the complement C of a positively ordered basis product α to be the signed ordered product of omitted labels such that α∧C(α)=Ω. Extend C linearly to coefficients. To find the sign, concatenate α with its sorted omitted labels and count the swaps to Ω. In five dimensions applying this signed rule twice multiplies by (−1)^(k(5−k)), where k is α's degree: it exchanges blocks of those two lengths. This exponent is always even (one of k and 5−k is even), so C² restores the original expression.

A representation specifies how transformations act on components, not just their number. In a label (3,2), the first entry is color, the second weak. A 1 is a singlet, unchanged by that factor; a 2 is the weak doublet; 3 is the color triplet; bar3 denotes the dual color action. The supplied inventory in census order is (1,1),(1,1),(3,2),(bar3,1),(bar3,1),(1,2).

Here is a concrete explanation of the dual label. Write Ω_C=c1∧c2∧c3. The wedges d1=c2∧c3, d2=−c1∧c3, d3=c1∧c2 obey cj∧di=0 for j≠i and ci∧di=Ω_C. Thus each di pairs with exactly one color label. A diagonal color action multiplies c1,c2,c3 by λ1,λ2,λ3 with product 1. Its action on di multiplies by the product of the other two λ's, equal to 1/λi. This inverse action explains duality. We verify the diagonal case; matching three dimensions alone would not verify this action.

For a hand-checkable phase example, i is a number with i²=−1, so i(−i)=1, 1/i=−i and 1/(−i)=i. The diagonal matrix diag(i,−i,1) simply multiplies c1 by i, c2 by −i and c3 by 1; no matrix multiplication algorithm is hidden here.

## C15.06-W1 — Worked complement and count

Take α=c1∧w1. Its omitted subset is c2,c3,w2. Concatenation c1,w1,c2,c3,w2 needs two swaps, so C(α)=+c2∧c3∧w2. Bidegree changes (1,1)→(2,1); charge changes 1→−2−2+3=−1. The complement is odd degree 3.

The source's Witten test counts weak doublets, not their individual components. Q contains three color copies of a two-component weak doublet. L adds one more doublet. Hence N=3+1=4, remainder 0 mod 2. Eight individual doublet components is a different count; six sectors is yet another count.

## C15.06-P1 — Practice and worked answers

Complement c1∧c2; check C twice. Under diag(i,−i,1), compute the multiplier of c1∧c3 and compare with the inverse c2 multiplier. Finally count weak doublets first in Q alone and then in the full census.

Answers: C(c1∧c2)=c3∧w1∧w2, charge 4 and bidegree (1,2). Concatenating c3,w1,w2,c1,c2 needs six swaps, so applying C again gives +c1∧c2. The multiplier of c1∧c3 is i×1=i, equal to 1/(−i)=i. The dual basis vector d2 has an initial minus sign; it retains that coefficient and receives the same multiplier i. Q alone supplies three doublets, an odd count. Restoring L gives four and remainder zero. Keep the incomplete Q-only trial labeled rather than treating it as the full model.

## Diagnostic checks

1. **C15.06-D1:** List the six representation labels in census order and explain what the bar changes.
2. Find the signed complement of c1∧w2 and its charge.
3. Does complement preserve the selected even sector?
4. Does four weak doublets prove physical chirality or all global anomaly conditions?

Worked answers: (1) (1,1),(1,1),(3,2),(bar3,1),(bar3,1),(1,2); the bar changes the action to the dual, not the dimension. (2) −c2∧c3∧w1, since concatenation requires three swaps. The omitted labels have q=−1; the coefficient minus sign does not alter q. (3) No: it exchanges even and odd sectors. (4) No. Exterior parity counts chosen labels; weak parity here counts doublet copies. Lorentz chirality is a separately specified spacetime property. Detector antipodal parity, A1 carry parity, projective coefficient signs, and family labels are other typed quantities, not substitutes for either count.

> Claim scope: Source KFM-X027 /proof_nodes/79/formula explicitly separates internal parity from Lorentz chirality; KFM-F036 /proof_nodes/83/formula supplies the four-doublet count. The diagonal check illustrates dual action; it is not a fresh proof of every group action. Full non-liftable quotient-bundle global anomaly verification remains separately scoped.

Next dependency: [Lesson 7](lesson-07.md) turns the checks into an appropriately scoped report.
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# Lesson 7 — From a finite census to a source claim

Essential question: How can a report preserve a strong mathematical result without changing what it establishes?

Goals: assemble a reproducible assumption-and-result report; classify finite calculations versus source interpretations; retain failed trials and unresolved scope explicitly.

Prerequisite bridge: Lessons 1–6 have supplied all operations. This lesson adds no new matter formula. It organizes the results so another person can reproduce the reasoning without guessing conventions.

Pacing: one 55-minute period: 5 retrieval, 20 explanation/example, 15 independent report practice, 15 diagnostic and repair.

## C15.07-E1 — Report the contract and the result together

A result is conditional on its inputs. Here those inputs are a five-label color-first carrier; exterior antisymmetry; selection of even degrees; common block weights a,b; the supplied left-Weyl representation inventory and index normalization; the top-form preservation condition; and a primitive sign convention. None is replaced by the statement “there are sixteen states.”

Use three kinds of checkable statement. A source fact says exactly what an archival record contains, with a path and pointer. A derived result follows from the declared inputs by displayed arithmetic. An interpretation attaches a physical meaning to that result. A proposed mechanism would explain why nature realizes those inputs; this course does not add one. There are no empirical measurement rows in this course. A comparison to reference theory identifies supplied Standard Model names and anomaly tests without promoting a calculation into a measurement.

The mature source calls its branch BR-06 a closed exact gauge-matter theorem under its own discharged premises. Preserve that source-local status. Our replay directly verifies the finite census and sums, not every upstream proof in that branch. The separately supplied accepted-integration record admits global-form possibilities Z1,Z2,Z3,Z6, rather than a uniquely selected physical member. These names designate possible global symmetry identifications; the task is to retain the distinction, not calculate their topology. Compiler direct authority is reported only for compiler M03,M07,M08. Those compiler numbers are a separate namespace from mathematical-backbone M11 used here. No compiler was freshly executed for this course.

## C15.07-W1 — Worked report card

|Input or claim|Evidence class|What the course establishes|
|---|---|---|
|H=C3⊕W2, color first; even exterior sector|Declared source construction|1+10+5=16, explicitly enumerated|
|q=−2r+3s, Y=q/6|Source convention with derived ratio|All six rows and all sixteen component assignments|
|Five local coefficients|Supplied reference-theory tests, fresh arithmetic|Zero in the stated q normalization; complete contributions retained|
|Complement and dual label|Derived subset map and diagonal action check|Even↔odd, q↔−q; inverse color multiplier example|
|Witten count|Source finite parity test, fresh arithmetic|3+1=4 doublets, even|
|One left-Weyl family including nu^c|Mature-source interpretation at its contract|Census matches supplied labels; internal degree does not select Lorentz chirality|
|Unique physical global form; arbitrary quotient bundles|Unresolved integration/global scope|Not settled by these finite tests|

Keep the synthetic trial (a,b)=(1,0) alongside the successful line: linear 24, cubic 108, both mixed 3, pure color 0. Its residual vector from the all-zero target is (24,108,3,3,0) in that named order. This vector preserves which equations fail. It is not discarded as an unhelpful example. The trial's full row contributions are in Lesson 4, so the sums are reversible to the retained ledger rather than standing alone.

## C15.07-P1 — Audit a short claim

A draft says: “We found sixteen states and zero linear charge. Therefore the physical family, chirality and unique global symmetry are established.” Identify the missing work and write a replacement.

Worked answer: The count omits explicit bidegrees and multiplicities; the one sum omits cubic, both mixed and pure-color ledgers. It also lacks descent residues, the representation-action check, Witten count, assumptions, and scope. A replacement is: “For the declared color-first even exterior carrier, the six bidegrees have multiplicities (1,1,6,3,3,2) and primitive q values (0,6,1,−4,2,−3). The five named local coefficients vanish using the stated indices; all descent residues are zero and there are four weak doublets. The complement and diagonal dual-action examples are verified. This reproduces the source's finite one-family census. Physical chirality and the integration's unresolved global-form selection remain separately typed.” Attach Lesson 4's ledgers, Lesson 3's table, and the retained (1,0) trial. This supplies the evidence the short claim omitted.

## Diagnostic checks

1. **C15.07-D1:** Why is the number sixteen insufficient to establish physical family count or chirality?
2. Which statement is freshly verified: the arithmetic 3+1=4, or every upstream theorem of BR-06?
3. What two records must remain separate when discussing global symmetry?
4. A report deletes the (0,1) trial because it fails. What must be restored?

Worked answers: (1) The number is a dimension within a selected internal carrier; it supplies neither a physical occupation rule nor a spacetime chirality assignment. (2) The finite arithmetic; the upstream branch retains its reported source status. (3) Mature source-local theorem contracts and accepted-integration dispositions, including the Z1,Z2,Z3,Z6 family and unresolved physical selection. (4) Its input, row contributions, normalization and output vector (16,40,2,2,0), all available in Lesson 4; failed coefficients carry information about the constraint.

> Claim scope: Primary source S02 /backbone_sequence/10 and /branch_proofs/6. Integration provenance and retrieval limitations are in sources.md. This is a finite mathematical course, not an empirical report or a fresh compiler certificate.

Next dependency: [Capstone](capstone.md) assembles and independently checks the full ledger using only these taught operations.
<!-- END: lesson-07 -->
