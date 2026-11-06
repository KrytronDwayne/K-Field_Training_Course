# Lesson 07 — A complete premise ledger

**Essential question:** Which parts of a result were supplied, chosen, or proved?

**Goals:** Classify five premise roles; build a complete action/phase ledger; identify missing replay inputs without inventing them.

**Prerequisite bridge.** The earlier lessons supplied all finite operations: action substitution, residual reconstruction, frame changes, phase products, tensor-basis reading and charge pairing. This lesson organizes those dependencies so that a numerical result cannot conceal a missing premise.

## C19.07-E1 — Five roles and an evidence column

A **locked root** is an input held fixed by the chosen source/version, such as the locked Cell3 geometry. A **theorem** is an implication derived from stated premises, such as integral pairing under Lesson 06's contract. A **constitutive rule** specifies how a model combines quantities, such as our chosen finite action. A **domain condition** restricts allowed cases, such as Δt>0 or a declared admitted-sector set. A **state coordinate** gives a value within that domain, such as q_1 or a boundary value. Roles concern use in an argument; they are not measures of truth. The same numerical coefficient can be a supplied state/model parameter while its positivity is a domain condition.

Keep evidence status separately: source fact, freshly checked finite implication, declared teaching assumption, interpretation, proposed mechanism, reference-theory comparison or unresolved input. Calling a sentence a theorem in an archive does not show that its proof has been loaded and replayed. A ledger row should include object, role, value or restriction, units/type, source pointer or example ID, and verification status.

The named trace-conjugation identity provides a small bridge from Lesson 03. For a square table A, Tr(A) is the sum of diagonal entries. Matrix multiplication uses (AB)_ij=Σ_k A_ik B_kj. Thus Tr(AB)=Σ_iΣ_k A_ik B_ki=Σ_kΣ_i B_ki A_ik=Tr(BA), because finite scalar sums may be reordered. If G has an inverse, Tr(GPG^−1)=Tr(PG^−1G)=Tr(P). This is a finite derived identity with a stated invertibility condition. It does not certify an unavailable source operator. No numerical matrix problem is assigned.

## C19.07-W1 — Classify a packet

| Object | Role in this argument | Scope and retained record |
|---|---|---|
| Source M_cell=BᵀB | Locked geometric input | Locked basis/version; not a numerical toy coefficient |
| Trace conjugation | Derived finite theorem | Finite square matrices and invertible G; derivation above |
| Toy action S=Σ(K−V) | Constitutive rule | Synthetic, left-endpoint convention |
| k>0,vpot>0,Δt>0 | Domain conditions | Restrict toy input values |
| k=2 AU·TU,vpot=2 AU/TU,Δt=1 TU | Supplied model/state inputs | Values retained independently of their positivity |
| q=(1,2,2) | State coordinates | Ordered values; endpoints fixed at 1 and 2 |
| a=(0,−4),m=(1,−4),r=(−1,0) AU | Derived finite records | a=m+r; retain each vector |
| Six labeled phases from P1 | State inputs in declared bases | UV,light,reg,heavy,cap,induced all retained |
| τ(E)=1 | Declared reading rule | Combined line basis and τ are part of specification |
| Admitted set {a,b} | Domain condition | Synthetic membership assumption |
| Boundary-sector values | State coordinates | Values within the declared domain, not its membership rule |

Locked geometry notation remains typed: M_cell is the Cell3 Gram metric and R_cell its inverse; G_phase and G_eff are distinct phase/effective metrics. B is the ordered source-locked basis; any row/column representation must be stated. This course performs no geometry substitution. If such a substitution is later added, preserve the ICRS columns [a b c], negative determinant, half-open cells and affine origin; an action symbol M alone does not authorize silently replacing it by a convenient metric.

## C19.07-P1 — Guided missing-input audit

A packet supplies q, k, vpot and five phase values, but omits induced, Δt, τ and the admitted-sector list. Can you finish it by assuming 1 for each absent item? Restore a complete **toy** record from earlier practice, and identify what still cannot be restored for the full source.

**Worked answer:** No. Missing is not a unit factor or a known duration. For the declared toy recover Δt=1 TU; q=(1,2,2); k=2 AU·TU; vpot=2 AU/TU; left endpoint convention; a=(0,−4) AU; m=(1,−4) AU; r=(−1,0) AU. Restore (−1,i,i,1,−i,i) in the six-label order and τ(E)=1. Restore the explicitly assumed admitted set {a,b}, with the complete phase rows of Lesson 06 when auditing that sector example. Do not attach one row to a different sector without a declaration. The full source still requires operator coefficients, typed topology carriers, actual boundary-sector values and time/action normalization; toy values do not supply them. Record S02 M15 and S03 AUD-009 pointers and the unresolved replay status.

**Role-classification practice:** Classify the locked M_cell, trace-conjugation identity, chosen toy action, condition Δt>0, assumed membership set {a,b}, and endpoint q_0=1. **Answer:** M_cell is a locked root in this ledger; trace conjugation is a derived theorem under its finite-square/invertible hypotheses; the toy action is a constitutive rule; Δt>0 and the membership set are domain conditions; q_0=1 is a state coordinate. The value Δt=1 TU is an input distinct from the condition Δt>0. These roles do not themselves establish evidence status.

> **Claim scope.** Source-reported architecture, finite proved identities and declared toy inputs occupy separate evidence columns. No measurement or physical mechanism is introduced by this bookkeeping. Source missing bodies retain the source's `VERIFIED_NOT_LOADED` gate label; that label is not a fresh verification by this course. Do not merge a mathematical-backbone module with a compiler label or promote dimension matching to an intertwiner proof.

## Diagnostics

1. **C19.07-D1:** What should a ledger do with a missing proof body or determinant factor?
2. Classify q_0=1, the condition Δt>0, and the identity a=m+r.
3. Why is “coefficient positive” different from “coefficient equals 2”?
4. Can an audit remove sector b because its closure residual is −2?

**Worked answers:** (1) Mark the object and retrieval gap explicitly; do not fabricate a replacement or claim replay. (2) State coordinate, domain condition, and derived identity under r=a−m. (3) Positivity restricts admissible values but does not supply one; the numerical value is a separate input with units. (4) No: b remains in the supplied domain. Preserve the residual and identify which conditions fail.

**Next dependency:** [Capstone](capstone.md) audits a complete finite packet and a deliberately incomplete one.
