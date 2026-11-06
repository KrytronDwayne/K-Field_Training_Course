# Lesson 6 — Certificates and precision residuals

**Essential question:** What can a certificate establish when its inputs or precision rules are missing?

**Goals:** Audit a certificate's fields; calculate a bound gap and a retained rounding residual; classify source exact claims separately from fresh replay.

**Bridge:** Lesson 5 taught lower and upper bounds under one fixed specification. A certificate packages the inputs, feasible path and argument so another reader can repeat the check. A descriptive title does not provide those objects.

Two 55-minute sessions: certificate audit, then precision and interval examples. Each: 5 retrieval, 20 explanation/example, 15 practice, 15 diagnostics/repair.

## C27.06-E1 — Read a certificate as a reproducible record

A usable route certificate identifies the objective and its units; admissible paths and constraints; fixed frame, metric and rulers; start/end and duration; the proposed path; a justified lower bound and feasible upper bound; their gap; numerical precision or interval rules; immutable source identity; and a replay procedure. If the procedure uses matrices, their entries and order must be available, not just their names. A SHA-256 digest is a content fingerprint: matching bytes produce the same digest. It establishes which file was checked, not whether the file's mathematical claims are true.

An interval [a,b) contains numbers at least a and strictly less than b. If a decimal was produced by a known truncation rule, the interval may express all original values consistent with that display. It does not make the displayed value equal to every member of the interval. Retain a reconstruction residual r=original−displayed, including its sign; then original=displayed+r. A tolerance or interval must come from a stated precision rule, not from the desire for a zero answer.

## C27.06-W1 — Compare an exact classroom certificate with source cards

Our synthetic record supplies G=[[2,1],[1,2]]L⁻², endpoints (0,0)L and (2,0)L, T=2τ, finite piecewise-constant paths without obstacles, J=ΣΔt vᵀGv, straight velocity (1,0)L/τ, L_b=U_b=4/τ, gap=0/τ, exact rational entries and the decomposition proof in Lesson 5. Recomputing the candidate cost and proof reproduces the claim. Its optional continuum extension has its own explicitly stated admissible class.

Now read these compact source cards, based on exact retrieved material [sources.md]:

| Card | What is actually supplied | What it does not supply |
|---|---|---|
| T20, whole 470-byte overview | A named quadratic-cost object and a named least-cost-certificate object, described as holding selected path, lower/upper bounds and gap | Numeric path, bounds, gap, complete objective and precision inputs |
| S02 /branch_proofs/12 | Source-reported closed exact QPC linear algebra; related formula identities | A fresh replay performed by this course |
| S03 /findings/7, AUD-008 | Missing G_phase, C, complete W_qpc; stored reconstruction residual | An interval rule authorizing treatment of that residual as a stored-precision closure coordinate |
| S03 /findings/8, AUD-009 | Missing-body status VERIFIED_NOT_LOADED | Permission to invent an absent proof body |

The stored residual is **4.58938078934712923077736690075e-12**, meaning that positive decimal times 10⁻¹². It is not literal zero. Preserve its full stored text; its source unit and interval typing must be retrieved before interpreting its size. AUD-008 requests that the matrices, units, order, precision and derivation be supplied. It does not resolve those missing fields by the act of requesting them. Our bounded exact-name search returned no matching certificate; that limited search is not proof that the certificate exists nowhere.

The source claim and present replay status can coexist: “S02 reports exact closure; this course has not loaded the full replay objects.” Do not silently replace the claim with our synthetic demonstration, and do not silently change an attributed exact claim into a claim that the source only meant “approximately equal.”

## C27.06-P1 — Practice and worked answers

Compare exact 1/3 with displayed 0.3333 under an explicitly supplied rule: truncate a positive number after four decimal places. Find the residual and allowed interval. Separately, given a candidate lower bound 3.9/τ and upper bound 4.1/τ for one fixed problem, compute the gap. Audit T20 using the checklist above.

**Answer:** 0.3333=3333/10000. Subtracting with denominator 30000 gives 1/3−3333/10000=(10000−9999)/30000=1/30000. The interval is [0.3333,0.3334); since 1/3 is larger than its lower end by 1/30000 and smaller than its upper end, it lies inside. Reconstruction is 3333/10000+1/30000=1/3, not “residual zero.” The bound gap is 4.1/τ−3.9/τ=0.2/τ. T20 supplies object names and a description of certificate fields, but the numeric entries and replay inputs remain absent from that overview. Obtain those objects with hashes before certifying a numeric source optimum. None of this toy truncation rule applies to AUD-008 unless its source explicitly adopts it.

> **Evidence scope:** These cards are source facts about retrieved records. Synthetic bounds and rational calculations are derived classroom results. The source precision bridge is unresolved. There is no claim of measured physical response here, and no retained closure coordinate is discarded.

## C27.06-D1 — Diagnostic checks

1. Is 4.58938078934712923077736690075e-12 exactly zero?
2. Does a matching hash independently prove the route optimal?
3. What does a positive upper-minus-lower gap leave unresolved?
4. Which source objects are required before exact numerical QPC route replay?

**Answers:** (1) No; retain the stored nonzero coordinate and request its typing. (2) No; it pins bytes. The mathematics still needs checking. (3) The minimum is bounded but not identified exactly by those bounds. (4) Locked G_phase, factor C, complete W_qpc, basis/order/units and their precision bridge, together with the objective, admissibility, time/endpoints, path, bounds/gap and replay procedure. A spectral-instance matrix alone is insufficient.

**Next dependency:** [Lesson 7](lesson-07.md) asks what additional observations could connect modeled cost to a detector.
