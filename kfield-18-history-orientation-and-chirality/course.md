# History, Orientation, and Chirality

Student course. See capstone.md for the synthesis assessment and sources.md for provenance.

<!-- BEGIN: lesson-01 -->
# Lesson 01 — Address histories as words

**Essential question:** How can an address remember a sequence of choices?

**Goals:** Generate all words through a stated depth; distinguish an empty label from a zero coefficient; apply a prefix and its conditional removal.

**Bridge:** Courses 06, 15 and 17 are the series prerequisites. Here we need only their habits of keeping ordered labels, signed quantities and distinct carriers. This lesson rebuilds the finite notation: a list of labels tells us which slots exist; a list of numbers tells us what occupies each slot. All classroom coefficients are dimensionless synthetic values, not measurements.

**Pacing:** One 55-minute period: retrieval 5, explanation/example 20, practice 15, diagnostics/repair 15 minutes.

## C18.01-E1 — Words and a ledger

Choose the classroom alphabet {a,b}. A word is a finite ordered string of these letters. Order matters: ab and ba are different. Its length is the number of letters. The empty word, Ω, has length zero. It is a legitimate address: the start before any choice. It is not the number zero.

Prefixing puts a letter on the **left**. Thus prefix a changes b into ab, and changes ab into aab. Our convention records the newest choice on the left. If you instead append on the right, you have defined a different operation and must say so.

A tree connects each word w to aw and bw. A depth cutoff d keeps words with length at most d. It does not tell us what to do when an operation leaves the displayed tree. We will specify that rule separately.

For each word w, let e_w mean a ledger with coefficient 1 in slot w and 0 in all other slots. These are unit coordinate vectors. A vector is a list of coefficients in a declared order; for example 2e_Ω−e_a has root coefficient 2 and a coefficient −1. Different unit coordinate vectors are called orthogonal: their dot product is zero. The dot product multiplies matching entries and adds the products. This is a bookkeeping model, with no probability interpretation assigned.

## C18.01-W1 — Build the depth-two tree

Start with Ω. Prefix either letter to obtain a,b. Prefix to both: a→aa,ba and b→ab,bb. Sorting into the fixed classroom order gives

| Length | Labels | Number |
|---|---|---:|
| 0 | Ω | 1 |
| 1 | a, b | 2 |
| 2 | aa, ab, ba, bb | 4 |

The total is 1+2+4=7. None of these labels is omitted, including Ω. Prefix a sends Ω to a and b to ab. Conditional removal of a sends ab back to b. It fails on ba because ba starts with b. In the later linear operator model a failed removal returns the **zero vector**, meaning all coefficients zero; it does not return e_Ω. Removing a from the one-letter word a does return e_Ω.

To see why those differ, e_Ω=(1,0,0,0,0,0,0), whereas the zero vector has seven zeros. A ledger (2,−1,0,3,0,−2,4) preserves the root, the signs and the zero slots.

## C18.01-P1 — Practice before checking

Draw the depth-one tree. Prefix b to Ω, a and b while allowing depth two. Then record 3e_Ω−2e_b in depth-one order. Explain what would happen to ba if a depth-one display were enforced.

**Worked answer:** The depth-one labels are Ω,a,b. Prefix b gives b,ba,bb respectively. The ledger is (3,0,−2). The last two outputs lie outside a depth-one display. A larger display keeps them; a truncating operator would send them to zero and require a separate record of the omitted coefficients for reconstruction. A drawing cutoff alone does not choose between these rules.

> **Claim scope:** This binary toy is an authored finite example. S02#/backbone_sequence/13 defines the source carrier F_hist=l²(B_8*): all finite words over the source eight-letter alphabet, including Ω. The star means all finite word lengths. The symbol l² means coefficient lists whose sum of squared magnitudes is finite. The source alphabet's complete typed replay definition is flagged in S03#/findings/8; we do not identify its letters with physical directions. Seven coordinate slots are not the source infinite carrier.

## Diagnostic checks

1. **C18.01-D1:** What extra rule must accompany a finite cutoff, and how does this tree differ from F_hist?
2. List the words of exactly length three without repeating or losing a branch.
3. Does removing a from a give zero? Does removing a from ba give Ω?
4. In (0,2,−1), has the root label been deleted?

**Worked answers:** (1) State how operations treat terminal words; our seven labels are a finite binary toy, while F_hist includes all finite words over B_8. (2) aaa,aab,aba,abb,baa,bab,bba,bbb; each of four length-two words has two children, so 8. (3) The first returns e_Ω; the second returns the zero vector under conditional removal. (4) No: the first slot remains and has coefficient zero.

**Next dependency:** [Lesson 02](lesson-02.md) converts these label operations into maps and accounts for both endpoints of a finite shift.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 02 — Shift operators and endpoint defects

**Essential question:** What information does a finite shift lose at its two ends?

