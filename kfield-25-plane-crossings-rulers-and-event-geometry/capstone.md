# Capstone — Build a replayable signed event ledger

Work across three 55-minute periods: input cards and operations 1–2; operations 3–6 and event rows; reconstruction, operation 7 and peer audit. All data are synthetic. Use exact fractions. You may consult the lessons and glossary. Submit input cards, calculations, a typed ledger and unresolved-information notes. No sky lookup, calculus or external experimental data are needed.

## Inputs supplied locally

**REV card:** Perpendicular Cartesian axes in metres; synthetic elapsed seconds from named epoch E0. x(t)=((−2 m/s)t,0,0), defined by this linear law around reporting interval [0,3/2] s. Family A: n=(3/5,4/5,0), o=0 m, d=3/5 m, polarity p=+1. Family B: n=(1,0,0), o=0 m, d=2 m, p=−1. Family B is a label, not a basis matrix. Exact model inputs imply exact derived roots; instrument uncertainty is not applicable. Preserve the reporting endpoints.

**Other cards:** Each below is separate from REV, with its own clock and path. Never blend them into one sensor run.

- RATE: n=(0,1,0), d=1 m, fixed o=0, first v=(2,0,0), then a separate run v=(0,−3,0) m/s, both initially x=0. Polarity +1.
- RULER: Fixed projected velocity +6/5 m/s, original spacing 3/5 m, revised spacing 6/5 m. Initial q=0 in both. These are separate ruler definitions.
- OSC: Oscillator period 1/4 s; expressly supplied hypothetical propagation speed 3 m/s. Comparison grid has projected sensor velocity +2 m/s and spacings 1/2 m (“optical-length reference”) and 1/4 m (“crystal-spacing reference”). These labels designate synthetic grids, not observed light or material data.
- LINE: s(1 s)=−1 m, s(3 s)=3 m; exact linear interpolation. CONTACT: s(t)=(1 m)(t/(1 s)−1)² on [0,2] s. JUMP: s=−1 m for t<1 s and +1 m for t≥1 s on [0,2] s. GAP: only s(1 s)=−1 m and s(2 s)=+1 m are supplied, with unknown continuity and no values inside (1,2) s. For each of these four separate cards use n=(1,0,0), o=0, d=1 m, k=0, x=(s,0,0) where known, and p=+1.
- SKY: Fictional Star R has H(t)=π(t/(1 h)−1) rad on [0,2] h, unwrapped. Distinct spatial family S has n=(1,0,0), o=0, d=1 m, x=((2 m/h)t,0,0), p=+1, and q=2t/(1 h). The hour clock is named E_H and must not be silently merged with E0 seconds.

## Tasks and backward map

Each numbered step is worth four points. The table specifies outputs and earlier explanation plus answered practice; the exercises below contain the actual requests.

| Step | Named input → required output | Earlier teaching | Answered practice |
|---|---|---|---|
| C25-CAP-01 | REV A, revised origin → q,s and separate revision | C25.01-E1, W1 | C25.01-P1 |
| C25-CAP-02 | RATE vectors → projected rates and zero branch | C25.02-E1, W1 | C25.02-P1 |
| C25-CAP-03 | RULER → T,f,φ with units | C25.03-E1, W1 | C25.03-P1 |
| C25-CAP-04 | OSC → clock rate, propagation length and role comparison | C25.04-E1, W1 | C25.04-P1 |
| C25-CAP-05 | LINE, CONTACT, JUMP, GAP → roots and event statuses | C25.05-E1, W1 | C25.05-P1, P2 |
| C25-CAP-06 | SKY → typed angular and spatial events | C25.06-E1, W1 | C25.06-P1 |
| C25-CAP-07 | REV plus exceptional cards → complete signed ledger/reconstruction | C25.07-E1, W1 | C25.07-P1, P2 |

### C25-CAP-01

For REV A, compute q at 1/2 s and signed distance to sheet −1. Create a separate origin revision o=(1,0,0) m. Show how q changes, and retain both origin cards.

### C25-CAP-02

Compute both RATE signed rates with dimensions. Give each unsigned rate and say whether a finite traversal period exists. Distinguish persistent occupancy from an isolated zero-rate crossing.

### C25-CAP-03

