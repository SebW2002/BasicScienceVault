---
aliases: [Logarithmic Functions, Logarithmusfunktion, ln function]
tags: [analysis, logarithm, function, type/overview, neuro]
---
# B3 Logarithmic Functions

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B3 Logarithmic Functions - Worksheet|✏️ Worksheet]] · [[B3 Logarithmic Functions - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
The logarithm as a *function* compresses huge ranges (sound pressure, light intensity, frequencies) into manageable scales – just like our senses do. It also turns exponential and power-law data into straight lines, which is how time constants and exponents are estimated from data.

## Definition
$\ln x$ is the **inverse function** of $e^x$:
$$y = \ln x \iff e^y = x, \qquad \ln(e^x) = x,\quad e^{\ln x} = x \;(x>0)$$
The graph of $\ln$ is the mirror image of $e^x$ at the line $y = x$ ([[B1 Properties of Functions]]).

| Property | $\ln x$ |
|---|---|
| Domain / range | $(0, \infty)$ / $\mathbb R$ |
| Zero | $x = 1$ ($\ln 1 = 0$) |
| Sign | $\ln x < 0$ for $0 < x < 1$, $\ln x > 0$ for $x > 1$ |
| Monotonic | strictly increasing (but ever more slowly) |
| Limits | $\ln x \to -\infty$ as $x \to 0^+$ (vertical asymptote $x=0$); $\ln x \to \infty$ as $x\to\infty$ |
| Growth | slower than any power: $\frac{\ln x}{x^a} \to 0$ for every $a > 0$ |
| Derivative | $(\ln x)' = \frac1x$ → [[B6 Differentiation Rules]] |

Other bases: $\log_b x = \frac{\ln x}{\ln b}$ – same shape, just scaled. All rules from [[A3 Logarithms]] apply.

## Linearising data
**Exponential data:** $y = A e^{-t/\tau}$ → take $\ln$:
$$\ln y = \ln A - \frac{1}{\tau}\, t$$
A plot of $\ln y$ vs. $t$ ("semi-log plot") is a **straight line** with slope $-1/\tau$.

**Power-law data:** $y = c\, x^a$ → $\log y = \log c + a\log x$. A **log–log plot** is a straight line with slope $a$.

## In neuroscience #neuro
- **Weber–Fechner law:** perceived magnitude $S = k\ln(I/I_0)$. Equal *ratios* of intensity feel like equal *steps*. Doubling a light from 10 to 20 lux feels like doubling from 100 to 200 lux.
- **Fitting time constants:** semi-log plot of a decaying PSP or current → slope gives $-1/\tau$. Two different slopes = two processes (e.g. fast and slow components).
- **Spectra:** EEG power spectra are shown on log–log axes; the "1/f" background then appears as a line whose slope (aperiodic exponent) is a biomarker.
- **Log-normal distributions:** firing rates and synaptic weights are roughly normally distributed **on a log axis** – most neurons fire slowly, a few fire very fast.
- **Information/entropy:** $H = -\sum p_i\log_2 p_i$ bits.
- **Frequency perception:** pitch is perceived logarithmically (octaves = doubling).

## Connections
- Inverse of → [[B2 Exponential Functions]]
- Rules → [[A3 Logarithms]]
- Derivative $1/x$, integral $\int \frac1x dx = \ln\lvert x\rvert$ → [[B6 Differentiation Rules]], [[B7 Antiderivatives and Integration]]
- Series $\ln(1+x)$ → [[B9 Taylor Series]]

## Where this is used in the vault
**Most important applications:** Log scales: pH, decibels, log–log EEG spectra ([[Ph09 Waves and Oscillations]]), dose–response on log concentration ([[Bio03 Proteins and Enzymes]]), log fold changes ([[Meth06 Omics and Sequencing]]).

**All notes that build on this topic:**
- *Physics:* [[Ph09 Waves and Oscillations]]
- *Chemistry:* [[Ch04 Acids Bases and pH]]
- *Biology:* [[Bio03 Proteins and Enzymes]] · [[Bio04 Nucleic Acids and Gene Expression]] · [[Bio06 Synapses and Neurotransmitters]]
- *Methods:* [[Meth03 Electrophysiology]] · [[Meth05 Molecular Biology Tools]] · [[Meth06 Omics and Sequencing]]
- *Computer Science:* [[CS03 Information Theory]] · [[CS06 Data Science Workflow]]
- *Programming:* [[Py06 pandas and Tabular Data]] · [[Py07 Python Plotting and Visualization]] · [[R05 dplyr and tidyr]] · [[R06 ggplot2 Visualization]] · [[MAT05 MATLAB Plotting]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Only defined for $x > 0$; zero at $x = 1$; negative below 1.
- Semi-log → exponentials become lines; log–log → power laws become lines.
- Logs compress: equal ratios become equal distances.