**Goals:** Apply prefix/removal maps; multiply a small matrix by a vector; compute root and terminal defects; distinguish finite, rectangular and infinite domains.

**Bridge:** Lesson 01 gave unit vectors and conditional prefix removal. We now use a simpler single chain of three positions, called 0,1,2. This radial *toy* tracks position along a chain, not all branches of the binary tree and not the source radial T_0.

**Pacing:** Two 55-minute periods. Each has retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15 minutes. Period A covers prefixing and matrix action; B covers endpoint defects and domain comparisons.

## C18.02-E1 — Maps, matrices and removal

A linear map acts on each unit vector and then adds the results with the original coefficients. On the full binary tree write L_a e_w=e_aw. Removal L_a† e_aw=e_w and L_a† e_bw=0; at the root L_a† e_Ω=0 because there is no first letter to remove. The dagger denotes the adjoint; for our real coordinate matrices it is the transpose, obtained by exchanging rows and columns. On all finite binary words, L_a†L_a=I: prefix then remove restores the input. I means the identity map, which changes nothing. Distinct prefixes have disjoint output labels, so L_a†L_b=0. Neither prefix reaches the empty word. Their combined ranges cover every nonempty word. These facts explain the analogous source relations without replacing B_8 by two letters.

For the three-state chain define S e_0=e_1, S e_1=e_2, S e_2=0. Terminal output is explicitly discarded by this map. In order (e_0,e_1,e_2),

```text
      [0 0 0]            [0 1 0]
S  =  [1 0 0]     S† =  [0 0 1]
      [0 1 0]            [0 0 0]
```

Column j records the output of input e_j. To multiply a matrix by a vector, multiply each row by the vector's entries and add. Thus S(x,y,z)=(0,x,y), while S†(x,y,z)=(y,z,0). To compose maps, apply the rightmost map first. S†S therefore means shift first, then remove.

## C18.02-W1 — Two different products

Apply S†S to (x,y,z): S gives (0,x,y), then S† gives (x,y,0). Hence S†S=diag(1,1,0). Here diag lists diagonal entries, all other entries being zero. Conversely S† first gives (y,z,0), then S gives (0,y,z), so SS†=diag(0,1,1). These products differ because they test different ends. A matrix product can always be verified on the unit inputs e_0,e_1,e_2; linearity then covers every vector.

## C18.02-P1 — Preserve the removed coefficient

Find Sf and S†Sf for f=(2,3,4). Recover f by adding a retained vector. Then use T(a,b)=(0,a,b) from two-coordinate inputs to three-coordinate outputs on (2,3).

**Worked answer:** Sf=(0,2,3), S†Sf=(2,3,0); store terminal vector (0,0,4), so f=(2,3,0)+(0,0,4). T(2,3)=(0,2,3), and T†(x,y,z)=(y,z). Thus T†T(2,3)=(2,3). The sum of squared input entries is 4+9=13, equal to the output sum 0+4+9. The terminal coordinate is absent from T's input domain; it has not been erased.

## C18.S01-E1 — Defects, ranks and index

The terminal defect is I−S†S. It keeps input information destroyed by S. The root defect is I−SS†. It keeps output information that cannot be reached by S. A map's rank counts independent output directions. Its kernel consists of inputs sent to zero; its kernel dimension counts independent lost input directions. Here the cokernel dimension counts independent missing output directions, equivalently the dimension of ker S†. Define index as dim ker S−dim ker S†. These are counts, with no physical units.

## C18.S01-W1 — Square versus rectangular

Subtracting the preceding diagonals gives I−S†S=diag(0,0,1) and I−SS†=diag(1,0,0). Each rank is 1. The kernel of S is all multiples of e_2; the kernel of S† is all multiples of e_0. The finite square index is 1−1=0.

For T from two to three coordinates, T†T=I_2, where the subscript states the number of slots. TT†=diag(0,1,1). Its input defect is zero, its output defect has rank 1, and its index is 0−1=−1. This rectangular count is consistent with its different domain and codomain dimensions. It is not a square truncation.

## C18.S01-P1 — A second endpoint ledger

Repeat the loss/reconstruction calculation for f=(1,−2,5). Compare T(1,−2).

**Worked answer:** Sf=(0,1,−2); S†Sf=(1,−2,0). Retain (0,0,5) and add it to recover f. T(1,−2)=(0,1,−2) has squared norm 5, as does its input. In contrast f has squared norm 30 and Sf has 5; the retained terminal vector contributes the other 25.

> **Claim scope:** A separate infinite unilateral shift U on l²(N_0) sends (x_0,x_1,…) to (0,x_0,x_1,…). N_0 means 0,1,2,…; square summability makes the norm finite. There is no last slot. U†U=I, ker U has dimension 0, ker U† is the root direction, and index is −1. This explanation concerns this explicitly defined U. M14's radial T_0 is a source-reported operator with a replay-definition gap under AUD-009. Neither our S nor an assertion of equal index supplies that missing definition.

