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
