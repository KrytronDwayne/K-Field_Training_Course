"""Author/recover course artifacts; standard library only, no source copies."""
from pathlib import Path
import json, hashlib
D=Path(__file__).resolve().parent
packet=json.loads((D/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(name,text): (D/name).write_text(text.strip()+'\n',encoding='utf-8')
def dump(name,obj): write(name,json.dumps(obj,indent=2,ensure_ascii=False))
def digest(name): return hashlib.sha256((D/name).read_bytes()).hexdigest()
lessons={}
lessons[1]='''# Lesson 01 — Symmetry as an operation with a rule

**Essential question:** What must an operation preserve before we call it a symmetry?

**Goals:** Apply and compose tuple rules; identify identity and inverse operations; test closure and two declared invariants.

**Bridge and pacing:** You can substitute numbers into formulas and square signed numbers. An ordered tuple is a list whose positions have names: (2,5) differs from (5,2). No abstract algebra is assumed. One 55-minute period: retrieval 5, explanation/example 20, practice 15, diagnostics/repair 15 minutes.

## C13.01-E1 — Rules before names

A carrier is the collection of objects on which a rule acts. For example, the carrier of ordered real pairs contains (2,5), (-1,0), and pairs with fractions. A transformation assigns one output pair to each input pair. The swap rule R(x,y)=(y,x) uses the same input values in reversed positions. The identity I(x,y)=(x,y) leaves every pair unchanged.

Composition means applying one rule and then another. In FG, apply G first and F second. The result must again be a rule on the same carrier. An inverse undoes a rule on every input. Swapping twice restores the original pair, so R is its own inverse. Closure means that every composition of listed operations is still on the list. Checking one numerical input is useful, but a rule about all pairs needs symbolic substitution: R(R(x,y))=R(y,x)=(x,y).

An invariant is a specified quantity unchanged by the operation. Here the sum x+y and squared norm x²+y² are invariant under swapping. The squared norm is found by squaring each component and adding; it is the square of Euclidean length. These coordinates are dimensionless. Symmetry is always relative to a carrier and structure being preserved; a word or a matching shape alone is insufficient.

A closed set with identity, inverses, and associative composition is called a group. Function composition is associative because either grouping performs the same sequence of rules. We will only need small operation tables, not a general group theory course.

## C13.01-W1 — A fully worked two-operation table

For the pair (2,5), R gives (5,2). Both have sum 7 and squared norm 4+25=29. Compose symbolically to get II=I, IR=R, RI=R, RR=I. The entire table is therefore:

| Left operation after top operation | I | R |
|---|---|---|
| I | I | R |
| R | R | I |

Every entry is I or R, proving closure. I has inverse I; R has inverse R. Preserve the input and rule name if you want to reconstruct the input from a transformed record.

> **Scope:** This is an exact finite mathematical example, not a detector observation. The source's root structure is introduced later; no physical mechanism has been assigned here.

## C13.01-P1 — Try a cycle, then check

On real triples define T(x,y,z)=(z,x,y). Apply T repeatedly to (1,2,3). Complete the composition table for I,T,T² and check the sum and squared norm at each stage. T² means T applied twice, not componentwise squaring.

**Worked practice answer:** The sequence is (1,2,3) → (3,1,2) → (2,3,1) → (1,2,3). For arbitrary symbols the third application also restores (x,y,z), so T³=I. Exponents add under composition. Remove complete groups of three applications: T⁴=T. This is addition modulo 3, meaning equal remainders after division by 3.

| After | I | T | T² |
|---|---|---|---|
| I | I | T | T² |
| T | T | T² | I |
| T² | T² | I | T |

All entries belong to the list. The inverse of T is T², and the inverse of T² is T. Each triple has sum 6 and squared norm 1+4+9=14. More generally, moving the terms of a sum does not change either invariant.

## Diagnostic checks

1. **C13.01-D1:** Is {I,T} closed? Give a counterexample and state the missing information in a claim that merely says “this is a symmetry.”
2. **C13.01-D2:** Apply R twice to (-2,4). Check its sum and squared norm.
3. **C13.01-D3:** What is T⁵? What is its inverse within the three-operation set?
4. **C13.01-D4:** Does the rule H(x,y)=(x+1,y-1) preserve the sum and squared norm on (2,5)? Is preserving one quantity enough to claim all quantities are preserved?

**Worked answers:** 1. TT=T² is missing. State a carrier, rule, composition, and intended invariant. 2. (-2,4) → (4,-2) → (-2,4); sum 2, squared norm 4+16=20. 3. Remove three applications: T⁵=T²; its inverse is T. 4. H(2,5)=(3,4); sum remains 7, but squared norm changes from 29 to 25. A symmetry of the sum need not preserve Euclidean length. This distinction prepares the side transfer.

**Next dependency:** [Lesson 02](lesson-02.md) uses a sum-preserving transfer whose difference changes.
'''
lessons[2]='''# Lesson 02 — Side transfers and the A1 pattern

**Essential question:** Why does moving one unit between two sides change their difference by two?

**Goals:** Derive and reverse side coordinates; check integer compatibility; compute the A1 parity class while retaining full information.

**Bridge and pacing:** Lesson 01 distinguished preserving a sum from preserving all quantities. Here the carrier is ordered integer side carries (C_b,C_c). A carry is a signed integer entry retained by the source's recursive description; it need not be positive. Two 55-minute periods, each with 5 minutes retrieval, 20 instruction/example, 15 practice, 15 diagnostic repair. Period A teaches transfers and inversion; period B teaches congruence and reconstruction.

## C13.02-E1 — Sum, difference, and recoverability

Define S=C_b+C_c and A=C_b-C_c. Add these equations to obtain S+A=2C_b. Subtract the second from the first to obtain S-A=2C_c. Thus C_b=(S+A)/2 and C_c=(S-A)/2. This is a change of coordinates, not information removal.

For integer carries both halves must be integers. This happens exactly when S and A are both even or both odd. “Same parity” means this shared remainder upon division by 2. If one is even and the other odd, their sum and difference are odd and division by 2 gives half-integers.

The native transfer is (C_b,C_c) → (C_b+1,C_c-1). Its output sum is C_b+1+C_c-1=S. Its output difference is C_b+1-(C_c-1)=A+2. The reverse transfer changes A by -2. After an integer k of forward transfers (negative k means reverse), the pair is (C_b+k,C_c-k), and A becomes A+2k.

Write Z for all integers. In the difference coordinate, the allowed weight values form P₁=Z and the transfer displacements form Q₁=2Z, the even integers. Here the A1 root steps are +2 and -2. A quotient groups values together when their difference is an allowed displacement. Thus P₁/Q₁ has two classes, even and odd, often written Z₂. Congruence A≡r mod 2 means A-r is divisible by 2. A negative example is -3≡1 mod 2, because -3-1=-4=2(-2).

Retain A=r+2k with r chosen from {0,1}, plus S. For A=-3, r=1 and k=-2. The class r alone cannot recover A. Also, at a fixed S, only the class compatible with that S occurs; the two-class statement concerns P₁ across both parities of S. This prevents counting two parity options on a single fixed-sum line when only one is allowed.

## C13.02-W1 — Transfer an odd difference

Start with (C_b,C_c)=(2,1). Then S=3 and A=1. Forward transfer gives (3,0), so S'=3 and A'=3. The sum stayed fixed; the difference rose by 2. Both differences have remainder 1. Initially A=1+2(0); finally A'=1+2(1). Decoding the final coordinates gives ((3+3)/2,(3-3)/2)=(3,0). Reverse by (-1,+1) to recover (2,1). Its squared norm changes from 5 to 9: the transfer is a symmetry of S, not of that squared norm.

> **Source scope:** S02 /backbone_sequence/5/side_modes and /backbone_sequence/8, plus /proof_nodes/54/formula (KFM-X020), ground these definitions. The finite derivation is checked here. A1 carry parity is not detector antipodal parity. No rounding or half-open cell rule is used in this lesson.

## C13.02-P1 — Transfer and reconstruct a negative example

Starting from (-1,3), calculate S,A, apply one forward transfer, and retain the parity class together with enough information to undo it. Then test the incompatible candidate S=1,A=0.

**Worked practice answer:** Initially S=2, A=-4=0+2(-2). The output is (0,2), with S'=2 and A'=-2=0+2(-1). The class is even at both stages. Store S=2, r=0, k=-2 for the input and the transfer count +1. Decode A=-4, then C_b=(2-4)/2=-1 and C_c=(2+4)/2=3. For S=1,A=0 the inverse gives (1/2,1/2), so this is not an integer carry record.

## Diagnostic checks

1. **C13.02-D1:** What does keeping only A mod 2 lose? Does carry parity determine detector parity?
2. **C13.02-D2:** Decode S=-1,A=3 and apply the reverse transfer.
3. **C13.02-D3:** Write A=-5 as r+2k using r∈{0,1}. Is it in the same class as A=7?
4. **C13.02-D4:** With S=4, can an integer carry pair have A=3? Explain using the inverse formulas.

**Worked answers:** 1. It loses the even displacement 2k; keep k and S or the original pair. Detector parity requires its own rule and carrier. 2. (C_b,C_c)=(1,-2); reverse gives (0,-1), with S=-1,A=1. 3. -5=1+2(-3). The difference 7-(-5)=12 is even, so both are odd. 4. No: (4+3)/2=7/2 and (4-3)/2=1/2 are not integers.

**Next dependency:** [Lesson 03](lesson-03.md) expands the transfer idea to three channels and a plane.
'''
lessons[3]='''# Lesson 03 — Three channels and the A2 plane

**Essential question:** What shape do unit transfers among three channels generate?

**Goals:** Draw and enumerate the six roots; compute dot products and Cartan entries; reconstruct any integer zero-sum triple using two simple roots.

**Bridge and pacing:** The two-side transfer added one unit and removed one. With three ordered channels, a transfer still has zero total change. Two 55-minute periods with 5 retrieval, 20 instruction/example, 15 practice, and 15 diagnostics each. Period A builds the plane and drawing; period B teaches dot products and reconstruction.

## C13.03-E1 — A plane inside triples

Let e₁=(1,0,0), e₂=(0,1,0), and e₃=(0,0,1). These are basis vectors: each identifies one channel. Add triples component by component and multiply them by numbers component by component. A unit transfer from channel j to channel i is e_i-e_j. It has one +1, one -1, and one zero. The six choices with i≠j form the A2 roots:

| Root | Triple |
|---|---|
| α₁=e₁-e₂ | (1,-1,0) |
| α₂=e₂-e₃ | (0,1,-1) |
| α₁+α₂=e₁-e₃ | (1,0,-1) |
| -α₁ | (-1,1,0) |
| -α₂ | (0,-1,1) |
| -(α₁+α₂) | (-1,0,1) |

Every listed sum is zero. All real triples with x+y+z=0 form a plane H. Two coordinates may be chosen freely, while z=-x-y is forced. All *integer* triples in H form the root lattice Q₂. A lattice consists of integer combinations of its generating vectors. The six roots are the shortest nonzero vectors of this lattice in the dot product below; the lattice also contains longer vectors and zero. “Root” and “root-lattice vector” are different descriptions.

For v=(x,y,z) and w=(p,q,r), define v·w=xp+yq+zr. Multiply matching coordinates, then add. The squared norm is v·v. This is the ordinary Euclidean dot product on an abstract dimensionless channel space, not the Cell3 metric M_cell. A negative dot product is allowed; a squared norm is never negative.

To draw H on paper while preserving this dot product, place α₁ at the arrow (√2,0) and α₂ at (-1/√2,√(3/2)) in ordinary horizontal/vertical drawing coordinates. A square root √a is the nonnegative number whose square is a. These arrows have squared lengths 2 and dot product -1. Plot their sum and the three negatives. The result is a six-vertex hexagon around the origin. Alternatively, plot coefficient pairs (m,n) for mα₁+nα₂ as (1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1); this is a useful coordinate chart but ordinary square-paper distances in that chart are not the root metric. Label which drawing convention you use.

The Cartan matrix is a compact table of normalized dot products. Our convention is C_ij=2(α_i·α_j)/(α_j·α_j). The denominator is the squared norm of the column root. No matrix multiplication is required to fill this table.

## C13.03-W1 — Compute and reconstruct

α₁·α₁=1²+(-1)²+0²=2. Likewise α₂·α₂=2. Their cross dot product is 1×0+(-1)×1+0×(-1)=-1. Therefore C₁₁=2×2/2=2, C₁₂=2×(-1)/2=-1, C₂₁=-1, C₂₂=2. The matrix is [[2,-1],[-1,2]].

For q=(2,-3,1), take 2α₁-α₂=(2,-2,0)+(0,-1,1)=(2,-3,1). In general mα₁+nα₂=(m,-m+n,-n). For a zero-sum q=(x,y,z), choose m=x,n=-z. The middle component becomes -x-z=y, so every integer zero-sum triple is obtained. The coefficients are unique because the first and third components determine them.

> **Source scope:** S02 /backbone_sequence/8 and /proof_nodes/63/formula (KFM-X021). The calculations establish the finite abstract root datum. They neither substitute a physical metric nor identify a detector action.

## C13.03-P1 — Build the atlas entry

Reconstruct (-1,3,-2), calculate the squared norm of α₁+α₂, calculate α₁·(α₁+α₂), and check the sums of the six roots. Fill the Cartan table yourself before looking back at the example. Draw the six roots as arrows in the length-preserving paper coordinates taught above; label each tip with its triple. Check opposite pairs and equal distances from the origin.

**Worked practice answer:** The coefficients are m=-1,n=2. Thus -α₁+2α₂=(-1,1,0)+(0,2,-2)=(-1,3,-2). Its squared norm is 1+9+4=14. The summed root is (1,0,-1), squared norm 2. Its dot product with α₁ is 1+0+0=1. Each root has one +1 and one -1, hence sum zero. The Cartan entries are 2,-1,-1,2 by the four products above. The drawing tips for α₁,α₂,α₁+α₂ are (√2,0),(-1/√2,√(3/2)),(1/√2,√(3/2)); their negatives supply the other three tips. Label these respectively (1,-1,0),(0,1,-1),(1,0,-1) and their negatives. Each tip has squared distance 2 from the origin. This is a regular hexagon. In the coefficient chart the six listed points also come in opposite pairs, but square-paper distances there are not the root metric.

## Diagnostic checks

1. **C13.03-D1:** Is (1/2,-1/2,0) in H? In Q₂? Explain.
2. **C13.03-D2:** Express (3,-1,-2) in simple roots and check every coordinate.
3. **C13.03-D3:** Is (2,-2,0) a root, a root-lattice vector, or neither? Compute its squared norm.
4. **C13.03-D4:** Calculate α₂·(α₁+α₂). Why must the Cartan diagonal equal 2 here?

**Worked answers:** 1. It sums to zero, so is in H, but has noninteger entries, so is not in Q₂. 2. 3α₁+2α₂=(3,-3,0)+(0,2,-2)=(3,-1,-2). 3. It is 2α₁ in Q₂, with squared norm 8; it is not one of the six roots. 4. 0×1+1×0+(-1)×(-1)=1. Each diagonal is twice a nonzero squared norm divided by itself.

**Next dependency:** [Lesson 04](lesson-04.md) adds fractional weights to the same plane without confusing them with roots.
'''
lessons[4]='''# Lesson 04 — Roots, weights, and quotient labels

**Essential question:** How can three channel weights belong to one quotient class?

**Goals:** Center channel vectors; derive the three-class test; preserve the full weight while making a quotient view.

**Bridge and pacing:** Lesson 03 built the integer zero-sum lattice Q₂. We now enlarge the allowed points while keeping the same plane. Two 55-minute periods, each with 5 retrieval, 20 explanation/example, 15 practice, 15 diagnostics. Period A teaches centering; period B teaches quotient membership and addition.

## C13.04-E1 — Centering and a larger lattice

The three channel vectors each have sum 1. Subtract the common mean vector h=(1/3,1/3,1/3) to put each in H. Define u_i=e_i-h. Then u₁=(2,-1,-1)/3, u₂=(-1,2,-1)/3, u₃=(-1,-1,2)/3. A fraction outside parentheses divides every entry. Their sum is zero, so u₃=-u₁-u₂. Differences are unchanged by subtracting the same h: u₁-u₂=e₁-e₂=α₁. To recover a channel vector, retain h and add it back. For a general triple v, retain its mean μ=(v₁+v₂+v₃)/3 along with v-μ(1,1,1).

Define the weight lattice P₂ to be all a u₁+b u₂ with integers a,b. In this course “weight” refers to these abstract vectors, not physical mass. Expanding gives

a u₁+b u₂=((2a-b)/3,(-a+2b)/3,-(a+b)/3).

This vector is integral exactly when a+b is divisible by 3. Necessity follows from its last component. For sufficiency, write a+b=3k. Then the first component is a-k, the second b-k, and the third -k, all integers. The sum is already zero. Conversely, any integer zero-sum (x,y,z) is in P₂: choose a=x-z,b=y-z. The displayed formula returns (x,y,z). Therefore Q₂ is exactly the integral part of P₂.

Two weights share a quotient class if their difference lies in Q₂. Their labels are the remainder of a+b after division by 3, chosen from {0,1,2}. Equal remainders make their coefficient-sum difference divisible by 3, precisely the condition just proved. This produces P₂/Q₂ with three classes, called Z₃. Adding weights adds coefficient sums, so class addition is remainder addition modulo 3. For example, 2+2 has remainder 1. Negative sums follow the same rule: -1=2+3(-1).

Keep the coefficients (a,b), not just the class. They reconstruct the vector exactly. Alternatively retain a chosen representative r u₁ and the full root-lattice displacement q=w-r u₁. Here r is the class label. Recording only r loses q; the quotient is a useful view, not a replacement for the original.

## C13.04-W1 — Representatives and channel differences

u₁ and 2u₁ are not integral: their first components are 2/3 and 4/3. But 3u₁=(2,-1,-1) is integral and zero-sum, hence in Q₂. Representatives 0,u₁,2u₁ have labels 0,1,2. Also u₁-u₂=(1,-1,0)=α₁. Thus u₁ and u₂ have the same label despite being different vectors. For u₃=-u₁-u₂ the coefficient sum is -2≡1 mod 3. All three channel weights lie in class 1. Their sum is zero, consistent with 1+1+1≡0.

> **Source scope:** S02 /backbone_sequence/8 and KFM-X021 give the centered weights and quotient. The divisibility proof here supplies an elementary reconstruction. “Three channel weights” and “three quotient classes” count different objects.

## C13.04-P1 — Compute before classifying

Find u₁+u₂ and 2u₁+u₂, their class labels, and u₂-u₁. For each result keep coefficients and identify whether it belongs to Q₂. Give a representative-plus-displacement record for u₁+u₂.

**Worked practice answer:** u₁+u₂=(1,1,-2)/3 has coefficients (1,1), sum 2, label 2, and is not integral. Relative to representative 2u₁, its displacement is u₂-u₁=(-1,1,0)=-α₁. Thus w=2u₁-α₁ reconstructs it. Next, 2u₁+u₂=(1,0,-1)=α₁+α₂ has coefficients (2,1), sum 3, label 0, and lies in Q₂. Finally u₂-u₁ has coefficients (-1,1), sum 0, label 0, and is a root. Adding it to u₁ changes the vector to u₂ without changing label 1.

## Diagnostic checks

1. **C13.04-D1:** Are u₁,u₂,u₃ representatives of three different quotient classes? What does a root step preserve and what does it change?
2. **C13.04-D2:** Find the coordinates and label of -u₁. Is it in Q₂?
3. **C13.04-D3:** For a=4,b=-1, find the vector and class. Reconstruct it from α₁,α₂.
4. **C13.04-D4:** If only class 2 is retained, can you distinguish 2u₁ from u₁+u₂? What extra record suffices?

**Worked answers:** 1. No, all have label 1. A root step changes the weight vector but preserves its class. 2. (-2,1,1)/3, class -1≡2; it is not integral. 3. (3,-2,-1), label 0 because 4-1=3; it equals 3α₁+α₂. 4. No. Keep (a,b), or representative 2u₁ together with displacement 0 or -α₁, respectively.

**Next dependency:** [Lesson 05](lesson-05.md) distinguishes these weights from other objects that also happen to carry three entries.
'''
lessons[5]='''# Lesson 05 — Primitive lifts and role separation

**Essential question:** When do identical-looking triples describe different things?

**Goals:** Decode and reconstruct a compatible address lift; distinguish 27 lift choices from three primitive channels; keep family, ray, and parity fields independently typed.

**Bridge and pacing:** Lesson 04 showed that a quotient label loses a displacement unless both are retained. Address reduction has the same bookkeeping need, but its carrier is different. One 55-minute period: 5 retrieval, 20 explanation/example, 15 practice, 15 diagnostics.

## C13.05-E1 — A record must say what its fields mean

The source keeps three ordered primitive-lift channels. For our finite model, represent channel identity by the formal basis e₁,e₂,e₃. “Formal” means that these symbols designate slots; they are not measured spatial directions. Each has sum 1; differences have sum zero. Centering gives u₁,u₂,u₃ from Lesson 04. The source's assertion about its full compiler is a source-reported contract; we use its finite channel model without running that compiler.

An address residue is another kind of triple. Modulo 3, we choose each component's representative from {0,1,2}. A compatible next-level lift of the residue ρ has the form ℓ=ρ+3v, where the balanced lift digit v has three entries in {-1,0,1}. Reduction of ℓ modulo 3 returns ρ because each added entry is divisible by 3. Given the representative ρ and ℓ, recover v=(ℓ-ρ)/3 componentwise. The source's general formula uses 3ⁿ; here we explicitly teach the n=1 instance. These choices represent next-level addresses modulo 9. There are 3×3×3=27 choices because each of three digit positions has three independent choices. Distinct digits give distinct lifts modulo 9: a digit difference in {-2,-1,0,1,2} cannot be a nonzero multiple of 3.

These 27 choices are not 27 primitive channel types. A particular digit need not sum to zero: v=(1,1,1) is allowed. Thus not every address-lift displacement is a root-lattice vector. The examples with zero-sum digits simply make comparison with Lesson 03 easy.

| Field | Meaning | What must remain separate |
|---|---|---|
| e_i; centered u_i | Formal channel; its centered weight | Address digit and spatial direction |
| ρ,v,ℓ | Residue, retained digit, reconstructed address | Three primitive channel types |
| F2 | An arbitrary family tag in our synthetic record | A number inferred from a quotient |
| [r_a:r_b:r_c] | Ratios representing a projective ray | Primitive channel basis |
| detector parity p | Sign under a specified antipodal detector operation | A1 integer remainder and family tag |

A projective ray records ratios: [1:2:3] and [2:4:6] label the same ray under positive rescaling. We use the source's positive-scale, oriented-ray convention here: negative multiples are not silently identified. In ordinary unoriented projective coordinates any nonzero common rescaling is identified, so its sign convention must be declared separately. If you replace an actual triple by a ratio view, also retain the removed scale to reconstruct it. Here the ray entries are supplied independently; no physical ray constants are being calculated. Detector parity +1 means a specified signal is unchanged under the detector's antipodal map; -1 means it changes sign. For example, a synthetic scalar function f(t)=t under t→-t has odd parity -1, whereas g(t)=t² has even parity +1. Arbitrary signals need not have a single definite parity. A parity tag does not recover a signal's values.

## C13.05-W1 — A lift and a channel difference

e₁-e₂=(1,-1,0)=α₁, and e₁-h=u₁, e₂-h=u₂. Separately take address residue ρ=(1,0,0) and digit v=(0,1,-1). Then ℓ=(1,0,0)+3(0,1,-1)=(1,3,-3). The last entry -3 has residue 0 because -3=0+3(-1). Reduction returns (1,0,0); decoding the digit gives ((1,3,-3)-(1,0,0))/3=(0,1,-1). This does not generate a new face-area ratio.

> **Source scope:** S02 /backbone_sequence/8/type_guards and /proof_nodes/58/formula (KFM-X014) distinguish primitive channels, compatible address lifts, and projective coordinates. Family tag F2, illustrative rays, and detector functions here are synthetic independent fields, not empirical assignments. Projective signs, chirality, and dyadic recursion receive no identification from this arithmetic.

## C13.05-P1 — Retain the entire record

Use ρ=(1,0,0), v=(-1,0,1), family tag F2, ray [1:2:3] with scale 2, and an independently supplied odd detector channel f(t)=t. Compute and reduce ℓ. State which data reconstruct the address, scaled ray, and detector values.

**Worked practice answer:** ℓ=(-2,0,3). Since -2=1+3(-1), its residue is (1,0,0). Store both ρ and v; their sum ρ+3v reconstructs ℓ. The scaled ray is (2,4,6), reconstructed from scale 2 and representative (1,2,3). The detector parity is -1 since f(-t)=-f(t); retaining f and t is still needed for values. Neither the family tag F2 nor this parity follows from a carry remainder or weight label. Do not overwrite any of these fields with another.

## Diagnostic checks

1. **C13.05-D1:** Why do 27 compatible address lifts not imply 27 primitive channels? Are primitive channels the projective ray coordinates?
2. **C13.05-D2:** For ρ=(1,0,0), v=(1,1,1), compute ℓ and its sum. Must every lift stay in a sum-one plane?
3. **C13.05-D3:** Recover v from ℓ=(1,-3,3),ρ=(1,0,0). Does keeping ρ alone suffice?
4. **C13.05-D4:** A record has carry A=2 and family F2. Can you infer odd or even detector parity? Give a finite reason.

**Worked answers:** 1. They count digit choices versus basis-channel slots, respectively; equal tuple lengths do not equate their roles. 2. ℓ=(4,3,3), sum 10; no, the digit has sum 3, not zero. 3. v=(0,-1,1); ρ alone leaves 27 choices at this level. 4. No. The independent synthetic detector functions f(t)=t and g(t)=t² have opposite parities while the supplied carry and family fields can remain identical.

**Next dependency:** [Lesson 06](lesson-06.md) asks for an explicit map before relating different carriers.
'''
lessons[6]='''# Lesson 06 — From a geometric pattern to an action

**Essential question:** What additional evidence turns a matching pattern into a specified action?

**Goals:** Verify the cyclic action on H and its roots; read its permutation matrix; test whether a supplied map respects two actions.

**Bridge and pacing:** Lesson 01 taught cycles; Lessons 03–05 supplied the root plane and distinct carriers. We can now say exactly where a symmetry acts. One 55-minute period: retrieval 5, instruction/example 20, practice 15, diagnostic repair 15 minutes.

## C13.06-E1 — Specify the carrier, operation, and map

Use H={(x,y,z):x+y+z=0} as the carrier and T(x,y,z)=(z,x,y) as the operation. An action assigns each operation a transformation of the carrier, consistently with composition and identity. The three-operation table of Lesson 01 supplies this consistency: I acts as identity and three applications of T return every input.

A matrix is a rectangular table of numbers encoding a linear rule. For column triples the matrix of T has rows (0,0,1),(1,0,0),(0,1,0). To apply a matrix, take the dot product of each row with the input column. The first output is 0x+0y+1z=z, the second x, the third y. The identity matrix has rows (1,0,0),(0,1,0),(0,0,1). Matrix composition means performing the corresponding rules in succession. A transpose swaps rows and columns; here Tᵀ sends (x,y,z) to (y,z,x), so it is T² and TᵀT=I.

For any v=(x,y,z), w=(p,q,r), Tv·Tw=zr+xp+yq=v·w. This proves preservation of all dot products, not only the norm of one example. Also the sum of Tv is z+x+y, so H is preserved. An invariant subset is a set whose members remain inside it under the operation; we will verify the root set has this property.

Suppose a second carrier Y has an operation U. A proposed identification f:H→Y must specify an actual rule, not just claim that both diagrams have six points. The condition f(Tv)=U(f(v)) says that transform-then-map equals map-then-transform. Such a map is called an intertwiner. If claiming a full identification of carriers, also show f is one-to-one and onto, or specify the intended restricted part. “One-to-one” means distinct inputs never share an output; “onto” means every intended target is reached.

For a finite taught example, use Y=H, f(v)=2v and U=T. Then f(Tv)=2Tv=T(2v)=U(f(v)) because T only moves coordinates. The inverse f⁻¹(w)=w/2 proves a full carrier identification on H. However f doubles lengths, so it does not identify the metric without a scale conversion. On Q₂, the same map is not onto Q₂: α₁/2 is not integral. Claims must state which carrier and structure they concern.

## C13.06-W1 — Trace the roots

Tα₁=T(1,-1,0)=(0,1,-1)=α₂. Tα₂=T(0,1,-1)=(-1,0,1)=-(α₁+α₂). Applying T again to that third root gives (1,-1,0)=α₁. The negatives form the other cycle because T(-v)=-T(v). Thus all six roots are permuted. T³=I and TᵀT=I certify the cycle and metric preservation on the stated carrier.

> **Scope:** This finite action is derived and explicitly verified. S02 /backbone_sequence/8 supplies the root datum, not an empirical detector intertwiner. A physical assignment needs its own target carrier, mapping, operations, and invariants. The missing physical identification remains an unresolved question, not a hidden premise.

## C13.06-P1 — A vector orbit and a map test

Apply T three times to q=(2,-3,1). Write the three matrix rows of T and multiply them by the column q. Express the first result using simple roots, check squared norm at each step, and test f(Tq)=T(f(q)) for f(v)=2v. Retain q alongside its weight quotient label.

**Worked practice answer:** q → (1,2,-3) → (-3,1,2) → q. The matrix rows (0,0,1),(1,0,0),(0,1,0) have dot products 1,2,-3 with q, giving the same first output. The first image equals α₁+3α₂=(1,-1,0)+(0,3,-3)=(1,2,-3). All squared norms equal 14 because the squared entries 4,9,1 are rearranged. The left map path gives 2(1,2,-3)=(2,4,-6); the right path gives T(4,-6,2)=(2,4,-6). Every orbit vector is integral and zero-sum, hence class 0 in P₂/Q₂. Store q and the operation exponent: class 0 alone does not reconstruct the orbit point.

## Diagnostic checks

1. **C13.06-D1:** A different device diagram resembles A2. What must be supplied to claim that its operation is the action just studied?
2. **C13.06-D2:** Use the matrix rows to evaluate T(-1,3,-2), then check sum and squared norm.
3. **C13.06-D3:** Let Y=H, U=I, and f(v)=v. Does f intertwine T with U? Test α₁.
4. **C13.06-D4:** Does f(v)=2v identify the six-root set with itself? Explain the difference from identifying H with H.

**Worked answers:** 1. A target carrier, target operation U, explicit map f, and a check f(Tv)=U(f(v)), with any metric conversion and reconstruction rule. Numerical resemblance alone supplies none of these. 2. (-2,-1,3), sum 0, squared norm 4+1+9=14. 3. No: f(Tα₁)=α₂ but U(f(α₁))=α₁. 4. No: 2α₁ is not a root. On real H division by 2 is available, so f is bijective there; the claim changes when the carrier changes.

**Next dependency:** [Capstone](capstone.md) combines the six lessons into a transfer atlas. No additional mathematics is required.
'''
for n,body in lessons.items(): write(f'lesson-{n:02}.md',body)
print('Authored six complete lessons')
