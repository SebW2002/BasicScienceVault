---
aliases: [Antiderivatives and Integration, Integration, Integrals, Stammfunktionen]
tags: [analysis, integral, type/overview, neuro]
---
# B7 Antiderivatives and Integration

> [[B0 Analysis MOC|↑ Analysis MOC]] · [[B7 Antiderivatives and Integration - Worksheet|✏️ Worksheet]] · [[B7 Antiderivatives and Integration - Solutions|✅ Solutions]] · [[Mistakes - Analysis|⚠️ Mistake log]]

## Why this matters
Integration **accumulates**: current over time gives charge, a rate over time gives a count, a probability density over an interval gives a probability. It is also the inverse of differentiation, which is how differential equations are solved.

## Antiderivative (indefinite integral)
$F$ is an antiderivative of $f$ if $F' = f$. All antiderivatives differ by a constant:
$$\int f(x)\,dx = F(x) + C$$

| $f(x)$ | $\int f(x)\,dx$ |
|---|---|
| $x^n$ ($n \neq -1$) | $\frac{x^{n+1}}{n+1} + C$ |
| $\frac1x$ | $\ln\lvert x\rvert + C$ |
| $e^x$ | $e^x + C$ |
| $e^{kx}$ | $\frac1k e^{kx} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\ln x$ | $x\ln x - x + C$ |

**Linearity:** $\int (a f + b g)\,dx = a\int f\,dx + b\int g\,dx$.
**Always check** by differentiating your answer!

## Definite integral
$$\int_a^b f(x)\,dx = \lim_{n\to\infty}\sum_{i=1}^{n} f(x_i)\,\Delta x$$
= signed area between graph and x-axis (areas below the axis count negative). It's the limit of a sum ([[A7 Sums Products and Factorials]], [[B5 Limits and Continuity]]).

## Fundamental theorem of calculus
$$\int_a^b f(x)\,dx = F(b) - F(a) = \Big[F(x)\Big]_a^b, \qquad \frac{d}{dx}\int_a^x f(t)\,dt = f(x)$$
Differentiation and integration are **inverse operations** ([[B6 Differentiation Rules]]).

## Techniques
**Substitution** (reverse chain rule): if the integrand contains $g(x)$ and its derivative $g'(x)$:
$$\int f(g(x))\,g'(x)\,dx = \int f(u)\,du, \quad u = g(x)$$
Example: $\int 2x\,e^{x^2}dx$, $u = x^2$, $du = 2x\,dx$ → $\int e^u du = e^{x^2} + C$. For definite integrals, transform the bounds too.

**Integration by parts** (reverse product rule):
$$\int u\,v'\,dx = u\,v - \int u'\,v\,dx$$
Choose $u$ = the factor that gets simpler when differentiated (polynomials, $\ln$). Example: $\int xe^x dx = xe^x - \int e^xdx = (x - 1)e^x + C$.

**Mean value of a function:** $\bar f = \frac{1}{b-a}\int_a^b f(x)\,dx$.
**Area between curves:** $\int_a^b \big(f(x) - g(x)\big)dx$ for $f \ge g$.

## In neuroscience #neuro
- **Charge from current:** $Q = \int I(t)\,dt$. For an exponentially decaying synaptic current $I(t) = I_0e^{-t/\tau}$:
  $$Q = \int_0^\infty I_0e^{-t/\tau}dt = I_0\tau$$
  This is why slow NMDA currents carry much more charge than fast AMPA currents of the same peak.
- **Spike counts from rates:** expected spikes $N = \int_{t_1}^{t_2} r(t)\,dt$.
- **Probability densities:** $P(a \le X \le b) = \int_a^b p(x)\,dx$, and $\int p = 1$. Exponential ISI density $\lambda e^{-\lambda t}$ has mean $\int_0^\infty t\lambda e^{-\lambda t}dt = \frac1\lambda$.
- **Solving the membrane equation:** $\tau\frac{dV}{dt} = -V$ → separate and integrate → $V(t) = V_0e^{-t/\tau}$.
- **Convolution / filtering:** the membrane potential is the input current convolved with a kernel, $V(t) = \int_0^\infty K(s)\,I(t - s)\,ds$ – the basis of linear–nonlinear (LN) models and receptive-field estimation.
- **Area under the curve** of an ERP/PSP or a ROC curve.

## Connections
- Solving ODEs by integration → [[B10 Differential Equations]]; double integrals → [[B11 Multivariable Calculus]]; Fourier coefficients as integrals → [[B12 Fourier Analysis]]
- Inverse of → [[B6 Differentiation Rules]] (fundamental theorem)
- Riemann sum → [[A7 Sums Products and Factorials]], limit → [[B5 Limits and Continuity]]
- Exponential integrals → [[B2 Exponential Functions]]; $\int\frac1x = \ln\lvert x\rvert$ → [[B3 Logarithmic Functions]]

## Where this is used in the vault
**Most important applications:** Charge = ∫ current ([[Ph02 Electricity and Charge]]), convolution with HRF/PSF ([[Meth04 In Vivo Imaging]], [[Meth01 Microscopy]], [[CS11 Time Series and Signal Processing]]), probability densities ([[CS02 Probability and Statistics]]).

**All notes that build on this topic:**
- *Physics:* [[Ph01 Mechanics and Energy]] · [[Ph02 Electricity and Charge]] · [[Ph03 Electric Fields and Potential]] · [[Ph05 Capacitance and RC Circuits]] · [[Ph07 Diffusion and Transport]] · [[Ph09 Waves and Oscillations]] · [[Ph11 Optics and Fluorescence]]
- *Methods:* [[Meth01 Microscopy]] · [[Meth04 In Vivo Imaging]]
- *Computer Science:* [[CS02 Probability and Statistics]] · [[CS08 Deep Neural Networks]] · [[CS09 Probabilistic and Bayesian Models]] · [[CS11 Time Series and Signal Processing]] · [[CS12 Neuroimaging Data Analysis]]
- *Programming:* [[Py08 SciPy Scientific Computing]] · [[MAT03 MATLAB Control Flow and Functions]] · [[Doc02 Math in Markdown]]

*(Overview of all connections: [[MOC-neuroscience-foundations]])*

## Key takeaways
- Don't forget $+C$; check by differentiating.
- $\int x^{-1}dx = \ln\lvert x\rvert$ is the exception to the power rule.
- Substitution undoes the chain rule, parts undoes the product rule.
- Integral of current = charge; integral of rate = count.
