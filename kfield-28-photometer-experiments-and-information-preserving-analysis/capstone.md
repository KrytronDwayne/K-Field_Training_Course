# Capstone — a complete information-preserving rehearsal

Work for three periods with the lessons available. Label the entire numerical submission **synthetic rehearsal**. Preserve raw inputs, ordered identities, every signed field, masks and inverse rules. Use the nine named steps below; each is worth 4 points, total 36.

Input card: device T, session A; toy bench frame x right, y away, z up; normal +z; gain setting 1; exposure 0.2 s; A nominal 500 nm (response A-toy), Clear broadband (C-toy); calibration missing. Sequence 0..4 has midpoint t=0..4 s, A=(2,5,8,1,3), C=(10,0,20,10,10). Row 3 has stipulated suspected-saturation flag with reason “synthetic instrument-status exercise”; raw values remain. Sequence 5 at expected t=5 s is absent. Optional separate B-toy at row 2 is nominal 600 nm with count 4.

Freeze Toy-v1 before calculations: z(t)=(1 m/s)t, origin 0, normal +z, spacing 2 m; q=t/(2 s); events integer q over midpoint interval [0,4] s; exact midpoint offsets (-1,0,1) s, no interpolation or zero padding. All flags travel with their keys. The four-point reflection and parity inputs below are separate synthetic exercise records, not selections silently extracted from session A.

## Student tasks

1. **C28-CAP-01 (lesson-01 P1):** Write the row-2 acquisition card and exposure support. Explain what A/B=8/4 can and cannot mean.
2. **C28-CAP-02 (lesson-02 P1):** Retain all five raw rows, the row-3 flag and a separate expected sequence-5 gap record. State a key that preserves simultaneous channels and explain how original sequence restores a sorted display.
3. **C28-CAP-03 (lesson-03 P1):** Compute all Clear ratios and reconstruct A. Separately calculate the exact closure for displaying 1/3 as 0.3333333333. Compare 0/5 and 0/0.
4. **C28-CAP-04 (lesson-04 P1):** For x=(3,1,-1,1), compute R, s, a and both defects. Also test (-2,0,2) for inversion about its middle sample. State how a weak channel would be retained.
5. **C28-CAP-05 (lesson-05 P1):** Solve the event rule, list all raw and normalized windows with support masks, and compute the center-2 side difference and sum. Explain why the rule cannot be called a physical sidereal prediction.
6. **C28-CAP-06 (lesson-06 P1):** Compute full-record and center-2-window means/details and reconstruct both inputs. State what the DFT inverse requires and why magnitude alone is insufficient.
7. **C28-CAP-07 (lesson-07 P1):** With synthetic positive box bounds k=[1.9,2.1] units/count and x=[0.9,1.1] counts, compute product bounds. Apply shared clock offset [-0.1,0.1] s to midpoint 2 s, then add exposure support. List unresolved contributors separately.
8. **C28-CAP-08 (lesson-08 P1):** Write a forward rehearsal protocol over midpoint interval [0,10) s at cadence 1 s, exposure 0.2 s. Include version, keys, geometry, masks, controls, stopping/interruptions, train/check roles and every outcome. Identify required replacements before a real physical test. Classify synthetic arithmetic, archived report, proposed mechanism and planned measurement.
9. **C28-CAP-09 (lesson-04 C28.S01-P1):** For x=(3,1,-1,1), compute Ex and Ox, their reconstruction and the odd DFT. Show an even comparator cannot represent Ox. Separately classify the source native ternary ladder, Fibonacci-cutoff proposal and 25–27→2 pathway, including the four-point aliasing boundary.

## Full answer key and point rubric

Each numbered answer gives four one-point criteria. Equivalent precise wording earns credit. All fields must be traceable to their declared input; a mismatch is repaired and retained rather than erased.

1. (1) Row key T/A/2/A with t=2 s and A=8 counts; paired C=20 with its own channel identity. (1) Exposure [1.9,2.1] s from 2±0.1. (1) +z normal, gain 1, nominal wavelengths and response IDs retained. (1) Ratio 2 is a count ratio, not calibrated spectral power; calibration is missing. B=4 is a separate supplied channel, not a fabricated full B series.

