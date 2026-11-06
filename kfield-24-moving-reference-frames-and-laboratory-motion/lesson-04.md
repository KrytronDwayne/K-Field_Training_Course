# 4. Adding vectors without mixing frames

Essential question: What motion is hidden when coordinates remain fixed?

Goals

- Explain a derivative as a rate approached by shorter intervals.
- Retain origin, turning-axis and local-motion velocity terms.
- Compute cancellation and acceleration in a supplied rotating example.

Prerequisite bridge: Begin with [Lesson 3](lesson-03.md). Use the four-term sum from Lesson 3, but now allow its axes to turn.


## C24.04-E1 — A fixed coordinate can move

A dot over a quantity means its instantaneous rate of change. Start with average velocity [p(t+h)-p(t)]/h for a nonzero time interval h. If shorter intervals approach one value, that limiting value is the derivative, written ṗ or dp/dt. A second derivative is the rate of change of velocity, called acceleration, in m/s². We use smooth prescribed functions here; a finite jump need not have an instantaneous derivative.

We need only a few rules. A constant has derivative zero, t has derivative one, and sums differentiate term by term. For a product f(t)g(t), expand its change as f(t+h)[g(t+h)-g(t)]+[f(t+h)-f(t)]g(t). Divide by h and let h approach zero. Continuity gives (fg)̇=f ġ+ḟ g. The same expansion applies to every entry of a matrix times a vector, without reversing their order.

For sin θ and cos θ with θ in radians, a small turn h changes the unit-circle point approximately by h(-sin θ,cos θ): its motion is tangent, perpendicular to the radius, with distance h per unit turn. Taking the limit gives d(sin θ)/dθ=cos θ and d(cos θ)/dθ=-sin θ. If θ=ωt, multiply these rates by angular speed ω, in rad/s. The argument ωt is an angle; writing cos t below is shorthand for cos[(1rad/s)t], not the cosine of a dimensional time.

Apply the product rule to p_world=o(t)+R(t)p_local(t):

v_world=ȯ+Ṙp_local+R v_local.

The terms mean origin motion, motion from turning axes, and local motion turned into world axes. Differentiate once more:

a_world=ö+R̈p_local+2Ṙv_local+R a_local.

The factor 2 comes from one Ṙv_local in each of the last two differentiated terms. This formula is taught here for interpretation and the supplied simple example; general calculus is not assumed.

A rotation about +z through θ is R=[(cos θ,-sin θ,0);(sin θ,cos θ,0);(0,0,1)], where semicolons separate rows. At θ=90° it is Lesson 1's matrix. For fixed axes Ṙ=0; a translating origin still contributes ȯ. Always convert compatible units and epochs before adding.

## C24.04-W1 — Stationary locally, moving globally

Let elapsed time t be in seconds, ω=1rad/s, origin o(t)=(t,0,0)m with its first component understood as (1m/s)t, and fixed p_local=(1,0,0)m. Then p_world=(t+cos t,sin t,0)m in this shorthand. The local velocity is zero but the world velocity is (1,0,0)+(-sin t,cos t,0)+(0,0,0)=(1-sin t,cos t,0)m/s. At t=0 it is (1,1,0)m/s. The circular piece has radius 1m; its acceleration is (-cos t,-sin t,0)m/s².

## C24.04-P1 — Cancellation retains its causes

At t=π/2 s, sin t=1 and cos t=0. Origin motion (1,0,0)m/s plus rotation motion (-1,0,0)m/s gives zero velocity. The particle has not been stationary for the whole interval. At t=0 acceleration is (-1,0,0)m/s²; only R̈p_local contributes, because ö, v_local and a_local are zero. The factor of ω²=1s⁻² gives the acceleration unit.

For a separate synthetic residual exercise suppose the model velocity is (1,1,0)m/s and a supplied comparison vector is (1.2,0.9,0)m/s. Residual r=comparison-model=(0.2,-0.1,0)m/s. Store model, r and the comparison; model+r exactly reconstructs it. A vanishing total or a small residual never licenses erasing signed components.

> Scope: These are analytic consequences of synthetic functions. They introduce no Solar/Galactic time law. The additive physical motion and a phase-transformed vector remain different types. Unresolved motion is retained as a vector residual, not silently set to zero.

## C24.04-D1 — Diagnostics

1. A point has v_local=0. Must v_world=0?
2. Name the missing term in ȯ+R v_local for turning axes.
3. In the worked example at t=π/2s, is acceleration also zero?
4. Why can a velocity in km/s not be added numerically to one in m/s?

Answers: 1. No; origin and rotation can move it. 2. Ṙp_local, with units (1/s)m=m/s. 3. No: (-cos(π/2),-sin(π/2),0)=(0,-1,0)m/s². 4. Convert first, using 1km/s=1000m/s, or the sum attaches unequal units to the same numbers.


Next dependency: [lesson-05](lesson-05.md). Carry your signed component ledger forward.
