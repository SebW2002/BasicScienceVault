---
aliases: [Properties of Functions, Funktionseigenschaften]
tags: [analysis, function, type/overview, neuro]
---
# B1 Properties of Functions

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B1 Properties of Functions - Worksheet|✏️ Worksheet]] · [[B1 Properties of Functions - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
Tuning curves, f–I curves, dose–response curves, activation functions in neural networks: they are all functions, and the first thing you do in a paper figure is read off their properties – where they are zero, where they peak, whether they saturate, whether they're symmetric.

## Basic vocabulary
A **function** $f: D \to \mathbb R$ assigns to every $x$ in the **domain** $D$ exactly one value $f(x)$. The set of all values is the **range**.

| Property | Definition | How to check |
|---|---|---|
| **Domain** | allowed $x$ | exclude: denominator $= 0$, $\sqrt{\text{negative}}$, $\ln(\le 0)$ |
| **Zeros** | $f(x) = 0$ | solve the equation ([[A8 Solving Equations]]); factored form helps |
| **y-intercept** | $f(0)$ | plug in 0 |
| **Even** (axis-symmetric) | $f(-x) = f(x)$ | only even powers, $\cos$, $\lvert x\rvert$ |
| **Odd** (point-symmetric) | $f(-x) = -f(x)$ | only odd powers, $\sin$, $\tan$ |
| **Monotonically increasing** | $x_1 < x_2 \Rightarrow f(x_1) \le f(x_2)$ | $f'(x) \ge 0$ → [[B6 Differentiation Rules]] |
| **Pole** | $f(x) \to \pm\infty$ as $x \to x_0$ | denominator zero that doesn't cancel |
| **Asymptote** | curve approaches a line | limits → [[B5 Limits and Continuity]] |
| **Injective / invertible** | different $x$ → different $f(x)$ | strictly monotonic ⇒ invertible |

## Rational functions $f(x) = \dfrac{p(x)}{q(x)}$
1. Factor numerator and denominator ([[A4 Factoring and Simplifying]]).
2. Common factor → **removable discontinuity** (a "hole"); remaining denominator zeros → **poles**.
3. Horizontal asymptote: compare degrees – numerator smaller → $y = 0$; equal → ratio of leading coefficients; numerator larger → no horizontal asymptote.

Example: $f(x) = \dfrac{x^2 - 1}{x^2 - x} = \dfrac{(x-1)(x+1)}{x(x-1)}$ → hole at $x = 1$, pole at $x = 0$, horizontal asymptote $y = 1$.

## Transformations of $y = f(x)$
| New function | Effect |
|---|---|
| $f(x) + c$ | shift up by $c$ |
| $f(x - c)$ | shift **right** by $c$ |
| $a \cdot f(x)$ | stretch vertically by $a$ (flip if $a<0$) |
| $f(bx)$ | compress horizontally by $b$ |
| $-f(x)$, $f(-x)$ | mirror at x-axis / y-axis |

**Composition:** $(f \circ g)(x) = f(g(x))$ – "first $g$, then $f$". Generally $f \circ g \neq g \circ f$.
**Inverse function:** solve $y = f(x)$ for $x$, swap names. Graph = mirror image at $y = x$. Example: $\ln$ and $\exp$ ([[B3 Logarithmic Functions]]).

## In neuroscience #neuro
- **Orientation tuning curve (Gaussian):** $r(\theta) = r_0 + r_\text{max}\, e^{-(\theta - \theta_\text{pref})^2 / (2\sigma^2)}$ – **even** about $\theta_\text{pref}$, maximum at the preferred orientation, width $\sigma$.
- **f–I curve:** firing rate vs. injected current – zero below rheobase, then **monotonically increasing**, often saturating.
- **Activation functions:** sigmoid $\sigma(x) = \frac{1}{1 + e^{-x}}$ (monotonic, asymptotes 0 and 1), ReLU $\max(0, x)$, tanh (odd).
- **Contrast response (Naka–Rushton):** $R(c) = R_\text{max}\dfrac{c^n}{c^n + c_{50}^n}$ – monotonic, horizontal asymptote $R_\text{max}$ (saturation).
- **Pole in practice:** conductance estimated from current, $g = \frac{I}{V - E}$, has a pole at $V = E$ – near the reversal potential conductance estimates explode with noise.

## Connections
- Monotonicity & extrema via $f'$ → [[B6 Differentiation Rules]], [[B8 Curve Sketching]]
- Asymptotes & poles via limits → [[B5 Limits and Continuity]]
- Inverse functions: [[B2 Exponential Functions]] ↔ [[B3 Logarithmic Functions]]
- Symmetry of trig functions → [[B4 Trigonometric Functions]]

## Where this is used in the vault
**Most important applications:** Sigmoid gating and dose–response curves ([[Bio02 Membranes and Transport]], [[Bio03 Proteins and Enzymes]]), I–V relations ([[Ph04 Circuits and Resistance]]), tuning curves ([[Bio07 Neural Circuits and Systems]]).

**All notes that build on this topic:**
- *Physics:* [[Ph04 Circuits and Resistance]]
- *Chemistry:* [[Ch04 Acids Bases and pH]]
- *Biology:* [[Bio02 Membranes and Transport]] · [[Bio03 Proteins and Enzymes]] · [[Bio07 Neural Circuits and Systems]]
- *Methods:* [[Meth05 Molecular Biology Tools]]
- *Computer Science:* [[CS07 Machine Learning Fundamentals]]
- *Programming:* [[Prog00 Shared Programming Concepts]] · [[Py03 Python Control Flow and Functions]] · [[R03 R Control Flow and Functions]] · [[R04 R Data Import and Tidy Data]] · [[MAT03 MATLAB Control Flow and Functions]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Domain first – denominators, roots, logs.
- Even: $f(-x) = f(x)$; odd: $f(-x) = -f(x)$; most functions are neither.
- Factor rational functions to tell holes from poles.
