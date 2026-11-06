# Lesson 04 — Phase factors and their product

**Essential question:** What can disappear from a product without disappearing from the specification?

**Goals:** Compute a six-factor phase product; test factor omission; retain unit-valued contributions and their provenance.

**Prerequisite bridge.** Lesson 03 taught the cycle 1,i,−1,−i and inverse phases. We now use the same multiplication for six contributions. The labels are part of the input: a correct total with a missing label is an incomplete record.

## C19.04-E1 — Six contributions with a declared reading rule

S02 M15 names six determinant-line contributions in this order: **UV, light, reg, heavy, cap, induced**. Here these are source-local labels, not permission to invent numerical physical values. For this finite analogy we choose a basis for each line and a common scalar reading rule called a trivialization, τ. Specifically, τ sends the combined chosen basis to the number 1. Lesson 05 teaches what this means and how it changes under rebasing. This declaration is why, for the present examples, multiplying the six coefficients gives the scalar phase directly.

Write Φ=z_UV z_light z_reg z_heavy z_cap z_induced. Each z is dimensionless, with values drawn from our four quarter-turn phases. Closure for this one specified packet means Φ=1. Multiplying by 1 does not change a number, but a factor whose value is 1 still records that a contribution was supplied and checked. Missing is different from known-to-be-1.

## C19.04-W1 — Multiply without losing the ledger

Our synthetic ordered coefficients are (i,i,−1,−i,i,1). With τ(basis)=1, calculate:

| Contribution | Value | Running product |
|---|---|---|
| UV | i | i |
| light | i | −1 |
| reg | −1 | 1 |
| heavy | −i | −i |
| cap | i | 1 |
| induced | 1 | 1 |

Thus Φ=1. To test deletion of heavy, multiply the remaining five values: i·i·(−1)·i·1=i. Independently divide the complete product by the omitted nonzero factor: 1/(−i)=i. The two routes agree. The omission changed the packet and its closure value. Retain the original factor list and the omission label; a bare result i does not identify which contribution was removed.

The closure residual is ρ=Φ−1. For the complete packet ρ=0; with heavy deleted it is i−1. This is an exact complex difference, not a reason to discard the nonclosing result. Complex differences are written a+bi: i−1=−1+i. We need not convert it to a size score.

## C19.04-P1 — Guided practice

Use (−1,i,i,1,−i,i) in the same label order and the same τ. Find every running product, then delete cap and compare. Explain why heavy stays in the record.

**Worked answer:** Running products are −1,−i,1,1,−i,1. Thus Φ=1. Without cap=−i the product is i, also 1/(−i)=i, with residual i−1. Heavy has value 1, but keeping it records a supplied contribution rather than an absent one. Both the complete and mutated factor lists remain available.

> **Claim scope.** Source M15 describes a tensor product of sections, not six unqualified scalar numbers. Our scalar calculation is valid after the stated basis and τ choice and for this synthetic packet only. A product of 1 neither supplies a global trivialization nor establishes every admitted sector. No physical phase value has been measured here.

## Diagnostics

1. **C19.04-D1:** What does Φ=1 establish for the worked packet, and what remains outside that result?
2. What happens numerically if induced=1 is omitted from W1? Is the record complete?
3. If a missing factor z must satisfy i z=1, find z. May you record it as a recovered source value?
4. What must accompany the residual i−1 for reconstruction of the omitted-factor test?

**Worked answers:** (1) The declared finite scalar product closes; other sectors and global line constructions remain unchecked. (2) The value stays 1, but the record is incomplete. (3) z=−i solves the equation, but this is a conditional algebraic requirement, not evidence of the source factor's value. (4) Keep the original factors, mutation label, basis/trivialization and computed product. Adding 1 to the residual recovers the product, not the individual factors.

**Next dependency:** [Lesson 05](lesson-05.md) explains why the chosen bases and τ cannot be omitted.
