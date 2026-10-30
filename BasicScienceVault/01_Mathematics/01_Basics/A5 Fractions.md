---
aliases: [Fractions, Rational Expressions, Brüche]
tags: [basics, fraction, algebra, type/overview, neuro]
---
# A5 Fractions

> [[A0 Basics MOC|↑ Basics MOC]] · [[A5 Fractions - Worksheet|✏️ Worksheet]] · [[A5 Fractions - Solutions|✅ Solutions]] · [[Mistakes - Basics|⚠️ Mistake log]]

## Why this matters
Rates, ratios, normalisations, conductances in parallel, saturation curves – neuroscience formulas are full of fractions. Fluent fraction handling is the most common hidden bottleneck when rearranging formulas.

## Rules
| Operation | Rule | Example |
|---|---|---|
| Expand / reduce | $\dfrac ab = \dfrac{ac}{bc}$ ($c \neq 0$) | $\dfrac{6}{8} = \dfrac34$ |
| Add / subtract | common denominator: $\dfrac ab + \dfrac cd = \dfrac{ad + bc}{bd}$ | $\dfrac23 + \dfrac34 = \dfrac{8+9}{12} = \dfrac{17}{12}$ |
| Multiply | $\dfrac ab \cdot \dfrac cd = \dfrac{ac}{bd}$ | $\dfrac35 \cdot \dfrac{10}{9} = \dfrac23$ |
| Divide | multiply by the reciprocal: $\dfrac ab : \dfrac cd = \dfrac ab \cdot \dfrac dc$ | $\dfrac47 : \dfrac{2}{21} = 6$ |
| Double fraction | multiply numerator & denominator by the common denominator | see below |

**Least common denominator (LCD):** factor the denominators first ([[A4 Factoring and Simplifying]]), e.g.
$$\frac{1}{x-1} - \frac{1}{x+1} = \frac{(x+1) - (x-1)}{(x-1)(x+1)} = \frac{2}{x^2 - 1}$$

**Double fractions:** multiply by the LCD of all inner fractions:
$$\frac{1 + \frac1x}{1 - \frac1x} = \frac{x + 1}{x - 1} \quad (\text{multiplied top and bottom by } x)$$

> [!warning] Classic mistakes
> $\dfrac{1}{a+b} \neq \dfrac1a + \dfrac1b$ · $\;\dfrac{a+b}{a} \neq b$ · $\;\dfrac ab + \dfrac cd \neq \dfrac{a+c}{b+d}$

## In neuroscience #neuro
- **Parallel conductances / resistances:** conductances in parallel add ($g = g_1 + g_2$); resistances combine as
  $$\frac1R = \frac1{R_1} + \frac1{R_2} \;\Rightarrow\; R = \frac{R_1 R_2}{R_1 + R_2}$$
  Opening more channels (adding parallel paths) lowers the input resistance.
- **Saturation curves (Michaelis–Menten, Hill / Naka–Rushton):**
  $$f(c) = \frac{c^n}{c^n + K^n}$$
  At $c = K$ the response is exactly half-maximal. Used for receptor binding, dose–response curves and contrast response functions in visual cortex.
- **Divisive normalisation:** a neuron's response divided by the pooled activity of its neighbours, $R_i = \dfrac{r_i}{\sigma + \sum_j r_j}$ – a "canonical computation" of cortex.
- **Ratios:** signal-to-noise ratio, paired-pulse ratio, $\Delta F/F$ in calcium imaging: $\dfrac{F - F_0}{F_0} = \dfrac{F}{F_0} - 1$.

## Connections
- Factor before finding the LCD or cancelling → [[A4 Factoring and Simplifying]]
- Equations with fractions → [[A8 Solving Equations]]
- Rational functions, poles, asymptotes → [[B1 Properties of Functions]]
- Quotient rule → [[B6 Differentiation Rules]]

## Where this is used in the vault
**Most important applications:** Saturation curves — Michaelis–Menten, receptor occupancy, Hill ([[Bio03 Proteins and Enzymes]]); parallel resistances ([[Ph04 Circuits and Resistance]]); lens equation ([[Ph11 Optics and Fluorescence]]); precision-weighted averages ([[CS09 Probabilistic and Bayesian Models]]).

**All notes that build on this topic:**
- *Physics:* [[Ph04 Circuits and Resistance]] · [[Ph05 Capacitance and RC Circuits]] · [[Ph11 Optics and Fluorescence]] · [[Ph12 Quantum Basics for Biophysics]]
- *Chemistry:* [[Ch05 Redox and Electrochemistry]]
- *Biology:* [[Bio01 Cell Biology]] · [[Bio02 Membranes and Transport]] · [[Bio03 Proteins and Enzymes]]
- *Methods:* [[Meth01 Microscopy]] · [[Meth02 Structural Biology]] · [[Meth04 In Vivo Imaging]]
- *Computer Science:* [[CS09 Probabilistic and Bayesian Models]] · [[CS14 Hardware Essentials]]
- *Programming:* [[Py01 Python Basics and Syntax]] · [[Py11 PsychoPy Experiment Control]] · [[R01 R Basics and Syntax]] · [[MAT08 Psychtoolbox]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Add only with a common denominator; multiply straight across; divide = multiply by reciprocal.
- Factor denominators first, then find the LCD.
- Remember excluded values (denominator ≠ 0).
