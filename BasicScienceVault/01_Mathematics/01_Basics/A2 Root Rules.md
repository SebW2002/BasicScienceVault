---
aliases: [Root Rules, Radicals, Wurzelgesetze]
tags: [basics, root, exponent, type/overview, neuro]
---
# A2 Root Rules

> [[A0 Basics MOC|↑ Basics MOC]] · [[A2 Root Rules - Worksheet|✏️ Worksheet]] · [[A2 Root Rules - Solutions|✅ Solutions]] · [[Mistakes - Basics|⚠️ Mistake log]]

## Why this matters
Roots appear wherever squares are undone: standard deviations, standard errors, distances (Pythagoras), RMS amplitudes and diffusion. The key insight: **a root is just a power with a fractional exponent**, so every root rule follows from [[A1 Exponent Rules]].

## Definition
For $a \ge 0$: $\sqrt[n]{a}$ is the non-negative number $b$ with $b^n = a$.
$$\sqrt[n]{a} = a^{1/n}, \qquad \sqrt[n]{a^m} = a^{m/n}$$

## The rules (for $a, b \ge 0$)
| Rule | Example |
|---|---|
| $\sqrt{a \cdot b} = \sqrt{a}\cdot\sqrt{b}$ | $\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt2$ |
| $\sqrt{\dfrac{a}{b}} = \dfrac{\sqrt a}{\sqrt b}$ ($b>0$) | $\sqrt{\tfrac{9}{16}} = \tfrac34$ |
| $\left(\sqrt[n]{a}\right)^m = \sqrt[n]{a^m}$ | $(\sqrt[3]{8})^2 = 4$ |
| $\sqrt[m]{\sqrt[n]{a}} = \sqrt[mn]{a}$ | $\sqrt{\sqrt{16}} = \sqrt[4]{16} = 2$ |
| $\sqrt{a^2} = \lvert a \rvert$ (for any real $a$) | $\sqrt{(-3)^2} = 3$ |

> [!warning] No rule for sums
> $\sqrt{a + b} \neq \sqrt a + \sqrt b$. Check: $\sqrt{9+16} = 5$, but $3 + 4 = 7$.

## Techniques
**Partial root extraction:** pull out perfect squares: $\sqrt{72} = \sqrt{36 \cdot 2} = 6\sqrt2$.

**Combining like roots:** like terms: $2\sqrt3 + 5\sqrt3 = 7\sqrt3$ – but $\sqrt2 + \sqrt3$ cannot be simplified.

**Rationalising the denominator:**
- Single root: $\dfrac{6}{\sqrt3} = \dfrac{6\sqrt3}{3} = 2\sqrt3$
- Sum/difference: use the third binomial formula $(a-b)(a+b) = a^2 - b^2$ ([[A6 Binomial Formulas and Theorem]]):
  $$\frac{1}{\sqrt5 - 2} = \frac{\sqrt5 + 2}{(\sqrt5-2)(\sqrt5+2)} = \frac{\sqrt5+2}{5-4} = \sqrt5 + 2$$

**Root equations:** square both sides – but squaring can create *false* solutions, so **always check** ([[A8 Solving Equations]]).

## In neuroscience #neuro
- **Standard error of the mean:** $\text{SEM} = \dfrac{\sigma}{\sqrt n}$. To halve the SEM you need **four times** as many trials ($\sqrt{4} = 2$). That's why "just a few more trials" rarely helps much.
- **Diffusion:** the root-mean-square distance a molecule diffuses in time $t$ is $x_\text{rms} = \sqrt{2Dt}$ (1D). Doubling the distance takes **four times** as long – this is why neurotransmitter diffusion across a ~20 nm cleft is fast, but diffusion along an axon is hopelessly slow (→ axonal transport is needed).
- **RMS amplitude** of an EEG/LFP signal: $\text{RMS} = \sqrt{\tfrac1n \sum x_i^2}$ (see [[A7 Sums Products and Factorials]]).
- **Euclidean distance** between electrodes in MNI space: $d = \sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2}$ ([[D1 Vectors in 2D and 3D]]).

## Typical pitfalls
- $\sqrt{a+b} = \sqrt a + \sqrt b$ ❌
- $\sqrt{x^2} = x$ ❌ (only for $x \ge 0$; in general $\lvert x\rvert$)
- Forgetting to check solutions after squaring an equation.

## Connections
- Roots are fractional powers → [[A1 Exponent Rules]]
- Rationalising uses $(a-b)(a+b)$ → [[A6 Binomial Formulas and Theorem]]
- Vector length → [[D1 Vectors in 2D and 3D]]
- Derivative of $\sqrt x = x^{1/2}$ → [[B6 Differentiation Rules]]

## Where this is used in the vault
**Most important applications:** Diffusion distance $\sqrt{2Dt}$ ([[Ph07 Diffusion and Transport]]), length constant $\lambda=\sqrt{r_m/r_i}$ ([[Ph10 Signal Propagation and Cable Theory]]), SEM and shot noise $\propto\sqrt N$ ([[CS02 Probability and Statistics]], [[Ph12 Quantum Basics for Biophysics]]).

**All notes that build on this topic:**
- *Physics:* [[Ph07 Diffusion and Transport]] · [[Ph10 Signal Propagation and Cable Theory]] · [[Ph12 Quantum Basics for Biophysics]]
- *Biology:* [[Bio01 Cell Biology]] · [[Bio05 Neurons and Action Potentials]]
- *Methods:* [[Meth01 Microscopy]] · [[Meth02 Structural Biology]] · [[Meth03 Electrophysiology]]
- *Computer Science:* [[CS02 Probability and Statistics]] · [[CS06 Data Science Workflow]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Convert roots to powers when in doubt: $\sqrt[n]{a^m} = a^{m/n}$.
- Roots distribute over products and quotients, **never** over sums.
- Square-root scaling ($\sqrt n$, $\sqrt t$) explains why precision and diffusion improve so slowly.