## Diagnostic checks

1. **C18.02-D1:** Why cannot S†S=I and infinite index −1 both be assigned to this square S?
2. **C18.S01-D1:** Count both defect ranks and the index for S. What changes for U?
3. Evaluate L_a†e_ab, L_a†e_ba and L_b†L_a e_b on the full toy word space.
4. Find the missing information after S acts on (0,0,7). Can S† alone recover it?

**Worked answers:** (1) e_2 is killed, so S†S e_2=0 rather than e_2. Its lost and missing directions each number one. (2) Terminal rank 1, root rank 1, index 0; U has terminal defect zero, root rank 1, index −1. For any finite square n-by-n matrix, kernel and cokernel dimensions both equal n−rank. (3) e_b, zero vector, zero vector: the first letter determines removal. (4) The output is zero; store 7e_2. S† applied to zero cannot recover 7.

**Next dependency:** [Lesson 03](lesson-03.md) asks which of these maps preserves length and which can reverse every possible output.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
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
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# Lesson 04 — History projectors

**Essential question:** When does selecting parts of a history produce a complete, nonoverlapping ledger?

**Goals:** Construct four finite q_n maps; verify self-adjointness, idempotence and orthogonality; reconstruct a vector with its zero coordinates retained.

**Bridge:** TT† in Lesson 03 selected the reachable coordinates. We now select one chain position at a time, using the same three-state S from Lesson 02. No new physical data enter.

**Pacing:** 55 minutes: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

## C18.04-E1 — Selection that stabilizes

A projector satisfies P²=P: selecting twice does the same as selecting once. This is idempotence. An orthogonal projector also satisfies P†=P, called self-adjointness. These two conditions must both be checked; idempotence alone does not guarantee orthogonal selection. Two orthogonal projectors are mutually orthogonal if their product is zero: the selected subspaces do not overlap. For self-adjoint projectors, checking one order suffices, since taking the adjoint gives the other order.

Let P_0=diag(1,0,0) select the root. Define q_n=S^n P_0(S†)^n for n=0,1,2,… . A power means repeated composition, and the zero power is I. Read right to left: move back n steps, keep the root, move forward n steps. The rank of a projector counts available selected directions, not the number of nonzero entries in one particular output.

## C18.04-W1 — Walk the selection along the chain

For v=(x,y,z), q_0v=(x,0,0). For q_1, first S†v=(y,z,0); P_0 keeps (y,0,0); S moves this to (0,y,0). For q_2, (S†)²v=(z,0,0); P_0 keeps it; S² gives (0,0,z). Three backward steps give zero, so q_3=0.

Thus q_0=diag(1,0,0), q_1=diag(0,1,0), q_2=diag(0,0,1), q_3=diag(0,0,0). Their ranks are 1,1,1,0. Transpose leaves each diagonal unchanged. Squaring a 0 or 1 leaves it unchanged, so q_n²=q_n. Multiplying different diagonals gives zero in each position, so q_nq_m=0 for n≠m. The first three sum to I_3.

For (1,2,3), the outputs are (1,0,0),(0,2,0),(0,0,3), and the zero vector. Adding them returns (1,2,3). Their squared norms are 1,4,9,0, which sum to 14, the original squared norm. This arithmetic checks completeness as well as disjointness.

## C18.04-P1 — Keep a zero output

Compute all q_n outputs through n=3 for (−1,4,0). State their ranks, verify q_1²=q_1 and q_1q_2=0, and reconstruct the vector.

**Worked answer:** The four outputs are (−1,0,0),(0,4,0),(0,0,0),(0,0,0). The projector ranks remain 1,1,1,0: q_2 can select a nonzero terminal input even though this particular input has terminal coefficient zero. Diagonal multiplication gives q_1²=diag(0,1,0), and q_1q_2=diag(0,0,0). Adding all four stored outputs gives (−1,4,0). Keep labels q_2 and q_3 to distinguish a zero coefficient from a zero operator.

> **Claim scope:** S02#/backbone_sequence/13 states q_n=W^n P_Π(W†)^n and imposes that P_Π lies in the root defect space for the orthogonality assertion. For an isometry W the root defect is the missing output subspace, ker W†. Our P_0 is in the corresponding root direction of the finite toy. A generic P is not interchangeable with P_0. For example P=I_3 gives q_0=I_3 and q_1=SS†=diag(0,1,1); q_0q_1 is nonzero. Finite verification cannot remove the source hypothesis.

## Diagnostic checks

1. **C18.04-D1:** What source condition prevents arbitrary replacement of P_Π? Give the toy counterexample above in your own words.
2. Compute q_2² and q_0q_2.
3. Is rank q_2 zero when q_2(−1,4,0)=0?
4. If only q_0v and q_1v are saved for v=(2,−1,7), what must be retained to reconstruct v?