Compute both RULER periods and frequencies. Give the original q and φ as functions of elapsed seconds. Explain why the revised ruler cannot overwrite the old ledger.

### C25-CAP-04

Compute OSC frequency and propagation wavelength. Compute the two reference-grid passage rates, then reverse sensor velocity. State what reverses and what remains positive. Compare the optical-grid magnitude with the oscillator frequency using the declared difference rule. Classify the result's evidence layer and identify an input needed for a physical detector interpretation.

### C25-CAP-05

Locate and verify the LINE root. Classify CONTACT and JUMP. State exactly what can be claimed about GAP. Keep endpoints, brackets, model/continuity assumptions and unresolved fields; do not fabricate a gap event.

### C25-CAP-06

For SKY, list all upper/lower passages and both quadratures in [0,2] h. Locate spatial sheet k=1. Retain the Star R identity, spatial normal, clock and unwrapped branches. Explain any coincidence.

### C25-CAP-07

List every REV A and B event in [0,3/2] s with direction and polarity. Use the same supporting brackets as Lesson 7 W1 and compute their endpoint distances. Add CONTACT and GAP rows with distinct statuses; reference your LINE and JUMP records too. Reconstruct signed distances from saved q,k,d and explain why the full vector path remains necessary. For the separate synthetic residual card y=[0,11/10,19/10] m and m=[0,1,2] m at [0,1,2] s, preserve e=y−m and verify y=m+e.

## Full worked answer key

**01:** At 1/2 s, x=(−1,0,0) m. Projection is −3/5 m; q=−1 and s_(−1)=−3/5+3/5=0 m. The new origin subtracts another 3/5 m from projection, so q_new=q_old−1 and equals −2 at that time. Old sheet −1 is relabeled −2 in this full-spacing revision. No original coordinate is overwritten.

**02:** First projected velocity is 0 m/s, so r=0/(1 m)=0 s⁻¹ and |r|=0. No finite traversal period. With x(0)=0 the first run stays in sheet 0 while moving parallel to it. Second projection is −3 m/s; r=−3 s⁻¹, |r|=3 s⁻¹ and T=1/3 s. Direction is decreasing index. The zero-rate branch remains in the record.

**03:** Original T=(3/5 m)/(6/5 m/s)=1/2 s and f=2 Hz. Revised T=1 s and f=1 Hz. Original q=2t/(1 s), φ=4πt/(1 s) rad. Separate spacing definitions count different sets of physical sheets; keeping both lets another reader reproduce either ledger.

**04:** f_osc=1/(1/4 s)=4 Hz. Propagation wavelength is (3 m/s)(1/4 s)=3/4 m; 3 m/s is the supplied hypothetical wave speed, not sensor speed or a light-speed claim. Grid rates are 2/(1/2)=+4 s⁻¹ and 2/(1/4)=+8 s⁻¹. Reversal gives −4 and −8 s⁻¹; their magnitudes and oscillator frequency stay positive. Difference index is |4−4|=0 Hz. Equal numerical rates do not identify physical roles. The comparison is a synthetic derived quantity, and detector response/transfer inputs are absent, so it is not a measured beat or energy transfer.

**05:** LINE slope=(3−(−1))/(3−1)=2 m/s. Root t*=1−(−1)(2)/4=3/2 s; verify −1+2(1/2)=0 m. Keep [1,3] s and [−1,3] m. CONTACT root is 1 s, with equal positive sides, zero instantaneous rate and bracket [0,2] s values [1,1] m. It is a contact, not a transverse passage. JUMP has no zero because its values are always −1 or +1 m; keep [0,2] s and [−1,+1] m with the discontinuity rule. GAP has unknown root existence, count, direction and times because continuity is unknown. Its endpoints remain [1,2] s and [−1,+1] m; do not report 3/2 s as a root. If an independent continuous model later becomes available, add a revision; do not rewrite the original gap state.

**06:** Star R: H=−π at 0 h is lower branch j=−1; H=0 at 1 h is upper j=0; H=π at 2 h is lower j=0. Negative quadrature H=−π/2 occurs at 1/2 h; positive H=π/2 at 3/2 h. Family S reaches k=1 at 1/2 h because 2t/(1 h)=1. This is coincident with the negative quadrature, but equations and inputs differ. Keep clock E_H hours, Star R, and S's n=(1,0,0), o=0, d=1 m. Do not convert these to real UTC predictions.

