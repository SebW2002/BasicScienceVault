---
aliases: [Complex Numbers, Komplexe Zahlen, Euler's Formula]
tags: [foundations, complex, type/overview, neuro]
---
# E2 Complex Numbers

> [[E0 Foundations MOC|↑ Foundations MOC]] · [[E2 Complex Numbers - Worksheet|✏️ Worksheet]] · [[E2 Complex Numbers - Solutions|✅ Solutions]] · [[Mistakes - Foundations|⚠️ Mistake log]]

## Why this matters
Complex numbers look abstract but are the most practical way to handle **oscillations**: one complex number stores both the **amplitude** and the **phase** of a rhythm. Every Fourier transform, time–frequency analysis, coherence or phase-locking measure in EEG/MEG/LFP analysis uses them. They also appear as eigenvalues of oscillating systems.

## Definition and arithmetic
$$i^2 = -1, \qquad z = a + bi\quad(a = \operatorname{Re}z,\ b = \operatorname{Im}z)$$
Powers of $i$ cycle: $i^1 = i$, $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, …

| Operation | Rule |
|---|---|
| Add | $(a + bi) + (c + di) = (a + c) + (b + d)i$ |
| Multiply | $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$ (expand, use $i^2 = -1$) |
| Conjugate | $\bar z = a - bi$ |
| Modulus | $\lvert z\rvert = \sqrt{a^2 + b^2}$, and $z\bar z = \lvert z\rvert^2$ |
| Divide | expand with the conjugate of the denominator: $\dfrac{z}{w} = \dfrac{z\bar w}{\lvert w\rvert^2}$ |

**Quadratic equations** with negative discriminant now have solutions: $x^2 + 2x + 5 = 0\Rightarrow x = -1\pm2i$ ([[A8 Solving Equations]]). Solutions of real equations come in conjugate pairs.

## The complex plane & polar form
Draw $z = a + bi$ as the point $(a, b)$. In polar coordinates ([[D4 Unit Circle Trigonometry]]):
$$z = r(\cos\varphi + i\sin\varphi) = r\,e^{i\varphi}, \qquad r = \lvert z\rvert,\ \varphi = \arg z$$
**Euler's formula:** $e^{i\varphi} = \cos\varphi + i\sin\varphi$ (follows from the Taylor series, [[B9 Taylor Series]]). Special case: $e^{i\pi} + 1 = 0$.

**Multiplication in polar form:** multiply moduli, **add** angles:
$$r_1e^{i\varphi_1}\cdot r_2e^{i\varphi_2} = r_1r_2\,e^{i(\varphi_1 + \varphi_2)}, \qquad (re^{i\varphi})^n = r^ne^{in\varphi}\ \text{(De Moivre)}$$
So multiplying by $e^{i\varphi}$ is a **rotation** by $\varphi$; $e^{i\omega t}$ is a point running around the unit circle – an oscillation.

## In neuroscience #neuro
- **Fourier transform:** for each frequency $f$, the Fourier coefficient is a complex number $X(f) = \lvert X\rvert e^{i\varphi}$: $\lvert X(f)\rvert$ = amplitude, $\lvert X(f)\rvert^2$ = power, $\arg X(f)$ = phase. Power spectra throw away the phase; phase-based measures use it.
- **Analytic signal / Hilbert transform & wavelets:** give a complex signal $z(t) = A(t)e^{i\varphi(t)}$ with instantaneous **amplitude envelope** $A(t)$ and **phase** $\varphi(t)$ – used for phase–amplitude coupling (e.g. theta phase modulating gamma amplitude).
- **Phase-locking value / inter-trial coherence:**
  $$\text{PLV} = \left\lvert\frac1N\sum_{k=1}^Ne^{i\varphi_k}\right\rvert$$
  – exactly the mean resultant length from [[D4 Unit Circle Trigonometry]], written compactly.
- **Coherence** between two signals uses the cross-spectrum $X(f)\overline{Y(f)}$.
- **Complex eigenvalues** $\lambda = a\pm bi$ of a dynamical system: $a$ = growth/decay rate, $b$ = angular frequency of oscillation ([[C4 Eigenvalues and Eigenvectors]]).

## Connections
- Fourier series and transforms in complex form → [[B12 Fourier Analysis]]
- Negative discriminants → [[A8 Solving Equations]]
- Polar form ↔ unit circle → [[D4 Unit Circle Trigonometry]]
- Euler's formula from series → [[B9 Taylor Series]], [[B2 Exponential Functions]], [[B4 Trigonometric Functions]]
- Oscillating linear systems → [[C4 Eigenvalues and Eigenvectors]]

## Where this is used in the vault
**Most important applications:** Fourier coefficients (amplitude + phase) for EEG and signals ([[CS11 Time Series and Signal Processing]], [[Meth03 Electrophysiology]]), complex eigenvalues = oscillations ([[CS10 Dynamical and Computational Neuro Models]]), diffraction phases ([[Meth02 Structural Biology]]).

**All notes that build on this topic:**
- *Physics:* [[Ph09 Waves and Oscillations]] · [[Ph11 Optics and Fluorescence]]
- *Methods:* [[Meth01 Microscopy]] · [[Meth02 Structural Biology]] · [[Meth03 Electrophysiology]]
- *Computer Science:* [[CS11 Time Series and Signal Processing]]
- *Programming:* [[Py01 Python Basics and Syntax]] · [[Py08 SciPy Scientific Computing]] · [[R01 R Basics and Syntax]] · [[MAT01 MATLAB Basics and Syntax]] · [[MAT06 MATLAB Signal Processing Toolbox]] · [[MAT09 EEGLAB]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- $i^2 = -1$; compute like with variables, then replace $i^2$.
- $z = re^{i\varphi}$: modulus = amplitude, argument = phase.
- Multiplying complex numbers multiplies amplitudes and adds phases.