**Worked answers:** (1) The selected subspace must lie in the root defect for the stated wandering construction. P=I makes selections overlap. (2) q_2²=diag(0,0,1)=q_2; q_0q_2=0. (3) No, rank is 1; the single input happens to have coefficient zero there. (4) Retain q_2v=(0,0,7), and preserve q_3's zero label. Then (2,0,0)+(0,−1,0)+(0,0,7)=(2,−1,7).

**Next dependency:** [Lesson 05](lesson-05.md) adds an orientation ledger so signs and order survive geometric changes as well as coordinate selections.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 05 — Spatial handedness and a time direction

**Essential question:** Which changes preserve orientation, and which must appear as sign changes in our ledger?

**Goals:** Calculate determinants for diagonal toy bases; track swaps, positive rescaling and reflections; distinguish a spatial orientation choice from a time direction.

**Bridge:** Earlier lessons required an ordered list of coordinates. A spatial basis also has an order. Changing that order can change orientation even when no vector length changes. This lesson teaches only diagonal determinants and elementary sign rules; no general determinant expansion is needed.

**Pacing:** 55 minutes: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

## C18.05-E1 — Keep an orientation ledger

A three-dimensional basis is an ordered set of three independent arrows. Put those arrows in the columns of B. A vector with coordinates u is represented by Bu. For B=diag(p,q,r), the arrows run along the three reference axes and their signed scale factors are p,q,r. The determinant is pqr. Its magnitude measures the volume scale of the coordinate box; its sign records handedness relative to the fixed reference orientation. Positive and negative determinants describe opposite handedness. Zero means a collapsed box, not a basis.

Multiplying one column by −1 reverses one arrow: it is a reflection and reverses the determinant sign. Swapping any two columns also reverses the sign; the order of the basis is part of its definition. Multiplying all three columns by a positive factor λ multiplies the determinant by λ³, preserving its sign. A positive rescale cannot repair or change handedness.

A coframe is the corresponding ordered set of coordinate readers, also called covectors. For the diagonal basis above the readers are x/p,y/q,z/r: each returns 1 on its matching basis arrow and 0 on the other two. The coframe determinant is 1/(pqr), so it has the same sign as the basis determinant. We need only this sign relationship here.

Time requires an additional reader τ and a declared positive or forward direction. In the ordered four-dimensional coframe (τ,θ¹,θ²,θ³), reversing τ reverses the four-dimensional orientation while leaving the spatial basis untouched. In this product convention the orientation sign is the time sign times the spatial coframe sign. Changing either once flips the product; changing both leaves the product unchanged but still changes two ledger entries. This is orientation bookkeeping, not a derivation of a physical arrow of time.

## C18.05-W1 — A swap and a time reversal

Take synthetic dimensionless B=diag(1,2,−3). Its determinant is 1·2·(−3)=−6. Its spatial coframe has determinant −1/6. With τ declared forward, the four-dimensional orientation sign is (+)(−)=−.

| Operation | Ordered spatial columns | det B | Time sign | Four-orientation sign |
|---|---|---:|---:|---:|
| Start | first, second, third | −6 | + | − |
| Swap columns 1 and 2 | second, first, third | +6 | + | + |
| Then reverse τ | second, first, third | +6 | − | − |

The final product sign matches the starting product, but neither the basis order nor time direction is the same. Keeping only the final sign would lose the history of changes.

## C18.05-P1 — Rescale, then reflect

Start with B=diag(2,1,−4), columns ordered as displayed and forward τ. Multiply all spatial lengths by 2. Then reverse only the third axis. Record the basis, determinant and four-orientation sign at every step.

**Worked answer:** Initially det B=2·1·(−4)=−8, sign −. Rescaling gives diag(4,2,−8) and determinant 4·2·(−8)=−64=8(−8), sign −. Reflecting the third axis gives diag(4,2,8), determinant +64 and sign +. Time stayed forward throughout. The reflected basis is a changed orientation, not the original source basis under another silent convention. The inverse operations are reflection again, then division of every spatial column by 2, which recovers the starting basis.

> **Claim scope:** S02 M14 uses the left-handed Cell3 spatial coframe together with the forward history covector. The course's locked convention is ICRS columns [a b c] with intentional negative determinant. Our integer diagonal B is a synthetic sign example, not numerical Cell3 geometry. No source constants, metric values or spatial units are inferred from it. Temporal direction, spatial handedness, internal exterior parity and detector parity are separate ledger fields. They do not become equal merely because each sometimes uses a plus/minus sign.

## Diagnostic checks

