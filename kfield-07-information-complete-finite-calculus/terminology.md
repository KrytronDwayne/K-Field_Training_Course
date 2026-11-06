# Terminology and notation

| Term/symbol | Meaning and first use |
|---|---|
| Sample ID; time | Original address versus recorded time; lesson 01. They are preserved separately. |
| SU | Synthetic signal-unit, a declared teaching unit; lesson 01. SU² denotes the product of two such units. |
| f_s, f_t; s→t | Start and end values on an oriented edge; lesson 01. |
| df | Full finite difference f_t−f_s, with the same units as f; lesson 01. |
| Rate | Finite difference divided by nonzero elapsed time; lesson 01. |
| Anchor | Retained starting value needed to decode differences; lesson 01. |
| Premise | A stated starting commitment, distinguished from a derived conclusion; lesson 01. |
| T, D, S | Transform, decoder, state in D(T(S))=S; lesson 01 premise card. |
| df dg | Signed joint finite interaction; product units; lesson 02. |
| m, d | Pair mean and signed half-difference, same units as the pair; lesson 03. Pair d is half the corresponding full edge difference. |
| E, I, Q | Fixed pair averaging, identity, and detail I−E; lesson 03. Q is not a geometric quadratic form. |
| Block support | Original sample IDs belonging to each pair; lesson 03. |
| Linear | Preserves addition and multiplication by scalar weights; lesson 04. |
| Idempotent; projection | E²=E; a linear rule with that property is a projection here; lesson 04. E² means composition E(Ef), not squaring entries. |
| Range B_coarse | Outputs of E, the block-constant arrays; lesson 04. Distinct from geometric basis B. |
| Pointwise product | Multiply entries at the same sample ID; lessons 02 and 04. |
| Subalgebra | Here, lists closed under sums, scalar multiples, pointwise products and containing 1; lesson 04. |
| Bimodule/block-factor rule | E(b_1 f b_2)=b_1 E(f)b_2 for block-constant factors; lesson 04. |
| Conditional expectation | Here, fixed finite block averaging with the stated factor property; lesson 04. No probability theory assumed. |
| qf, qg | Short names for Qf,Qg; lesson 04. |
| E_star, Q_star | Three-entry counterexample rule and I−E_star; lesson 04 only. |
| M_0,M_1; r_0,r_1 | Stage-labeled models and residual fields, not sample subscripts; lesson 05. |
| Reconstruction error | Reconstructed minus original at every ID; lesson 05. |
| K, L; psi=(u,v); j | Explicit matrix rules, input pair and output pair; lesson 06. Matrices are taught as row recipes. |
| Singular; invertible | Respectively the lesson's nonunique/unreachable-output map K; and uniquely reversible map L; lesson 06. |
| Kernel | Input changes mapped to zero; lesson 06. |
| t | Free input coordinate in lesson 06; distinct from the endpoint label t of lesson 01. |
| c; cokernel information | Compatibility coordinate j_2−2j_1 for K, recording an output obstruction; lesson 06. |
| j_fit; rho | Declared first-equation-matching output and residual (0,c); lesson 06. |
| Ledger; typed view | Replayable operation record; display with units/support/rules/source retained; lesson 07. |
| A, δ | Mean anchor and full difference of the two means; lesson 07. |

The source's geometry symbols M_cell, R_cell, G_phase, O_K and B are reserved by input-contract.json and are not used as computational variables here. Mathematical M04 and compiler M04 are not interchangeable labels. EG-A1–EG-A6 keep the exact source logical role given in lesson 01.
