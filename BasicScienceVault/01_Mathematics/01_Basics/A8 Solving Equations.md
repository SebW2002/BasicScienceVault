---
aliases: [Solving Equations, Gleichungen lösen, Rearranging Formulas]
tags: [basics, equation, algebra, type/overview, neuro]
---
# A8 Solving Equations

> [[A0 Basics MOC|↑ Basics MOC]] · [[A8 Solving Equations - Worksheet|✏️ Worksheet]] · [[A8 Solving Equations - Solutions|✅ Solutions]] · [[Mistakes - Basics|⚠️ Mistake log]]

## Why this matters
Most "maths" in a neuroscience course is actually rearranging a formula to get the quantity you want: a time constant from a fit, a reversal potential, the time a neuron needs to reach threshold. This note collects all equation types you need.

## The principle: equivalence transformations
Do **the same** to both sides: add/subtract any term, multiply/divide by a **non-zero** term, apply an **invertible** function (exp, ln, cube root …).
Careful with operations that are *not* equivalence transformations:
- **Squaring** can add false solutions → always check ([[A2 Root Rules]]).
- **Dividing by a variable** can lose solutions: from $x^2 = 2x$, dividing by $x$ gives only $x = 2$ – but $x = 0$ is also a solution. Instead: $x^2 - 2x = 0 \Rightarrow x(x - 2) = 0$.

## Equation types
### Linear
$ax + b = c \Rightarrow x = \dfrac{c - b}{a}$ ($a \neq 0$). Collect $x$-terms on one side, then [[A4 Factoring and Simplifying|factor out]] $x$.

### Quadratic $ax^2 + bx + c = 0$
$$x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \qquad \text{or for } x^2 + px + q = 0:\quad x_{1,2} = -\frac p2 \pm \sqrt{\left(\frac p2\right)^2 - q}$$
Discriminant $D = b^2 - 4ac$: $D > 0$ two, $D = 0$ one, $D < 0$ no real solutions (but complex ones → [[E2 Complex Numbers]]).
Shortcuts: no constant term → factor out $x$; no linear term → $x^2 = k$, $x = \pm\sqrt k$.

### Product = 0
$A \cdot B = 0 \iff A = 0 \text{ or } B = 0$. The most powerful trick: **factor, then set each factor to zero**.

### Substitution
$x^4 - 5x^2 + 4 = 0$: set $u = x^2$ → $u^2 - 5u + 4 = 0$ → $u \in \{1, 4\}$ → $x \in \{\pm1, \pm2\}$.

### Fractional equations
State the domain (denominators ≠ 0), multiply by the common denominator, solve, check against the domain.

### Exponential & logarithmic equations
Isolate the exponential, then take $\ln$: $\;e^{kt} = c \Rightarrow t = \dfrac{\ln c}{k}$. Isolate the log, then exponentiate: $\ln x = a \Rightarrow x = e^a$ ([[A3 Logarithms]]).

### Absolute value
$\lvert x - a \rvert = b$ ($b \ge 0$) $\iff x - a = b$ or $x - a = -b$.

### Inequalities
Like equations, **but** multiplying/dividing by a negative number **flips** the sign: $-2x > 6 \Rightarrow x < -3$.

## In neuroscience #neuro
**Time to threshold.** A passive membrane charged by a constant current follows (see [[B2 Exponential Functions]])
$$V(t) = V_\infty\left(1 - e^{-t/\tau}\right)$$
When does it reach $V_\theta$? Isolate the exponential, take $\ln$:
$$e^{-t/\tau} = 1 - \frac{V_\theta}{V_\infty} \;\Rightarrow\; t = -\tau \ln\!\left(1 - \frac{V_\theta}{V_\infty}\right)$$
If $V_\theta \ge V_\infty$ the log is undefined → the neuron **never** fires (the current is "sub-rheobase"). This formula gives the firing rate of the leaky integrate-and-fire neuron.

**Rearranging standard formulas:** $\tau = RC \Rightarrow C = \tau/R$; $\;I = g(V - E) \Rightarrow V = E + I/g$; $\;$ Ohm's law; reversal potential from the Nernst equation; steady state $dV/dt = 0$.

## Connections
- Tools for isolating: [[A4 Factoring and Simplifying]], [[A5 Fractions]], [[A2 Root Rules]], [[A3 Logarithms]]
- Several equations at once → [[C3 Linear Systems and Gaussian Elimination]]
- Zeros of functions → [[B1 Properties of Functions]], [[B8 Curve Sketching]]
- Negative discriminant → [[E2 Complex Numbers]]

## Where this is used in the vault
**Most important applications:** Rearranging formulas: time to threshold, Ohm's law, steady states ([[Ph05 Capacitance and RC Circuits]], [[Bio05 Neurons and Action Potentials]]).

**All notes that build on this topic:**
- *Physics:* [[Ph04 Circuits and Resistance]] · [[Ph05 Capacitance and RC Circuits]] · [[Ph11 Optics and Fluorescence]]
- *Chemistry:* [[Ch01 Atomic Structure]]
- *Biology:* [[Bio05 Neurons and Action Potentials]]
- *Methods:* [[Meth02 Structural Biology]] · [[Meth03 Electrophysiology]]
- *Programming:* [[Py08 SciPy Scientific Computing]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Factor and use "product = 0" instead of dividing by variables.
- Check solutions after squaring and against the domain.
- Isolate the exp/log first, then apply its inverse.
- Inequalities flip when multiplying by negatives.