1. **C18.05-D1:** Can the magnitude 8 of a spatial determinant determine a forward time choice? Explain.
2. What happens to det diag(1,2,−3) if all columns are multiplied by positive 3?
3. What happens to the determinant sign after two successive column swaps?
4. A colleague reflects Cell3's third column “to fix the negative determinant.” What information must the record state?

**Worked answers:** (1) No. Magnitude is a volume scale; the time covector and its direction are additional premises. (2) It becomes 27(−6)=−162, still negative. (3) Two sign flips restore the sign, but the final column order must still be recorded; two different swaps can produce a different order. (4) State the reflected column and changed orientation; this is not the locked basis. Retain the original ordered columns and inverse transformation.

**Next dependency:** [Lesson 06](lesson-06.md) introduces graded labels without identifying them with spatial handedness.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 06 — Chirality as a graded construction

**Essential question:** How can two independent kinds of labels be correlated without being identified?

**Goals:** Construct projectors from a two-state grading; compute a four-state correlation and its complement; verify an anticommutation example; calculate supplied angular/spin counts with their scope limits.

**Bridge:** Lesson 04 taught projectors and Lesson 05 separated orientation fields. Here we use plus/minus labels in algebra, but declare what each labels. A shared sign is not a shared physical meaning.

**Pacing:** Three 55-minute periods, each retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15. A: grading and matrix products. B: paired labels and reconstruction. C: angular/spin counts and source scope.

## C18.06-E1 — A grading splits a carrier

A carrier is the space of states on which maps act. A grading G gives a plus or minus label and obeys G²=I. In our two-coordinate example G=diag(1,−1). Acting twice restores (x,y): G(x,y)=(x,−y), then G²(x,y)=(x,y).

Define P_plus=(I+G)/2 and P_minus=(I−G)/2. Division of a matrix by 2 divides every entry. Thus P_plus=diag(1,0), P_minus=diag(0,1). They select the plus and minus slots. Algebra also verifies this for any G²=I: (I+G)²/4=(I+2G+G²)/4=(I+G)/2, and (I−G)(I+G)/4=(I−G²)/4=0. The two projectors sum to I. For orthogonal projectors, additionally require G†=G; our diagonal G meets it.

A second map X swaps the two slots: X=[[0,1],[1,0]]. Compare GX and XG. Acting on (x,y), GX gives (y,−x), while XG gives (−y,x). Their sum is zero. The relation GX+XG=0 is called anticommutation. It says this X exchanges the two grades. It does not identify G with a spacetime operator.

Now form two **independent** label sets, (L,R) and (even,odd). Their paired carrier has four labels in the fixed order (L,even),(L,odd),(R,even),(R,odd). The tensor symbol ⊗ means pair the factors: a map A⊗B applies A to the first label and B to the second. For these selector maps it simply keeps pairs satisfying both selections. Applying a first-factor selector and a second-factor selector in either order gives the same answer, so they commute.

Set P_L=diag(1,0), P_R=diag(0,1) in the (L,R) factor; P_even=diag(1,0), P_odd=diag(0,1) in the other. Define Π=P_L⊗P_even+P_R⊗P_odd. It keeps the correlated pairs (L,even) and (R,odd). The pairs (L,odd) and (R,even) still exist, in the complement. To align the source convention P_L=(I−γ_5)/2, the toy γ in (L,R) order would be diag(−1,+1). The earlier generic G=diag(+1,−1) had no L/R names attached. Declaring this sign assignment prevents a silent convention swap.

## C18.06-W1 — Select, then retain the complement

The two terms of Π are diag(1,0,0,0) and diag(0,0,0,1), so Π=diag(1,0,0,1). Hence Π²=Π and Π†=Π. On v=(1,2,3,4), Πv=(1,0,0,4). The complement (I−Π)v=(0,2,3,0) is retained. Their sum recovers v; squared norms 17 and 13 sum to the original 30. Orthogonality is visible slot by slot.

Notice that L was not renamed even. There are two L-labeled coordinates, with different second labels. A rule selecting one pair does not eliminate the need for both label sets.

## C18.06-P1 — Independent practice

Apply Π and I−Π to (2,−1,0,3). Reconstruct. Separately compute GX and XG as matrices, verify their sum, and check P_minus² and P_minus P_plus.

**Worked answer:** The two parts are (2,0,0,3) and (0,−1,0,0); their sum is (2,−1,0,3), squared norms 13+1=14. GX=[[0,1],[−1,0]], XG=[[0,−1],[1,0]], so their sum is the zero matrix. P_minus²=diag(0,1) and P_minus P_plus=diag(0,0). Separate-factor selection commutes because each leaves the other label untouched.

## C18.S02-E1 — Supplied representation counts

The angular branch supplies a family of carriers H_ell, with ell=0,1,2,… and dimension 2ell+1. Dimension counts independent coordinate slots. The direct sum through cutoff m means placing these carriers beside one another, so their dimensions add. The sum 1+3+…+(2m+1) equals (m+1)²: starting from 1=1², the next odd number 2m+1 is exactly the difference (m+1)²−m².

