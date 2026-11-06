# Lesson 4 — Optical, oscillator, and crystal rulers

**Essential question:** When can we compare two rates without treating their physical sources as identical?

**Goals:** Classify length and time rulers; calculate a comparison with supplied speed; separate a numerical difference from an observed detector beat.

**Time:** 55 minutes: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

**Prerequisite bridge:** Lesson 3 converts a length spacing and projected velocity into a passage frequency. A ruler's unit is necessary information, but it does not completely describe what is being counted.

## C25.04-E1 — Attach a meaning to each number

T10 names three ruler semantics: optical wavelength, oscillator period and matter crystal spacing. A wavelength is the distance between repeating wave phases at a specified time and in a specified medium/frame. An oscillator period is the time for a repeating process to complete a cycle. Crystal spacing is a distance between declared material planes. The word “ruler” allows a calculation to use one of these spacings; it does not make the physical objects interchangeable.

| Input | Unit | Meaning | Additional input for a rate or length |
|---|---|---|---|
| Optical wavelength λ | m | Repeating optical phase spacing | Relative phase motion and geometry for actual encounters |
| Oscillator period P | s | Time per cycle | f_osc=1/P; length also needs a declared speed |
| Crystal spacing d_crystal | m | Material plane separation | Sensor/material relative projected velocity |

If a wave propagates at speed u and has period P, it travels uP in one cycle. Thus its wavelength is λ=uP under that wave's propagation model. Sensor velocity is not automatically u. If a ruler is deliberately treated as a fixed reference grid, r=n·v/d applies; if its actual phase sheets move, Lesson 2 requires their motion too.

To compare two nonnegative frequencies on one time convention, we may define a **difference frequency** f_diff=|f_1−f_2|. Subtract first, then take absolute value. This arithmetic does not supply the interaction or detection law needed for a physical beat. A baseband signal is a lower-frequency detector output; an exposure average alone specifies no frequency-conversion mechanism. THz means 10¹² Hz, a unit scale, not a detector transfer rule.

## C25.04-W1 — Worked synthetic comparison

Declare a fixed reference-grid model with projected velocity +2 m/s. An illustrative optical-length ruler λ=0.5 m gives r_opt=2/0.5=+4 s⁻¹. A separate crystal-spacing ruler d_crystal=0.25 m gives r_crystal=2/0.25=+8 s⁻¹. These are intentionally large teaching spacings, not claims about a real optical or crystal experiment. An independent oscillator with P=0.5 s has f_osc=2 Hz.

Under the declared comparison f_diff=||r_opt|−f_osc|, the difference is |4−2|=2 Hz. It is a derived comparison index, not an established optical detector beat. The rate 4 used the reference-grid assumption, not an unstated light propagation speed.

## C25.04-P1 — Practice and worked answer

An oscillator period is 1/4 s. A separate hypothetical propagation model expressly supplies u=3 m/s. Compute frequency and wavelength. Reverse the sensor in W1; report what reverses and what remains positive.

**Answer:** f_osc=1/(1/4)=4 Hz. λ=uP=3×1/4=3/4 m. The speed belongs to this hypothetical propagation model, not to ordinary light or to the sensor. W1 passage rates become −4 and −8 s⁻¹; their magnitudes stay 4 and 8. The P=1/4 s oscillator frequency remains +4 Hz. The W1 oscillator with P=1/2 s is a different input and remains +2 Hz. Keep the two oscillator IDs.

> **Claim scope:** T10's ruler categories and its directional/magnitude distinction are source facts. All numbers above are synthetic. T10 reports a physical Earth/CMB speed of 369812.50200040644 m/s in ICRS; that source value is not used as a propagation speed, phase-transformed velocity or universal speed in these exercises. A proposed detector mechanism must declare its own transfer inputs.

## Diagnostics

1. **C25.04-D1:** Two rates are both 4 Hz. Does this identify their mechanisms?
2. **C25.04-D2:** A period of 2 s is given without speed. Can you assign a wavelength?
3. **C25.04-D3:** Compare rates 7 Hz and 3 Hz under the defined difference rule.
4. **C25.04-D4:** Why is “average a THz input, therefore obtain this baseband beat” incomplete?

**Worked answers:** (1) No: equal values and units do not identify their physical roles. Retain labels, speeds and clocks. (2) Frequency is 1/2 Hz; wavelength is unresolved without speed/propagation model. (3) |7−3|=4 Hz, retaining both original rates. (4) It omits the detector response, interaction and exposure-transfer model. Preserve that missing-input status rather than inventing a conversion.

**Next dependency:** [Lesson 5](lesson-05.md) locates events from a declared signed path and tests what endpoint samples can establish.
