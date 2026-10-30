---
aliases: [Curve Sketching, Kurvendiskussion, Function Analysis]
tags: [analysis, curve-sketching, derivative, type/overview, neuro]
---
# B8 Curve Sketching

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B8 Curve Sketching - Worksheet|✏️ Worksheet]] · [[B8 Curve Sketching - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
Curve sketching combines everything from Analysis into one procedure: given a formula, find out what the graph looks like and where its important points are. In neuroscience you use exactly this to find **peak times** of PSPs, **optimal stimuli** of tuning curves and the **most sensitive point** of a sigmoid.

## The checklist
| Step | What | How |
|---|---|---|
| 1 | Domain | exclude division by 0, $\ln(\le0)$, $\sqrt{<0}$ ([[B1 Properties of Functions]]) |
| 2 | Symmetry | $f(-x) = f(x)$ even / $f(-x) = -f(x)$ odd |
| 3 | Zeros & y-intercept | $f(x) = 0$; $f(0)$ |
| 4 | Behaviour at boundaries | limits $x\to\pm\infty$, near poles ([[B5 Limits and Continuity]]) |
| 5 | **Extrema** | $f'(x) = 0$ (necessary) + sign change of $f'$ or $f''(x) \neq 0$ (sufficient) |
| 6 | **Monotonicity** | $f' > 0$ increasing, $f' < 0$ decreasing |
| 7 | **Inflection points** | $f''(x) = 0$ + sign change of $f''$ (or $f''' \neq 0$) |
| 8 | **Curvature** | $f'' > 0$ convex (left curve, "cup"), $f'' < 0$ concave ("cap") |
| 9 | Sketch | plot all points, asymptotes, then connect |

### Classifying critical points
At $x_0$ with $f'(x_0) = 0$:
- $f''(x_0) < 0$ → **local maximum** (curve bends down)
- $f''(x_0) > 0$ → **local minimum**
- $f''(x_0) = 0$ → test fails; check sign change of $f'$ (e.g. $x^3$ at 0: no extremum, saddle point)

> [!warning] $f'(x_0) = 0$ alone is **not** sufficient for an extremum ($f(x) = x^3$ at $x = 0$).

## Worked example: $f(x) = x^3 - 3x$
1. Domain $\mathbb R$. 2. $f(-x) = -f(x)$ → odd. 3. $x(x^2 - 3) = 0 \Rightarrow x \in\{0, \pm\sqrt3\}$. 4. $x\to\pm\infty$: $f\to\pm\infty$.
5. $f'(x) = 3x^2 - 3 = 0 \Rightarrow x = \pm1$; $f''(x) = 6x$: $f''(-1) = -6 < 0$ → max at $(-1, 2)$; $f''(1) = 6 > 0$ → min at $(1, -2)$.
6. Increasing on $(-\infty, -1]$ and $[1, \infty)$, decreasing on $[-1, 1]$.
7. $f''(x) = 0 \Rightarrow x = 0$, sign change → inflection point $(0, 0)$.

## In neuroscience #neuro
- **Alpha function** (model of a PSP/synaptic conductance):
  $$\alpha(t) = \frac{t}{\tau}\,e^{1 - t/\tau}, \quad t \ge 0$$
  $\alpha'(t) = \frac1\tau e^{1-t/\tau}\left(1 - \frac t\tau\right) = 0 \Rightarrow t = \tau$. Peak time $= \tau$, peak value $= 1$ (that's why the factor $e$ is included). Rises fast, decays slowly, inflection at $t = 2\tau$.
- **Difference of exponentials** $e^{-t/\tau_d} - e^{-t/\tau_r}$: peak time $t^* = \frac{\tau_r\tau_d}{\tau_d - \tau_r}\ln\frac{\tau_d}{\tau_r}$ – derived exactly by setting $f' = 0$.
- **Sigmoid:** no extrema, monotonically increasing, inflection point at the midpoint = steepest slope = highest sensitivity.
- **Gaussian tuning curve** $e^{-x^2/(2\sigma^2)}$: maximum at the preferred stimulus, inflection points at $\pm\sigma$ – the **flanks** (steepest parts) are where discrimination is best, not the peak!
- **Optimisation:** finding optimal parameters = finding extrema of a cost/likelihood function.

## Connections
- Tools: [[B6 Differentiation Rules]], [[B5 Limits and Continuity]], [[B1 Properties of Functions]]
- Zeros → [[A8 Solving Equations]]
- Exponential examples → [[B2 Exponential Functions]]
- Local behaviour by Taylor → [[B9 Taylor Series]]

## Where this is used in the vault
**Most important applications:** Peak time of PSPs, steepest point of sigmoids ([[Bio06 Synapses and Neurotransmitters]], [[Bio02 Membranes and Transport]]), maximum likelihood and optima ([[CS02 Probability and Statistics]], [[CS04 Optimization]]).

**All notes that build on this topic:**
- *Physics:* [[Ph07 Diffusion and Transport]] · [[Ph08 Thermodynamics and Statistics]]
- *Chemistry:* [[Ch04 Acids Bases and pH]]
- *Biology:* [[Bio02 Membranes and Transport]] · [[Bio03 Proteins and Enzymes]] · [[Bio05 Neurons and Action Potentials]] · [[Bio06 Synapses and Neurotransmitters]]
- *Computer Science:* [[CS02 Probability and Statistics]] · [[CS03 Information Theory]] · [[CS04 Optimization]] · [[CS10 Dynamical and Computational Neuro Models]]
- *Programming:* [[Py07 Python Plotting and Visualization]] · [[MAT05 MATLAB Plotting]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- $f' = 0$ → candidates; $f''$ or sign change → decide.
- $f'' = 0$ + sign change → inflection (steepest/flattest point).
- Always state points as coordinates $(x, f(x))$.