Pairing each angular slot with two spin labels doubles the count. The source also supplies a regrouping rule: for ell≥1 the spin-paired block splits into labels j=ell+1/2 and j=ell−1/2, with counts 2j+1 each. At ell=0 only j=1/2 remains. We evaluate this supplied rule; we do not derive the rotation representation theory called the SO(3)/SU(2) tower or Clebsch–Gordan splitting. The two spin labels here are not the L/R chirality labels from the earlier exercise.

The source quantity C₂ has supplied eigenvalue ell(ell+1). In this use an eigenvalue is the factor by which an operator scales vectors in its labeled block. These are dimensionless representation values. No conversion into physical energy is supplied.

## C18.S02-W1 — Cutoff two

At m=2 the counts are 1,3,5. Total 9=(2+1)²; spin pairing gives 18. C₂ values are 0·1=0, 1·2=2 and 2·3=6. For ell=1, j=3/2 has dimension 2(3/2)+1=4 and j=1/2 has dimension 2; 4+2=6 equals twice 3. This is a count check, not an occupation count measured in a material.

## C18.S02-P1 — Cutoff three

Compute the total through m=3, its spin-paired count, C₂ for ell=3, the split at ell=2, and the allowed split at ell=0.

**Worked answer:** Add 7 to 9 to get 16=4²; spin pairing gives 32. C₂=3·4=12. At ell=2, j=5/2 and 3/2 have dimensions 6 and 4, giving 10=2·5. At ell=0, j=1/2 has dimension 2. There is no negative-j summand; do not invent one to extend the formula.

> **Claim scope:** S02 M14 supplies a spacetime Clifford construction and a correlation with exterior parity on a different factor. The toy G and Π verify grading algebra only. S02#/branch_proofs/5 and /proof_nodes/4, /18, /25 supply the angular/spin rules. Their exact representation scope does not supply a physical Cell3 angular Hamiltonian (the operator specifying angular energy), an energy spacing or physical occupation rule. Source-reported algebra, our finite checks and any proposed physical interpretation remain separate.

## Diagnostic checks

1. **C18.06-D1:** Why is our two-by-two grading not a complete physical chirality construction? Why does Π not mean L=even?
2. On (0,5,−2,0), find Π and its complement. Which part contains the entire record?
3. **C18.S02-D1:** Can counts 9 and 18 determine energy levels or physical occupation? What input is missing?
4. Evaluate the angular total and spin total at m=1; explain the ell=0 exception.

**Worked answers:** (1) No spacetime coframe, metric or full Clifford matrices were supplied for G. Π operates on pairs of independently defined labels. (2) Π gives zero; the complement is (0,5,−2,0), which must be retained. (3) No; a physical Hamiltonian and occupation/selection rule are not specified by the count. (4) 1+3=4, spin total 8. At ell=0 only the j=1/2 block of dimension 2 is present.

**Next dependency:** [Lesson 07](lesson-07.md) reads the archived K4 construction with a premise ledger and checks a separate finite CP witness.
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# Lesson 07 — The source K4 construction

**Essential question:** What has to be supplied before a finite identity can support a source-level chirality statement?

**Goals:** Classify source premises and replay gaps; connect a coframe to a declared grading convention; compute small commutators; verify a determinant existence witness without inferring a physical CP phase.

**Bridge:** Lessons 01–04 supplied history maps, Lesson 05 tracked spatial and temporal orientation, and Lesson 06 kept independent graded factors distinct. These provide the vocabulary for reading M14. This lesson adds complex arithmetic only as needed for the CP supplement.

**Pacing:** Three 55-minute periods, each retrieval 5, explanation/example 20, practice 15, diagnostics/repair 15. A: source cards and premise ledger. B: complex arithmetic and commutators. C: diagonal determinant witness and scope comparison.

## C18.07-E1 — Source cards and the K4 ledger

K4 here names the source's oriented four-dimensional coframe construction. A coframe reads coordinates (Lesson 05); a metric convention specifies how these directions enter a signed length expression. A Clifford construction assigns matrices γ to directions with anticommutation relations determined by that metric. We read those relations as a source contract, not as an assigned proof of their physical realization.

