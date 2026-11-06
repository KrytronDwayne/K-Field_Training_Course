# Photon-equivalent model energy

**Essential question:** What does an energy equivalent calculate, and what inputs would identify physical transfer?

**Goals:** Calculate an input-equivalent energy interval with units; calculate a photon equivalent; explain transfer ambiguity and retain signed extensions.

**Prerequisite bridge.** Lesson 5 gives dimensionless g. Multiplying a dimensionless ratio by a quantity leaves that quantity's units unchanged. Power measures energy per unit time; one watt is one joule per second. Energy equals constant power times elapsed time. An interval [a,b] lists a lower and upper bound, not necessarily a probability statement.

## C26.06-E1 — Follow the types through the calculation

T35 and the energy-work estimators define input-equivalent power as g times the supplied LED band power. If band power is W_band and exposure duration is τ, the model energy is E_eq=g W_band τ. The word band matters: it is the modeled power allocated to a wavelength range, not necessarily total lamp power. For positive g and τ, multiply both power endpoints by gτ to obtain the energy interval. The result inherits the calibration and estimator assumptions of its inputs.

Reference photon energy is E_photon=hc/λ, with Planck constant h in energy·time, speed c in length/time and wavelength λ in length. Units cancel to energy. Then N_eq=E_eq/E_photon is a dimensionless photon equivalent. It can be fractional because it is a ratio, not an observed integer photon count. For real-unit reference calculations the pinned source supplies h=6.62607015×10⁻³⁴ J·s and c=299792458 m/s; 1 nm=10⁻⁹ m. Our main exercise uses explicitly toy constants to keep multiplication hand-checkable.

## C26.06-W1 — Worked synthetic calculation

Take g=4/3, power=3 energy-units/time-unit and τ=2 time-units. Then E_eq=(4/3)·3·2=8 energy-units. With toy h=6 energy-units·time-unit, c=10 length-units/time-unit and λ=3 length-units, E_photon=6·10/3=20 energy-units. The equivalent count is 8/20=2/5.

If power lies in [3,6] with the same units, E_eq lies in [(4/3)·3·2,(4/3)·6·2]=[8,16] energy-units. N_eq lies in [2/5,4/5]. These endpoints express the stated input interval only. They do not automatically include unknown detector calibration or exposure-transfer effects.

## C26.06-P1 — Practice and worked answer

Keep the same toy power interval, duration and photon energy, but use g=−1/4. **Answer:** Multiplying endpoints gives −3/2 and −3 energy-units. A negative multiplier reverses order, so write [−3,−3/2]. The signed equivalent count interval is [−3/20,−3/40]. This is a signed arithmetic extension, not a claim of a negative number of detected photons. Preserve the negative contrast and its reference.

The source's five positive energy rows are a selected subset of its eight positive-gain rows. We do not fill the other source energy fields with this extension; a null source field remains null, not zero.

## Why an equivalent does not identify transfer

A detector output might be represented by a product of an input factor and a responsivity factor. The pairs (2,3) and (1,6) both give scalar output 6. Observing that output cannot distinguish the factors. This small example illustrates the optical-transfer ambiguity described in T50's optical-transfer obstruction; it is not a reproduction of a compiler proof.

To connect an input equivalent to transferred apparatus energy, the source calls for radiometric calibration (counts mapped to a physical radiation quantity), a blank/reference ledger, uncertainty information, and an exposure transfer function. A transfer function states how time-varying input becomes the recorded output. Down-conversion means a process that makes high-frequency structure affect a lower-frequency channel. A long exposure alone is not a specification of that process. T35 retains an explicit down-conversion obligation for its modeled optical-scale carriers.

The source also keeps raw acquisition, LED datasheet, angular interpolation/mechanical uncertainty and independent replay obligations. These are concrete missing links in that source contract, rather than reasons to erase the reported signed responses.

## C26.06-D1 — Diagnostic checks and answers

1. Why does g W_band τ have energy units? **Answer:** g has no units; energy/time multiplied by time gives energy.
2. For the toy W1, what happens if λ doubles? **Answer:** Photon energy halves to 10, so the energy equivalent stays 8 but photon equivalent doubles to 4/5.
3. Can output 6 choose between (2,3) and (1,6)? **Answer:** No. Both products are 6; an independent calibration or other constraining measurement is needed.
4. Does a null energy field mean zero energy? **Answer:** No. It means no value supplied in that field. Keep the row and its other defined quantities.

> **Claim scope:** Input-equivalent energy and photon equivalent are model calculations. Transferred energy and detected photon counts are different measurement claims. The toy constants are not physical constants; the signed extension is not a modification of the source ledger.

**Next dependency:** [Lesson 7](lesson-07.md) reads the signed archive ledger and its repeated plane costs.
