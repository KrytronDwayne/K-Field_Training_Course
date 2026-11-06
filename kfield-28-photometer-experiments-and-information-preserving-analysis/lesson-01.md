# 1. From light to channel readings

Essential question: What must accompany a number before it becomes an interpretable reading?

Goals:

- Specify channel and orientation identities
- Compute exposure support
- Separate counts from calibrated quantities

## Prerequisite bridge

Use signed arithmetic, fractions, units and coordinate arrows. The named earlier courses are background; all operators required here are taught locally.

Pacing: 1 period(s) of 55 minutes. Acquisition identities, exposure and calibration.

## C28.01-E1 — first principles

A photometer turns light arriving at a detector into a recorded number. A channel is one named response pathway of that instrument. A wavelength label describes where a response is nominally located; it does not say that the detector accepts only that exact wavelength. A nanometre (nm) is one billionth of a metre. Keep the response identity even when a full response curve is unavailable.

Counts are the instrument's numeric output. Gain is an instrument setting that changes how the input becomes output. Exposure is the duration over which a reading is collected. Calibration is a documented relation between an instrument output and a specified reference quantity under stated conditions. Without that relation, counts remain counts. Dividing by exposure can produce counts per second, but does not manufacture watts, a unit of power.

Orientation specifies which way the sensor faces. Here +z means the positive third axis of a declared toy laboratory frame: x points right on the bench, y points away from the observer, and z points upward. The sensor normal is the perpendicular arrow out of its receiving surface. This toy frame is not an astronomical frame.

A midpoint timestamp locates the middle of an exposure, not the entire reading at an instant. For duration e, half lies before the midpoint and half after it: support is [t-e/2,t+e/2]. Square brackets include the endpoints. In this course t is elapsed seconds from a synthetic session start. It is not a UTC epoch. One real run would need both its UTC start and its clock convention.

Our common acquisition is synthetic device T, session A, gain setting 1, exposure e=1/5 s, fixed +z normal, A nominal 500 nm, and broadband Clear response identity C-toy. No calibration is supplied. Rows 0 through 4 have midpoint times 0,1,2,3,4 s, A counts 2,5,8,1,3 and Clear counts 10,0,20,10,10. These values were authored for arithmetic. Read the list in order: position 0 is the first row, not row 1.

> Claim scope: All counts and instrument settings in this lesson are authored teaching inputs. No measured optical power is supplied.

## C28.01-W1 — worked example

Toy acquisition A has sequence 0..4, elapsed mid-exposure times 0..4 s, channel A nominal 500 nm, raw counts (2,5,8,1,3), Clear (10,0,20,10,10), fixed +z sensor normal, gain setting 1, exposure 1/5 s and calibration not supplied. Each exposure spans t-1/10 to t+1/10 s. These are authored counts, not observations.

## C28.01-P1 — guided practice

**Student task.** For row 2 of the common acquisition, write its midpoint, exposure support, A and Clear counts, orientation, gain and calibration status. A separate B-toy channel nominally 600 nm has count 4 at that row. Compute A/B and explain whether it is calibrated spectral power.

### Worked answer

At row 2 the midpoint is 2 s, exposure support [1.9,2.1] s, raw A=8, Clear=20. If a separate channel B is nominal 600 nm with raw count 4, retain its own wavelength and response identity; a count ratio 8/4=2 does not yet give a spectral power ratio.

The row retains fixed +z in the toy bench frame, gain 1, A-toy/C-toy response IDs and missing calibration. Its channel keys are T/A/2/A and T/A/2/Clear. B-toy has its own key and only the supplied row-2 count.

## C28.01-D1 — diagnostic checks

1. What interval supports row 4?
2. Do equal counts with gain 1 and gain 2 establish equal incident energy?
3. Why retain a response identity beside 500 nm?
4. What is known when calibration is absent?

## Worked answers

1. 4 ± 0.1 gives [3.9,4.1] s.
2. No. The gain/calibration relations are needed; preserve both settings.
3. A nominal wavelength does not specify the full accepted wavelength response.
4. The counts, settings, orientation and timing remain known; an optical-power conversion is unresolved.

Next dependency: [lesson-02](lesson-02.md) uses these operations. Reconstruct the worked input and explain the diagnostic answers before proceeding. Source boundaries: [sources](sources.md).