| Card | Source content, paraphrased | Premise or scope to retain |
|---|---|---|
| H: S02#/backbone_sequence/13 | F_hist=l²(B_8*), prefix maps, empty-word root; W is isometric but not onto | Full word carrier; W and the radial T_0 are separately named source operators |
| Q: same pointer | q_n=W^n P_Π(W†)^n are orthogonal projectors | P_Π must be a projection in the root defect space |
| O: same pointer | Left-handed spatial coframe plus forward history covector fixes oriented K4 coframe | Ordered space and time conventions are explicit inputs |
| C: same pointer | Clifford anticommutation and γ_5=iγ_0γ_1γ_2γ_3, P_L=(I−γ_5)/2, P_R=(I+γ_5)/2 | Matrices, signature and index conventions must agree |
| F: same pointer | Π_phys=P_L⊗P_even+P_R⊗P_odd | Spacetime chirality and exterior parity act on distinct factors |
| R: same pointer | Radial index Ind(T_0)=−1; tensoring with retained matter/family carrier transports signed class | A source-reported radial statement; its typed operator/domain are required for replay |
| A: S03#/findings/8, AUD-009 | B_8 and T_0 are among missing replay objects | Record VERIFIED_NOT_LOADED for missing bodies; do not replace them by toys |

The letter i in card C obeys i²=−1. A metric signature records which squared directions have plus or minus signs. To illustrate why a convention matters, suppose four matrices anticommute in distinct directions and have squares +I,−I,−I,−I respectively. Moving the factors of (γ_0γ_1γ_2γ_3)² past each other makes six sign flips, so its square is (+1)(−1)³I=−I. Multiplication by i twice contributes −1; hence γ_5²=I in this example. This conditional calculation explains the role of the convention. It does not assert that we have recovered the archive's complete matrix realization. The subscripted γ_0…γ_3 in the product must be reconciled with the metric's upper/lower-index convention before a full replay.

Once γ_5²=I holds, the idempotence algebra of Lesson 06 applies to P_L and P_R. Orthogonality as self-adjoint projection additionally uses the appropriate adjoint convention; the course does not silently infer it from a bare square identity. For a tensor correlation, the two factors must already be independently defined. The source M14 requires backbone modules M03 and M11. Those are mathematical-backbone labels, not automatic identities with compiler module numbers from a different integration ledger.

For recognition-level dependency tracing, S02#/backbone_sequence/2 names M03 as the Lucas-sheet and two-recursion module; its dyadic refinement and ternary address systems remain distinct. S02#/backbone_sequence/10 names M11 as the exterior-matter module. Exterior degree counts how many distinct basis labels enter an exterior product; even/odd refers to that count. Its carrier context supplies the internal parity language, not the spacetime L/R label. These source cards explain what the prerequisites contribute without assigning a reconstruction of their full algebra. Preserve the color-first ordering C_3 direct-sum W_2 when referring back to that internal carrier; a weak-first convention needs an explicit permutation. None of this changes the four-slot toy's declared order.

## C18.07-W1 — Classify a claimed derivation

Consider: “Our three-by-three shift has index −1, so the physical chirality selection is verified.” The actual S has kernel dimension 1 and cokernel dimension 1, so its fresh finite index is 0. The source radial statement is about T_0 on a specified infinite radial subspace, not S. Card A records the unloaded operator definition. The finite grading computation checks projector identities once a grading is supplied; cards O,C,F specify additional coframe and carrier premises. Therefore the accurate ledger contains a finite result, a source-reported radial result with a replay gap, and a conditional correlation construction. None is silently substituted for another.

## C18.07-P1 — Build your own premise ledger

Classify these four entries and attach a card: (a) three-state shift index 0; (b) source radial index −1; (c) Π_phys correlates P_L with P_even; (d) left-handed coframe with forward history. State what would have to be supplied to replay (b).

**Worked answer:** (a) Fresh finite computation from Lesson 02, not a source replay. (b) Source-reported statement, card R, with card A gap: the complete typed T_0, its domain/radial carrier and pinned proof or replay certificate. (c) Source correlation, card F, with distinct factors. (d) Declared orientation premises, card O. Keep exact source pointers with each source entry. Matching dimensions, signs or names would not supply a map that preserves the relevant operations, sometimes called an intertwiner.

**Dependency-card practice (part of C18.07-P1):** Match M03 and M11 to “address/recursion context” and “internal exterior-parity carrier,” then state whether either label is automatically a compiler-module authority. **Answer:** M03 supplies address/recursion context; M11 supplies exterior-matter context. Their backbone numbering does not identify compiler modules with the same numbers.

## C18.S03-E1 — Complex arithmetic, commutators and a witness

A complex number a+bi has real part a and imaginary part b, with i²=−1. Multiply by distributing: (a+bi)(c+di)=(ac−bd)+(ad+bc)i. Its conjugate is a−bi; its squared magnitude is a²+b². For complex matrices, † means conjugate transpose. A matrix product still uses row-by-column sums, keeping order.

Define the commutator [A,B]=AB−BA. It measures the difference between the two orders. It is different from the anticommutator AB+BA in Lesson 06. A pointwise map multiplies each slot by its own number without mixing slots. Two such maps are diagonal in the same slot order and commute: in each slot the factors are just numbers. This is the real pointwise carry-algebra restriction of S02#/proof_nodes/9. General real matrices need not commute; diagonality in a common basis, not “real” alone, supplies this example's commutativity.

