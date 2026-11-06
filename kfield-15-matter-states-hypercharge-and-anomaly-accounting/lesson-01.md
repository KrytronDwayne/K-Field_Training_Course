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
