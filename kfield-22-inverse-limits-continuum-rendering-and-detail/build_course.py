from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent
packet=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(name,text):
    (ROOT/name).write_text(text.strip()+'\n',encoding='utf-8')
def dump(name,obj):
    write(name,json.dumps(obj,indent=2,ensure_ascii=False))
def digest(name): return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
lessons={}
lessons[1]=r'''
# Lesson 01 — Finite prefixes and compatible sequences

Essential question: How can several short addresses describe the beginning of one history?

Goals: Compute a residue from signed digits; test every adjacent reduction; preserve an incompatible proposal with its failure record.

Bridge and pacing: You need signed arithmetic, powers and division with remainder. Courses 06, 07 and 18 provide the wider series context; all address operations needed here are rebuilt below. One 55-minute period: retrieval 5, explanation/example 20, practice 15, diagnostics/repair 15 minutes.

## C22.01-E1 — A remainder is an address

For a positive integer m, two integers represent the same residue modulo m when their difference is a multiple of m. We store the representative between 0 and m−1. Thus −2 and 7 represent the same residue modulo 9: adding one copy of 9 to −2 gives 7. The expression “a mod m” means this stored remainder, not an approximate decimal.

At depth d we use m=3^d. Increasing d adds one base-three digit. Our balanced digits are −1, 0, 1 and are stored **least significant first**: u₁ contributes units, u₂ contributes threes, u₃ contributes nines. To convert a prefix, form t_d=u₁+3u₂+…+3^(d−1)u_d and then a_d=t_d mod 3^d. The signed t_d and the nonnegative a_d are two representations, not two different histories. Preserve both when calculating.

The reduction map π_d takes a depth-(d+1) residue and reduces it modulo 3^d. A sequence is compatible when π_d(a_(d+1))=a_d at every step. Why does adding a digit work? Its contribution is a multiple of 3^d, so it changes nothing modulo 3^d. Compatibility checks consistency across resolution levels; it does not require the displayed integers to increase.

The source uses three coordinates. A_d=(Z/3^d Z)^3 means ordered triples of residues; Z here denotes integers, and the exponent 3 means three entries. Reduce each coordinate separately. An example using one coordinate can be embedded as (a_d,0,0); the two zeros remain part of the record. Addresses and digits are dimensionless.

## C22.01-W1 — Worked history

Use digits (1,−1,0,1,−1). Read each row as one more digit, not as a reversal of the previous row.

|d|3^d|signed sum t_d|stored a_d|
|---|---|---|---|
|1|3|1|1|
|2|9|1−3=−2|7|
|3|27|−2+0=−2|25|
|4|81|−2+27=25|25|
|5|243|25−81=−56|187|

Now reduce: 7 mod3=1; 25 mod9=7; 25 mod27=25; 187 mod81=25. Every adjacent test passes. The triple history is (1,0,0), (7,0,0), (25,0,0), (25,0,0), (187,0,0). The unchanged integer 25 at two depths carries different depth labels.

> Claim scope: S02, /backbone_sequence/17/definitions and /backbone_sequence/2/recursions/ternary_address supply the residue system. This small digit example is synthetic, verified arithmetic. It is not a measured trajectory. Five rows leave all later digits unresolved.

## C22.01-P1 — Practice, then check

Convert digits (0,1,−1,0,1) at depths 1–5. Test every reduction. Separately test the proposed depth-1/depth-2 list (1,8).

Answer: signed sums are 0,3,−6,−6,75; residues are 0,3,21,75,75. Reductions give 3 mod3=0, 21 mod9=3, 75 mod27=21, 75 mod81=75. The proposal (1,8) fails because 8 mod3=2, not 1. Save the original proposal and failed equation; do not silently replace 8.

## Diagnostics — C22.01-D1

1. Are −2 and 7 different depth-2 addresses?
2. Must a compatible residue list increase as ordinary integers?
3. Does a five-digit prefix specify the sixth digit?
4. Is the triple transition (1,0,2) → (7,3,5), at moduli 3 and 9, compatible?

Worked answers: (1) No: their difference is 9. (2) No: (2,2) is compatible, and (2,2,2,2,2) can continue; increase is not the test. (3) No: each of −1,0,1 remains possible. (4) Yes: reducing 7,3,5 modulo3 gives 1,0,2, respectively. No coordinate may be skipped.

Next dependency: [Lesson 02](lesson-02.md) uses shared reductions to define address closeness.
'''
lessons[2]=r'''
# Lesson 02 — A different meaning of closeness

Essential question: Can two addresses be close while their integer representatives are far apart?

Goals: Compute two explicitly named distances; compare triple address distances; distinguish an exact shared prefix from incomplete knowledge.

Bridge and pacing: Lesson 01 taught remainders and reduction. A shared depth-k residue means the first k low-order digits agree. One 55-minute period: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15 minutes.

## C22.02-E1 — What does the distance measure?

Ordinary real distance between integers a and b is |a−b|. Absolute value removes the sign of the difference, so both |−9| and |9| equal 9. This measures separation on a number line.

Address distance measures a different feature. If two distinct complete addresses share exactly k low-order balanced digits before they differ, define δ=3^(−k)=1/3^k. If they are identical at every depth, define δ=0. With no shared digit k=0 and δ=1. More shared digits make δ smaller. For ordinary integers, divide their nonzero difference by 3 repeatedly until it is no longer divisible by 3. The number of successful divisions is k: equality modulo 3^k is exactly divisibility of the difference by 3^k. Integers here specify complete compatible histories through all of their residues.

For triples take the **maximum** of the three coordinate address distances. A triple agrees to depth k only if every coordinate does. For a finite pair of records agreeing through depth N, you can only say δ≤3^(−N) for their possible infinite extensions; equality requires the next digit to differ. Do not assume a missing tail is zero.

## C22.02-W1 — Worked comparison

Integers 1 and 28 differ by 27. Divide 27 by 3 to get 9, then 3, then 1: three divisions. They agree modulo3, modulo9 and modulo27, but not modulo81. Their address distance is 1/27 while their real distance is 27. By contrast, 1 and 2 differ by 1, which has no factor of 3: δ=1 and real distance=1. Thus the pair with the larger number-line separation has the smaller address distance.

> Claim scope: This distance is a mathematical definition for the ternary histories of S02 M18. No experimental metric or physical length is being inferred. Later, the real renderer will give another real-valued representation, distinct from the integer number line used here.

## C22.02-P1 — Practice, then check

Compare 4 and 13 in both distances. Then find the address distance between (1,4,0) and (28,13,0).

Answer: 13−4=9=3², so k=2, δ=1/9, real distance=9. The triple coordinate address distances are 1/27,1/9,0; their maximum is 1/9. The zero coordinate is retained and contributes distance zero.

## Diagnostics — C22.02-D1

1. Find both distances for 0 and 81.
2. Two finite histories agree through depth 3, with no tail rule. Is their distance exactly 1/27?
3. What is the address distance between a complete history and itself?
4. Histories begin (1,−1,−1,…) and (0,1,1,…), with every displayed tail continuing constantly. Do they share their first residue?

Worked answers: (1) Real distance 81; address distance 1/81, since 81=3⁴. (2) Only the bound δ≤1/27 is known. They might agree farther or forever. (3) Zero by definition; no finite first-difference depth exists. (4) No, their first residues are 1 and 0, so δ=1. Lesson 04 will calculate that these distinct histories render the same real coordinate. A renderer cannot be assumed to recover every history.

Next dependency: [Lesson 03](lesson-03.md) constructs complete histories from compatible finite levels.
'''
lessons[3]=r'''
# Lesson 03 — The ternary inverse limit

Essential question: What makes infinitely many finite addresses one object?

Goals: Construct a compatible infinite rule; distinguish a prefix from a complete point; enumerate next-level choices in three coordinates.

Bridge and pacing: Lessons 01–02 supplied residues, reductions and prefix closeness. Two 55-minute periods: each uses retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15. Period 1 builds scalar rules; period 2 combines triples and studies unresolved continuation.

## C22.03-E1 — Keep the entire ladder

At depth d there are 3^d choices for one residue. For three coordinates there are (3^d)³=27^d addresses. A deeper address reduces to exactly one shallower address, but a shallow address has many extensions. This direction explains the word “inverse”: the linking maps go from finer information back to coarser information.

The inverse limit A∞ is the set of all sequences (a₁,a₂,a₃,…) whose entries belong to their respective A_d and satisfy every reduction equation. A “set” is a collection; an element here is a whole compatible history, not its last finite row. The notation Z₃³ names the same triple ternary-history structure. The subscript 3 names the ternary completion; it is not the three-element set Z/3Z. This definition introduces no calculus.

A complete digit rule constructs an example: for each positive integer j, tell us which digit u_j to use, and apply the prefix rule from Lesson 01. Adding the next term 3^d u_(d+1) cannot change the old residue. Conversely, at each level the three choices −1,0,1 give distinct extensions because their differences are not multiples of 3. This allows the history to be read back one digit at a time. The infinite rule is a compact specification, not a claim that infinitely many entries were physically stored.

## C22.03-W1 — An exact all-positive rule

Set u_j=1 for every j. The first four signed sums are 1, 1+3=4, 1+3+9=13, and 1+3+9+27=40. All lie in their storage ranges. The general expression is t_d=(3^d−1)/2. Check it without infinite sums: it gives t₁=1 and the difference t_(d+1)−t_d=(3^(d+1)−3^d)/2=3^d, exactly the next contribution. Therefore reduction is compatible at every depth, not just the four listed depths.

An explicit triple point uses rules “all +1”, “all 0”, “all −1” for its first, second and third coordinates. At depths 1–4 its nonnegative residue triples are (1,0,2), (4,0,5), (13,0,14), (40,0,41). Preserve the signed third sums −1,−4,−13,−40 alongside them. No physical units attach to these entries.

> Claim scope: S02 /backbone_sequence/17 defines A∞ and its paired real rendering. We have constructed explicit inverse-limit points and explained the notation; we have not assigned any arbitrary operator to them. The ternary depth is distinct from the dyadic refinement in S02 /backbone_sequence/2/recursions/group_dyadic. Counts 27^d here do not license a substitution of dyadic depth.

## C22.03-P1 — Practice, then check

Use all −1 digits to construct four levels and check compatibility. How many next triple addresses extend any fixed depth-d triple?

Answer: signed sums −1,−4,−13,−40 reduce to 2,5,14,41. Check 5 mod3=2, 14 mod9=5, 41 mod27=14. In one coordinate the extensions of residue a can be written a, a+3^d, a+2·3^d in the next storage range. Independently choosing one for each of three coordinates gives 3·3·3=27 extensions. Balanced digit labels may require reduction but describe the same three choices.

## Diagnostics — C22.03-D1

1. What is the fifth all-positive signed sum?
2. How many triple addresses exist at depth 2?
3. Is a four-row table with no continuation rule an exact infinite point?
4. Does verifying four reductions alone establish a proposed rule at every depth?

Worked answers: (1) 40+81=121=(243−1)/2. (2) 9³=729=27². (3) No; it specifies a family of possible extensions. Record “continuation unresolved.” (4) No; use the general difference argument when a rule is supplied. A finite failure disproves compatibility, but finitely many successes alone leave the rest untested.

Next dependency: [Lesson 04](lesson-04.md) renders the digit rule while preserving this exact address ladder.
'''
lessons[4]=r'''
# Lesson 04 — A convergent real-space renderer

Essential question: How can a finite image have a certified error bound without erasing its infinite history?

Goals: Derive a geometric sum and tail; choose depth by testing powers; convert coordinate bounds to length bounds; preserve distinct histories with a shared image.

Bridge and pacing: Lesson 03 supplied a full digit rule; a real sum now uses decreasing weights instead of the increasing weights of address residues. Three 55-minute periods, each with retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15. Periods cover geometric sums, vector bounds, then endpoint histories. All vector and matrix operations required here are defined below.

## C22.04-E1 — From finite sum to controlled tail

Write S_N=r+r²+…+r^N. Multiplying by r shifts the terms: rS_N=r²+…+r^(N+1). Subtracting cancels the middle terms, so (1−r)S_N=r−r^(N+1). If r≠1, division gives S_N=r(1−r^N)/(1−r). This is a finite identity. To pass to an infinite sum we additionally need |r|<1, so r^N tends to zero. For q=|r|<1, the sum of absolute weights after N is q^(N+1)/(1−q). Absolute values matter because cancellation of signed terms can hide a large tail of separate contributions.

The normalized M18 renderer is z_N=(1/2)Σ_(j=1)^N 3^(−j)u_j, with u_j an ordered triple of balanced digits. Σ means add the indicated terms. Calculate each coordinate separately. Each digit has absolute value at most 1, so each coordinate of z−z_N has absolute value at most (1/2)Σ_(j>N)3^(−j)=1/(4·3^N). This proves convergence: two sufficiently deep partial sums differ by at most the same shrinking tail bound. The complete real-number system supplies their limit z. Keep the full digit rule or the unresolved continuation as well as N and z_N; a bound describes the missing contribution but is not a replacement for it.

For a vector w=(w₁,w₂,w₃), define ||w||∞=max(|w₁|,|w₂|,|w₃|). A matrix B acts by row sums: (Bz)_i=B_i1 z₁+B_i2 z₂+B_i3 z₃. Define ||B||∞ as the largest sum of absolute entries in a row. The triangle inequality |a+b|≤|a|+|b| gives ||Bw||∞≤||B||∞||w||∞. Thus r_N=Bz_N has tail at most ||B||∞/(4·3^N). Here r_N denotes a physical displacement, whereas the scalar r earlier in the geometric formula was a ratio. Absolute positions would be x_N=O_K+r_N with declared origin O_K; differences use x−O_K. If B entries have length units, r and its bound do too.

## C22.04-W1 — Worked bounds (alias C22-TAIL-EX1)

First use d_j=2^(−j). The sum is S_N=1−2^(−N); the remaining positive tail is exactly 2^(−N). For tolerance 0.01, check successive powers: 1/64=0.015625>0.01 and 1/128=0.0078125≤0.01. The smallest acceptable depth is 7. This check uses no logarithms.

For the M18 normalized coordinate bound and tolerance 1/1000, depth 5 gives 1/(4·243)=1/972>1/1000; depth 6 gives 1/2916<1/1000. Hence N=6 is the smallest depth guaranteed for every allowed digit history. A specific history can have a smaller actual tail.

Use the **synthetic** length-valued matrix B=diag(2,3,4) LU, meaning rows (2,0,0), (0,3,0), (0,0,4) in an illustrative length unit LU. It is not the source-locked Cell3 basis. Its maximum absolute row sum is 4 LU, so the physical tail is at most 1/3^N LU. For the all-positive first-coordinate rule and zero other coordinates, z_N=((1−3^(−N))/4,0,0). At N=2, z₂=(2/9,0,0), r₂=(4/9,0,0) LU; the limit r=(1/2,0,0) LU. The actual remaining displacement is (1/18,0,0) LU, below the general bound 1/9 LU. Store that signed remainder, not merely its norm.

> Claim scope: S02 /backbone_sequence/17/definitions/3 and /backbone_sequence/17/proof/1 and /backbone_sequence/17/proof/2 supply the renderer and normalized bound. These calculations derive their finite consequences. The diagonal B and LU are teaching choices with no asserted Cell3 handedness or numerical calibration. No observation or mechanism claim is added.

## C22.04-P1 — Practice, then check (alias C22-TAIL-P1)

(a) Choose the smallest N for the binary-weight tail tolerance 1/32. (b) For the synthetic B above, certify a physical infinity-norm tolerance 1/1000 LU. (c) Render first-coordinate histories h=(1,−1,−1,…) and k=(0,1,1,…), each with the indicated constant tail and zero other coordinates. Compute their depth-2 images and their infinite images; retain both histories.

Answer: (a) N=5 since 2^(−5)=1/32 and depth 4 gives 1/16. (b) N=7 since 1/729>1/1000 but 1/2187≤1/1000. (c) Σ_(j≥2)3^(−j)=1/6. Thus z(h)=(1/2)(1/3−1/6)=1/12 and z(k)=(1/2)(1/6)=1/12 in the first coordinate. At depth 2, z₂(h)=1/9 and z₂(k)=1/18. Their signed tails are −1/36 and +1/36, respectively, each attaining the normalized depth-2 bound. Their first residues differ, so the complete histories remain distinct. For this synthetic B their common physical first coordinate is 1/6 LU. The mature object is the ordered pair (exact history, image); saving the image alone would lose which history occurred.

## Diagnostics — C22.04-D1 (alias C22-TAIL-D1)

1. Does the infinite-tail argument apply when scalar ratio r=1?
2. Do opposite signed contributions permit deleting both terms?
3. Is 1/(4·3^N) automatically a length bound for every B?
4. At depth 3 compute the normalized all-positive scalar image and its exact tail.

Worked answers: (1) No. The finite sum is N, division by 1−r fails, and partial sums grow. (2) No. Their sum may vanish but the individual contributions and their rule remain information. (3) No: it is dimensionless; multiply by the declared matrix norm for a physical bound. (4) z₃=(1−1/27)/4=13/54; limit 1/4; tail 1/108. The tail is positive for this rule, while the absolute bound permits either sign for other rules.

Next dependency: [Lesson 05](lesson-05.md) asks what a finite-prefix observation can distinguish even when finer history is retained.
'''
lessons[5]=r'''
# Lesson 05 — Cylinder observations

Essential question: What can an observation see if it reads only a finite prefix?

Goals: Evaluate an observation through reduction; find the prefix depth it actually needs; preserve finer addresses sharing one value.

Bridge and pacing: Lesson 01 taught reduction and Lesson 04 separated histories from rendered values. One 55-minute period: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

## C22.05-E1 — One observation, many histories

A function assigns an output to each allowed input. An observation f_d on depth-d residues uses just that finite address. To apply it at depth d+1, first reduce and then use f_d. The notation f_d∘π_d means exactly this two-step operation, called composition. It is also called a pullback of the observation to the finer level.

A cylinder is the collection of all complete histories sharing a chosen finite prefix. A cylinder observation is constant as you vary the unresolved tail inside that cylinder. No literal cylinder in physical space is required. If two finer inputs reduce to the same prefix, a function of that prefix must return the same output. The converse need not hold: an observation can also group several different prefixes into one output.

In three coordinates, declare whether the function reads the whole prefix triple or only one coordinate. Recording a scalar observation is not an instruction to erase the other coordinates. A useful table stores full address, prefix depth, observation rule and observation value together. This gives a reproducible coarse view while retaining fine distinctions.

## C22.05-W1 — A depth-one indicator

Define f₁(a)=1 if a mod3=1 and 0 otherwise. The outputs 0 and 1 are dimensionless labels. At depth 2, f₁(1)=f₁(4)=f₁(7)=1 because all three reduce to 1 modulo3. At depth 3 each depth-2 residue a has extensions a+9k for k=0,1,2. Since 9k is divisible by3, the output stays the same. For example the extensions of 4 are 4,13,22, all giving 1. The function reads the first prefix, even when evaluated on depth-3 inputs.

> Claim scope: S02 /backbone_sequence/17/proof/3 states finite-prefix observables and consistent pullback. The function here is an authored mathematical example, not a sensor measurement. Equal outputs identify an observation class, not an entire exact history.

## C22.05-P1 — Practice, then check

Let g₂(a)=a mod9. Evaluate it on depth-3 residues 7,16,25. Recover their balanced first three digits and identify what g₂ ignores. For triple inputs (a,b,c), keep b and c in the ledger even though g₂ reads only a.

Answer: each output is 7. The digit triples are (1,−1,1), (1,−1,−1), (1,−1,0): their signed sums are 7,−11,−2, respectively, and their mod27 residues are 7,16,25. All share their first two digits. The third digit and all later continuation are invisible to g₂. Store each separate input beside output 7; do not replace the three rows by a single unlabeled row.

## Diagnostics — C22.05-D1

1. Can an observation that reads the third balanced digit always be described as depth-one?
2. What is f₁(8) in the worked example?
3. Does equal g₂ force equal third digits?
4. Can the constant observation f(a)=0 use no digits at all?

Worked answers: (1) No: 7,16,25 have the same depth-one prefix but different third digits. A general third-digit reader needs depth 3. (2) 8 mod3=2, so f₁(8)=0. (3) No; the practice table is an explicit counterexample. (4) Yes, depth zero suffices because the output ignores every input. The input histories should still be retained if the record is to preserve them.

Next dependency: [Lesson 06](lesson-06.md) decomposes coarse and fine information into pieces that reconstruct the input exactly.
'''
lessons[6]=r'''
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
'''
lessons[7]=r'''
# Lesson 07 — Infinite objects and operator domains

Essential question: Why can an operation work on every finite truncation and still fail on a complete sequence?

Goals: Specify an operator's input space, domain and action; prove convergence with a block bound; test two sequences against an explicit domain; classify source claims by supplied assumptions.

Bridge and pacing: Lesson 04 proved geometric convergence, and Lesson 06 taught dot products, identity operations and reconstruction. Two 55-minute periods, each retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15. Period 1 develops the sequence space and block proof; period 2 tests domains and source cards. No calculus is needed.

## C22.07-E1 — An input rule includes an allowed set

An operator is a function that acts on objects such as vectors or sequences. Its carrier (ambient space) specifies what kinds of objects are under discussion. Its domain is the subset on which this particular action has an allowed output. Giving an action formula alone does not specify either set.

For this lesson use real sequences x=(x₁,x₂,…) indexed by positive integers. Define ℓ² as those sequences for which Σx_n² is finite. Its norm is ||x||₂=√(Σx_n²); its inner product is ⟨x,y⟩=Σx_n y_n. To justify this infinite inner product, first prove a finite inequality. For lists a₁,…,a_N and b₁,…,b_N, put A=Σa_n², B=Σb_n² and C=Σa_n b_n, where these three sums stop at N. If B=0, every b_n is zero and C=0. If B>0, the sum of squares Σ(a_n−t b_n)²=A−2tC+t²B is nonnegative for every real t. Choose t=C/B to obtain A−C²/B≥0, hence |C|≤√A√B. This is the finite dot-product inequality. Apply it to a_n=|x_n| and b_n=|y_n|: each finite sum Σ|x_n y_n| is at most ||x||₂||y||₂. These nonnegative partial sums increase and stay bounded, so they converge. Thus the signed inner product converges absolutely: the total size of every remaining signed tail is bounded by the corresponding absolute tail, which tends to zero. Merely bounded signed partial sums would not be enough. The temporary finite-sum names A,B,C in this proof are scalars; B here is not the length-valued matrix of Lesson04. Convergence in this norm means the norm of the difference tends to zero. This is stronger than saying every fixed coordinate converges. These are mathematical specifications; no measured sequence is introduced.

We need a convergence test for Σ1/n². Split positive integers into blocks 2^k≤n<2^(k+1), for k=0,1,2,… . The block has 2^k entries, each at most 1/(2^k)². Its sum is therefore at most 2^(−k). Adding the block bounds gives 1+1/2+1/4+…=2 by Lesson 04. Partial sums of 1/n² increase but stay at most 2, so they approach a finite limit. Moreover the sum from n=2^K onward is at most Σ_(k≥K)2^(−k)=2^(1−K), which tends to zero. We do not need the exact sum.

Define D by (Dx)_n=nx_n, with domain Dom(D)={x∈ℓ²: Σn²x_n²<∞}. The domain condition says precisely that the proposed output lies in ℓ². A rule can be meaningful on a proper subset of its carrier. D is unbounded: the sequence with a single 1 in position m has norm 1, while its output has norm m; no fixed constant bounds all output norms by that constant times the input norm. Unbounded does not mean undefined everywhere.

## C22.07-W1 — Finite success and infinite failure

Let x_n=1/n. Its squared sum is Σ1/n², finite by the block proof, so x∈ℓ². But Dx=(1,1,1,…), whose first N squared entries sum to N. Thus Dx∉ℓ² and x∉Dom(D).

Let x^(N) retain the first N entries of x and set all later entries to zero. This is an explicitly labeled truncation accompanied by the exact removed tail rule x_n=1/n for n>N. Every x^(N) belongs to Dom(D), since its weighted squared sum is the finite number N. Also x^(N)→x in ℓ²: its squared error is the tail of Σ1/n², bounded by the block argument. Yet x is outside the domain. Finite membership and input convergence alone cannot pass an operator through a limit. The output norms √N already reveal the failure.

> Claim scope: D is an explicitly authored domain example, not an archival K-Field history operator. S02 M18's convergent renderer supplies neither this D nor a universal claim about other operators. Self-adjointness (equality with the adjoint on the appropriate domain) is an advanced property whose proof is outside this course; it must never be inferred merely from renderer convergence or a label.

## C22.07-P1 — Practice, then check

Test y_n=1/n² for the domain of D and compute Dy. Then inspect this source card: “M18 specifies compatible addresses, a real renderer and a retained-detail filtration; no particular history-operator action or operator domain is stated in that module.” List what would still be needed to apply a proposed history operator H.

Answer: Σy_n²=Σ1/n⁴≤Σ1/n²<∞ because n≥1. The weighted sum Σn²y_n²=Σ1/n² is finite, so y∈Dom(D) and (Dy)_n=1/n∈ℓ². For H one needs the carrier (for example, histories themselves or functions on histories are different choices), domain, action, norm/topology or inner product where relevant, and the convergence mode for any infinite formula. The card does not provide these for H; mark them “not supplied for H,” not “false” or “supplied by D.”

## Diagnostics — C22.07-D1

1. Why is the constant sequence (1,1,…) outside ℓ²?
2. Does y_n=1/n³ belong to Dom(D)?
3. If every finite truncation lies in Dom(D), must the full sequence lie there?
4. What information belongs in a final paired-rendering report?

Worked answers: (1) Its first N squared entries sum to N without a finite bound. (2) Yes: the input square sum 1/n⁶ and weighted square sum 1/n⁴ are each bounded termwise by 1/n². (3) No; x_n=1/n is the worked counterexample. (4) Exact digit rule or unresolved continuation, residue history and depth, signed partial image, declared B and units, tail bound and any known signed tail, retained detail vectors and reconstruction, plus source status and any proposed operator's missing assumptions.

Next dependency: [Capstone](capstone.md) uses these seven taught operations to produce a complete, source-scoped report.
'''
for n,body in lessons.items(): write(f'lesson-{n:02}.md',body)

# Save authored drafts and hashes before subsequent independent audit.
m=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8-sig'))
m['checkpoints']=[{'id':f'lesson-{n:02}','kind':'lesson','path':f'lesson-{n:02}.md','status':'drafted','dependencies':([f'lesson-{n-1:02}'] if n>1 else []),'sha256':digest(f'lesson-{n:02}.md'),'summary':packet['course_map'][n-1]['title']} for n in lessons]
m['next_action']='Independently audit lessons, write supporting materials, verify examples and assemble'
dump('manifest.json',m)
print('Seven complete lesson drafts saved and hashed.')
