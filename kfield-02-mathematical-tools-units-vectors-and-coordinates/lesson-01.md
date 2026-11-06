# Lesson 01 — Units and scientific notation

**Essential question:** How can a number change while the quantity it describes stays the same?

**Goals:** Convert lengths and times with unit factors; express numbers in scientific notation; distinguish a period from a frequency and convert both correctly.

**Prerequisite bridge.** You can multiply fractions and solve a linear equation. A conversion factor is a fraction equal to one: 100 cm and 1 m name the same length. Multiplying by their ratio changes the description, not the object. Course-01's distinction between a stated input and a derived result is used here: our numbers are invented teaching inputs, and arithmetic produces the results.

## Build the idea

A quantity consists of a number and a unit. The unit says what counts as one. Length, time, and frequency are different kinds of quantities, called dimensions. We write their dimensions as L, T, and T^-1. A frequency counts repeated cycles per unit time; a cycle is a count, not a length. You may add 2 m to 30 cm after converting to a common unit, but adding 2 m to 3 s has no defined meaning here.

Our exact unit relations are 1 m = 100 cm = 1000 mm, 1 km = 1000 m, 1 min = 60 s, and 1 ms = 0.001 s. A hertz, Hz, means one cycle per second; 1 kHz = 1000 Hz. Write conversion factors so unwanted units cancel. For example, 250 cm × (1 m / 100 cm) = 2.5 m. Reversing the factor would leave cm²/m rather than the desired m.

Scientific notation writes a nonzero number as a × 10^n with 1 ≤ |a| < 10 and integer n. Positive powers count repeated factors of ten; negative powers mean reciprocals. Thus 10^-3 = 1/1000, 3200 = 3.2 × 10^3, and 0.0048 = 4.8 × 10^-3. When multiplying powers of ten, add exponents: (3 × 10^2)(2 × 10^-3) = 6 × 10^-1. Zero is simply zero. A negative value keeps its sign, as in -0.002 = -2 × 10^-3.

A period T is the time for one cycle. For evenly repeating cycles, frequency f = 1/T because one cycle divided by its duration gives cycles per second. Conversely T = 1/f. Convert the time unit before labeling the reciprocal Hz. The reciprocal of 4 ms is 0.25 per millisecond, which is 250 per second, not 0.25 Hz.

## Fully worked synthetic example

An invented scanner moves 36 mm in one repeating cycle lasting 4 ms. Express the length, period, and frequency using metres and seconds.

1. Length: 36 mm × (1 m / 1000 mm) = 0.036 m = 3.6 × 10^-2 m.
2. Period: 4 ms × (1 s / 1000 ms) = 0.004 s = 4 × 10^-3 s.
3. Frequency: f = 1/(0.004 s) = 250 s^-1 = 250 Hz = 0.25 kHz.
4. Reverse checks: 0.036 m × 1000 mm/m = 36 mm; 250 cycles/s × 0.004 s/cycle = 1. The original inputs are recovered without rounding.

The displacement per cycle alone does not specify a path or mechanism. We have calculated units and a repeat rate, not inferred how the scanner works.

> **Claim scope:** All device values in this course are synthetic. Unit definitions and the arithmetic are reference mathematics; no measurement or physical mechanism is being reported. Exact fractions are preferred. When a decimal must be displayed approximately, the rule will be nearest chosen decimal place with halfway values away from zero, and the unrounded value will remain available.

## Guided practice

Convert 7.5 cm to metres and 2 min to seconds. Write the factors before calculating: 7.5 × (1/100) m = 0.075 m; 2 × 60 s = 120 s. A 2 Hz repeat has period 1/2 s. Check each by multiplying back to its starting unit.

## Diagnostic checks

1. Convert 0.003 km to metres and then millimetres.
2. Write 0.00072 s in scientific notation and milliseconds.
3. A repeat has period 20 ms. Find f in Hz and kHz.
4. Explain what is wrong with “3 m + 2 s = 5” and with “2 Hz = 2 seconds.”

## Worked answers

1. 0.003 × 1000 = 3 m; 3 × 1000 = 3000 mm. Multiplying the original by 10^6 gives the same millimetres.
2. 7.2 × 10^-4 s; multiplying seconds by 1000 ms/s gives 0.72 ms.
3. T = 0.020 s; f = 1/0.020 = 50 Hz = 0.050 kHz. The product fT is one cycle.
4. Length and time cannot be added in this model. Hz has dimension T^-1, whereas seconds have T. A 2 Hz repeat has period 0.5 s.

**Next dependency:** [Lesson 02](lesson-02.md) applies unit factors to areas and volumes, where the conversion factor must also be squared or cubed.
