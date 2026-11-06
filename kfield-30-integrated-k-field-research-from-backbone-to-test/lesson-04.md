# Lesson 4 — Choosing discriminating experiments

Essential question: Which next observation most directly separates the remaining candidate explanations?

Goals: Compare candidates on shared inputs; count distinguishable outcomes in a finite design; freeze a sign prediction; state the limits of a minimality argument.

Prerequisite bridge: Lesson 3 exhibited different states with the same sum and a row that separates them. A **candidate mechanism** explains how a state produces a response. Its parameters are the adjustable quantities in that explanation. To compare mechanisms fairly, specify the same input, units and measurement procedure before comparing their predictions.

## C30.04-E1 — A prediction must survive the observation

An experiment is informative when candidates predict different observable outcomes under a common contract. Repeating a sum channel can reveal temporal changes or transfer problems, but it cannot distinguish two fixed candidates whose sums are identical. A difference channel can separate them if its sign convention and calibration are independently known.

Explanatory compression means accounting for several observations with fewer independent choices. It is useful when accompanied by accurate predictions and retained residuals. It is not permission to delete inconvenient channels. Compare which observations each candidate explains, which parameters it fixes in advance, which it leaves free, and what would count as a mismatch. A candidate that chooses a new parameter after every result needs a new version; the original prediction remains in the ledger.

Cross-domain recurrence is a target for explanation. A common structure across geometry and instruments may motivate a shared mechanism. First keep the domains typed: a nanometre Cell3 basis and a unit-sphere galaxy coordinate system have different units and metrics. Connecting them requires an explicit transformation and new predictions, not merging their labels.

## C30.04-W1 — Two questions for four synthetic states

Consider states 00,01,10,11, each an ordered pair of bits. A bit is a value 0 or 1. Ask Q1, “is the first bit 1?”, and Q2, “is the second bit 1?” The answer pairs are respectively no/no, no/yes, yes/no, yes/yes. Thus these two questions distinguish all four states. One binary question has only two possible answers. Four states assigned to two answers must share an answer somewhere, so one question cannot distinguish all four. This proves minimality for this declared finite example.

I01 `/results/10` reports six goal-specific two-question portfolios with their own formal minimality witnesses. Our four-state count explains a design principle; it does not replace those witnesses or identify their actual questions. I01 explicitly leaves experimental execution open. Keep its six portfolios as designs, without fabricating favorable outcomes.

## C30.04-P1 — A mechanism comparison table

Use thetaA=(2,1) and thetaB=(1,2), fixed before any test, with all coordinates dimensionless. Complete the table and choose a discriminator.

| Proposed response state | sum | difference | newly fitted parameters allowed during check |
|---|---:|---:|---:|
| A | 3 | +1 | 0 |
| B | 3 | −1 | 0 |

Answer: The sum cannot choose. A calibrated difference sign can distinguish these fixed states. Record both predictions and preserve an “unresolved” outcome if calibration or the measured interval does not distinguish the signs. Neither table row alone is a detailed physical mechanism: a fuller candidate must explain why its state and transfer arise. State that remaining mechanism gap explicitly.

As a synthetic planning rule only, suppose a calibrated difference has a declared bounded error of 1/4. A predicts [3/4,5/4], B predicts [−5/4,−3/4]. These intervals do not overlap. A value 0 lies in neither, so retain a mismatch with both candidates. Do not force it into the nearer label or erase the value. A real interval must come from its actual calibration and uncertainty contract, not from this teaching choice.

> Claim scope: Binary counting and the table are exact finite deductions on synthetic inputs. The mechanism candidates and error bound are authored examples. Source portfolio minimality remains source-reported, and actual detection remains a prospective task.

## C30.04-D1 — Diagnostics and worked answers

1. Can one yes/no question distinguish four unrestricted states? **Answer:** No; at most two answer classes are available.
2. If both models predict sum 3, what does sum 3 choose? **Answer:** Neither model uniquely; preserve both.
3. If the difference is 0 under the toy interval rule, which candidate wins? **Answer:** Neither; the value is outside both intervals and remains a mismatch requiring explanation.
4. A researcher changes thetaA after reading the result. What record is needed? **Answer:** Preserve the original prediction/residual, declare the revised candidate and its extra choice, and reserve new independent data for its check.

Next dependency: [Lesson 5](lesson-05.md) freezes this comparison into a complete protocol.
