---
aliases: [Taylor Series, Taylorreihen, Linearization, Taylor Polynomial]
tags: [analysis, taylor, derivative, type/overview, neuro]
---
# B9 Taylor Series

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B9 Taylor Series - Worksheet|✏️ Worksheet]] · [[B9 Taylor Series - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
Nonlinear functions are hard; polynomials are easy. Taylor series approximate any smooth function near a point by a polynomial. The first-order version – **linearisation** – is the reason why linear models work at all in neuroscience: every smooth system looks linear if you zoom in far enough.

## The Taylor polynomial
Approximation of $f$ around the point $a$:
$$T_n(x) = \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x - a)^k = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots$$
For $a = 0$ it's called a **Maclaurin** series. As $n\to\infty$ it becomes the **Taylor series**, which (inside its radius of convergence) equals $f$.

| Order | Name | Meaning |
|---|---|---|
| $T_0 = f(a)$ | constant | value |
| $T_1 = f(a) + f'(a)(x-a)$ | **linearisation** / tangent | value + slope |
| $T_2$ | quadratic approximation | + curvature |

The more terms, the better the approximation – and the further from $a$ it stays accurate. The error of $T_n$ is roughly the size of the first omitted term.

## Series to know by heart (around $a = 0$)
| Function | Series | Valid for |
|---|---|---|
| $e^x$ | $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = \sum \frac{x^k}{k!}$ | all $x$ |
| $\sin x$ | $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$ | all $x$ |
| $\cos x$ | $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$ | all $x$ |
| $\ln(1 + x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$ | $-1 < x \le 1$ |
| $\frac1{1-x}$ | $1 + x + x^2 + x^3 + \dots$ (geometric series) | $\lvert x\rvert < 1$ |
| $(1 + x)^n$ | $1 + nx + \binom n2 x^2 + \dots$ | $\lvert x\rvert < 1$ |

**Small-$x$ approximations** (first order): $e^x \approx 1 + x$, $\;\sin x \approx x$, $\;\cos x\approx 1 - \frac{x^2}2$, $\;\ln(1+x)\approx x$, $\;(1+x)^n \approx 1 + nx$, $\;\sqrt{1+x}\approx 1 + \frac x2$.

Neat consequences: differentiating $\sum\frac{x^k}{k!}$ term by term gives the same series → $(e^x)' = e^x$; substituting $ix$ gives Euler's formula $e^{ix} = \cos x + i\sin x$ ([[E2 Complex Numbers]]).

## In neuroscience #neuro
- **Linearisation around an operating point:** a neuron with sigmoid response $\sigma(x)$ near $x = 0$ behaves like $\sigma(x) \approx \frac12 + \frac x4$ – small inputs are processed linearly. This justifies linear receptive-field models for small stimulus fluctuations.
- **Stability of fixed points:** near a fixed point $x^*$, $\frac{dx}{dt} = f(x) \approx f'(x^*)(x - x^*)$. If $f'(x^*) < 0$ perturbations decay (stable). In several dimensions $f'$ becomes the **Jacobian matrix** and stability is decided by its eigenvalues ([[C4 Eigenvalues and Eigenvectors]]). This is how bifurcations in Hodgkin–Huxley / FitzHugh–Nagumo models are analysed.
- **Euler method:** numerical simulation of $\frac{dV}{dt} = f(V)$ uses the first-order Taylor step
  $$V(t + \Delta t) \approx V(t) + \Delta t\cdot f(V(t))$$
  Error per step $\sim\Delta t^2$ → small time steps needed.
- **Initial slope of exponentials:** $1 - e^{-t/\tau}\approx \frac t\tau$ for $t \ll \tau$ – at first a capacitor charges linearly.
- **Small-angle approximations** in optics / eye movements: $\sin\theta\approx\theta$, $\tan\theta\approx\theta$ (in radians).

## Connections
- Euler method and stability of ODEs → [[B10 Differential Equations]]; multivariable Taylor (Jacobian, Hessian) → [[B11 Multivariable Calculus]]
- Needs derivatives → [[B6 Differentiation Rules]]; factorials and $\Sigma$ → [[A7 Sums Products and Factorials]]
- $(1+x)^n$ → [[A6 Binomial Formulas and Theorem]]
- Limits like $\frac{\sin x}{x}\to1$ → [[B5 Limits and Continuity]]
- Local shape (tangent, curvature) → [[B8 Curve Sketching]]
- Jacobian & stability → [[C4 Eigenvalues and Eigenvectors]]
- Euler's formula → [[E2 Complex Numbers]]

## Where this is used in the vault
**Most important applications:** Euler integration and linearisation of neuron models ([[CS10 Dynamical and Computational Neuro Models]], [[Ph05 Capacitance and RC Circuits]]), Jacobians ([[CS01 Mathematical Foundations]]).

**All notes that build on this topic:**
- *Physics:* [[Ph05 Capacitance and RC Circuits]] · [[Ph10 Signal Propagation and Cable Theory]]
- *Computer Science:* [[CS01 Mathematical Foundations]] · [[CS10 Dynamical and Computational Neuro Models]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- $T_1$ = tangent line = linearisation.
- Know the series of $e^x$, $\sin$, $\cos$, $\ln(1+x)$, $\frac1{1-x}$.
- Linear approximations are only good close to the expansion point.
