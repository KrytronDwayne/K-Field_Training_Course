# Capstone — A reproducible sixteen-state census

Allow three 55-minute periods: 10 minutes planning, 100 construction/calculation, 35 independent cross-checking, 20 explanation and repair. Work from the declared rules; the answer key follows the tasks. No new theory is required. All charges are dimensionless and all anomaly ledgers use q=6Y unless explicitly converted.

## Student task

Use the ordered basis (c1,c2,c3,w1,w2), the even exterior carrier, the source left-Weyl inventory and the index rules taught in Lesson 4.

1. **C15-CAP-01 (10 points):** Sort w1∧c1 and c3∧c1∧c2, evaluate c1∧w1∧c1, and derive the even-state count. Inputs: three products and five labels. Output: signed canonical products and degree counts. Preparation: C15.01-E1, W1, P1, D1 in Lesson 1.
2. **C15-CAP-02 (15 points):** Enumerate all allowed bidegrees with multiplicities. List the five degree-four products and give the sign from exchanging each product's color and weak blocks. Inputs: r bounds 0–3 and s bounds 0–2. Output: exhaustive six-row census plus five explicit products. Preparation: C15.02-E1, W1, P1, D1.
3. **C15-CAP-03 (15 points):** For every one of the sixteen basis products, give q,Y and the residue of q+2t+3p modulo 6 at a=−2,b=3. Give the six-row grouped table too. Inputs: products from steps 1–2. Output: sixteen assignments with multiplicity cross-check. Preparation: C15.03-E1, W1, P1, D1.
4. **C15-CAP-04 (20 points):** Produce sector contributions and totals for the five named local tests. Replay (a,b)=(1,0), retaining all nonzero contributions. Explain conversion from q to Y normalization. Inputs: census and declared quadratic/cubic indices. Output: two ledgers and their residual vectors in a named order. Preparation: C15.04-E1, W1, P1, D1.
5. **C15-CAP-05 (15 points):** Expand and factor the general cubic; complete its quadratic factor's square; solve the primitive integer line and state the sign and determinant contracts. Inputs: general six charges ar+bs. Output: verified polynomial identity and primitive pair. Preparation: C15.05-E1, W1, P1, D1, with cube expansion taught in Lesson 4.
6. **C15-CAP-06 (15 points):** Find the signed complement of c1∧w1, check its charge and double complement; verify the dual-color multiplier of c1∧c3 under diag(i,−i,1); list the six representation labels and count Witten doublets. Inputs: ordered top form and full census. Output: signed examples, inverse-action comparison and parity count with its scope. Preparation: C15.06-E1, W1, P1, D1.
7. **C15-CAP-07 (10 points):** Write an assumption/evidence table and a source-scoped conclusion. Retain the failing trial and distinguish finite results, source interpretation, compiler authority and global-form scope. Inputs: prior six outputs and sources.md. Output: reproducible report with boundaries. Preparation: C15.07-E1, W1, P1, D1.

## Full worked answer key

### Step 1

w1∧c1=−c1∧w1 (one swap). c3∧c1∧c2=+c1∧c2∧c3 (two swaps). c1∧w1∧c1=0 (repetition). The even counts are binom(5,0)=1, binom(5,2)=5×4/2=10, binom(5,4)=5; sum 16. The full exterior count is 32, so choosing the even carrier is an explicit selection.

### Step 2

The allowed pairs and m=binom(3,r)binom(2,s) are (0,0):1; (0,2):1; (1,1):6; (2,0):3; (2,2):3; (3,1):2. These sum to 16 and exhaust r,s with r+s even. Degree-four products are c2∧c3∧w1∧w2, c1∧c3∧w1∧w2, c1∧c2∧w1∧w2, c1∧c2∧c3∧w2, c1∧c2∧c3∧w1. The first three exchange blocks with sign (−1)^4=+1; the last two with sign (−1)^3=−1.

### Step 3

Each row below is one basis product; coefficient signs from reordering are retained separately and do not change its charge.

|Basis product|Sector|q|Y|descent integer|residue mod 6|
|---|---|---:|---|---:|---:|
|1|nu^c|0|0|0|0|
|w1∧w2|e^c|6|1|6|0|
|c1∧w1|Q|1|1/6|6|0|
|c1∧w2|Q|1|1/6|6|0|
|c2∧w1|Q|1|1/6|6|0|
|c2∧w2|Q|1|1/6|6|0|
|c3∧w1|Q|1|1/6|6|0|
|c3∧w2|Q|1|1/6|6|0|
|c1∧c2|u^c|−4|−2/3|0|0|
|c1∧c3|u^c|−4|−2/3|0|0|
|c2∧c3|u^c|−4|−2/3|0|0|
|c1∧c2∧w1∧w2|d^c|2|1/3|6|0|
|c1∧c3∧w1∧w2|d^c|2|1/3|6|0|
|c2∧c3∧w1∧w2|d^c|2|1/3|6|0|
|c1∧c2∧c3∧w1|L|−3|−1/2|0|0|
|c1∧c2∧c3∧w2|L|−3|−1/2|0|0|

The grouped table, in order nu^c,e^c,Q,u^c,d^c,L, has bidegrees (0,0),(0,2),(1,1),(2,0),(2,2),(3,1), multiplicities (1,1,6,3,3,2), charges (0,6,1,−4,2,−3), trialities (0,0,1,2,2,0) and weak parities (0,0,1,0,0,1). Divide each charge by 6 to obtain the listed Y. Substitution gives descent integers (0,6,6,0,6,0), all with zero remainder.

