# Lesson 4 — Unbroken charge and mass formulas

Essential question: What can algebra determine from supplied couplings and a vacuum magnitude?

Goals: substitute values with correct units; derive the rho identity on its domain; distinguish a formula input from its output.

Bridge: lesson 3 selected the neutral direction without selecting v. Here v enters two supplied formulas. Two 55-minute periods each use 5 retrieval, 20 teaching/examples, 15 practice, 15 diagnostics/repair. Period 1 focuses on squares and units; period 2 on cancellation, boundaries, and rescaling.

## C16.04-E1 — An identity with a domain

The source compiler formulas are

m_W² = g2² v²/4, and m_Z² = (g2²+gY²)v²/4.

Here g2 and gY are real dimensionless coupling inputs; v≥0 has mass unit μ. A coupling records a strength in the supplied convention. W and Z label two gauge-boson mass outputs; detailed particle dynamics are outside this calculation. Squared masses have unit μ², and the masses themselves are the nonnegative square roots. Square each input before adding: g2²+gY² is generally different from (g2+gY)².

Define c²_theta = g2²/(g2²+gY²). The source notation for this number is cos²θ. In this course the ratio is its operational definition; no trigonometry or angle extraction is required. It is defined when g2²+gY²>0. Define rho, written ρ, by ρ=m_W²/(m_Z² c²_theta) only if that denominator is nonzero.

Substitute before cancelling:

m_Z² c²_theta = [(g2²+gY²)v²/4] × [g2²/(g2²+gY²)] = g2²v²/4 = m_W².

The cancelled factor g2²+gY² must be nonzero. To divide by the resulting m_W² also requires g2≠0 and v≠0. On that domain, ρ=(g2²v²/4)/(g2²v²/4)=1. The result is dimensionless because μ² cancels. This is a derived algebraic identity conditional on the supplied formulas, not a derivation of those formulas from a kinetic field theory.

## C16.04-W1 — Worked substitution

Choose synthetic g2=3, gY=4, v=2 μ. Then g2²=9, gY²=16, v²=4 μ². We obtain m_W²=9×4/4=9 μ² and m_Z²=(9+16)×4/4=25 μ². Thus m_W=3 μ and m_Z=5 μ. Also c²_theta=9/25. The rho denominator is 25×9/25=9 μ², nonzero; ρ=9/9=1.

## C16.04-P1 — Practice and scaling

Choose synthetic g2=4, gY=3, v=2 μ. Calculate squared masses, masses, c²_theta, and ρ. Then double only v. Finally set v=0 and test whether ρ can be evaluated.

Worked answer: m_W²=16×4/4=16 μ²; m_Z²=(16+9)×4/4=25 μ². Nonnegative roots give 4 μ and 5 μ. c²_theta=16/25, and the denominator 25×16/25=16 μ² gives ρ=1. At v=4 μ, squared masses are 64 and 100 μ²; masses are 8 and 10 μ. Doubling v multiplies v² by four, so it quadruples squared masses and doubles positive masses while leaving the couplings and ratio fixed. At v=0 both squared masses vanish, and the displayed ratio is 0/0, which is undefined.

> Claim scope: S02 /proof_nodes/80 supplies the mass-squared relations and reports the compiler rho identity. Our fresh verification is substitution and cancellation on the explicit nonzero domain. Values are synthetic; matching scale and numerical couplings are retained inputs. No measured mass or compiler execution is asserted.

## Diagnostics and worked answers

1. **C16.04-D1:** Is rho numerically 1 at v=0? Answer: the displayed expression is undefined there. A limiting value is a different statement and is not used to fill 0/0.
2. **C16.04-D2:** If g2=0, gY=3, v=2 μ, what fails? Answer: m_W²=0, m_Z²=9 μ², c²_theta=0; the rho denominator is zero. If both couplings vanish, even c²_theta is undefined.
3. **C16.04-D3:** Does changing gY from 3 to −3 change P1? Answer: no; gY enters through gY²=9 in these formulas. This degeneracy means the squared-mass outputs alone do not recover every sign.
4. **C16.04-D4:** Is 25 μ² a mass? Answer: it is a squared mass; its nonnegative square root is 5 μ. Confusing them would break units and scaling.

Next dependency: [Lesson 5](lesson-05.md) treats coefficient matrices as additional inputs, independent of charge cancellation.
