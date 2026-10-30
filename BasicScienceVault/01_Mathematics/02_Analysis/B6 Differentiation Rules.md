---
aliases: [Differentiation Rules, Derivatives, Ableitungsregeln]
tags: [analysis, derivative, type/overview, neuro]
---
# B6 Differentiation Rules

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B6 Differentiation Rules - Worksheet|✏️ Worksheet]] · [[B6 Differentiation Rules - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
The derivative is the **rate of change**. Neural dynamics are written as differential equations ($\frac{dV}{dt} = \dots$), capacitive current is $C\frac{dV}{dt}$, learning rules follow gradients $\frac{\partial E}{\partial w}$, and sensitivity of a response to a stimulus is a slope.

## Definition
$$f'(x) = \frac{df}{dx} = \lim_{h\to0}\frac{f(x+h) - f(x)}{h}$$
Geometrically: slope of the tangent at $x$. Physically: instantaneous rate of change ([[B5 Limits and Continuity]]).

## Basic derivatives
| $f(x)$ | $f'(x)$ |
|---|---|
| $c$ (constant) | $0$ |
| $x^n$ (any real $n$) | $n x^{n-1}$ |
| $\sqrt x = x^{1/2}$ | $\frac{1}{2\sqrt x}$ |
| $\frac1x = x^{-1}$ | $-\frac1{x^2}$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x\ln a$ |
| $\ln x$ | $\frac1x$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |

## The rules
| Rule | Formula | Example |
|---|---|---|
| Constant factor | $(c\,f)' = c\,f'$ | $(5x^3)' = 15x^2$ |
| Sum | $(f + g)' = f' + g'$ | $(x^2 + \sin x)' = 2x + \cos x$ |
| **Product** | $(f g)' = f'g + fg'$ | $(x^2e^x)' = 2xe^x + x^2e^x$ |
| **Quotient** | $\left(\dfrac fg\right)' = \dfrac{f'g - fg'}{g^2}$ | $\left(\dfrac{x}{x+1}\right)' = \dfrac{(x+1) - x}{(x+1)^2} = \dfrac1{(x+1)^2}$ |
| **Chain** | $\big(f(g(x))\big)' = f'(g(x))\cdot g'(x)$ | $(e^{-x^2})' = e^{-x^2}\cdot(-2x)$ |

**Chain rule mantra:** "outer derivative (inner left untouched) **times** inner derivative".
Examples: $(\sin 3x)' = 3\cos 3x$; $\;(\ln(x^2+1))' = \frac{2x}{x^2+1}$; $\;(e^{-t/\tau})' = -\frac1\tau e^{-t/\tau}$; $\;\big((3x+2)^4\big)' = 4(3x+2)^3\cdot3$.

**Higher derivatives:** $f''$ = derivative of $f'$ (curvature, acceleration).
**Partial derivatives:** for $f(x, y)$, $\frac{\partial f}{\partial x}$ treats $y$ as a constant.
**L'Hôpital:** for $\frac00$ or $\frac\infty\infty$: $\lim\frac fg = \lim\frac{f'}{g'}$ (differentiate numerator and denominator *separately*, not the quotient rule!).

## In neuroscience #neuro
- **Membrane equation:** the capacitive current is $I_C = C_m\frac{dV}{dt}$. The leaky integrate-and-fire model:
  $$\tau_m\frac{dV}{dt} = -(V - E_L) + R_m I(t)$$
  Steady state: $\frac{dV}{dt} = 0 \Rightarrow V = E_L + R_mI$.
- **Sigmoid activation** $\sigma(x) = \frac1{1+e^{-x}}$ has the elegant derivative $\sigma'(x) = \sigma(x)\big(1 - \sigma(x)\big)$ – maximal (0.25) at $x = 0$: the neuron is most sensitive to input changes in the middle of its range.
- **Gradient descent / learning rules:** change weights against the gradient of an error, $\Delta w = -\eta\frac{\partial E}{\partial w}$. For $E = \frac12(y - wx)^2$: $\frac{\partial E}{\partial w} = -(y - wx)x$ → the **delta rule** $\Delta w = \eta(y - wx)x$.
- **Sensitivity / discrimination:** the slope of a tuning curve $r'(\theta)$ determines how well small stimulus changes can be discriminated (Fisher information $\propto r'^2$).
- **Hodgkin–Huxley:** a system of four differential equations; its gating variables follow $\frac{dm}{dt} = \alpha_m(1-m) - \beta_m m$.

## Connections
- Derivatives in several variables (gradient, Jacobian) → [[B11 Multivariable Calculus]]; equations with derivatives → [[B10 Differential Equations]]
- Definition as a limit → [[B5 Limits and Continuity]]
- Inverse operation → [[B7 Antiderivatives and Integration]] (fundamental theorem)
- $f'$ → monotonicity and extrema → [[B1 Properties of Functions]], [[B8 Curve Sketching]]
- Derivatives at a point build Taylor polynomials → [[B9 Taylor Series]]
- Linearising a system: Jacobian matrix → [[C4 Eigenvalues and Eigenvectors]]
- Power rule ← [[A1 Exponent Rules]]

## Where this is used in the vault
**Most important applications:** Capacitive current $C\,dV/dt$ ([[Ph05 Capacitance and RC Circuits]]), Fick's law ([[Ph07 Diffusion and Transport]]), Faraday's law ([[Ph06 Magnetism and Induction]]), Hodgkin–Huxley ([[Bio05 Neurons and Action Potentials]]), gradients and backprop ([[CS04 Optimization]], [[CS08 Deep Neural Networks]]).

**All notes that build on this topic:**
- *Physics:* [[Ph01 Mechanics and Energy]] · [[Ph02 Electricity and Charge]] · [[Ph03 Electric Fields and Potential]] · [[Ph05 Capacitance and RC Circuits]] · [[Ph06 Magnetism and Induction]] · [[Ph07 Diffusion and Transport]] · [[Ph08 Thermodynamics and Statistics]] · [[Ph09 Waves and Oscillations]] · [[Ph10 Signal Propagation and Cable Theory]]
- *Chemistry:* [[Ch05 Redox and Electrochemistry]]
- *Biology:* [[Bio03 Proteins and Enzymes]] · [[Bio04 Nucleic Acids and Gene Expression]] · [[Bio05 Neurons and Action Potentials]] · [[Bio06 Synapses and Neurotransmitters]]
- *Computer Science:* [[CS01 Mathematical Foundations]] · [[CS04 Optimization]] · [[CS08 Deep Neural Networks]] · [[CS10 Dynamical and Computational Neuro Models]]
- *Programming:* [[Py09 Python Machine Learning Libraries]] · [[Doc02 Math in Markdown]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Rewrite roots and fractions as powers before differentiating.
- Product rule: $f'g + fg'$ (not $f'g'$!). Quotient: "low d-high minus high d-low, over low squared" (German: NAZ − ZAN).
- Chain rule: never forget the inner derivative.
