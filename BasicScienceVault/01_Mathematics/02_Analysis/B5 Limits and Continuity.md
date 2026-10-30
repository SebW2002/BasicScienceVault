---
aliases: [Limits and Continuity, Grenzwerte, Stetigkeit]
tags: [analysis, limit, continuity, type/overview, neuro]
---
# B5 Limits and Continuity

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B5 Limits and Continuity - Worksheet|✏️ Worksheet]] · [[B5 Limits and Continuity - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
Limits are the foundation of derivatives ("instantaneous rate") and integrals ("infinitely fine sums"). Practically, they tell you **where a system ends up** ($t \to \infty$), how a function behaves near forbidden points, and whether a model jumps.

## The idea
$$\lim_{x \to a} f(x) = L$$
means: as $x$ gets arbitrarily close to $a$ (but $\neq a$), $f(x)$ gets arbitrarily close to $L$. The value $f(a)$ itself doesn't matter – it may not even exist.

**One-sided limits:** $\lim_{x\to a^-}$ (from the left), $\lim_{x\to a^+}$ (from the right). The limit exists only if both agree.

## Limit rules
If $\lim f = F$ and $\lim g = G$ exist: limits of sums, differences, products, quotients ($G \neq 0$) and of continuous functions are computed term by term.

## Toolbox for computing limits
| Situation | Technique | Example |
|---|---|---|
| $f$ continuous at $a$ | just plug in | $\lim_{x\to2}(3x^2 - 1) = 11$ |
| $\frac00$ with polynomials | factor & cancel | $\lim_{x\to3}\frac{x^2-9}{x-3} = \lim_{x\to3}(x+3) = 6$ |
| $\frac00$ with roots | expand with conjugate | $\frac{\sqrt x - 2}{x-4} = \frac{1}{\sqrt x + 2} \to \frac14$ |
| $x \to \infty$, rational | divide by highest power | $\frac{3x^2+1}{x^2-5} \to 3$ |
| $\frac{c}{0}$ ($c \neq 0$) | pole → $\pm\infty$, check sign | $\lim_{x\to0^+}\frac1x = +\infty$ |
| $\frac00$ or $\frac\infty\infty$ in general | L'Hôpital: $\lim\frac fg = \lim\frac{f'}{g'}$ | → [[B6 Differentiation Rules]] |

**Important standard limits**
$$\lim_{x\to0}\frac{\sin x}{x} = 1, \qquad \lim_{n\to\infty}\left(1 + \frac an\right)^n = e^a, \qquad \lim_{x\to\infty} x^k e^{-x} = 0, \qquad \lim_{x\to\infty}\frac{\ln x}{x} = 0$$
Hierarchy for $x \to \infty$: $\ln x \ll x^a \ll e^x$ – "exponential beats power beats log".

## Continuity
$f$ is **continuous at $a$** if $\lim_{x\to a} f(x) = f(a)$ (limit exists, value exists, both agree). Intuitively: you can draw the graph without lifting the pen.

| Discontinuity | Example |
|---|---|
| Removable (hole) | $\frac{x^2-1}{x-1}$ at $x = 1$ |
| Jump | Heaviside step $H(x)$ at $0$ |
| Pole (infinite) | $\frac1{x-2}$ at $x = 2$ |

Polynomials, $e^x$, $\sin$, $\cos$ are continuous everywhere; $\ln$, roots and rational functions on their domains. **Intermediate value theorem:** a continuous function that is negative at $a$ and positive at $b$ has a zero in between.

## In neuroscience #neuro
- **Instantaneous firing rate:** $r(t) = \lim_{\Delta t\to0}\frac{\text{spikes in } [t, t+\Delta t)}{\Delta t}$ – in practice estimated with finite windows or kernels.
- **Steady states:** $\lim_{t\to\infty}V(t)$ for $V(t) = V_\infty + (V_0 - V_\infty)e^{-t/\tau}$ is $V_\infty$ ([[B2 Exponential Functions]]).
- **Integrate-and-fire neurons** are deliberately *discontinuous*: when $V$ hits threshold it jumps back to reset. The spike itself is modelled as a jump or a Dirac delta.
- **Step functions** (Heaviside) model stimulus onset, current injection and threshold nonlinearities.
- **Small-time-step limit:** numerical simulations (Euler method) become exact only in the limit $\Delta t \to 0$ ([[B9 Taylor Series]]).

## Connections
- Derivative = limit of difference quotient → [[B6 Differentiation Rules]]
- Integral = limit of sums → [[B7 Antiderivatives and Integration]]
- Asymptotes, poles, holes → [[B1 Properties of Functions]]
- Factoring to cancel $\frac00$ → [[A4 Factoring and Simplifying]]
- $\varepsilon$–$\delta$ definition uses quantifiers → [[E1 Sets Logic and Quantifiers]]

## Where this is used in the vault
**Most important applications:** Steady states as $t\to\infty$, convergence of gradient descent ([[CS04 Optimization]]), threshold/jump nonlinearities in integrate-and-fire models ([[CS10 Dynamical and Computational Neuro Models]]).

**All notes that build on this topic:**
- *Computer Science:* [[CS04 Optimization]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Plug in first; if you get $\frac00$, simplify (factor, conjugate, L'Hôpital).
- For $x\to\infty$: divide by the highest power; exponential beats power beats log.
- Continuous = limit equals function value.
