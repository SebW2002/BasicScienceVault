---
aliases: [Logarithms, Log Rules, Logarithmen]
tags: [basics, logarithm, type/overview, neuro]
---
# A3 Logarithms

> [[A0 Basics MOC|↑ Basics MOC]] · [[A3 Logarithms - Worksheet|✏️ Worksheet]] · [[A3 Logarithms - Solutions|✅ Solutions]] · [[Mistakes - Basics|⚠️ Mistake log]]

## Why this matters
The logarithm answers: **"To which power must I raise $b$ to get $x$?"** It turns multiplication into addition, which is why it appears in the Nernst equation, decibels, information theory and psychophysics. It is the inverse of exponentiation ([[B2 Exponential Functions]] ↔ [[B3 Logarithmic Functions]]).

## Definition
$$\log_b(x) = y \iff b^y = x \qquad (b > 0,\ b \neq 1,\ x > 0)$$

Important bases:
| Notation | Base | Typical use |
|---|---|---|
| $\ln x$ | $e \approx 2.718$ | calculus, physics, Nernst equation |
| $\log_{10} x$ (often $\lg x$) | 10 | decibels, pH, orders of magnitude |
| $\log_2 x$ | 2 | information in **bits** |

Special values: $\log_b 1 = 0$, $\log_b b = 1$, $\log_b(b^y) = y$, $b^{\log_b x} = x$.

## The rules (for $x, y > 0$)
| # | Rule | Comes from |
|---|---|---|
| 1 | $\log_b(x \cdot y) = \log_b x + \log_b y$ | $b^m b^n = b^{m+n}$ |
| 2 | $\log_b\!\left(\dfrac{x}{y}\right) = \log_b x - \log_b y$ | $b^m / b^n = b^{m-n}$ |
| 3 | $\log_b(x^r) = r \cdot \log_b x$ | $(b^m)^r = b^{mr}$ |
| 4 | $\log_b x = \dfrac{\ln x}{\ln b} = \dfrac{\log_{10} x}{\log_{10} b}$ | change of base |

> [!warning] What does **not** work
> $\log(x + y) \neq \log x + \log y$ · $\;\log x \cdot \log y \neq \log(xy)$ · $\;\dfrac{\log x}{\log y} \neq \log\dfrac{x}{y}$ · $\;(\log x)^2 \neq 2\log x$

## Worked examples
1. $\log_2 8 = 3$ since $2^3 = 8$; $\;\log_{10} 0.01 = -2$ since $10^{-2} = 0.01$.
2. $\log_9 27 = \dfrac{3}{2}$ since $9^{3/2} = (\sqrt9)^3 = 27$.
3. Expand: $\ln\dfrac{x^3\sqrt y}{z} = 3\ln x + \tfrac12 \ln y - \ln z$.
4. Combine: $\log_3 18 - \log_3 2 = \log_3 9 = 2$.
5. Solve $3^x = 20$: take $\ln$ of both sides: $x \ln 3 = \ln 20 \Rightarrow x = \dfrac{\ln 20}{\ln 3}$.

## In neuroscience #neuro
- **Nernst equation** – equilibrium potential of an ion:
  $$E_\text{ion} = \frac{RT}{zF}\ln\frac{[\text{ion}]_\text{out}}{[\text{ion}]_\text{in}} \;\approx\; \frac{61.5\,\text{mV}}{z}\,\log_{10}\frac{[\text{ion}]_\text{out}}{[\text{ion}]_\text{in}} \quad (37\,°\text{C})$$
  Example K⁺: out 5 mM, in 140 mM → $61.5 \cdot \log_{10}(5/140) \approx 61.5 \cdot (-1.45) \approx -89\,\text{mV}$. A **tenfold** concentration ratio always gives $\pm 61.5\,\text{mV}$ (for $z = 1$) – that's rule 3 at work.
- **Decibels:** power ratio $\text{dB} = 10\log_{10}(P/P_0)$, amplitude ratio $\text{dB} = 20\log_{10}(A/A_0)$ (because $P \propto A^2$ → rule 3). Used for EEG power, filter attenuation, hearing.
- **Information theory:** distinguishing $N$ equally likely stimuli needs $\log_2 N$ bits. Entropy $H = -\sum p_i \log_2 p_i$.
- **Weber–Fechner law:** perceived intensity $S = k\ln(I/I_0)$ – every *doubling* of intensity adds the same amount of sensation.
- **Log-scaled axes:** frequency axes in spectra, log-normally distributed firing rates and synaptic weights.

## Connections
- Inverse of exponentiation → [[A1 Exponent Rules]], [[B2 Exponential Functions]]
- As a function (graph, domain, derivative) → [[B3 Logarithmic Functions]]
- Solving exponential equations → [[A8 Solving Equations]]
- Products of likelihoods become sums of log-likelihoods → [[A7 Sums Products and Factorials]]

## Where this is used in the vault
**Most important applications:** **The** most-used math tool: pH and Henderson–Hasselbalch ([[Ch04 Acids Bases and pH]]), Nernst/GHK ([[Ch05 Redox and Electrochemistry]]), $\Delta G^\circ=-RT\ln K$ ([[Ph08 Thermodynamics and Statistics]]), entropy in bits ([[CS03 Information Theory]]), qPCR Ct and log fold changes ([[Meth05 Molecular Biology Tools]]).

**All notes that build on this topic:**
- *Physics:* [[Ph03 Electric Fields and Potential]] · [[Ph05 Capacitance and RC Circuits]] · [[Ph07 Diffusion and Transport]] · [[Ph08 Thermodynamics and Statistics]] · [[Ph09 Waves and Oscillations]] · [[Ph12 Quantum Basics for Biophysics]]
- *Chemistry:* [[Ch01 Atomic Structure]] · [[Ch03 Intermolecular Forces and Solubility]] · [[Ch04 Acids Bases and pH]] · [[Ch05 Redox and Electrochemistry]] · [[Ch07 Organic Chemistry Essentials]] · [[Ch08 Biomolecules]]
- *Biology:* [[Bio03 Proteins and Enzymes]] · [[Bio04 Nucleic Acids and Gene Expression]] · [[Bio05 Neurons and Action Potentials]]
- *Methods:* [[Meth04 In Vivo Imaging]] · [[Meth05 Molecular Biology Tools]] · [[Meth06 Omics and Sequencing]]
- *Computer Science:* [[CS02 Probability and Statistics]] · [[CS03 Information Theory]] · [[CS05 Data Formats and Representation]] · [[CS07 Machine Learning Fundamentals]] · [[CS09 Probabilistic and Bayesian Models]] · [[CS10 Dynamical and Computational Neuro Models]] · [[CS11 Time Series and Signal Processing]]
- *Programming:* [[Py07 Python Plotting and Visualization]] · [[R07 R Statistical Modelling]] · [[R08 R Mixed-Effects Models]] · [[MAT05 MATLAB Plotting]] · [[MAT06 MATLAB Signal Processing Toolbox]] · [[MAT07 MATLAB Statistics Toolbox]] · [[MAT09 EEGLAB]] · [[Doc02 Math in Markdown]] · [[Doc06 LaTeX Math]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- $\log$ converts: product → sum, quotient → difference, power → factor.
- Only defined for positive arguments.
- Factor 10 in concentration = constant step in potential; factor 10 in power = 10 dB.
