# Lesson 5 — The K-Field research map

**Essential question:** Which rules connect a geometric description to an instrument reading?

**Goals:** Trace geometry → state → dynamics → instrument; verify a finite return identity; annotate the chain with assumptions, provenance, and retained residuals.

**Prerequisite bridge:** You can classify claims, attach source addresses, reconstruct x = M+r, and compare predictions. New coordinate notation is taught below; matrix calculation is not assumed.

## Four links answer different questions

Geometry describes locations, directions, distances, and conventions. State specifies the current configuration. Dynamics supplies a rule changing that state. An instrument rule maps state and settings to a predicted reading. Every arrow needs a rule. Geometry alone does not specify starting state, time evolution, or detector calibration.

| Link | Necessary question | Gap to flag |
|---|---|---|
| Geometry | Which coordinates, origin, unit, direction order? | Missing basis or origin |
| State | Which configuration is occupied now? | Missing initial values |
| Dynamics | How does state change per step? | Missing update or time interval |
| Instrument | What reading does the state predict? | Missing gain, offset or transfer rule |

A coordinate triple is an ordered list of three numbers. In our synthetic geometry, q = (q1,q2,q3) is a dimensionless address; subscripts select entries. The origin O_K = (5,0,0) mm marks zero address. Define position x = O_K + (2q1,3q2,−4q3) mm. Multiply entries by their respective scales and add the origin entry by entry. The negative scale reverses the third direction and must be preserved. These teaching constants are not mature Cell3 constants. Here x is position; a sensor reading will be explicitly named x_reading when both occur.

## Worked geometry and source bridge

For q = (1,−1,2), displacement x−O_K = (2,−3,−8) mm and position x = (7,−3,−8) mm. Reverse by subtracting the origin and dividing entries by their scales: ((7−5)/2,−3/3,−8/(−4)) = (1,−1,2). The mm units cancel. Omitting the origin would give 7/2 rather than 1 in the first entry. Reversal needs nonzero scales: a zero first scale sends q1 = 1 and q1 = 2 to the same first displacement, so neither can be recovered uniquely.

For source reading, a matrix is a table specifying a linear coordinate rule. B denotes the ordered basis rule. B^T is its transposed table, exchanging rows and columns. Matrix multiplication composes the rules, applying the rightmost first. I is the identity rule returning its input unchanged; an inverse undoes a rule. S02 writes G = B^T B and R = G^−1, named M_cell and R_cell here. Its `B R B^T=I` is a return identity. Invertibility is a hypothesis, not established by writing the symbol for an inverse.

The synthetic B is diagonal: each output uses only its corresponding input. Transposing such a table leaves it unchanged. Its scales are (2,3,−4) mm, M_cell scales (4,9,16) mm², and R_cell scales (1/4,1/9,1/16) mm^−2. The composite B R B^T multiplies each coordinate by 2×(1/4)×2 = 1, 3×(1/9)×3 = 1, or (−4)×(1/16)×(−4) = 1. Units cancel too. It therefore returns every triple. This checks the synthetic identity; S02's non-diagonal locked basis remains a separately addressed source claim.

## Worked complete chain

Use state q = (q1,0,0), initially q1 = 1. One dynamics step lasts 1 s and adds 1 to q1. After two steps q1 = 3. Assume instrument rule M = 5 DU + (2 DU)q1 with fixed gain and offset; an offset is the added baseline. It predicts 11 DU. For synthetic x_reading = 12 DU, retain r = 12−11 = 1 DU and recover 12 = 11+1. Geometry gives first position 5+2×3 = 11 mm. Coincidence with the number 11 DU does not equate position and instrument reading: their units and rules differ.

In source work, S02 supplies a geometric contract and S06 a reported response and replay description. The conditional Earth-coupling link names `EarthOnlyAttribution`. Show that premise and the absent raw residual explicitly instead of drawing an unsupported causal arrow between files.

> **Claim scope:** Both worked chains are synthetic. Mature S02 uses ordered ICRS columns [a b c], intentional negative determinant, and stored precision. Its closure discrepancy remains reported information. No force, transferred energy, or instrument law is derived from geometry alone here.

## Guided practice

Send q = (−1,2,0) through the geometry and reverse it. In the dynamics example, start q1 = 0 and take three steps. Predict M and retain the residual for a synthetic 10 DU reading. Label geometry, initial state, dynamics, and instrument rule separately.

## Diagnostic checks

1. Why subtract O_K before reversing the coordinate rule?
2. Recompute the three return factors. Why is the third positive?
3. Start q1 = 2, take one step, and use the same instrument rule. Find M and r for x_reading = 9 DU.
4. Map S02 and S06: name a source contract, reported measurement, formal-model report, and unresolved input.

## Worked answers

Guided practice: displacement (−2,6,0) mm gives x = (3,6,0) mm. Reversal ((3−5)/2,6/3,0/(−4)) gives (−1,2,0). Dynamics ends q1 = 3, M = 11 DU, r = 10−11 = −1 DU. Coordinate scales/origin define geometry; zero is initial state; adding one per second is dynamics; 5+2q1 DU is the instrument rule.

1. B acts on displacement from the origin. Reversing absolute position changes the address.
2. The products are 1,1,1. Two negative factors yield a positive product; neither direction sign is dropped.
3. q1 becomes 3, M = 11 DU, r = 9−11 = −2 DU; 11−2 = 9 DU reconstructs the reading.
4. S02's ordered locked basis and precision are a contract. S06's angular clock is reported measurement metadata; its 97-state replay is a formal-model report. Raw residuals are unavailable; Earth-only attribution is an additional conditional input.

**Next dependency:** [Capstone](capstone.md) builds and defends the complete evidence map.
