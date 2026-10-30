---
aliases: [Exponent Rules, Power Laws, Potenzgesetze]
tags: [basics, exponent, type/overview, neuro]
---
# A1 Exponent Rules

> [[A0 Basics MOC|↑ Basics MOC]] · [[A1 Exponent Rules - Worksheet|✏️ Worksheet]] · [[A1 Exponent Rules - Solutions|✅ Solutions]] · [[Mistakes - Basics|⚠️ Mistake log]]

## Why this matters
Neuroscience constantly mixes scales: picoamperes and gigaohms, milliseconds and hours, single synapses and $10^{14}$ of them. Exponent rules let you convert units, estimate orders of magnitude in your head and understand power laws. They are also the basis for [[A2 Root Rules|roots]] (fractional exponents) and [[A3 Logarithms|logarithms]] (the inverse question: *which* exponent?).

## Definitions
For a base $a$ and natural number $n$: $a^n = \underbrace{a \cdot a \cdots a}_{n \text{ times}}$.

| Definition | Meaning | Example |
|---|---|---|
| $a^0 = 1$ (for $a \neq 0$) | empty product | $7^0 = 1$ |
| $a^{-n} = \dfrac{1}{a^n}$ | negative exponent = reciprocal | $2^{-3} = \tfrac18$ |
| $a^{1/n} = \sqrt[n]{a}$ | fractional exponent = root | $27^{1/3} = 3$ |
| $a^{m/n} = \left(\sqrt[n]{a}\right)^m = \sqrt[n]{a^m}$ | combine both | $8^{2/3} = 2^2 = 4$ |

## The rules
| # | Rule | In words |
|---|---|---|
| 1 | $a^m \cdot a^n = a^{m+n}$ | same base, multiply → **add** exponents |
| 2 | $\dfrac{a^m}{a^n} = a^{m-n}$ | same base, divide → **subtract** exponents |
| 3 | $(a^m)^n = a^{m \cdot n}$ | power of a power → **multiply** exponents |
| 4 | $(a \cdot b)^n = a^n \cdot b^n$ | same exponent, multiply bases |
| 5 | $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ | same exponent, divide bases |

> [!warning] There is **no** rule for sums
> $(a+b)^n \neq a^n + b^n$ and $a^m + a^n \neq a^{m+n}$. For $(a+b)^n$ see [[A6 Binomial Formulas and Theorem]].

## Worked examples
1. $x^3 \cdot x^4 = x^{7}$ (rule 1)
2. $\dfrac{y^{10}}{y^{4}} = y^{6}$ (rule 2)
3. $(2x^3)^2 = 2^2 \cdot (x^3)^2 = 4x^6$ (rules 4 + 3)
4. $\dfrac{a^{-2} b^{3}}{a^{4} b^{-1}} = a^{-2-4} b^{3-(-1)} = a^{-6}b^{4} = \dfrac{b^4}{a^6}$
5. $16^{3/4} = \left(\sqrt[4]{16}\right)^3 = 2^3 = 8$ — take the root first, the numbers stay small.

### Scientific notation
Write numbers as $m \times 10^k$ with $1 \le m < 10$. Then multiply mantissas and **add** exponents:
$$(3 \times 10^{4}) \cdot (2 \times 10^{-7}) = 6 \times 10^{-3}$$

| Prefix | Factor | Prefix | Factor |
|---|---|---|---|
| k (kilo) | $10^{3}$ | m (milli) | $10^{-3}$ |
| M (mega) | $10^{6}$ | µ (micro) | $10^{-6}$ |
| G (giga) | $10^{9}$ | n (nano) | $10^{-9}$ |
| | | p (pico) | $10^{-12}$ |

## In neuroscience #neuro
- **Ohm's law at the membrane:** $V = I \cdot R$. A current of $0.5\,\text{nA}$ into a cell with input resistance $100\,\text{M}\Omega$:
  $V = 0.5 \times 10^{-9}\,\text{A} \cdot 10^{8}\,\Omega = 0.5 \times 10^{-1}\,\text{V} = 50\,\text{mV}$.
- **Orders of magnitude:** ~$8.6 \times 10^{10}$ neurons and ~$10^{14}$ synapses in the human brain → roughly $10^{14}/10^{11} = 10^3$ synapses per neuron (order of magnitude).
- **Power laws:** many neural quantities follow $y = c\,x^{a}$. The EEG power spectrum falls roughly like $P(f) \propto f^{-\beta}$ ("1/f noise"); Stevens' psychophysical law $\psi = k\,\phi^{a}$ links stimulus intensity $\phi$ to perceived magnitude $\psi$. Doubling $f$ multiplies $P$ by $2^{-\beta}$ — a pure exponent rule.
- **Ion concentrations:** e.g. intracellular Ca²⁺ ≈ $10^{-7}\,\text{M}$ vs. extracellular ≈ $10^{-3}\,\text{M}$ → ratio $10^{4}$.

## Typical pitfalls
- $a^m \cdot a^n = a^{m \cdot n}$ ❌ → exponents are **added**.
- $-2^2 = -4$, but $(-2)^2 = 4$. The minus sign is not part of the base unless in brackets.
- $(2x)^3 = 2x^3$ ❌ → $8x^3$.
- Collect your own in [[Mistakes - Basics]].

## Connections
- Fractional exponents → [[A2 Root Rules]]
- Inverse question "which exponent?" → [[A3 Logarithms]]
- Variable in the exponent → [[B2 Exponential Functions]]
- Derivative of $x^n$ (power rule) → [[B6 Differentiation Rules]]

## Where this is used in the vault
**Most important applications:** Units and orders of magnitude everywhere (pA, mV, nS, GB/h); power laws such as Coulomb $1/r^2$, scattering $\lambda^{-4}$, FRET $r^{-6}$; PCR doubling $2^n$.

**All notes that build on this topic:**
- *Physics:* [[Ph01 Mechanics and Energy]] · [[Ph02 Electricity and Charge]] · [[Ph03 Electric Fields and Potential]] · [[Ph06 Magnetism and Induction]] · [[Ph09 Waves and Oscillations]] · [[Ph10 Signal Propagation and Cable Theory]] · [[Ph11 Optics and Fluorescence]] · [[Ph12 Quantum Basics for Biophysics]]
- *Chemistry:* [[Ch01 Atomic Structure]] · [[Ch02 Chemical Bonds]] · [[Ch04 Acids Bases and pH]] · [[Ch05 Redox and Electrochemistry]] · [[Ch08 Biomolecules]]
- *Biology:* [[Bio01 Cell Biology]] · [[Bio04 Nucleic Acids and Gene Expression]] · [[Bio05 Neurons and Action Potentials]] · [[Bio06 Synapses and Neurotransmitters]]
- *Methods:* [[Meth01 Microscopy]] · [[Meth02 Structural Biology]] · [[Meth03 Electrophysiology]] · [[Meth05 Molecular Biology Tools]] · [[Meth06 Omics and Sequencing]]
- *Computer Science:* [[CS05 Data Formats and Representation]] · [[CS08 Deep Neural Networks]] · [[CS13 Reproducibility and Research Software]] · [[CS14 Hardware Essentials]]
- *Programming:* [[Py01 Python Basics and Syntax]] · [[Py04 Python Files and Data Formats]] · [[R01 R Basics and Syntax]] · [[MAT01 MATLAB Basics and Syntax]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Same base: multiply ↔ add exponents, divide ↔ subtract.
- Negative exponent = reciprocal, fractional exponent = root.
- Always convert to powers of ten before calculating with units.