2. (1) Raw ledger rows (sequence,t,A,C) are (0,0,2,10),(1,1,5,0),(2,2,8,20),(3,3,1,10),(4,4,3,10), with counts and seconds typed. (1) Row 3 retains its stipulated flag/reason beside A=1 and C=10. (1) Expectation ledger says sequence 5,t=5 absent, no invented count. (1) Keys include device/session/sequence/channel; original sequence can restore order despite duplicate timestamps or display sorting.

3. (1) r=(1/5,undefined,2/5,1/10,3/10), mask (1,0,1,1,1); row 3 retains its diagnostic flag independently. (1) Products return 2,8,1,3 on valid rows; retained row 1 returns A=5,C=0 directly. (1) Exact delta=1/30000000000 and A=(display+delta)*3=1 for the separate rounding example. (1) 0/5=0 is valid; 0/0 is undefined. Keep inputs, decimal rule, response identities and masks.

4. (1) Rx=(1,-1,1,3), s=(2,0,0,2). (1) a=(1,1,-1,-1), so s+a=(3,1,-1,1). (1) Same defect=(2,2,-2,-2), inverted defect=(4,0,0,4). For (-2,0,2), reversal=(2,0,-2)=-x and inverted defect=(0,0,0). (1) Retain both signs, fixed center/support and every channel; a nonzero center contributes to the same component, and weakness is not a deletion rule.

5. (1) Events at t=0,2,4 s; raw windows (absent,2,5),(5,8,1),(1,3,absent) with masks (0,1,1),(1,1,1),(1,1,0). (1) Ratio windows (absent,1/5,undefined),(undefined,2/5,1/10),(1/10,3/10,absent), validity masks (0,1,0),(0,1,1),(1,1,0); keep reasons for absent versus undefined. (1) Center-2 side difference 4, sum 6, center 8 retained. (1) Geometry is synthetic; real site/time/ephemeris/orientation/event/calibration versions remain required. No center shifts or dropped edge windows.

6. (1) Full mean 19/5, detail (-9/5,6/5,21/5,-14/5,-4/5), reconstructing (2,5,8,1,3). (1) Window mean 14/3, detail (1/3,10/3,-11/3), reconstructing (5,8,1). (1) Support, ordering, flags, weights and both fields retained; different means have different supports. (1) DFT requires both complex coordinates, sample order, transform signs and inverse 1/4; single pulses at different positions have equal magnitudes but different phases.

7. (1) Positive box bounds give [1.9*0.9,2.1*1.1]=[1.71,2.31] output units. (1) Midpoint [1.9,2.1] s. (1) Possible exposure support [1.8,2.2] s; each exposure still lasts 0.2 s and common clock offset is shared. (1) Retain missing calibration, orientation/angular uncertainty, gaps, zero Clear, stipulated saturation, unresolved channel structure and transfer assumptions as distinct contributors. These synthetic bounds do not calibrate the actual instrument.

8. (1) Forward-Toy-v1 freezes ten expected midpoints 0..9, duration interval [0,10), gain/orientation/response IDs and exposure 0.2; acquisition coverage begins -0.1 relative to first midpoint. (1) Freeze q=t/(2 s), exact offsets/no interpolation, all raw/ratio/parity/mean-detail fields and validity reasons; prior training is none for this authored toy, and future values cannot tune the check rule. (1) Stop after tenth scheduled midpoint or record interruption; retain every outcome and a separately identified same-setting blank/reference control. (1) Real-test v1 remains planned until site, UTC time scale, ephemeris, physical geometry and calibration/transfer references replace the toy inputs. Archive statements stay reported; 25–27→2 stays proposed; toy arithmetic stays synthetic. A changed rule receives a new exploratory version.

9. (1) Hx=(-1,1,3,1), Ex=(1,1,1,1), Ox=(2,0,-2,0); sum restores x. (1) Odd DFT=(0,4,0,4); inverse gives (2,0,-2,0). (1) (p,q,p,q) dot Ox=2p-2p=0; all circular shifts are also even, so comparator blindness cannot justify dropping Ox. (1) S05 R021's 1,3,9,27 is a source synthesis; R026's Fibonacci-related cutoff continuation and R028's 25–27→2 are separate branches, the latter a retained proposed pathway. Four samples alias native 25 and 27 modulo 4 and cannot newly verify their coupling. Retain the unrepresented odd field and full comparison residuals.

Final reconstruction audit: all five raw A values remain recoverable; all three event windows remain listed; all invalid/absent reasons remain distinguishable; reflection and half-turn parity are separate; proposed mechanism is not silently promoted to measured energy. Use sources.md for exact source addresses.
