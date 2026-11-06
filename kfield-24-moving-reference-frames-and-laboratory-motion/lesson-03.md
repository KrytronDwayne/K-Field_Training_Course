# 3. The nested laboratory motion chain

Essential question: Which motions belong in a laboratory velocity?

Goals

- Name the four relative velocity terms and their shared contract.
- Compute a signed sum and a decomposed displacement.
- Recognize double counting and source-epoch gaps.

Prerequisite bridge: Begin with [Lesson 2](lesson-02.md). Use common-axis components from Lesson 2 to add relative motions.


## C24.03-E1 — A chain of relative motions

Imagine walking inside a moving train: your velocity relative to the track combines your motion relative to the train and the train's motion relative to the track, when both use the same axes and time. Our additive classroom chain extends this idea. Write v_A/B for the velocity of A relative to B. EMB means Earth–Moon barycenter, the shared mass-center reference for Earth and Moon. CMB means cosmic microwave background; the source uses a CMB comparison frame. It is not the Galactic-center drawing gauge.

In common axes, at one epoch, in m/s, use

v_lab/CMB = v_Sun/CMB + v_EMB/Sun + v_Earth/EMB + v_lab/Earth.

Each numerator is the next denominator, so intermediate reference motions are accounted for once. Here Earth means its center for the relative translational term; the laboratory term includes its motion relative to that center. A terrestrial component expressed in Earth-fixed axes must first be rotated into the common axes. The formula is the declared additive kinematic model of this course, not a derivation of relativistic velocity addition.

## C24.03-W1 — Four signed ledgers

At t0 use synthetic constant vectors (10,0,0), (0,2,0), (-1,0,0), (0,0,1) m/s, in chain order. Add coordinate by coordinate: (10+0-1+0,0+2+0+0,0+0+0+1)=(9,2,1) m/s. With x0=(1,2,3)m and two elapsed seconds, keep the four displacements:

|Term|Displacement (m)|
|---|---|
|Sun/CMB|(20,0,0)|
|EMB/Sun|(0,4,0)|
|Earth/EMB|(-2,0,0)|
|lab/Earth|(0,0,2)|

Their sum is (18,4,2)m; x(2)=(19,6,5)m. Subtract each displacement to recover (1,2,3)m. Keeping only the total would conceal the opposing x contributions.

## C24.03-P1 — Change one term

Reverse only Earth/EMB to (+1,0,0)m/s. The new total is (11,2,1)m/s and endpoint (23,6,5)m. Relative to the first endpoint the change is (4,0,0)m, because a change from -1 to +1 is +2m/s for two seconds. Keep both ledgers; do not overwrite the original.

## Source card: physical velocity

T40 admits the physical vector at `/derived_results/earth_cmb/V_E_icrs_m_s` in the linear-inertia source; T10 gives its speed. Its ICRS components are (-359003.19906581304,76679.88603400199,-44701.060100687995)m/s, with speed 369812.50200040644m/s. The inspected authority does not attach an explicit vector epoch. A publication timestamp cannot fill that field. See [sources](sources.md) for its exact path and hash.

> Scope: The four tiny classroom velocities are synthetic and do not estimate that source vector. The source vector is an already composed Earth/CMB object, not an extra independent chain term. G_phase V is a phase-transformed vector and is denied as a physical velocity by T40. An experiment-local 361.838…km/s trajectory mentioned in the blueprint is separately typed; it is not a replacement authority or a fifth term. No real propagation is assigned without its full epoch contract.

## C24.03-D1 — Diagnostics

1. Which term accounts for Earth relative to EMB?
2. Can you add Earth/CMB to Sun/CMB and EMB/Sun to improve the sum?
3. Does zero y in one term allow deletion of that term?
4. Can publication time be used as the missing vector epoch?

Answers: 1. v_Earth/EMB, including its sign. 2. No; Earth/CMB already includes upstream motions, so this double counts. 3. No: other components and the zero itself belong to the ledger. 4. No: record “not specified” and withhold real propagation. Synthetic time is declared separately.


Next dependency: [lesson-04](lesson-04.md). Carry your signed component ledger forward.
