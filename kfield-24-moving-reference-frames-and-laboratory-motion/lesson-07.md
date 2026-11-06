# 7. A reproducible trajectory contract

Essential question: Could another person reconstruct your trajectory?

Goals

- Write a complete synthetic trajectory input contract.
- Reconstruct an initial point from decomposed displacements.
- Identify missing real-source inputs without inventing them.

Prerequisite bridge: Begin with [Lesson 6](lesson-06.md). Combine all six earlier lessons into a reproducible input record.


## C24.07-E1 — Reproducibility is part of the result

A trajectory is a rule assigning positions to times. To repeat it, a reader needs more than its speed. A contract records what each input means, where it came from, and how to use it. UTC labels civil epochs; an elapsed second is a duration. UTC can contain leap seconds, so a real calculation must state its time conversion. TAI is an atomic time scale, TT a terrestrial time scale and TDB a barycentric dynamical time scale used in ephemeris work. These labels are not interchangeable; this course supplies no conversion constants. A real conversion must name its tables, method and version.

An ephemeris supplies celestial positions or motions as functions of time. Earth orientation parameters (EOP) describe Earth's orientation for converting terrestrial and celestial axes. A site record names latitude, longitude, height and their datum, the reference surface/convention. A geometry digest identifies exact bytes of a geometry definition; SHA-256 is the fingerprint used in our source ledger. A digest identifies a file, not a proof of its physical claims.

Record origin, axes, units, epoch/time scale, site, ephemeris/EOP versions, geometry and rotation conventions, every component velocity, update or interpolation rule, and residual/reconstruction rules. Interpolation means a declared rule for values between supplied times. “Not applicable: synthetic” differs from “unknown: required for a real calculation.”

## C24.07-W1 — A fully specified toy packet

|Field|Value|
|---|---|
|Evidence class|Synthetic definition and derived arithmetic|
|Epoch|2026-11-05T00:00:00Z|
|Duration convention|Elapsed SI seconds, 0≤t≤2s; no leap crossing in this stipulated exercise|
|Frame|F, fixed right-handed orthonormal axes and fixed origin O; no real celestial origin asserted|
|Position and velocity units|m and m/s|
|Initial point|(1,2,3)m|
|Four terms in chain order|(10,0,0);(0,2,0);(-1,0,0);(0,0,1)m/s|
|Rule|Each term constant; x(t)=x0+t(9,2,1)|
|Site; ephemeris; EOP; time conversion|Not applicable: synthetic fixed-frame definition|
|Geometry|The stated F axes; identity orientation; no Cell3 numerical geometry used|
|Residual|No measured comparison supplied; not a claim of zero physical residual|
|Reconstruction|Subtract all four signed displacements from endpoint|

At t=2s this gives (19,6,5)m. The synthetic chain labels demonstrate bookkeeping; they do not turn F into a measured astronomical trajectory.

## C24.07-P1 — Reverse and audit

Reverse the endpoint: (19,6,5)-(20,0,0)-(0,4,0)-(-2,0,0)-(0,0,2)=(1,2,3)m. Subtracting the negative Earth/EMB displacement adds 2m in x.

Now prepare a real-source card from Lesson 3. Preserve ICRS, m/s, the full three-component physical vector, source SHA-256 4651a532fe43e8091748ef4f7e28bb899e1a2ea798d689ba1724e99530cd55ab and pointer `/derived_results/earth_cmb/V_E_icrs_m_s`. Mark vector epoch “not specified in inspected authority.” Site, propagation ephemeris/EOP and the complete transformation chain are not supplied for a new real propagation. Keep that operation pending rather than filling fields from publication time. The source speed remains readable; a new time-resolved laboratory path is not thereby specified.

> Scope: This is a complete synthetic trajectory and an intentionally incomplete real propagation request. A mechanism explaining an observed residual would be a separate proposed mechanism. Our input and residual records remain available whether or not such a mechanism is offered. Source facts, derived calculations, interpretations and unresolved inputs retain distinct labels.

## C24.07-D1 — Diagnostics

1. Why does total speed fail to reproduce a trajectory?
2. What must accompany a normalized direction?
3. How do you reconstruct a comparison vector from a model and residual?
4. Is an absent ephemeris the same in the toy packet and a real propagation request?

Answers: 1. Speed lacks direction, initial position, time and frame. 2. Original magnitude, units and orientation/frame metadata; multiply back to recover the vector. 3. comparison=model+residual, retaining every signed component. 4. No: it is explicitly unnecessary for the synthetic definition but a missing required input for the specified real calculation. Do not relabel missing data as zero.


Next dependency: [capstone](capstone.md). Carry your signed component ledger forward.