**07:** All following REV rows are exact synthetic linear passages with direction −, source REV, clock E0 seconds, stated extension and original fixed normals. Time localization is {t}, not a measurement-uncertainty claim.

| Event ID | Family:k | Time s | Bracket s | Endpoint s_k values m | p |
|---|---|---:|---|---|---:|
| R-A0 | A:0 | 0 | [0,1/2] | [0,−3/5] | +1 |
| R-A−1 | A:−1 | 1/2 | [0,1] | [3/5,−3/5] | +1 |
| R-A−2 | A:−2 | 1 | [1/2,3/2] | [3/5,−3/5] | +1 |
| R-A−3 | A:−3 | 3/2 | [1,3/2] | [3/5,0] | +1 |
| R-B0 | B:0 | 0 | [0,1] | [0,−2] | −1 |
| R-B−1 | B:−1 | 1 | [1/2,3/2] | [1,−1] | −1 |

Keep boundary rows because the reporting interval is closed. Their two-sided passage classification uses the supplied extension; it is not inferred from only one-sided samples. Coincident rows at 0 and 1 s retain both family IDs and shared-path dependence.

| Additional record | Time/localization | Support | Status and direction | Card |
|---|---|---|---|---|
| C-0 | {1 s} | [0,2] s, [1,1] m | contact; no sign reversal | CONTACT |
| G-0 | unresolved in (1,2) s | [1,2] s, [−1,+1] m | gap; existence/count/direction unknown | GAP |
| L-0 | {3/2 s} | [1,3] s, [−1,3] m | linear positive passage | LINE |
| J-0 | jump at 1 s; no zero | [0,2] s, [−1,+1] m | discontinuity; passage not assigned | JUMP |

All four use their separate n=(1,0,0), o=0, d=1 m, k=0, p=+1 cards. They are not segments of REV. GAP has unresolved uncertainty rather than a singleton root.

Reconstruction uses s_k=d(q−k). For R-A−2, q=−2t/(1 s) and k=−2, giving (3/5)(−2t/(1 s)+2) m; the endpoints produce +3/5 and −3/5 m. The same operation gives every pair in the table. R-B−1 gives 2(−t/(1 s)+1) m, yielding +1 and −1 m. Projection alone loses tangential components, so the REV path remains referenced. Residual e=[0,1/10,−1/10] m; m+e=[0,11/10,19/10] m exactly, retaining signs, time order and all components.

## Rubric — 28 points

For each of seven steps, award one point for each column below. A point can be earned after an explicitly recorded correction during the audit period. Do not award evidence-classification credit to a numerically correct result labeled as a real observation.

| Step | Inputs/domain (1) | Operation (1) | Reconstruction or classification (1) | Retention/boundary (1) |
|---|---|---|---|---|
| 01 | n,o,d, REV units | q=−1 and revised q=−2 | s_(−1)=0 | Both origin cards retained |
| 02 | Fixed n,d and two v values | 0 and −3 s⁻¹ | Zero occupancy versus passage | Magnitudes plus no finite zero-rate T |
| 03 | Both spacings and speed | T=1/2,1 s; f=2,1 Hz | φ=4πt/(1 s) | Separate ruler IDs and units |
| 04 | P,u and grid meanings | f=4 Hz; λ=3/4 m; rates 4,8 | Derived difference 0, no detector promotion | Signed reversals and missing transfer input |
| 05 | Endpoints/continuity of four cards | LINE root 3/2 s | Contact/jump correctly classified | Unknown gap and original brackets kept |
| 06 | E_H, Star R and spatial S | Five angular times and sheet time | Distinct coincident event equations | Unwrapped branches and normal retained |
| 07 | Card IDs, normals, p, clocks | Six REV rows and distance pairs | Residual and s_k replay | Contact, gap, LINE, JUMP and endpoint status |

**Completion check:** No operation is introduced for the first time here. Resolve missing cards, lost signs or fabricated gap roots before accepting the ledger, even if a numerical score would otherwise be high. The goal is a reproducible account of all specified information.