### Step 4

|Sector|linear mq|cubic mq³|color mixed|weak mixed|pure color|
|---|---:|---:|---:|---:|---:|
|nu^c|0|0|0|0|0|
|e^c|6|216|0|0|0|
|Q|6|6|1|3/2|2|
|u^c|−12|−192|−2|0|−1|
|d^c|6|24|1|0|−1|
|L|−6|−54|0|−3/2|0|
|Total|0|0|0|0|0|

Names in column order: gravity²–U1, U1³, SU3²–U1, SU2²–U1, SU3³. T(3)=T(bar3)=T(2)=1/2, with spectator copies only; pure-color coefficients +1 for 3 and −1 for bar3. For example Q's mixed contributions are 2(1)(1/2)=1 and 3(1)(1/2)=3/2.

At (1,0), the charge list is (0,0,1,2,2,3):

|Sector|mq|mq³|color mixed|weak mixed|pure color|
|---|---:|---:|---:|---:|---:|
|nu^c|0|0|0|0|0|
|e^c|0|0|0|0|0|
|Q|6|6|1|3/2|2|
|u^c|6|24|1|0|−1|
|d^c|6|24|1|0|−1|
|L|6|54|0|3/2|0|
|Total|24|108|3|3|0|

The residual vectors from the all-zero target are (0,0,0,0,0) and (24,108,3,3,0), with full rows retained. In Y normalization divide linear/mixed by 6 and cubic by 216: the second vector becomes (4,1/2,1/2,1/2,0). Changing normalization does not erase the failures.

### Step 5

General charges are 0,2b,a+b,2a,2a+2b,3a+b. The weighted cubic is 8b³+30(a+b)³+24a³+2(3a+b)³, whose expansion is 108a³+144a²b+108ab²+40b³. Multiplying (3a+2b)(36a²+24ab+20b²) gives a²b coefficient 72+72 and ab² coefficient 60+48, reproducing the expansion. The quadratic is 36(a+b/3)²+16b², positive for nonzero real (a,b), so cancellation forces 3a+2b=0. Both mixed sums equal that linear factor; the linear anomaly is eight times it.

Integer solutions are (a,b)=(−2k,3k). Nonzero primitive solutions have |k|=1. Color negative and weak positive selects (−2,3); the opposite pair is the other convention. The zero pair is not a primitive generator. The determinant lock preserves Ω for every central phase parameter: its exponent is (3a+2b)θ. This is a stated top-form preservation contract, not a claim about every possible carrier.

### Step 6

C(c1∧w1)=c2∧c3∧w2: two swaps give positive orientation. Bidegree becomes (2,1), odd degree 3, and charge is −4+3=−1. C twice gives the original because exchanging blocks of lengths 2 and 3 produces six swaps. Under diag(i,−i,1), c1∧c3 multiplies by i; the inverse c2 multiplier is 1/(−i)=i. The oriented dual vector −c1∧c3 retains its initial minus coefficient. This checks the diagonal dual action, not merely a dimension match.

Representation labels in census order are (1,1),(1,1),(3,2),(bar3,1),(bar3,1),(1,2). Weak doublets count as three Q copies plus one L copy, N=4, residue zero mod 2. This is separate from exterior parity, physical Lorentz chirality, detector parity and carry parity. It does not settle every global quotient-bundle anomaly.

### Step 7

A full-credit table identifies the input carrier/order, antisymmetry, even-sector selection, common weights, left-Weyl inventory, T normalization, determinant contract and primitive sign convention. Derived rows identify explicit subset counts, charges/descent, five ledgers, complement sign, diagonal action and four-doublet parity. A source row cites S02 /backbone_sequence/10 and /branch_proofs/6 with its hash in sources.md. An integration row retains Z1,Z2,Z3,Z6 and the unresolved physical member; another distinguishes compiler M03,M07,M08 authority from backbone M11. No fresh compiler execution or empirical observation is claimed. Retain the full (1,0) trial rather than deleting its nonzero residuals.

A suitable conclusion: “The supplied carrier and conventions yield the sixteen internal components and source one-family charge labels. The displayed finite local sums and parity/descent tests pass. The mature source's wider theorem status remains source-scoped; physical chirality selection and the integration's global-form/global-bundle questions are not replaced by this census.”

## Rubric and repair

Award step 1: signs/repetition 6, count 4. Step 2: bidegrees/multiplicities 8, explicit degree-four list 5, block signs 2. Step 3: charges/Y 8, residues 4, all sixteen components and grouping 3. Step 4: correct weights 5, primitive ledger 5, retained trial ledger 7, normalization 3. Step 5: expansion/factor 5, square/positivity 4, integers/sign 4, determinant hypothesis 2. Step 6: complement/orientation 5, dual action 4, representations/count 4, boundaries 2. Step 7: assumptions/provenance 4, evidence distinctions 4, residual retention 2. Total 100.

Give method credit when one arithmetic slip propagates consistently, but require correction before declaring the construction verified. Any omitted sector, doubled index weight, discarded sign, or physical/global claim unsupported by the contract requires targeted repair regardless of total score. Repair using the mapped lesson practice, then recompute the affected capstone rows; do not change the original trial inputs to force a pass.
