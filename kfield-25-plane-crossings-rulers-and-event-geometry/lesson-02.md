# Lesson 2 — Crossing rates from velocity

**Essential question:** Which part of velocity changes the sheet coordinate?

**Goals:** Derive a fixed-family rate from two positions; preserve sign and dimensions; identify extra inputs when geometry moves.

**Time:** Two 55-minute periods, each retrieval 5, teaching/example 20, practice 15, checks/repair 15. Period 1 covers fixed geometry and P1; period 2 covers changing geometry, P2 and D3–D4.

**Prerequisite bridge:** Lesson 1 gives q=n·(x−o)/d. Velocity is displacement divided by elapsed time, separately for each coordinate. A delta Δ means final minus initial: Δx=x(t_2)−x(t_1), Δt=t_2−t_1>0.

## C25.02-E1 — Derive before naming

Hold n,o,d fixed. Subtract q values; the origin terms cancel, leaving Δq=n·Δx/d. Divide by Δt. For constant velocity v=Δx/Δt:

`signed rate r=Δq/Δt=n·v/d`.

The **projected velocity** n·v has units m/s. Dividing by spacing in metres gives s⁻¹. Positive r increases sheet index; negative r decreases it. Absolute value |r| is unsigned; save r alongside it. A rate of 2 s⁻¹ means two spacings per second, not necessarily two recorded events in every short window. Starting phase and endpoint inclusion matter.

The dot notation q̇ means instantaneous rate. For linear motion it equals r. When motion changes, a finite ratio is an average; q̇ describes the rate approached over shorter intervals at one instant. No limit calculations are required here.

## C25.02-W1 — Worked projection and reversal

For n=(3/5,4/5,0), d=3/5 m, v=(2,0,0) m/s, n·v=6/5 m/s. Therefore r=(6/5)/(3/5)=2 s⁻¹. Independent check: in half a second x advances 1 m; its projection advances 3/5 m, exactly one spacing, giving 1/(1/2 s)=2 s⁻¹.

Reverse v to (−2,0,0) m/s. Projection becomes −6/5 m/s and r=−2 s⁻¹. Both magnitudes are 2 Hz if one cycle denotes a sheet interval, but sheet orders are opposite. Taking absolute value alone loses direction.

## C25.02-P1 — Practice and worked answer

Let n=(0,1,0), d=1 m. Find r for v=(2,0,0) and v=(0,−3,0) m/s. How long does the nonzero constant rate take to traverse one interval?

**Answer:** First dot product is zero; r=0 and motion is parallel to sheets. There is no finite traversal period. A path already on a sheet may remain on it. Second dot product is −3 m/s; r=−3 s⁻¹. Three spacings per second gives a positive interval of 1/3 s, with direction still negative.

## Moving geometry — finite replay first

Take n=(1,0,0), d=1 m, x(t)=((2 m/s)t,0,0), but o(t)=((1 m/s)t,0,0). At 0 s, q=0. At 1 s, x−o=(1,0,0) m, so q=1. The rate is 1 s⁻¹. Using sensor velocity alone gives a wrong result because the sheets move too.

If normal or spacing changes, evaluate their values at both endpoints. For stationary x=(2,0,0) m, o=0, n=(1,0,0), let d rise from 1 m to 2 m over one second. Then q changes from 2 to 1: average rate −1 s⁻¹ despite zero sensor velocity.

**C25.02-P2:** Sensor and origin both move at (2,0,0) m/s. Initially x−o=(3,0,0) m; n=(1,0,0), d=1 m. Find q at 0 and 2 s. **Answer:** Relative position stays 3 m, so both values are 3 and rate is zero. Record persistent occupancy of sheet 3, not an isolated passage.

**Recognition-only full derivative:** For differentiable inputs,

`q̇=[ṅ·(x−o)+n·(v−ȯ)]/d − q ḋ/d`.

Here ṅ is normal rate, ȯ origin velocity, ḋ spacing rate. The terms describe turning sheets, relative translation and changing scale; each has units s⁻¹. This is a product/quotient derivative rule. Its calculus derivation is outside the assessed core; endpoint replay is required and taught above. Fixed-family rate cannot be applied to changing geometry without checking the extra terms.

> **Claim scope:** These are synthetic kinematics. T10 distinguishes directional crossing rate and magnitude-based beat frequency under its own contract. A geometric rate alone does not establish detector response. T45 preserves separate display scales and specified motion inputs; camera movement does not supply missing physical velocities.

## Diagnostics

1. **C25.02-D1:** Why is zero rate not a zero-second period?
2. **C25.02-D2:** Projected velocity is −4 m/s and d=2 m. Give signed/unsigned rates.
3. **C25.02-D3:** Which input changes in the moving-origin example, and what rate results?
4. **C25.02-D4:** Can n·v/d alone capture changing spacing for a stationary point?

**Worked answers:** (1) Traversal time requires dividing by a nonzero rate; zero has no finite traversal period. (2) −2 s⁻¹ and 2 s⁻¹, decreasing sheet index. (3) Origin moves at 1 m/s and sensor at 2 m/s; relative projection gives 1 s⁻¹. (4) No: q changed from 2 to 1 while v=0. Use the full definition and spacing history.

**Next dependency:** [Lesson 3](lesson-03.md) converts constant rates into time scales.