CP is the source branch's name for charge-conjugation/parity-related structure. This course assesses the algebra and its declared scope; it does not identify a commutator with a measured CP invariant. In the source restricted pointwise algebra, a CP-odd expression built with a commutator vanishes because that commutator is zero. A separately supplied complex noncommutative algebra is outside that restriction.

## C18.S03-W1 — Compare two kinds of operators

Let A=diag(1,2), B=diag(3,4). AB=diag(3,8)=BA, so [A,B]=0.

Now let X=[[0,1],[1,0]] and Y=[[0,−i],[i,0]]. Row-by-column multiplication gives XY=diag(i,−i): the upper-left entry is 0·0+1·i=i. Conversely YX=diag(−i,i). Subtracting yields [X,Y]=diag(2i,−2i)=2i diag(1,−1), which is nonzero. This explicitly establishes noncommutativity. It does not by itself calculate a physical CP phase.

For a separate source-style determinant witness, a positive diagonal matrix A_0 has positive diagonal entries. Its square root S has their positive square roots. Let A_0=diag(4,1,1/4), S=diag(2,1,1/2), so S²=A_0 and det A_0=1. Here S is local notation for a square root, not Lesson 02's shift. Its inverse S^−1=diag(1/2,1,2) is checked by multiplication to I.

Let ω=−1/2+i√3/2. Squaring gives ω²=−1/2−i√3/2, and multiplying these gives ω³=1. Powers therefore repeat every three. Set D=diag(1,ω,ω²), phase label k=1, Y_u=S and Y_d=D S^−1 D. These Y symbols are names for the supplied source-style matrices; they are not measured mixing matrices. Diagonal multiplication gives Y_d=diag(1/2,ω²,2ω⁴)=diag(1/2,ω²,2ω). Then Y_uY_d=diag(1,ω²,ω); its determinant is 1·ω²·ω=ω³=1. The source general witness allows supplied positive A with det A=1 and supplied k. We need only this diagonal specialization for core work.

## C18.S03-P1 — Compute before interpreting

For A=diag(1,−1) and B=[[0,1+i],[1−i,0]], calculate AB, BA and [A,B]. Separately recompute the preceding A_0,S,D witness and determine whether Y_u and Y_d commute. Explain what determinant 1 establishes.

**Worked answer:** AB=[[0,1+i],[−1+i,0]], BA=[[0,−1−i],[1−i,0]]. Subtract: [A,B]=[[0,2+2i],[−2+2i,0]]. In the determinant witness S²=A_0, Y_d=diag(1/2,ω²,2ω), and the product is diag(1,ω²,ω) with determinant 1. Both Y matrices are diagonal, so they commute. Thus determinant 1 alone cannot imply a nonzero CP invariant. The witness verifies a possible algebraic identity under supplied inputs, not a predicted physical phase or mixing matrix.

> **Claim scope:** Primary pointers: S02#/backbone_sequence/13; angular branch pointers are in Lesson 06. CP pointers are S02#/branch_proofs/10, /proof_nodes/9 and /proof_nodes/76. The last reports an exact finite existence witness with A and k supplied, and explicitly excludes prediction of a physical CKM/PMNS matrix or CP phase; those names denote physical mixing matrices beyond this course's computation. AUD-009's VERIFIED_NOT_LOADED is a source audit disposition for unavailable replay bodies, not a claim that this course freshly verified them. All numerical vectors and small matrices here are explicitly synthetic or source-style teaching specializations. No empirical observation has been invented.

## Diagnostic checks

1. **C18.07-D1:** Which card prevents a finite toy from replacing the physical chirality-selection proof? Name two missing premises or bodies.
2. **C18.S03-D1:** Are all real matrices commuting? Use G=diag(1,−1) and X from Lesson 06 as a counterexample, and state the source obstruction's actual restriction.
3. If k=0 makes D=I, what is Y_uY_d? Does this predict a physical phase?
4. Why must a ledger keep angular counts, a commutator and a determinant witness as separate results?

**Worked answers:** (1) Cards A and R identify the replay gap; cards O,C,F identify further required structure. Examples: B_8's typed definition, T_0's domain, coframe/metric convention, retained matter/family carrier. (2) GX−XG=[[0,2],[−2,0]]≠0, although both matrices are real. The source obstruction is for commutative pointwise carry operators. (3) Y_uY_d=SS^−1=I; determinant 1. k was supplied, so this is an identity under an input, not a phase prediction. (4) They answer different questions: number of representation slots, dependence on operation order, and existence of a determinant identity. No supplied rule converts one into the others.

**Next dependency:** [Capstone](capstone.md) assembles these finite computations and the source-premise ledger into one auditable model.
<!-- END: lesson-07 -->

